from PyQt5.uic import loadUi
import logging
import mysql.connector as mdb
from mysql.connector import Error
import serial
import re
import serial.tools.list_ports
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import time
import datetime
import cv2
import os
import shutil
from escpos import SerialConnection
from escpos.impl.epson import GenericESCPOS
from PyQt5.QtGui import QIcon, QTextDocument
from PyQt5.QtCore import Qt, QTextCodec, QByteArray
from PyQt5.QtWidgets import (QDialog, QFileDialog, QMessageBox, QToolBar)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

#Logging and console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class registraSegundaPesadaSolas(QDialog):
    def __init__(self, ticket, parent=None):
        super(registraSegundaPesadaSolas, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Segunda_SOLAS_Trailer_Automatica.ui', self)
        logger.debug("Operador_Segunda_SOLAS_Trailer_Automatica")
        logger.debug("Operador registra segunda pesada SOLAS Automatica Trailer")
        self.DB_Connect()
        self.btnr.clicked.connect(self.regresar)
        self.btn_guardar.clicked.connect(self.ObtenDatos)
        logger.debug("Inicia Segunda Pesada SOLAS")

        self.NumeroTicket = ticket
        logger.debug("Número de ticket: {}".format(self.NumeroTicket))
        self.lcdNumber_9.display(self.NumeroTicket)

        try:
            self.thread = GetData(self)
            self.thread.dataChanged.connect(self.onDataChanged)
            self.thread.start()
        except Exception as e:
            logger.exception("Error al tratar de abrir el puerto: %s" % e)
        logger.debug("Thread is Running?: %s" % self.thread.isRunning())
        logger.debug("Serial is open?: %s" % self.thread.ser.isOpen())

        try:
            self.cur.execute("SELECT * FROM totalco_boleto_ent WHERE id_bol_entra='" + ticket + "'")
            self.row = self.cur.fetchone()
            logger.debug("Peso de Entrada: %s" % self.row[9])
            self.pesoentrada = self.row[9]
        except Exception as e:
            logger.debug("Error: {}".format(e))

        self.lcdNumber_3.display(self.pesoentrada)

        # Contenedor
        try:
            self.cur.execute("SELECT * FROM totalco_contenedor")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_contenedor.addItem(str(resultado[1]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Chofer
        try:
            self.cur.execute("SELECT * FROM totalco_operadores")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_operador.addItem(str(resultado[1]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Destino Venta SOLAS
        try:
            self.cur.execute("SELECT * FROM totalco_destino_vta_solas WHERE id_destino_vta_solas > 0")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_destinosolas.addItem(str(resultado[1]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Maniobra
        try:
            self.cur.execute("SELECT * FROM totalco_maniobra")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_maniobra.addItem(str(resultado[1]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

    def onDataChanged(self, KG):
        logger.debug("Kilos en el onDataChanged: {}".format(KG))

        if self.pesoentrada > KG:
            resta = self.pesoentrada - KG
        else:
            resta = KG - self.pesoentrada

        logger.debug("Kilos Netos: {}".format(resta))

        self.lcdNumber_7.display(KG)
        self.lcdNumber_1.display(resta)
        # logger.debug("Kilos en el LCD: %s" % self.lcdNumber_7.value())
        logger.debug("ilos en el LCD: {}".format(self.lcdNumber_7.value()))
        # logger.debug("Kilos Netos en el LCD: %s" % self.lcdNumber_1.value())
        logger.debug("Kilos netos en el LCD {}".format(self.lcdNumber_1.value()))

    def ObtenDatos(self):
        # Validar Peso
        peso_insertar = int(self.lcdNumber_7.value())
        logger.debug("Peso: {}".format(peso_insertar))

        if peso_insertar != "":
            logger.debug("No esta vacío")
            if int(peso_insertar) > 0:
                logger.debug("Peso es mayor a 0: {}".format(peso_insertar))
                reply = QMessageBox.question(self, "Guardar", "¿Estás completamente seguro de guardar?",
                                             QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    self.insertarDatos()
            else:
                QMessageBox.critical(self, "Mensaje", "El peso no debe ser igual o menor a 0.", QMessageBox.Ok)
        else:
            logger.debug("El campo de peso no debe estar vacio: {}".format(peso_insertar))
            QMessageBox.critical(self, "Mensaje", "No debe estar vacío.", QMessageBox.Ok)

    def insertarDatos(self):
        logger.debug("Insertar Datos?")
        ## INICIO

        # El tipo de operacion es una entrada
        # identifica_pedido_tipo
        # 1 = Entrada
        # 2 = Salida
        # 3 = Movimiento Interno
        # 4 = Traspaso de sucursal
        # 5 = Devolución de compra
        # 6 = Devolución de venta

        identifica_pedido_tipo = 2

        # Peso
        # logger.debug("Peso en insertar datos del LCD: %s" % int(self.lcdNumber_7.value()))
        logger.debug("Peso en insertar datos del LCD: {}".format(self.lcdNumber_7.value()))
        PesoTara = int(self.lcdNumber_7.value())

        # Peso Neto
        # logger.debug("Peso en insertar datos del LCD: %s" % self.lcdNumber_1.value())
        logger.debug("Peso en insertar datos del LCD: {}".format(self.lcdNumber_1.value()))
        PesoNeto = self.lcdNumber_1.value()

        # Contenedor ID
        id_contenedor = self.comboBox_contenedor.itemData(self.comboBox_contenedor.currentIndex())
        contenedor = self.comboBox_contenedor.currentText()
        logger.debug("Contenedor ID: {}".format(id_contenedor))
        logger.debug("Contenedor: {}".format(contenedor))

        try:
            self.cur.execute("SELECT cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor FROM totalco_contenedor cont INNER JOIN totalco_contenedor_tipo contTipo ON (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo) WHERE cont.id_contenedor ='" + str(id_contenedor) + "'")
            self.row = self.cur.fetchone()
            self.claveContenedor = self.row[0]
            logger.debug("Clave contenedor: {}".format(self.claveContenedor))
            self.tipoContenedor = self.row[1]
            logger.debug("Tipo de Contenedor: {}".format(self.tipoContenedor))
        except Exception as e:
            logger.debug("Error: {}".format(e))

        # Operador ID
        id_operador = self.comboBox_operador.itemData(self.comboBox_operador.currentIndex())
        operador = self.comboBox_operador.currentText()
        logger.debug("Operador ID: {}".format(id_operador))
        logger.debug("Operador: {}".format(operador))

        # Destino
        id_destino = self.comboBox_destinosolas.itemData(self.comboBox_destinosolas.currentIndex())
        destino = self.comboBox_destinosolas.currentText()
        logger.debug("Destino ID: {}".format(id_destino))
        logger.debug("Destino: {}".format(destino))

        # Maniobra ID
        id_maniobra = self.comboBox_maniobra.itemData(self.comboBox_maniobra.currentIndex())
        maniobra = self.comboBox_maniobra.currentText()
        logger.debug("Maniobra ID: {}".format(id_maniobra))
        logger.debug("Maniobra: {}".format(maniobra))

        # # Observaciones
        # observaciones = self.observaciones.toPlainText()
        # logger.debug("Observaciones: {}".format(observaciones))

        # Observaciones
        observaciones = self.observaciones.displayText()
        logger.debug("Observaciones: {}".format(observaciones))

        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row = self.cur.fetchone()
            self.id_usuario = self.row[0]
            self.pesador = self.row[5]
        except Exception as e:
            logger.debug("Error: {}".format(e))

        # Obtener Tiempo
        logger.debug("Determinar fecha y hora actual")
        ts = time.time()
        # Obtener la fecha
        fecha_s = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        logger.debug("Fecha: {}".format(fecha_s))

        # Obtener la hora
        hora_s = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        logger.debug("Hora actual: {}".format(hora_s))
        self.fechahora = fecha_s + " " + hora_s

        ##
        # Consulta para crear el directorio de camaras
        ##
        try:
            self.cur.execute("SELECT * FROM totalco_info_gral")
            self.row = self.cur.fetchone()
            self.sucursal = self.row[3]

        except Exception as e:
            logger.debug("Error: {}".format(e))

        # Obtener la imagen
        logger.debug("Captura de Cámaras")
        ##
        # Se agrega la sucursal para crear el directorio
        ##
        path_to_watch = "2aPesada" + self.sucursal

        ##
        # Se verifica si se pesa con cámaras
        ##
        try:
            self.cur.execute("SELECT * FROM totalco_camaras_activas")
            self.row = self.cur.fetchone()
            self.cam_activas = self.row[0]
            # 0 para pesar con cámaras
            # 1 para no pesar con cámaras
            if self.cam_activas == 0:
                logger.debug("Camaras Activas")
            else:
                logger.debug("Camaras inactivas")

        except Exception as e:
            logger.debug("Error: {}".format(e))

        # Se crea directorio para cámaras

        try:
            new_dir_w = os.path.join(path_to_watch, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            dir_linux = path_to_watch + "/" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            try:
                if not os.path.exists(new_dir_w):
                    os.makedirs(new_dir_w)
            except Exception as e:
                logger.exception("Error al crear el directorio para las imagenes: %s" % e)
            logger.debug("Directorio Windows: {}".format(new_dir_w))
            logger.debug("Directorio Linux: {}".format(dir_linux))
        except Exception as e:
            logger.debug("Error en el path del directorio de cámaras")

        ##
        # Se verifica el status de las camaras, sin es igual a 0 se pesa con Camaras
        ##
        if self.cam_activas == 0:

            # Inicio Cámara 1

            try:
                self.cur.execute("SELECT * FROM totalco_camaras WHERE id_camara='1'")
                self.row = self.cur.fetchone()
                self.camara_usuario = self.row[1]
                self.camara_password = self.row[2]
                self.camara_ip = self.row[3]
                self.camara_canal = self.row[4]
            except Exception as e:
                logger.debug("Error: {}".format(e))

            try:
                source = "rtsp://" + self.camara_usuario + ":" + self.camara_password + "@" + self.camara_ip + "/ISAPI/Streaming/channels/" + self.camara_canal + "/picture"
                logger.debug("Source: {}".format(source))
                cap = cv2.VideoCapture(source)
                ret, frame = cap.read()
                rgbImage = frame  # Capturar imagen a color
                imageName1 = ("camara1_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            except Exception as e:
                logger.debug("Error al obtener la imagen")
            # Guardar la imagen
            try:
                cv2.imwrite(imageName1, rgbImage)
                logger.debug("CV2: Nombre de imagen: {}".format(imageName1))
            except Exception as e:
                logger.exception("Error con las camaras: {}".format(e))
            # Se libera
            try:
                cap.release()
                logger.debug("Nombre de imagen: %s" % imageName1)
                if not imageName1:
                    return
            except Exception as e:
                logger.debug("Error al guardar la imagen")
            try:
                shutil.move(imageName1, new_dir_w)
            except Exception as e:
                logger.debug("Error al colocar la imagen el directorio")
            # Fin Cámara 1

            # Inicio Cámara 2
            try:
                self.cur.execute("SELECT * FROM totalco_camaras WHERE id_camara='2'")
                self.row = self.cur.fetchone()
                self.camara_usuario = self.row[1]
                self.camara_password = self.row[2]
                self.camara_ip = self.row[3]
                self.camara_canal = self.row[4]
            except Exception as e:
                logger.debug("Error: {}".format(e))

            try:
                source = "rtsp://" + self.camara_usuario + ":" + self.camara_password + "@" + self.camara_ip + "/ISAPI/Streaming/channels/" + self.camara_canal + "/picture"
                cap = cv2.VideoCapture(source)
                ret, frame = cap.read()
                rgbImage = frame  # Capturar imagen a color
                imageName2 = ("camara2_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            except Exception as e:
                logger.debug("Error al obtener la imagen")
            # Guardar la imagen
            try:
                cv2.imwrite(imageName2, rgbImage)
                logger.debug("CV2: Nombre de imagen: {}".format(imageName2))
            except Exception as e:
                logger.exception("Error con las camaras: {}".format(e))
            # Se libera
            try:
                cap.release()
                logger.debug("Nombre de imagen: %s" % imageName2)
                if not imageName2:
                    return
            except Exception as e:
                logger.debug("Error al guardar la imagen")
            try:
                shutil.move(imageName2, new_dir_w)
            except Exception as e:
                logger.debug("Error al colocar la imagen el directorio")
            # Fin Cámara 2

            # Inicio Cámara 3
            try:
                self.cur.execute("SELECT * FROM totalco_camaras WHERE id_camara='3'")
                self.row = self.cur.fetchone()
                self.camara_usuario = self.row[1]
                self.camara_password = self.row[2]
                self.camara_ip = self.row[3]
                self.camara_canal = self.row[4]
            except Exception as e:
                logger.debug("Error: {}".format(e))

            try:
                source = "rtsp://" + self.camara_usuario + ":" + self.camara_password + "@" + self.camara_ip + "/ISAPI/Streaming/channels/" + self.camara_canal + "/picture"
                cap = cv2.VideoCapture(source)
                ret, frame = cap.read()
                rgbImage = frame  # Capturar imagen a color
                imageName3 = ("camara3_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            except Exception as e:
                logger.debug("Error al obtener la imagen")
            # Guardar la imagen
            try:
                cv2.imwrite(imageName3, rgbImage)
                logger.debug("CV2: Nombre de imagen: {}".format(imageName3))
            except Exception as e:
                logger.exception("Error con las camaras: {}".format(e))
            # Se libera
            try:
                cap.release()
                logger.debug("Nombre de imagen: %s" % imageName3)
                if not imageName3:
                    return
            except Exception as e:
                logger.debug("Error al guardar la imagen")
            try:
                shutil.move(imageName3, new_dir_w)
            except Exception as e:
                logger.debug("Error al colocar la imagen el directorio")
            # Fin Cámara 3

            # Inicio Cámara 4
            try:
                self.cur.execute("SELECT * FROM totalco_camaras WHERE id_camara='4'")
                self.row = self.cur.fetchone()
                self.camara_usuario = self.row[1]
                self.camara_password = self.row[2]
                self.camara_ip = self.row[3]
                self.camara_canal = self.row[4]
            except Exception as e:
                logger.debug("Error: {}".format(e))

            try:
                source = "rtsp://" + self.camara_usuario + ":" + self.camara_password + "@" + self.camara_ip + "/ISAPI/Streaming/channels/" + self.camara_canal + "/picture"
                cap = cv2.VideoCapture(source)
                ret, frame = cap.read()
                rgbImage = frame  # Capturar imagen a color
                imageName4 = ("camara4_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            except Exception as e:
                logger.debug("Error al obtener la imagen")
            # Guardar la imagen
            try:
                cv2.imwrite(imageName4, rgbImage)
                logger.debug("CV2: Nombre de imagen: {}".format(imageName4))
            except Exception as e:
                logger.exception("Error con las camaras: {}".format(e))
            # Se libera
            try:
                cap.release()
                logger.debug("Nombre de imagen: %s" % imageName4)
                if not imageName4:
                    return
            except Exception as e:
                logger.debug("Error al guardar la imagen")
            try:
                shutil.move(imageName4, new_dir_w)
            except Exception as e:
                logger.debug("Error al colocar la imagen el directorio")
            # Fin Cámara 4

        ##
        # De lo contrario se pesa sin Camaras
        ##
        else:
            logger.debug("Sin camaras")
            imageName1 = ("NO_camara1_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            imageName2 = ("NO_camara2_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            imageName3 = ("NO_camara3_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')
            imageName4 = ("NO_camara4_" + str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg')

        # Insert en la base de datos

        # tipo de pesada
        # 0 = Automatica(A través del indicador)
        # 1 = Manual(Se mete tecleando el peso, sólo con el usuario de supervisor lo puede hacer)
        self.tipo_pesada = '0'

        #
        # Completo
        # La primera pesada siempre será incompleto
        # 0 = incompleto
        # 1 = completo
        completo = '1'

        #
        # ES UNA PESADA SOLAS
        # O NO es pesada SOLAS
        # 1 ES PESADA SOLAS
        solas = '1'

        try:
            query = "INSERT INTO totalco_boleto_sal(id_bol_sal, id_bol_entra, fecha_s, hora_s, peso_bruto, peso_tara, peso_neto, tipo_pesada, identifica_pedido_tipo, " \
                    "solas, completo, observaciones, id_destino_vta_solas, ruta_windows, ruta_linux, captura_cam1, captura_cam2, captura_cam3, id_usuario, id_contenedor, id_maniobra, mbv_vgm_neto, captura_cam4, id_operador) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                .format(self.NumeroTicket, self.NumeroTicket, fecha_s, hora_s, self.pesoentrada, PesoTara, PesoNeto, self.tipo_pesada,
                identifica_pedido_tipo, solas, completo, observaciones, destino, new_dir_w, dir_linux, imageName1, imageName2, imageName3, self.id_usuario, id_contenedor, id_maniobra, PesoNeto, imageName4, id_operador)
            logger.debug("Query: {}".format(query))
            self.cur.execute(query)
            self.conn.commit()
        except Error as e:
            logger.debug("Error al insertar en la BD: {}".format(e))

        try:
            query = """ UPDATE totalco_boleto_ent SET completo = %s WHERE id_bol_entra = %s """
            data = (completo, self.NumeroTicket)
            self.cur.execute(query, data)
            self.conn.commit()
        except Exception as e:
            logger.debug("Error al terminar ticket de primera pesada: {}".format(e))

        try:
            self.cur.execute("SELECT * FROM totalco_info_gral WHERE id_info_gral ='1'")
            self.row = self.cur.fetchone()
            self.empresa = self.row[2]
            logger.debug("Empresa: {}".format(self.empresa))
        except Exception as e:
            logger.debug("Error: {}".format(e))

        try:
            self.cur.execute("SELECT * FROM totalco_bascula ORDER BY id_bascula DESC limit 1")
            self.row = self.cur.fetchone()
            logger.debug("Query Last ID: {}".format(self.row))
            self.ultimo = self.row[0]
            logger.debug("Ultimo registro: {}".format(self.ultimo))
        except Exception as e:
            logger.debug("Error ULTIMO BASCULA: {}".format(e))

        try:
            self.cur.execute("SELECT * FROM totalco_bascula WHERE id_bascula ='" + str(self.ultimo) + "'")
            self.row = self.cur.fetchone()
            logger.debug("Query Bascula: {}".format(self.row))
            self.marca = self.row[1]
            logger.debug("Marca: {}".format(self.marca))
            self.numeroSerie = self.row[2]
            logger.debug("Numero de Serie: {}".format(self.numeroSerie))
            self.modInstrumento = self.row[3]
            logger.debug("Mod Instrumento: {}".format(self.modInstrumento))
            self.aprobModelo = self.row[4]
            logger.debug("Aprob Modelo: {}".format(self.aprobModelo))
            self.hologramaVerificacion = self.row[5]
            logger.debug("Holograma: {}".format(self.hologramaVerificacion))
            self.certificadoCalidad = self.row[6]
            logger.debug("Certificado Calidad: {}".format(self.certificadoCalidad))
        except Error as e:
            logger.debug("Error BASCULA: {}".format(e))

        # Impresora
        self.impresora = self.comboBox_impresora.currentText()
        logger.debug("Impresora: {}".format(self.impresora))

        self.PesoTara = PesoTara
        self.PesoNeto = PesoNeto

        if self.impresora == "Impresora de Cinta":
            logger.debug("Se usará impresora de cinta")

            try:
                self.cur.execute("SELECT * FROM totalco_puertocom WHERE id_puerto='1'")
                self.row = self.cur.fetchone()
                self.pto_impresora = self.row[1]
                self.baudrate = self.row[2]
                self.bytesize = self.row[3]
                self.stopbits = self.row[4]
                self.parity = self.row[5]

                self.impresora = self.pto_impresora + "," + self.baudrate + "," + self.bytesize + "," + self.stopbits + "," + self.parity
                logger.debug("Datos de impresora: {}".format(self.impresora))

            except Exception as e:
                logger.debug("Error: {}".format(e))

            try:
                conn = SerialConnection.create('{}'.format(self.impresora))
                printer = GenericESCPOS(conn)
                printer.init()
                # DATOS DEL TICKET
                printer.text("SEGUNDA PESADA")
                printer.text("Fecha/Hora: {}".format(self.fechahora))
                printer.text(f"Boleto: {self.NumeroTicket}")
                printer.text("Peso: {}".format(int(PesoTara)))
                printer.text("Bruto: {}".format(int(PesoTara)))
                printer.text("Tara: {}".format(int(PesoNeto)))
                printer.text("Tipo de Contenedor: {}".format(str(self.tipoContenedor)))
                printer.text("ID de Contenedor: {}".format(str(self.claveContenedor)))
                printer.text("MASA BRUTA VERIFICADA (MBV)=")
                printer.text("Verified Gross Mass (VGM)=")
                printer.text("Neto: {}".format(int(PesoNeto)))
                printer.text("BASCULA MARCA: {}".format(self.marca))
                printer.text("Num Serie: {}".format(self.numeroSerie))
                printer.text("Mod Instrumen: {}".format(self.modInstrumento))
                printer.text("Aprob Modelo: {}".format(self.aprobModelo))
                try:
                    printer.text("Holograma Verifi: {}".format(self.hologramaVerificacion))
                except Exception as e:
                    logger.debug(f"Error en variable Holograma de verificacion: {self.hologramaVerificacion}")
                try:
                    printer.text("Certificado Cal: {}".format(self.certificadoCalidad))
                except Exception as e:
                    logger.debug(f"Error en variable Certificado Cal {self.certificadoCalidad}")
                try:
                    printer.text(" ")
                except Exception as e:
                    logger.debug(f"Error en el espacio")
                try:
                    printer.text("_______________________")
                except Exception as e:
                    logger.debug(f"Error en ____")
                try:
                    printer.text(" ")
                except Exception as e:
                    logger.debug(f"Error en el segundo espacio")
                try:
                    printer.text("{}".format(self.pesador))
                except Exception as e:
                    logger.debug(f"Error en variable pesador {self.pesador}")
                try:
                    printer.text("Operador de Bascula\n")
                except Exception as e:
                    logger.debug(f"Error en Operador de Bascula")

            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<tbody><tr><td>&nbsp;</td><td></td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><thead><tr><th>SEGUNDA PESADA</th><th></th></tr></thead><tbody><tr><td>FECHA Y HORA</td><td>{self.fechahora}</td></tr></tbody><tbody><tr><td>PESO</td><td>{self.PesoTara}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BRUTO</td><td>{self.PesoTara}</td></tr></tbody><tbody><tr><td>TARA</td><td>{self.PesoNeto}</td></tr></tbody><tbody><tr><td>TIPO DE CONTENEDOR</td><td>{self.tipoContenedor}</td></tr></tbody><tbody><tr><td>ID DE CONTENEDOR</td><td>{self.claveContenedor}</td></tr></tbody><tbody><tr><td>MASA BRUTA VERIFICADA (MBV)=</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>VERIFIED GROSS MASS (VGM) =</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>NETO</td><td>{self.PesoNeto}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BASCULA MARCA</td><td>{self.marca}</td></tr></tbody><tbody><tr><td>NUM SERIE</td><td>{self.numeroSerie}</td></tr></tbody><tbody><tr><td>MOD INSTRUMENTO</td><td>{self.modInstrumento}</td></tr></tbody><tbody><tr><td>APROB MODELO</td><td>{self.aprobModelo}</td></tr></tbody><tbody><tr><td>HOLOGRAMA VERIFI</td><td>{self.hologramaVerificacion}</td></tr></tbody><tbody><tr><td>CERTIFICADO CAL</td><td>{self.certificadoCalidad}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>FIRMA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>_________________________</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>{self.pesador}</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>OPERADOR DE BASCULA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody>"
            except Exception as e:
                logger.exception("Falla en llenado de datos con variables")

            reporteHtml = """
                <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                    <style>
                    h3 {
                        font-family: Helvetica-Bold;
                        text-align: center;
                       }

                    table {
                           font-family: arial, sans-serif;
                           border-collapse: collapse;
                           width: 100%;
                          }

                    td {
                        text-align: left;
                        padding-top: 4px;
                        padding-right: 6px;
                        padding-bottom: 2px;
                        padding-left: 6px;
                       }

                    th {
                        text-align: left;
                        padding: 4px;
                        background-color: black;
                        color: white;
                       }

                    tr:nth-child(even) {
                                        background-color: #dddddd;
                                       }
                    </style>
            </head>
                <body>
                <img src="images/logo.jpg" width="100" height="80" align="right">
                <br>
                <br>
                <br>
                <br>
                    <h3></h3>
                    <table class="default" width="100%">                                                                
                        [DATOS]
                    </table>                        
                        <h3>RE IMPRESION DE TICKET<br/></h3>
                </body>
        </html>
                """.replace("[DATOS]", datos)

            datos = QByteArray()
            datos.append(str(reporteHtml))
            codec = QTextCodec.codecForHtml(datos)
            unistr = codec.toUnicode(datos)

            if Qt.mightBeRichText(unistr):
                self.documento.setHtml(unistr)
            else:
                self.documento.setPlainText(unistr)

            self.vistaPrevia()

            ###
            # FINAL DE IMPRESORA WINDOWS
            ###

        ## FINAL
        logger.debug("Aqui finaliza")
        self.despuesDeInsertarDatos()

    def vistaPrevia(self):
        if not self.documento.isEmpty():
            logger.debug("Dentro de vista previa")
            impresion = QPrinter(QPrinter.HighResolution)

            vista = QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("Vista previa")
            vista.setWindowFlags(Qt.Window)
            vista.resize(800, 600)
            try:
                exportarPDF = vista.findChildren(QToolBar)
                exportarPDF[0].addAction(QIcon("images/exportarPDF.png"), "Exportar a PDF", self.exportarPDF)
            except Exception as e:
                logger.debug(f"Error con imagen: {e}")

            vista.paintRequested.connect(self.vistaPreviaImpresion)
            vista.exec_()
        else:
            QMessageBox.critical(self, "Vista previa", "No hay datos para visualizar.   ",
                                 QMessageBox.Ok)

    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def Imprimir(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)

            dlg = QPrintDialog(impresion, self)
            dlg.setWindowTitle("Imprimir documento")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.documento.print_(impresion)

            del dlg
        else:
            QMessageBox.critical(self, "Imprimir", "No hay datos para imprimir.   ",
                                 QMessageBox.Ok)

    def exportarPDF(self):
        if not self.documento.isEmpty():
            try:
                nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Impresion de ticket 2a_" + str(self.NumeroTicket),
                                                               "Archivos PDF (*.pdf);;All Files (*)",
                                                               options=QFileDialog.Options())
            except Exception as e:
                logger.exception("Error al exportar: {}".format(e))

            if nombreArchivo:
                try:
                    impresion = QPrinter(QPrinter.HighResolution)
                    impresion.setOutputFormat(QPrinter.PdfFormat)
                    impresion.setOutputFileName(nombreArchivo)
                    self.documento.print_(impresion)

                    QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.   ",
                                            QMessageBox.Ok)
                except Exception as e:
                    logger.exception("Error con los datos exportados: {}".format(e))
        else:
            QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.   ",
                                 QMessageBox.Ok)

    def despuesDeInsertarDatos(self):
        reply = QMessageBox.question(
            self, "Message",
            "Pesada guardada",
            QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            if (self.thread.isRunning()):
                self.thread.terminate()
                logger.debug("New Status Thread: %s" % self.thread.isRunning())
                if (self.thread.ser.isOpen()):
                    self.thread.ser.close()
                    logger.debug("New Serial Status: %s" % self.thread.ser.isOpen())
                    self.hide()

    def regresar(self):
        logger.debug("Cerrar ventana")
        self.close()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje", "Estas seguro de cancelar?", QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            logger.debug("Close")
            if (self.thread.isRunning()):
                self.thread.terminate()
                logger.debug("New Status Thread: %s" % self.thread.isRunning())
                if (self.thread.ser.isOpen()):
                    self.thread.ser.close()
            self.close()
        else:
            logger.debug("Cancel")
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            logger.debug("Key Scape")
            self.close()

    ## DATABASE CONECCT

    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

class GetData(QThread):

    dataChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.DB_Connect()

        try:
            self.cur.execute("SELECT * FROM totalco_puertocomserial WHERE id_puerto='1'")
            self.row = self.cur.fetchone()
            self.puertoIndicador = self.row[1]
            self.baudrate = self.row[2]
            logger.debug("Puerto de serial indicador {}".format(self.puertoIndicador))
            logger.debug("baudrate {}".format(self.baudrate))
        except Exception as e:
            logger.debug("Error: {}".format(e))

        self.ser = serial.Serial(port=self.puertoIndicador, baudrate=self.baudrate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)

    def __del__(self):  # part of the standard format of a QThread
        self.wait()

    def run(self):  # also a required QThread function, the working part
        self.ser.close()
        self.ser.open()
        self.ser.flush()
        self.ser.reset_input_buffer()

        while True:
            while self.ser.inWaiting() == 0:
                pass
            try:
                data = self.ser.readline()
                logger.debug("Data: %s\n" % data)
                dataarray = data.decode().rstrip().split(',')
                logger.debug("Data Array: %s\n" % dataarray)
                peso = re.findall(r'[0-9]', dataarray[2])
                pesofinal = ''.join(peso)
                pesofinalentero = round(float(pesofinal), 3)
                self.ser.reset_input_buffer()
                KG = int(pesofinalentero)
                logger.debug("Kilogramos en el GETDATA: %s\n" % KG)
                self.dataChanged.emit(KG)
            except Exception as e:
                logger.exception("Error al obtener el peso: %s" % e)

    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))