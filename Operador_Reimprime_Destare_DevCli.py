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

class reimprimirDevCliDestare(QDialog):
    def __init__(self, ticketres, parent=None):
        super(reimprimirDevCliDestare, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Reimprime_Destare_DevCli.ui', self)
        logger.debug("Operador_Reimprime_Destare_DevCli")
        logger.debug("Operador re imprime ticket de Devolución de Cliente Destare")
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
            self.cur.execute("SELECT id_portacontenedor FROM totalco_boleto_ent WHERE id_bol_entra ='" + str(self.NumeroTicket) + "'")
            self.row = self.cur.fetchone()
            self.portacontenedor = self.row[0]
        except Exception as e:
            logger.debug("Error: {}".format(e))

        if self.portacontenedor:
            logger.debug("No esta vacio")
            logger.debug("Es una caja")
            try:
                self.cur.execute("SELECT cliente, operador_entrada, producto, fecha_primera, hora_primera, usuario_primera, observaciones_entrada, placas_portacontenedor, primera_pesada, segunda_pesada, peso_neto_embalaje, fecha_segunda, hora_segunda, destino, observaciones_salida, usuario_segunda, total_embalaje, peso_neto_sin_embalaje_redondeo, fecha_destare, hora_destare, observaciones, usuario_desatara, operador_salida, peso_neto_sin_embalaje FROM totalco_destare WHERE numero_ticket ='" + str(self.NumeroTicket) + "'")
                self.row = self.cur.fetchone()

                self.EFechaHora = str(self.row[3]) + " " + str(self.row[4])
                self.cliente = self.row[0]
                self.operador_entrada = self.row[1]
                self.producto = self.row[2]
                self.usuario_primera = self.row[5]
                self.observaciones_entrada = self.row[6]
                self.placas_portacontenedor = self.row[7]
                self.Placas.setText(str(self.placas_portacontenedor))
                self.pesoEntrada = self.row[8]
                self.pesoTara = self.row[9]
                self.pesoNeto = self.row[10]
                self.SFechaHora = str(self.row[11]) + " " + str(self.row[12])
                self.destino = self.row[13]
                self.observaciones_salida = self.row[14]
                self.usuario_segunda = self.row[15]
                self.pesoembalaje = self.row[16]
                self.pesoNetoRedondeado = self.row[17]
                self.DFechaHora = str(self.row[18]) + " " + str(self.row[19])
                self.ObservacionesDestare = self.row[20]
                self.usario_destara = self.row[21]
                self.operador_salida = self.row[22]
                self.pesoNetoSinEmbalaje = self.row[23]

            except Exception as e:
                logger.debug("Error: {}".format(e))
        else:
            logger.debug("Esta vacío")
            logger.debug("Es un torton")
            try:
                self.cur.execute("SELECT cliente, operador_entrada, producto, fecha_primera, hora_primera, usuario_primera, observaciones_entrada, placas, primera_pesada, segunda_pesada, peso_neto_embalaje, fecha_segunda, hora_segunda, destino, observaciones_salida, usuario_segunda, total_embalaje, peso_neto_sin_embalaje_redondeo, fecha_destare, hora_destare, observaciones, usuario_desatara, operador_salida, peso_neto_sin_embalaje FROM totalco_destare WHERE numero_ticket ='" + str(self.NumeroTicket) + "'")
                self.row = self.cur.fetchone()

                self.EFechaHora = str(self.row[3]) + " " + str(self.row[4])
                self.cliente = self.row[0]
                self.operador_entrada = self.row[1]
                self.producto = self.row[2]
                self.usuario_primera = self.row[5]
                self.observaciones_entrada = self.row[6]
                self.placas = self.row[7]
                self.Placas.setText(str(self.placas))
                self.pesoEntrada = self.row[8]
                self.lcdNumber_3.display(self.pesoEntrada)
                self.pesoTara = self.row[9]
                self.pesoNeto = self.row[10]
                self.SFechaHora = str(self.row[11]) + " " + str(self.row[12])
                self.destino = self.row[13]
                self.observaciones_salida = self.row[14]
                self.usuario_segunda = self.row[15]
                self.pesoembalaje = self.row[16]
                self.pesoNetoRedondeado = self.row[17]
                self.DFechaHora = str(self.row[18]) + " " + str(self.row[19])
                self.ObservacionesDestare = self.row[20]
                self.usario_destara = self.row[21]
                self.operador_salida = self.row[22]
                self.pesoNetoSinEmbalaje = self.row[23]

            except Exception as e:
                logger.debug("Error: {}".format(e))

        self.Cliente.setText(str(self.cliente))
        self.Operador.setText(str(self.operador_entrada))
        self.Operador2a.setText(str(self.operador_salida))
        self.Producto.setText(str(self.producto))
        self.EFecha.setText(str(self.EFechaHora))
        self.ObservacionesCompra.setPlainText(str(self.observaciones_entrada))
        self.lcdNumber_3.display(self.pesoEntrada)
        self.lcdNumber_7.display(self.pesoTara)
        self.lcdNumber_1.display(self.pesoNeto)
        self.SFecha.setText(str(self.SFechaHora))
        self.ObservacionesCompra2.setPlainText(str(self.observaciones_salida))

        # self.PesoNetoSinEmbalaje = 0
        self.lcdNumber_4.display(self.pesoNetoSinEmbalaje)

        # self.PesoNetoSinEmbalajeRedondeado = 0
        self.lcdNumber_6.display(self.pesoNetoRedondeado)

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
                printer.text("{}".format(self.empresa))
                printer.text("Boleto # {}".format(self.NumeroTicket))
                printer.text("RE IMPRESION")
                printer.text("Cliente: {}".format(self.cliente))
                printer.text("Primera Pesada: {}".format(self.pesoEntrada))
                printer.text("Fecha/Hora: {}".format(self.EFechaHora))
                printer.text("Placas: {}".format(self.placas_insert))
                printer.text("Producto: {}".format(self.producto))
                printer.text("Chofer: {}".format(self.operador_entrada))
                printer.text("Pesador: {}".format(self.usuario_primera))
                printer.text("Observaciones: {}".format(self.observaciones_entrada))
                printer.text("================================")

            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<thead><tr><th>PRIMERA PESADA</th><th></th></tr></thead><tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr><tbody><tbody><tr><td>PLACAS</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_entrada}</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usuario_primera}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones_entrada}</td></tr></tbody>"
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
                printer.text("Boleto # {}".format(self.NumeroTicket))
                printer.text("RE IMPRESION")
                printer.text("Segunda Pesada: {}".format(int(self.pesoTara)))
                printer.text("Peso Neto: {}".format(int(self.pesoNeto)))
                printer.text("Fecha/Hora: {}".format(self.SFechaHora))
                printer.text("Chofer: {}".format(self.operador_salida))
                printer.text("Pesador: {}".format(self.usuario_segunda))
                printer.text("Destino: {}".format(self.destino))
                printer.text("Observaciones: {}".format(self.observaciones_salida))
                printer.text("================================")

            except Exception as e:
                logger.exception("Error con la impresora de tickets: {}".format(e))

        else:
            logger.debug("Se imprimirá con Windows")
            self.documento = QTextDocument()
            self.documento.clear()

            datos = ""
            item_widget = []
            try:
                datos += f"<tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr><tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><tbody><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody><br><br><br><thead><tr><th>SEGUNDA PESADA</th><th></th></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>2A PESADA</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>PESO NETO</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>FECHA/HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_salida}</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usuario_segunda}</td></tr></tbody><tbody><tr><td>DESTINO</td><td>{self.destino}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones_salida}</td></tr></tbody>"
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
        logger.debug("Aqui finaliza 2a Pesada")
        self.despuesDeInsertarDatos()

    def insertarDatos3(self):
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
                printer.text("{}".format(self.empresa))
                printer.text("Boleto # {}".format(self.NumeroTicket))
                printer.text("RE IMPRESION")
                printer.text("Cliente: {}".format(self.cliente))
                printer.text("Chofer: {}".format(self.operador_salida))
                printer.text("Producto: {}".format(self.producto))
                printer.text("Placas: {}".format(self.placas_insert))
                printer.text("Primera Pesada: {}".format(self.pesoEntrada))
                printer.text("Fecha/Hora: {}".format(self.EFechaHora))
                printer.text("Segunda Pesada: {}".format(self.pesoTara))
                printer.text("Fecha/Hora: {}".format(self.SFechaHora))
                printer.text("Peso Neto: {}".format(self.pesoNeto))
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
                datos += f"<tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></tbody><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_entrada}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>PLACAS</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr><tbody><tbody><tr><td>2A PESADA</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>PESO NETO</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>PESO TOTAL EMBALAJE</td><td>{self.pesoembalaje}</td></tr></tbody><tbody><tr><td>PESO NETO CON DESTARE</td><td>{self.pesoNetoRedondeado}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.DFechaHora}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.ObservacionesDestare}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usario_destara}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>FIRMA DE CONFORMIDAD</td><td>&nbsp;</td></tr></tbody>"
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
        logger.debug("Aqui finaliza 2a Pesada")
        self.despuesDeInsertarDatos()

    def insertarDatos4(self):
        logger.debug("Re imprimir Ticket?")

        # Placas
        self.placas_insert = self.Placas.displayText()
        logger.debug("Placas: {}".format(self.placas_insert))

        #Chofer
        self.chofer = self.Operador2a.displayText()
        logger.debug(f"Chofer: {self.chofer}")

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

        # if self.impresora == "Impresora de Cinta":
        #     logger.debug("Se usará impresora de cinta")
        #     try:
        #         self.cur.execute("SELECT * FROM totalco_puertocom WHERE id_puerto='1'")
        #         self.row = self.cur.fetchone()
        #         self.pto_impresora = self.row[1]
        #         self.baudrate = self.row[2]
        #         self.bytesize = self.row[3]
        #         self.stopbits = self.row[4]
        #         self.parity = self.row[5]
        #
        #         self.impresora = self.pto_impresora + "," + self.baudrate + "," + self.bytesize + "," + self.stopbits + "," + self.parity
        #         logger.debug("Datos de impresora: {}".format(self.impresora))
        #
        #     except Exception as e:
        #         logger.debug("Error: {}".format(e))
        #
        #     try:
        #         conn = SerialConnection.create('{}'.format(self.impresora))
        #         printer = GenericESCPOS(conn)
        #         printer.init()
        #         # DATOS DEL TICKET
        #         printer.text("{}".format(self.empresa))
        #         printer.text("Boleto # {}".format(self.NumeroTicket))
        #         printer.text("RE IMPRESION")
        #         printer.text("Cliente: {}".format(self.cliente))
        #         printer.text("Primera Pesada: {}".format(self.pesoEntrada))
        #         printer.text("Fecha/Hora: {}".format(self.EFechaHora))
        #         printer.text("Placas: {}".format(self.placas_insert))
        #         printer.text("Producto: {}".format(self.producto))
        #         printer.text("Chofer: {}".format(self.operador_entrada))
        #         printer.text("Pesador: {}".format(self.usuario_primera))
        #         printer.text("Observaciones: {}".format(self.observaciones_entrada))
        #         printer.text("================================")
        #         printer.text("Boleto # {}".format(self.NumeroTicket))
        #         printer.text("RE IMPRESION")
        #         printer.text("Segunda Pesada: {}".format(int(self.pesoTara)))
        #         printer.text("Peso Neto: {}".format(int(self.pesoNeto)))
        #         printer.text("Fecha/Hora: {}".format(self.SFechaHora))
        #         printer.text("Chofer: {}".format(self.operador_salida))
        #         printer.text("Pesador: {}".format(self.usuario_segunda))
        #         printer.text("Destino: {}".format(self.destino))
        #         printer.text("Observaciones: {}".format(self.observaciones_salida))
        #         printer.text("================================")
        #
        #     except Exception as e:
        #         logger.exception("Error con la impresora de tickets: {}".format(e))
        #
        # else:
        logger.debug("Se imprimirá con Windows")
        self.documento = QTextDocument()
        self.documento.clear()

        datos = ""
        item_widget = []
        try:
            datos += f"<thead><tr><th>PRIMERA PESADA</th><th></th></tr></thead><tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr><tbody><tbody><tr><td>PLACAS</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_entrada}</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usuario_primera}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones_entrada}</td></tr></tbody><thead><tr><th>SEGUNDA PESADA</th><th></th></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>2A PESADA</td><td>{self.pesoTara}</td></tr></tbody><tbody><tr><td>PESO NETO</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>FECHA/HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_salida}</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.usuario_segunda}</td></tr></tbody><tbody><tr><td>DESTINO</td><td>{self.destino}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones_salida}</td></tr></tbody>"
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
                   border: 1px solid black;
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
            <table class="default" width="100%">                                                                
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
        logger.debug("Aqui finaliza 2a Pesada")
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