from PyQt5.uic import loadUi
import logging
import mysql.connector as mdb
import time
import datetime
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

class imprimirDestareVenta(QDialog):
    def __init__(self, destarar_ticket,destarar_primeraPesada,destarar_segundaPesada,destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp, parent=None):
        super(imprimirDestareVenta, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Imprimir_Destare_Venta.ui', self)
        logger.debug("Operador_Imprimir_Destare_Venta")
        logger.debug("Operador registra Destare de Venta")
        self.DB_Connect()
        self.btnr.clicked.connect(self.regresar)
        self.btn_guardar.clicked.connect(self.ObtenDatos)

        self.NumeroTicket = destarar_ticket
        logger.debug("Número de ticket: {}".format(self.NumeroTicket))
        self.lcdNumber_9.display(self.NumeroTicket)

        self.pesoEntrada = destarar_primeraPesada
        self.lcdNumber_3.display(self.pesoEntrada)

        self.pesoSalida = destarar_segundaPesada
        self.lcdNumber_7.display(self.pesoSalida)

        self.pesoNeto = destarar_pesoNeto
        self.lcdNumber_1.display(self.pesoNeto)

        logger.debug("Valor de yute antes del if: {}".format(pyute))

        if pyute:
            self.yute = pyute
            logger.debug("Valor de yute: {}".format(pyute))
        else:
            self.yute = 0
            logger.debug("Valor de yute vacío")

        if ppropileno:
            self.propileno = ppropileno
            logger.debug("Valor de propileno: {}".format(ppropileno))
        else:
            self.propileno = 0
            logger.debug("Valor de propileno vacío")

        if praspa:
            self.raspa = praspa
            logger.debug("Valor de saco raspa: {}".format(praspa))
        else:
            self.raspa = 0
            logger.debug("Valor de propileno vacío")

        if psaco:
            self.saco = psaco
            logger.debug("Valor del saco: {}".format(psaco))
        else:
            self.saco = 0
            logger.debug("Valor de saco vacío")

        if psaco10:
            self.saco10 = psaco10
            logger.debug("Valor del saco: {}".format(psaco10))
        else:
            self.saco10 = 0
            logger.debug("Valor de saco vacío")

        if ptarima:
            self.tarima = ptarima
            logger.debug("Valor de tarima: {}".format(ptarima))
        else:
            self.tarima = 0
            logger.debug("Valor de tarima vacío")

        if pchep:
            self.chep = pchep
            logger.debug("Valor de tarima chep: {}".format(pchep))
        else:
            self.chep = 0
            logger.debug("Valor de tarima chep vacío")

        if ptreforzada:
            self.treforzada = ptreforzada
            logger.debug("Valor de tarima reforzada: {}".format(ptreforzada))
        else:
            self.treforzada = 0
            logger.debug("Valor de tarima reforzada vacío")

        if psacoesp:
            self.sacoesp = psacoesp
            logger.debug("Valor de saco especial: {}".format(psacoesp))
        else:
            self.sacoesp = 0
            logger.debug("Valor del saco vacío")

        if ptarimaesp:
            self.tarimaesp = ptarimaesp
            logger.debug("Valor de tarima especial: {}".format(ptarimaesp))
        else:
            self.tarimaesp = 0
            logger.debug("Valor de tarima especial vacío")

        self.pesoYute = 1
        self.pesoPropileno = 0.20
        self.pesoRaspa = 0.70
        self.pesoSuperSaco = 3
        self.pesoSuperSaco10 = 10
        self.pesoTarima = 5
        self.pesoTarimaChep = 25
        self.pesoTarimaReforzada = 45

        try:
            self.cur.execute("SELECT peso FROM totalco_saco_tarima WHERE id_st = 1")
            self.row = self.cur.fetchone()
            self.peso_saco_especial = self.row[0]
        except Exception as e:
            logger.debug("Error: {}".format(e))

        logger.debug("Peso saco especial: {}".format(self.peso_saco_especial))

        try:
            self.cur.execute("SELECT peso FROM totalco_saco_tarima WHERE id_st = 2")
            self.row = self.cur.fetchone()
            self.peso_tarima_especial = self.row[0]
        except Exception as e:
            logger.debug("Error: {}".format(e))

        logger.debug("Peso tarima especial: {}".format(self.peso_tarima_especial))

        try:
            self.yuted.setText(str(self.yute))
            self.propilenod.setText(str(self.propileno))
            self.raspad.setText(str(self.raspa))
            self.sacod.setText(str(self.saco))
            self.saco10d.setText(str(self.saco10))
            self.tarimad.setText(str(self.tarima))
            self.chepd.setText(str(self.chep))
            self.treforzadad.setText(str(self.treforzada))
            self.sacoespd.setText(str(self.sacoesp))
            self.tarimaespd.setText(str(self.tarimaesp))
        except Exception as e:
            logger.debug("Error: {}".format(e))

        self.ResPesoYute = int(self.yute) * int(self.pesoYute)
        self.YutePeso.setText(str(self.ResPesoYute))

        self.ResPesoPropi = float(self.propileno) * float(self.pesoPropileno)
        self.PropilenoPeso.setText(str(round(self.ResPesoPropi, 2)))

        self.ResPesoRaspa = float(self.raspa) * float(self.pesoRaspa)
        self.RaspaPeso.setText(str(round(self.ResPesoRaspa, 2)))

        self.ResSaco = int(self.saco) * int(self.pesoSuperSaco)
        self.SacoPeso.setText(str(self.ResSaco))

        self.ResSaco10 = int(self.saco10) * int(self.pesoSuperSaco10)
        self.Saco10Peso.setText(str(self.ResSaco10))

        self.ResTarima = int(self.tarima) * int(self.pesoTarima)
        self.TarimaPeso.setText(str(self.ResTarima))

        self.ResChep = int(self.chep) * int(self.pesoTarimaChep)
        self.ChepPeso.setText(str(self.ResChep))

        self.ResTreforzada = int(self.treforzada) * int(self.pesoTarimaReforzada)
        self.TreforzadaPeso.setText(str(self.ResTreforzada))

        self.ResSacoesp = float(self.sacoesp) * float(self.peso_saco_especial)
        self.SacoespPeso.setText(str(round(self.ResSacoesp, 2)))

        self.ResTarimaEsp = float(self.tarimaesp) * float(self.peso_tarima_especial)
        self.TarimaespPeso.setText(str(round(self.ResTarimaEsp, 2)))

        self.ResTotal = self.ResPesoYute + self.ResPesoPropi + self.ResPesoRaspa + self.ResSaco + self.ResSaco10 + self.ResTarima + self.ResChep + self.ResTreforzada + self.ResSacoesp + self.ResTarimaEsp
        self.EmbalajePeso.setText(str(round(self.ResTotal, 2)))

        self.PesoNetoSinEmbalaje = self.pesoNeto - self.ResTotal
        self.lcdNumber_4.display(self.PesoNetoSinEmbalaje)

        self.PesoNetoSinEmbalajeRedondeado = round(self.PesoNetoSinEmbalaje)
        self.lcdNumber_6.display(self.PesoNetoSinEmbalajeRedondeado)

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
                self.cur.execute(
                    "SELECT pri.id_bol_entra AS ticket, cli.id_cliente AS IDCliente, cli.nombre_cliente AS Cliente, opee.id_operador AS IDOpeEntrada, opee.nombre AS OperadorE, opes.id_operador AS IDOpeSalida, opes.nombre AS OperadorS, trac.id_tractor AS IDTractor, trac.placas AS Placas, prod.id_producto AS IDProducto, prod.nombre_producto AS Producto, pri.fecha_e AS FEntrada, pri.hora_e AS HEntrada,seg.fecha_s AS FSalida, seg.hora_s AS HSalida, usere.id_usuario AS IDUserEntrada, usere.nombre_usuario AS UsuarioE, users.id_usuario AS IDUserSalida, users.nombre_usuario AS UsuarioS, pri.observaciones AS ObservacionesE, seg.observaciones AS ObservacionesS, seg.id_maniobra AS Maniobra, pri.tipo_pesada AS TipoPesadaEntrada, seg.tipo_pesada AS TipoPesadaSalida, porta.id_portacontenedor AS IDPortacontenedor, porta.placas AS PlacasCaja, trans.id_transporte AS IdTransporte, trans.linea AS Linea FROM totalco_boleto_ent pri INNER JOIN totalco_boleto_sal seg ON (pri.id_bol_entra = seg.id_bol_sal) INNER JOIN totalco_cliente cli ON (pri.id_cliente = cli.id_cliente) INNER JOIN totalco_operadores opee ON (pri.id_operador = opee.id_operador) INNER JOIN totalco_operadores opes ON (seg.id_operador = opes.id_operador) INNER JOIN totalco_tractor trac ON (pri.id_tractor = trac.id_tractor) INNER JOIN totalco_producto prod ON (pri.id_producto = prod.id_producto) INNER JOIN usuarios usere ON (pri.id_usuario = usere.id_usuario) INNER JOIN usuarios users ON (seg.id_usuario = users.id_usuario) INNER JOIN totalco_portacontenedor porta ON (pri.id_portacontenedor = porta.id_portacontenedor) INNER JOIN totalco_transporte trans ON (trac.id_transporte = trans.id_transporte) WHERE pri.id_bol_entra ='" + str(
                        self.NumeroTicket) + "'")
                self.row = self.cur.fetchone()

                self.EFechaHora = str(self.row[11]) + " " + str(self.row[12])
                self.SFechaHora = str(self.row[13]) + " " + str(self.row[14])

                self.id_cliente = self.row[1]
                self.cliente = self.row[2]
                self.id_operador_entrada = self.row[3]
                self.operador_entrada = self.row[4]
                self.id_operador_salida = self.row[5]
                self.operador_salida = self.row[6]
                self.id_tractor = self.row[7]
                self.placas = self.row[8]
                self.id_producto = self.row[9]
                self.producto = self.row[10]
                self.fecha_primera = self.row[11]
                self.hora_primera = self.row[12]
                self.fecha_segunda = self.row[13]
                self.hora_segunda = self.row[14]
                self.id_usuario_primera = self.row[15]
                self.usuario_primera = self.row[16]
                self.id_usuario_segunda = self.row[17]
                self.usuario_segunda = self.row[18]
                self.observaciones_entrada = self.row[19]
                self.observaciones_salida = self.row[20]
                self.id_maniobra = self.row[21]
                if self.id_maniobra == 0:
                    self.maniobra = "Interna"
                else:
                    self.maniobra = "Externa"
                self.id_tipo_pesadaEntrada = self.row[22]
                if self.id_tipo_pesadaEntrada == 0:
                    self.tipo_pesadaEntrada = "Automatica"
                else:
                    self.tipo_pesadaEntrada = "Manual"
                self.id_tipo_pesadaSalida = self.row[23]
                if self.id_tipo_pesadaSalida == 0:
                    self.tipo_pesadaSalida = "Automatica"
                else:
                    self.tipo_pesadaSalida = "Manual"

                self.id_portacontenedor = self.row[24]
                self.placas_portacontenedor = self.row[25]

                self.Placas.setText(str(self.placas_portacontenedor))

                self.id_lineatransportista = self.row[26]
                self.linea_transportista = self.row[27]

            except Exception as e:
                logger.debug("Error: {}".format(e))

        else:
            try:
                self.cur.execute("SELECT pri.id_bol_entra AS ticket, cli.id_cliente AS IDCliente, cli.nombre_cliente AS Cliente, opee.id_operador AS IDOpeEntrada, opee.nombre AS OperadorE, opes.id_operador AS IDOpeSalida, opes.nombre AS OperadorS, trac.id_tractor AS IDTractor, trac.placas AS Placas, prod.id_producto AS IDProducto, prod.nombre_producto AS Producto, pri.fecha_e AS FEntrada, pri.hora_e AS HEntrada,seg.fecha_s AS FSalida, seg.hora_s AS HSalida, usere.id_usuario AS IDUserEntrada, usere.nombre_usuario AS UsuarioE, users.id_usuario AS IDUserSalida, users.nombre_usuario AS UsuarioS, pri.observaciones AS ObservacionesE, seg.observaciones AS ObservacionesS, seg.id_maniobra AS Maniobra, pri.tipo_pesada AS TipoPesadaEntrada, seg.tipo_pesada AS TipoPesadaSalida, trans.id_transporte AS IdTransporte, trans.linea AS Linea FROM totalco_boleto_ent pri INNER JOIN totalco_boleto_sal seg ON (pri.id_bol_entra = seg.id_bol_sal) INNER JOIN totalco_cliente cli ON (pri.id_cliente = cli.id_cliente) INNER JOIN totalco_operadores opee ON (pri.id_operador = opee.id_operador) INNER JOIN totalco_operadores opes ON (seg.id_operador = opes.id_operador) INNER JOIN totalco_tractor trac ON (pri.id_tractor = trac.id_tractor) INNER JOIN totalco_producto prod ON (pri.id_producto = prod.id_producto) INNER JOIN usuarios usere ON (pri.id_usuario = usere.id_usuario) INNER JOIN usuarios users ON (seg.id_usuario = users.id_usuario) INNER JOIN totalco_transporte trans ON (trac.id_transporte = trans.id_transporte) WHERE pri.id_bol_entra ='" + str(self.NumeroTicket) + "'")
                self.row = self.cur.fetchone()

                self.EFechaHora = str(self.row[11]) + " " + str(self.row[12])
                self.SFechaHora = str(self.row[13]) + " " + str(self.row[14])

                self.id_cliente = self.row[1]
                self.cliente = self.row[2]
                self.id_operador_entrada = self.row[3]
                self.operador_entrada = self.row[4]
                self.id_operador_salida = self.row[5]
                self.operador_salida = self.row[6]
                self.id_tractor = self.row[7]
                self.placas = self.row[8]
                self.id_producto = self.row[9]
                self.producto = self.row[10]
                self.fecha_primera = self.row[11]
                self.hora_primera = self.row[12]
                self.fecha_segunda = self.row[13]
                self.hora_segunda = self.row[14]
                self.id_usuario_primera = self.row[15]
                self.usuario_primera = self.row[16]
                self.id_usuario_segunda = self.row[17]
                self.usuario_segunda = self.row[18]
                self.observaciones_entrada = self.row[19]
                self.observaciones_salida = self.row[20]
                self.id_maniobra = self.row[21]
                if self.id_maniobra == 0:
                    self.maniobra = "Interna"
                else:
                    self.maniobra = "Externa"
                self.id_tipo_pesadaEntrada = self.row[22]
                if self.id_tipo_pesadaEntrada == 0:
                    self.tipo_pesadaEntrada = "Automatica"
                else:
                    self.tipo_pesadaEntrada = "Manual"
                self.id_tipo_pesadaSalida = self.row[23]
                if self.id_tipo_pesadaSalida == 0:
                    self.tipo_pesadaSalida = "Automatica"
                else:
                    self.tipo_pesadaSalida = "Manual"

                self.id_portacontenedor = None
                self.placas_portacontenedor = None

                self.Placas.setText(str(self.placas))

                self.id_lineatransportista = self.row[24]
                self.linea_transportista = self.row[25]

            except Exception as e:
                logger.debug("Error: {}".format(e))

        self.Cliente.setText(str(self.cliente))
        self.Operador.setText(str(self.operador_salida))
        self.Producto.setText(str(self.producto))
        self.EFecha.setText(str(self.EFechaHora))
        self.SFecha.setText(str(self.SFechaHora))

    def ObtenDatos(self):
        reply = QMessageBox.question(
            self, "Guardar",
            "¿Estás completamente seguro de guardar?",
            QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.insertarDatos()

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

        self.id_identifica_pedido_tipo = 2
        self.identifica_pedido_tipo = "VENTA"

        logger.debug("Tipo de pedido: {} {}".format(self.id_identifica_pedido_tipo, self.identifica_pedido_tipo))

        # Observaciones
        self.observaciones_destare = self.observaciones.displayText()
        logger.debug("Observaciones: {}".format(self.observaciones))

        # Placas
        self.placas_insert = self.Placas.displayText()
        logger.debug("Placas: {}".format(self.placas_insert))

        self.ResTotal2 = self.EmbalajePeso.displayText()
        logger.debug("Peso de Embalaje: {}".format(self.ResTotal2))

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
        self.fecha_destare = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        logger.debug("Fecha: {}".format(self.fecha_destare))

        # Obtener la hora
        self.hora_destare = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        logger.debug("Hora actual: {}".format(self.hora_destare))

        self.fechahoraDestare = self.fecha_destare + " " + self.hora_destare


        # Insert en la base de datos

        #
        # Stattus Destare
        # 1 = completo
        self.status = '1'

        try:
            query = "INSERT INTO totalco_destare(numero_ticket, id_cliente, cliente, id_producto, producto, " \
                    "id_operador_entrada, operador_entrada, id_operador_salida, operador_salida, id_tractor, placas, primera_pesada, fecha_primera, " \
                    "hora_primera, segunda_pesada, fecha_segunda, hora_segunda, peso_neto_embalaje, peso_neto_sin_embalaje, peso_neto_sin_embalaje_redondeo," \
                    "yute, total_peso_yute, propileno, total_peso_propileno, supersaco, total_peso_supersaco, tarimas, total_peso_tarima, total_embalaje, " \
                    "fecha_destare, hora_destare, observaciones, observaciones_entrada, observaciones_salida, id_tipo_pesadaEntrada, tipo_pesadaEntrada, " \
                    "id_tipo_pesadaSalida, tipo_pesadaSalida, id_identifica_pedido_tipo, identifica_pedido_tipo, id_maniobra, maniobra, id_usuario_destara, " \
                    "usuario_desatara, id_usuario_primera, usuario_primera, id_usuario_segunda, usuario_segunda, id_portacontenedor, placas_portacontenedor, status, " \
                    "id_transportista, linea_trasnportista, raspa, total_peso_raspa, super_saco10, total_peso_saco10," \
                    "tarimas_chep, total_peso_tarima_chep, tarimas_reforzada, total_peso_tarima_reforzada, sacos_especiales, total_peso_saco_especial," \
                    "tarimas_especiales, total_peso_tarima_especial) VALUES " \
                    "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'" \
                    ", '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'" \
                    ", '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'," \
                    "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.NumeroTicket, self.id_cliente, self.cliente,
                    self.id_producto, self.producto, self.id_operador_entrada, self.operador_entrada,
                    self.id_operador_salida, self.operador_salida, self.id_tractor, self.placas, self.pesoEntrada, self.fecha_primera, self.hora_primera,
                    self.pesoSalida, self.fecha_segunda, self.hora_segunda, self.pesoNeto, self.PesoNetoSinEmbalaje, self.PesoNetoSinEmbalajeRedondeado, self.yute,
                    self.ResPesoYute, self.propileno, self.ResPesoPropi, self.saco, self.ResSaco, self.tarima, self.ResTarima, self.ResTotal, self.fecha_destare,
                    self.hora_destare, self.observaciones_destare, self.observaciones_entrada, self.observaciones_salida, self.id_tipo_pesadaEntrada, self.tipo_pesadaEntrada,
                    self.id_tipo_pesadaSalida, self.tipo_pesadaSalida, self.id_identifica_pedido_tipo, self.identifica_pedido_tipo, self.id_maniobra, self.maniobra,
                    self.id_usuario, self.pesador, self.id_usuario_primera, self.usuario_primera, self.id_usuario_segunda, self.usuario_segunda,
                    self.id_portacontenedor, self.placas_portacontenedor, self.status, self.id_lineatransportista, self.linea_transportista, self.raspa,
                                                                                                     self.ResPesoRaspa,
                                                                                                     self.saco10,
                                                                                                     self.ResSaco10,
                                                                                                     self.chep,
                                                                                                     self.ResChep,
                                                                                                     self.treforzada,
                                                                                                     self.ResTreforzada,
                                                                                                     self.sacoesp,
                                                                                                     self.ResSacoesp,
                                                                                                     self.tarimaesp,
                                                                                                     self.ResTarimaEsp)
            logger.debug("Query: {}".format(query))
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            logger.debug("Error al insertar en la BD: {}".format(e))

        try:
            query = """ UPDATE totalco_boleto_sal SET destare = %s WHERE id_bol_sal = %s """
            data = (self.status, self.NumeroTicket)
            self.cur.execute(query, data)
            self.conn.commit()
        except Exception as e:
            logger.debug("Error al actualizar el status del destare en la segunda pesada: {}".format(e))

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
                printer.text("Cliente: {}".format(self.cliente))
                printer.text("Chofer: {}".format(self.operador_salida))
                printer.text("Producto: {}".format(self.producto))
                printer.text("Placas: {}".format(self.placas_insert))
                printer.text("Primera Pesada: {}".format(self.pesoEntrada))
                printer.text("Fecha/Hora: {}".format(self.EFechaHora))
                printer.text("Segunda Pesada: {}".format(self.pesoSalida))
                printer.text("Fecha/Hora: {}".format(self.SFechaHora))
                printer.text("Peso Neto: {}".format(self.pesoNeto))
                printer.text("Peso Total Embalaje: {}".format(self.ResTotal2))
                printer.text("Peso Neto con Destare: {}".format(int(self.PesoNetoSinEmbalajeRedondeado)))
                printer.text("Fecha/Hora: {}".format(self.fechahoraDestare))
                printer.text("Observaciones: {}".format(self.observaciones_destare))
                printer.text(" ")
                printer.text("Pesador: {}".format(self.pesador))
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
                datos += f"<tbody><tr><td>EMPRESA</td><td>{self.empresa}</td></tr></thead><tbody><tr><td>BOLETO</td><td>{self.NumeroTicket}</td></tr></tbody><tbody><tr><td>CLIENTE</td><td>{self.cliente}</td></tr></tbody><tbody><tr><td>CHOFER</td><td>{self.operador_salida}</td></tr></tbody><tbody><tr><td>PRODUCTO</td><td>{self.producto}</td></tr></tbody><tbody><tr><td>PLACAS</td><td>{self.placas_insert}</td></tr></tbody><tbody><tr><td>1A PESADA</td><td>{self.pesoEntrada}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.EFechaHora}</td></tr><tbody><tbody><tr><td>2A PESADA</td><td>{self.pesoSalida}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.SFechaHora}</td></tr></tbody><tbody><tr><td>PESO NETO</td><td>{self.pesoNeto}</td></tr></tbody><tbody><tr><td>PESO TOTAL EMBALAJE</td><td>{self.ResTotal2}</td></tr></tbody><tbody><tr><td>PESO NETO CON DESTARE</td><td>{self.PesoNetoSinEmbalajeRedondeado}</td></tr></tbody><tbody><tr><td>FECHA Y HORA</td><td>{self.fechahoraDestare}</td></tr></tbody><tbody><tr><td>OBSERVACIONES</td><td>{self.observaciones_destare}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>PESADOR</td><td>{self.pesador}</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td><br></td><td>&nbsp;</td></tr></tbody><tbody><tr><td>FIRMA DE CONFORMIDAD</td><td>&nbsp;</td></tr></tbody>"
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
            <br>
            <br>
                <table class="default">                                                              
                    [DATOS]
                </table>
                    <br>                    
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
                nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Impresion del destare ticket " + str(self.NumeroTicket),
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