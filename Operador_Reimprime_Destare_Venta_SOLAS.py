from PyQt5.uic import loadUi
import logging
import mysql.connector as mdb
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

class reimprimirVentaSolasDestare(QDialog):
    def __init__(self, ticketres, parent=None):
        super(reimprimirVentaSolasDestare, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Reimprime_Destare_Venta_SOLAS.ui', self)
        logger.debug("Operador_Reimprime_Destare_Venta_SOLAS")
        logger.debug("Operador re imprime ticket de Venta SOLAS 2a Pesada")
        self.DB_Connect()
        self.btnr.clicked.connect(self.regresar)
        self.btn_guardar.clicked.connect(self.ObtenDatos)
        self.btn_guardar2.clicked.connect(self.ObtenDatos2)
        self.btn_guardar3.clicked.connect(self.ObtenDatos3)
        self.btn_1a2a.clicked.connect(self.ObtenDatos4)


        self.NumeroTicket = ticketres
        logger.debug("Número de ticket: {}".format(self.NumeroTicket))
        self.lcdNumber_9.display(self.NumeroTicket)

        try:
            self.cur.execute("SELECT cliente, operador_entrada, producto, fecha_primera, hora_primera, usuario_primera, observaciones_entrada, placas_portacontenedor, primera_pesada, segunda_pesada, peso_neto_embalaje, fecha_segunda, hora_segunda, clave_contenedor, contenedor_tipo, linea_trasnportista, operador_salida, total_embalaje, peso_neto_sin_embalaje_redondeo, fecha_destare, hora_destare, observaciones, usuario_desatara, peso_neto_sin_embalaje FROM totalco_destare WHERE numero_ticket ='" + str(self.NumeroTicket) + "'")
            self.row = self.cur.fetchone()

            self.EFechaHora = str(self.row[3]) + " " + str(self.row[4])
            self.cliente = self.row[0]
            self.operador_entrada = self.row[1]
            self.producto = self.row[2]
            self.usuario_segunda = self.row[5]
            self.placas_portacontenedor = self.row[7]
            self.Placas.setText(str(self.placas_portacontenedor))
            self.pesoEntrada = self.row[8]
            self.pesoTara = self.row[9]
            self.pesoNeto = self.row[10]
            self.SFechaHora = str(self.row[11]) + " " + str(self.row[12])
            self.claveContenedor = self.row[13]
            self.tipoContenedor = self.row[14]
            self.linea = self.row[15]
            self.operador_salida = self.row[16]
            self.pesoembalaje = self.row[17]
            self.pesoNetoRedondeado = self.row[18]
            self.DFechaHora = str(self.row[19]) + " " + str(self.row[20])
            self.ObservacionesDestare = self.row[21]
            self.usario_destara = self.row[22]
            self.pesoNetoSinEmbalaje = self.row[23]

        except Exception as e:
            logger.debug("Error: {}".format(e))

        self.Cliente.setText(str(self.cliente))
        self.Operador.setText(str(self.operador_entrada))
        self.Operador2a.setText(str(self.operador_salida))
        self.Producto.setText(str(self.producto))
        self.EFecha.setText(str(self.EFechaHora))
        self.lcdNumber_3.display(self.pesoEntrada)
        self.lcdNumber_7.display(self.pesoTara)
        self.lcdNumber_1.display(self.pesoNeto)
        self.SFecha.setText(str(self.SFechaHora))
        self.Clave.setText(str(self.claveContenedor))
        self.TipoContenedor.setText(str(self.tipoContenedor))
        self.lcdNumber_6.display(self.pesoNetoRedondeado)
        self.lcdNumber_4.display(self.pesoNetoSinEmbalaje)


    def ObtenDatos(self):
        reply = QMessageBox.question(
            self, "Guardar",
            "¿Estás completamente seguro de re imprimir?",
            QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.insertarDatos()

    def ObtenDatos2(self):
        reply = QMessageBox.question(
            self, "Guardar",
            "¿Estás completamente seguro de re imprimir?",
            QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.insertarDatos2()

    def ObtenDatos3(self):
        reply = QMessageBox.question(
            self, "Guardar",
            "¿Estás completamente seguro de re imprimir?",
            QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.insertarDatos3()

    def ObtenDatos4(self):
        reply = QMessageBox.question(
            self, "Guardar",
            "¿Estás completamente seguro de re imprimir?",
            QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.insertarDatos4()

    def insertarDatos(self):
        logger.debug("Re imprimir Ticket?")

        # Placas
        self.placas_insert = self.Placas.displayText()
        logger.debug("Placas: {}".format(self.placas_insert))

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
                printer.text_center("CERTIFICADO DE PESO")
                # printer.text("RE IMPRESION")
                printer.text(" ")
                printer.text("{}".format(self.empresa))
                printer.text(" ")
                printer.text("Placas Portacontenedor: {}".format(self.placas_insert))
                printer.text("Empresa(Cliente): {}".format(self.cliente))
                printer.text("Linea Transportista: {}".format(self.linea))
                printer.text(" ")
                printer.text("PRIMERA PESADA")
                printer.text("Boleto: {}".format(self.NumeroTicket))
                printer.text("Fecha/Hora: {}".format(self.EFechaHora))
                printer.text("Peso: {}".format(int(self.pesoEntrada)))
                printer.text("Producto".format(self.producto))

            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<thead><tr><th>CERTIFICADO DE PESO</th><th></th></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>RE IMPRESION</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>PLACAS PORTACONTENEDOR</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>EMPRESA(CLIENTE)</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>LINEA TRANSPORTISTA</td><td>{self.linea}</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>PRIMERA PESADA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr></tbody><tbody><tr><td>PESO</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody>"
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
            <img src="images/logo.jpg" width="100" height="80" align="left">
            <br>
            <br>
            <br>
            <br>
                <h3>RE IMPRESION DE TICKET<br/></h3>                    
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
        logger.debug("Aqui finaliza 1a Pesada")
        self.despuesDeInsertarDatos()

    def insertarDatos2(self):
        logger.debug("Re imprimir Ticket?")

        # Placas
        self.placas_insert = self.Placas.displayText()
        logger.debug("Placas: {}".format(self.placas_insert))

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
        except Exception as e:
            logger.debug("Error BASCULA: {}".format(e))

        # Impresora
        self.impresora = self.comboBox_impresora.currentText()
        logger.debug("Impresora: {}".format(self.impresora))

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
                printer.text("Fecha/Hora: {}".format(self.SFechaHora))
                printer.text("Ticket: {}".format(self.NumeroTicket))
                printer.text("Peso: {}".format(int(self.pesoTara)))
                printer.text("Bruto: {}".format(int(self.pesoTara)))
                printer.text("Tara: {}".format(int(self.pesoNeto)))
                printer.text("Tipo de Contenedor: {}".format(str(self.tipoContenedor)))
                printer.text("ID de Contenedor: {}".format(str(self.claveContenedor)))
                printer.text("MASA BRUTA VERFICADA (MBV)")
                printer.text("Verified Griss Mass (VGM)")
                printer.text("Neto: {}".format(int(self.pesoNeto)))
                printer.text("BASCULA MARCA: {}".format(self.marca))
                printer.text("Num Serie: {}".format(self.numeroSerie))
                printer.text("Mod Instrumen: {}".format(self.modInstrumento))
                printer.text("Aprob Modelo: {}".format(self.aprobModelo))
                printer.text("Holograma Verifi: {}".format(self.hologramaVerificacion))
                printer.text("Certificado Cal: {}".format(self.certificadoCalidad))
                printer.text(" ")
                printer.text("_________________________")
                printer.text("{}\n".format(self.usuario_segunda))
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
                datos += f"<tbody><tr><td>&nbsp;</td><td></td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><thead><tr><th>SEGUNDA PESADA</th><th></th></tr></thead><tbody><tr><td>FECHA Y HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>PESO</td><td>{self.pesoTara}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BRUTO</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>TARA</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>TIPO DE CONTENEDOR</td><td>{self.tipoContenedor}</td></tr></tbody><tbody><tr><td>ID DE CONTENEDOR</td><td>{self.claveContenedor}</td></tr></tbody><tbody><tr><td>MASA BRUTA VERIFICADA (MBV)=</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>VERIFIED GROSS MASS (VGM) =</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>NETO</td><td>{self.pesoNeto}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BASCULA MARCA</td><td>{self.marca}</td></tr></tbody><tbody><tr><td>NUM SERIE</td><td>{self.numeroSerie}</td></tr></tbody><tbody><tr><td>MOD INSTRUMENTO</td><td>{self.modInstrumento}</td></tr></tbody><tbody><tr><td>APROB MODELO</td><td>{self.aprobModelo}</td></tr></tbody><tbody><tr><td>HOLOGRAMA VERIFI</td><td>{self.hologramaVerificacion}</td></tr></tbody><tbody><tr><td>CERTIFICADO CAL</td><td>{self.certificadoCalidad}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>FIRMA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>_________________________</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>{self.usuario_segunda}</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>OPERADOR DE BASCULA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody>"
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
        logger.debug("Aqui finaliza 2a Pesada")
        self.despuesDeInsertarDatos()

    def insertarDatos3(self):
        logger.debug("Re imprimir Ticket?")
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
                printer.text("Boleto: {}".format(self.NumeroTicket))
                printer.text("RE IMPRESION")
                printer.text("Cliente: {}".format(self.cliente))
                printer.text("Chofer: {}".format(self.operador_salida))
                printer.text("Producto: {}".format(self.producto))
                printer.text("Placas contenedor: {}".format(self.placas_portacontenedor))
                printer.text("C. Contenedor: {}".format(self.claveContenedor))
                printer.text("Primera Pesada: {}".format(self.pesoEntrada))
                printer.text("Fecha/Hora: {}".format(self.EFechaHora))
                printer.text("Segunda Pesada: {}".format(int(self.pesoTara)))
                printer.text("Fecha/Hora: {}".format(self.SFechaHora))
                printer.text("Peso Neto: {}".format(int(self.pesoNeto)))
                printer.text("Peso Total Embalaje: {}".format(self.pesoembalaje))
                printer.text("Peso Neto con Destare: {}".format(int(self.pesoNetoRedondeado)))
                printer.text("Fecha/Hora: {}".format(self.DFechaHora))
                printer.text("Observaciones: {}".format(self.ObservacionesDestare))
                printer.text(" ")
                printer.text("Pesador: {}".format(self.usario_destara))
                printer.text(" ")
                printer.text("________________________________")
                printer.text("Firma de conformidad")

            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_entrada}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>PLACAS CONTENEDOR</td><td>{self.placas_portacontenedor}</td></tr></tbody><tbody><tr><td>C. CONTENEDOR</td><td>{self.claveContenedor}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr><tbody><tbody><tr><td>2A PESADA</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>PESO NETO</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>PESO TOTAL EMBALAJE</td><td>{self.pesoembalaje}</td></tr></tbody><tbody><tr><td>PESO NETO CON DESTARE</td><td>{self.pesoNetoRedondeado}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.DFechaHora}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.ObservacionesDestare}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usario_destara}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>FIRMA DE CONFORMIDAD</td><td>&nbsp;</td></tr></tbody>"
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
                <h3>RE IMPRESION DE TICKET<br/></h3>
                <table class="default">                                                              
                    [DATOS]
                </table>
                    <br>
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

    def insertarDatos4(self):
        logger.debug("Re imprimir Ticket?")


        # Placas
        self.placas_insert = self.Placas.displayText()
        logger.debug("Placas: {}".format(self.placas_insert))

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
        except Exception as e:
            logger.debug("Error BASCULA: {}".format(e))

        # Impresora
        self.impresora = self.comboBox_impresora.currentText()
        logger.debug("Impresora: {}".format(self.impresora))

        # if self.impresora == "Impresora de Cinta":
        #     logger.debug("Se usará impresora de cinta")
        #     Q = QMessageBox()
        #     Q = QMessageBox.information(Q, 'Error',
        #                                 'Utilizar impresora Windows.',
        #                                 QMessageBox.Ok)

            # try:
            #     self.cur.execute("SELECT * FROM totalco_puertocom WHERE id_puerto='1'")
            #     self.row = self.cur.fetchone()
            #     self.pto_impresora = self.row[1]
            #     self.baudrate = self.row[2]
            #     self.bytesize = self.row[3]
            #     self.stopbits = self.row[4]
            #     self.parity = self.row[5]
            #
            #     self.impresora = self.pto_impresora + "," + self.baudrate + "," + self.bytesize + "," + self.stopbits + "," + self.parity
            #     logger.debug("Datos de impresora: {}".format(self.impresora))
            #
            # except Exception as e:
            #     logger.debug("Error: {}".format(e))
            #
            # try:
            #     conn = SerialConnection.create('{}'.format(self.impresora))
            #     printer = GenericESCPOS(conn)
            #     printer.init()
            #     # DATOS DEL TICKET
            #     printer.text("CERTIFICADO DE PESO")
            #     # printer.text("RE IMPRESION")
            #     # printer.text(" ")
            #     printer.text("{}".format(self.empresa))
            #     # printer.text(" ")
            #     printer.text("Placas Portacontenedor: {}".format(self.placas_insert))
            #     printer.text("Empresa(Cliente): {}".format(self.cliente))
            #     printer.text("Linea Transportista: {}".format(self.linea))
            #     # printer.text(" ")
            #     printer.text("PRIMERA PESADA")
            #     printer.text("Ticket: {}".format(self.NumeroTicket))
            #     printer.text("Fecha/Hora: {}".format(self.EFechaHora))
            #     printer.text("Primera Pesada: {}".format(int(self.pesoEntrada)))
            #     # printer.text(" ")
            #     # printer.text("================================")
            #     printer.text("SEGUNDA PESADA")
            #     printer.text("RE IMPRESION")
            #     printer.text("Fecha/Hora: {}".format(self.SFechaHora))
            #     printer.text("Peso: {}".format(int(self.pesoTara)))
            #     # printer.text("================================")
            #     printer.text("Bruto: {}".format(int(self.pesoTara)))
            #     printer.text("Tara: {}".format(int(self.pesoNeto)))
            #     printer.text("Tipo de Contenedor: {}".format(str(self.tipoContenedor)))
            #     printer.text("ID de Contenedor: {}".format(str(self.claveContenedor)))
            #     printer.text("MASA BRUTA VERIFICADA (MBV)=")
            #     printer.text("Verified Gross Mass (VGM)=")
            #     printer.text("Neto: {}".format(int(self.pesoNeto)))
            #     # printer.text("================================")
            #     printer.text("BASCULA MARCA: {}".format(self.marca))
            #     printer.text("Num Serie: {}".format(self.numeroSerie))
            #     printer.text("Mod Instrumento: {}".format(self.modInstrumento))
            #     printer.text("Aprob Modelo: {}".format(self.aprobModelo))
            #     printer.text("Holograma Verifi: {}".format(self.hologramaVerificacion))
            #     printer.text("Certificado Cal: {}".format(self.certificadoCalidad))
            #     # printer.text(" ")
            #     printer.text(" ")
            #     printer.text("Firma: _________________________")
            #     printer.text("{}".format(self.usuario_segunda))
            #     printer.text("Operador de Bascula")
            #     # printer.text(" ")
            #     # printer.text("================================")
            #
            # except Exception as e:
            #     logger.exception("Error con la impresora de tickets: {}".format(e))

        # else:
        logger.debug("Se imprimirá con Windows")
        self.documento = QTextDocument()
        self.documento.clear()

        datos = ""
        item_widget = []
        try:
            datos += f"<br><thead><tr><th>CERTIFICADO DE PESO</th><th></th></tr></thead><tbody><tr><td>RE IMPRESION</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></tbody><tbody><tr><td>PLACAS PORTACONTENEDOR</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>EMPRESA(CLIENTE)</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>LINEA TRANSPORTISTA</td><td>{self.linea}</td></tr></tbody><tbody><tr><td>PRIMERA PESADA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr></tbody><tbody><tr><td>PESO</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><thead><tr><th>SEGUNDA PESADA</th><th></th></tr></thead><tbody><tr><td>FECHA Y HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>PESO</td><td>{self.pesoTara}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BRUTO</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>TARA</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>TIPO DE CONTENEDOR</td><td>{self.tipoContenedor}</td></tr></tbody><tbody><tr><td>ID DE CONTENEDOR</td><td>{self.claveContenedor}</td></tr></tbody><tbody><tr><td>MASA BRUTA VERIFICADA (MBV)=</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>VERIFIED GROSS MASS (VGM) =</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>NETO</td><td>{self.pesoNeto}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>BASCULA MARCA</td><td>{self.marca}</td></tr></tbody><tbody><tr><td>NUM SERIE</td><td>{self.numeroSerie}</td></tr></tbody><tbody><tr><td>MOD INSTRUMENTO</td><td>{self.modInstrumento}</td></tr></tbody><tbody><tr><td>APROB MODELO</td><td>{self.aprobModelo}</td></tr></tbody><tbody><tr><td>HOLOGRAMA VERIFI</td><td>{self.hologramaVerificacion}</td></tr></tbody><tbody><tr><td>CERTIFICADO CAL</td><td>{self.certificadoCalidad}</td></tr></tbody><thead><tr><th>&nbsp;</th><th></th></tr></thead><tbody><tr><td>FIRMA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>_________________________</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>{self.usuario_segunda}</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>OPERADOR DE BASCULA</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody>"
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
        logger.debug("Aqui finaliza 1a y 2a Pesada")
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
            nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Re impresion del destare ticket " + self.NumeroTicket,
                                                           "Archivos PDF (*.pdf);;All Files (*)",
                                                           options=QFileDialog.Options())

            if nombreArchivo:

                impresion = QPrinter(QPrinter.HighResolution)
                impresion.setOutputFormat(QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)

                QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.   ",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.   ",
                                 QMessageBox.Ok)

    def despuesDeInsertarDatos(self):
        reply = QMessageBox.question(
            self, "Message",
            "Ticket Re impreso",
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