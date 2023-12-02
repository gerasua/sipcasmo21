from PyQt5.uic import loadUi
import logging
import mysql.connector as mdb
import time
import datetime
import cv2
import os
import shutil
from escpos import SerialConnection
from escpos.impl.epson import GenericESCPOS
from PyQt5.QtGui import QIntValidator
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

class registraPrimeraDevClientTrailerManual(QDialog):
    def __init__(self, fn=None, parent=None):
        super(registraPrimeraDevClientTrailerManual, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Primera_DevCliente_Trailer_Manual.ui', self)
        logger.debug("Operador_Primera_DevCliente_Trailer_Manual")
        logger.debug("Operador registra primera pesada devolucion de cliente Trailer Manual")
        self.DB_Connect()
        self.btnr.clicked.connect(self.regresar)
        self.btn_guardar.clicked.connect(self.ObtenDatos)
        logger.debug("Inicia Primera Pesada")

        # Peso de entrada
        e1 = self.Peso
        e1.objectName()
        e1.setValidator(QIntValidator())

        # Carta Porte
        e2 = self.cartaporte
        e2.objectName()
        e2.setValidator(QIntValidator())

        # Folio
        e3 = self.folio
        e3.objectName()
        e3.setValidator(QIntValidator())

        # Placas tracto
        try:
            self.cur.execute("SELECT * FROM totalco_tractor WHERE tipo='TRAILER'")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_placas.addItem(str(resultado[3]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Placas de la caja
        try:
            self.cur.execute("SELECT id_portacontenedor, placas FROM `totalco_portacontenedor` WHERE caja_porta = '0' ORDER BY id_portacontenedor")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_PlacasCaja.addItem(str(resultado[1]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Clientes
        try:
            self.cur.execute("SELECT * FROM totalco_cliente WHERE id_cliente  > 0")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_cliente.addItem(str(resultado[2]), int(resultado[0]))
        except Exception as e:
            logger.exception("Error For: {}".format(e))

        # Producto
        try:
            self.cur.execute("SELECT * FROM totalco_producto")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_productos.addItem(str(resultado[2]), int(resultado[0]))
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

    def ObtenDatos(self):
        # Validar Peso
        peso_insertar = self.Peso.displayText()
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

        identifica_pedido_tipo = 6

        # Peso
        peso_insertar = self.Peso.displayText()
        logger.debug("Peso: {}".format(peso_insertar))

        # Placas Tracto ID
        id_tractor = self.comboBox_placas.itemData(self.comboBox_placas.currentIndex())
        placas = self.comboBox_placas.currentText()
        logger.debug("Placas ID: {}".format(id_tractor))
        logger.debug("Placas: {}".format(placas))

        # Placas Caja ID
        id_placas_caja = self.comboBox_PlacasCaja.itemData(self.comboBox_PlacasCaja.currentIndex())
        placas_caja = self.comboBox_PlacasCaja.currentText()
        logger.debug("Placas Caja ID: {}".format(id_placas_caja))
        logger.debug("Placas Caja: {}".format(placas_caja))

        # Cliente ID
        id_cliente = self.comboBox_cliente.itemData(self.comboBox_cliente.currentIndex())
        cliente = self.comboBox_cliente.currentText()
        logger.debug("Cliente ID: {}".format(id_cliente))
        logger.debug("Cliente: {}".format(cliente))

        # Prducto ID
        id_producto = self.comboBox_productos.itemData(self.comboBox_productos.currentIndex())
        producto = self.comboBox_productos.currentText()
        logger.debug("Producto ID: {}".format(id_producto))
        logger.debug("Producto: {}".format(producto))

        # Operador ID
        id_operador = self.comboBox_operador.itemData(self.comboBox_operador.currentIndex())
        operador = self.comboBox_operador.currentText()
        logger.debug("Operador ID: {}".format(id_operador))
        logger.debug("Operador: {}".format(operador))

        cartaPorte = self.cartaporte.displayText()
        logger.debug("Numero Carta Porte: {}".format(cartaPorte))

        folio = self.folio.displayText()
        logger.debug("Numero de folio: {}".format(folio))

        lote = self.lote.displayText()
        logger.debug("Numero de folio: {}".format(lote))

        # Observaciones
        observaciones = self.observaciones.displayText()
        logger.debug("Observaciones: {}".format(observaciones))

        # Observaciones Manual
        observaciones_manual = self.Observaciones_Manual.toPlainText()
        logger.debug("Observaciones Manual: {}".format(observaciones_manual))

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
        fecha_e = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        logger.debug("Fecha: {}".format(fecha_e))

        # Obtener la hora
        hora_e = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        logger.debug("Hora actual: {}".format(hora_e))
        fechahora = fecha_e + " " + hora_e

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
        path_to_watch = "1aPesada" + self.sucursal

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
        self.tipo_pesada = '1'

        #
        # Completo
        # La primera pesada siempre será incompleto
        # 0 = incompleto
        # 1 = completo
        completo = '0'

        #
        # ES UNA PESADA SOLAS
        # O NO es pesada SOLAS
        # 1 ES PESADA SOLAS
        solas = '0'

        try:
            query = "INSERT INTO `totalco_boleto_ent` (`id_producto`, `id_cliente`, `fecha_e`, `hora_e`, `id_tractor`, `id_operador`, `peso_e`, `tipo_pesada`, `id_usuario`, " \
                    "`completo`, `solas`, `observaciones`, `identifica_pedido_tipo`, `ruta_windows`, `ruta_linux`, `captura_cam1`, `captura_cam2`, `captura_cam3`, `id_portacontenedor`, `carta_porte`, `folio`, `lote`, `observaciones_manual`, `captura_cam4`) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')" \
                    "".format(id_producto, id_cliente, fecha_e, hora_e, id_tractor, id_operador, peso_insertar, self.tipo_pesada, self.id_usuario, completo, solas, observaciones,
                              identifica_pedido_tipo, new_dir_w, dir_linux, imageName1, imageName2, imageName3, id_placas_caja,cartaPorte, folio, lote, observaciones_manual, imageName4)
            logger.debug("Query: {}".format(query))
            self.cur.execute(query)
            numboleto = self.cur.lastrowid
            if self.cur.lastrowid:
               logger.debug("Last insert id: {}".format(self.cur.lastrowid))
            else:
                logger.debug("Last insert id not found")
            self.conn.commit()
        except Exception as e:
            logger.debug("Error al insertar en la BD: {}".format(e))

        try:
            self.cur.execute("SELECT * FROM totalco_info_gral WHERE id_info_gral ='1'")
            self.row = self.cur.fetchone()
            self.empresa = self.row[2]
            logger.debug("Empresa: {}".format(self.empresa))
        except Exception as e:
            logger.debug("Error: {}".format(e))

        # Impresora
        self.impresora = self.comboBox_impresora.currentText()
        logger.debug("Impresora: {}".format(self.impresora))

        self.NumeroTicket = numboleto
        self.cliente = cliente
        self.peso_insertar = peso_insertar
        self.fechahora = fechahora
        self.placas_caja = placas_caja
        self.producto = producto
        self.chofer = operador
        self.observaciones = observaciones

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
                printer.text("{}".format(self.empresa))
                printer.text("Devolucion de Cliente")
                printer.text("Boleto # {}".format(numboleto))
                printer.text("Cliente: {}".format(cliente))
                printer.text("Primera Pesada: {}".format(peso_insertar))
                printer.text("Fecha/Hora: {}".format(fechahora))
                printer.text("Placas: {}".format(placas_caja))
                printer.text("Producto: {}".format(producto))
                printer.text("Chofer: {}".format(operador))
                printer.text("Pesador: {}".format(self.pesador))
                printer.text("Observaciones: {}".format(observaciones))
                printer.text("================================")

                # Pesada guardada
            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<thead><tr><th>PRIMERA PESADA</th><th></th></tr></thead><tbody><tr><td>DEVOLUCION DE CLIENTE</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></tbody><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.peso_insertar}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.fechahora}</td></tr></tbody><tbody><tr><td>PLACAS</td><td>{self.placas_caja}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.chofer}</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.pesador}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones}</td></tr></tbody>"
            except Exception as e:
                logger.exception("Falla en llenado de datos con variables PESADA SENCILLA")

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
                <img src="images/logo.jpg" width="100" height="80" align="left">
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>                                           
                        <table class="default" width="100%">                                            
                            [DATOS]
                        </table>
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
                nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Impresion de ticket 1a_" + str(self.NumeroTicket),
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
            self.hide()

    def regresar(self):
        logger.debug("Cerrar ventana")
        self.close()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de cancelar?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
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