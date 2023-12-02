################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice
from PySide2 import QtUiTools
import mysql.connector as mdb
from mysql.connector import Error
import logging
from PySide2.QtGui import QIntValidator
from PySide2 import QtXml

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

# GUI FILE
from app_modules import *

import ctypes
myappid = 'cafestomari.sipcasmo.systemversion.01'# arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Window2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DB_Connect()

        ## EVENT ==> BOTONES
        try:
            # BOTONES PRIMERA PESADA
            self.ui.btn_1a.clicked.connect(self.primera_menu)
            self.ui.btn_back_1p.clicked.connect(self.page_1a_pesada)
            self.ui.btn_entrada.clicked.connect(self.menu_entrada)
            self.ui.btn_back_1p_menu.clicked.connect(self.primera_menu)
            self.ui.btn_1a_compra.clicked.connect(self.primera_menu_tracto_compra)
            self.ui.btn_back_1p_menu_entrada.clicked.connect(self.menu_entrada)
            self.ui.btn_1a_traspaso.clicked.connect(self.primera_menu_tracto_traspaso)
            self.ui.btn_back_1p_menu_entrada_3.clicked.connect(self.menu_entrada)
            self.ui.btn_salida.clicked.connect(self.primera_menu_salida_venta_traspaso)
            self.ui.btn_back_1p_menu_salida_tracto.clicked.connect(self.primera_menu_salida_venta_traspaso)
            self.ui.btn_interno.clicked.connect(self.menu_movin)
            self.ui.btn_back_movin.clicked.connect(self.primera_menu)
            self.ui.btn_devoluciones.clicked.connect(self.menu_devolucion)
            self.ui.btn_back_devoluciones.clicked.connect(self.primera_menu)

            # BOTONES PRIMERA PESADA ==> COMPRA
            self.ui.btnPrimeraPesadaCompraTorton.clicked.connect(self.primeraPesadaCompraTorton)
            self.ui.btnPrimeraPesadaCompraTrailer.clicked.connect(self.primeraPesadaCompraTrailer)

            # BOTONES PRIMERA PESADA ==> TRASPASO # ENTRADA
            self.ui.btnPrimeraPesadaTraspasoTorton.clicked.connect(self.primeraPesadaTraspasoTorton)
            self.ui.btnPrimeraPesadaTraspasoTrailer.clicked.connect(self.primeraPesadaTraspasoTrailer)

            # BOTONES PRIMERA PESADA ==> TRASPASO # SALIDA
            self.ui.btnPrimeraPesadaTraspasoTorton_salida.clicked.connect(self.primeraPesadaSalidaTraspasoTorton)
            self.ui.btnPrimeraPesadaTraspasoTrailer_salida.clicked.connect(self.primeraPesadaSalidaTraspasoTrailer)
            self.ui.btn_regresar_menu_traspaso_salida.clicked.connect(self.primera_menu_salida_venta_traspaso)

            # BOTONES PRIMERA PESADA ==> SALIDA
            self.ui.btn_menu_salida.clicked.connect(self.primera_menu_tracto_salida)
            self.ui.btn_menu_salida_traspaso.clicked.connect(self.primera_menu_tracto_traspaso_salida)
            self.ui.btnPrimeraPesadaSalidaTorton.clicked.connect(self.primeraPesadaSalidaTorton)
            self.ui.btnPrimeraPesadaSalidaTrailer.clicked.connect(self.primeraPesadaSalidaTrailer)
            self.ui.btn_regresar_menu_salida.clicked.connect(self.primera_menu)

            # BOTONES PRIMERA PESADA ==> MOVIMIENTO INTERNO
            self.ui.btn_movin_torton.clicked.connect(self.primeraPesadaInternoTorton)

            # BOTONES PRIMERA PESADA ==> DEVOLUCIONES
            self.ui.btn_dev_decliente.clicked.connect(self.menu_devolucion_Cliente_Torton_Trailer)
            self.ui.btn_dev_aprov.clicked.connect(self.menu_devolucion_Proveedor_Torton_Trailer)

            # BOTONES PRIMERA PESADA ==> DEVOLUCIONES ==> DE CLIENTE
            self.ui.btn_devcliente_regresar.clicked.connect(self.menu_devolucion)
            self.ui.btn_devclient_torton.clicked.connect(self.primeraPesadaDevClienteTorton)
            self.ui.btn_devclient_trailer.clicked.connect(self.primeraPesadaDevClienteTrailer)

            # BOTONES PRIMERA PESADA ==> DEVOLUCIONES == A PROVEEDOR
            self.ui.btn_devprov_regresar.clicked.connect(self.menu_devolucion)
            self.ui.btn_devprov_torton.clicked.connect(self.primeraPesadaDevProvTorton)
            self.ui.btn_devprov_trailer.clicked.connect(self.primeraPesadaDevProvTrailer)

            # BOTON PRIMERA PESADA ==> SOLAS
            self.ui.btn_1a_solas.clicked.connect(self.primeraPesadaSOLAS)

            # BOTONES DATOS
            self.ui.btn_aduana.clicked.connect(self.menu_aduana)
            self.ui.btn_cliente.clicked.connect(self.menu_cliente)
            self.ui.btn_contenedor.clicked.connect(self.menu_contenedor)
            self.ui.btn_transportista.clicked.connect(self.menu_transportista)
            self.ui.btn_operador.clicked.connect(self.menu_operador)
            self.ui.btn_producto.clicked.connect(self.menu_producto)
            self.ui.btn_proveedor.clicked.connect(self.menu_proveedor)
            self.ui.btn_tracto.clicked.connect(self.datos_menu_tractos)
            self.ui.btn_sucursal.clicked.connect(self.menu_sucursal)
            self.ui.btn_destinos.clicked.connect(self.datos_menu_destinos)

            # BOTONES ADUANA
            self.ui.btnBuscarAduana.clicked.connect(self.gotoBuscarAduana)
            self.ui.BuscarlineEditAduana.returnPressed.connect(self.gotoBuscarAduana)
            self.ui.btnNuevaAduana.clicked.connect(self.gotoNuevaAduana)
            self.ui.btnActualizaAduana.clicked.connect(self.gotoActualizaAduana)
            self.ui.btnEliminarAduana.clicked.connect(self.gotoEliminaAduana)
            self.ui.btn_refrescarAduana.clicked.connect(self.gotoRefrescar)

            # BOTONES CLIENTES
            self.ui.btnBuscarCliente.clicked.connect(self.gotoBuscarCliente)
            self.ui.BuscarlineEditCliente.returnPressed.connect(self.gotoBuscarCliente)
            # self.ui.btnEliminarCliente.clicked.connect(self.gotoEliminaCliente)
            self.ui.btnActualizarCliente.clicked.connect(self.gotoActualizaCliente)
            self.ui.btn_refrescarCliente.clicked.connect(self.gotoRefrescarCliente)
            self.ui.btnNuevoCliente.clicked.connect(self.gotoNuevoCliente)

            # BOTONES TRANSPORTISTA
            self.ui.btnBuscarTransportista.clicked.connect(self.gotoBuscarTransportista)
            self.ui.BuscarlineEditTransportista.returnPressed.connect(self.gotoBuscarTransportista)
            # self.ui.btnEliminarTransportista.clicked.connect(self.gotoEliminaTransportista)
            self.ui.btnNuevaLinea.clicked.connect(self.gotoNuevaLinea)
            self.ui.btnActualizarTransportista.clicked.connect(self.gotoActualizaTransportista)
            self.ui.btn_refrescarTransportista.clicked.connect(self.gotoRefrescarTransportista)

            # BOTONES OPERADORES
            self.ui.btnBuscarOperador.clicked.connect(self.gotoBuscarOperador)
            self.ui.BuscarlineEditOperador.returnPressed.connect(self.gotoBuscarOperador)
            # self.ui.btnEliminarOperador.clicked.connect(self.gotoEliminaOperador)
            self.ui.btnNuevoOperador.clicked.connect(self.gotoNuevoOperador)
            self.ui.btn_refrescarOperador.clicked.connect(self.gotoRefrescarOperador)
            self.ui.btnActualizarOperador.clicked.connect(self.gotoActualizaOperador)

            # BOTONES PRODUCTOS
            self.ui.btnBuscarProducto.clicked.connect(self.gotoBuscarProducto)
            self.ui.BuscarlineEditProducto.returnPressed.connect(self.gotoBuscarProducto)
            self.ui.btnEliminarProducto.clicked.connect(self.gotoEliminaProducto)
            self.ui.btnNuevoProducto.clicked.connect(self.gotoNuevoProducto)
            self.ui.btn_refrescarProducto.clicked.connect(self.gotoRefrescarProducto)
            self.ui.btnActualizarProducto.clicked.connect(self.gotoActualizaProducto)

            # BOTONES PROVEEDOR
            self.ui.btnBuscarProveedor.clicked.connect(self.gotoBuscarProveedor)
            self.ui.BuscarlineEditProveedor.returnPressed.connect(self.gotoBuscarProveedor)
            # self.ui.btnEliminarProveedor.clicked.connect(self.gotoEliminaProveedor)
            self.ui.btnNuevoProveedor.clicked.connect(self.gotoNuevoProveedor)
            self.ui.btn_refrescarProveedor.clicked.connect(self.gotoRefrescarProveedor)
            self.ui.btnActualizarProveedor.clicked.connect(self.gotoActualizaProveedor)

            # BOTONES SUCURSALES
            self.ui.btnBuscarSucursal.clicked.connect(self.gotoBuscarSucursal)
            self.ui.BuscarlineEditSucursal.returnPressed.connect(self.gotoBuscarSucursal)
            self.ui.btnEliminarSucursal.clicked.connect(self.gotoeliminarSucursal)
            self.ui.btnNuevoSucursal.clicked.connect(self.gotoNuevoSucursal)
            self.ui.btn_refrescarSucursal.clicked.connect(self.gotoRefrescarSucursal)
            self.ui.btnActualizarSucursal.clicked.connect(self.gotoActualizarSucursal)

            # BOTONES MENU TRACTOS
            self.ui.btn_back_menutracto.clicked.connect(self.datos_menu)
            self.ui.btn_TipoTracto.clicked.connect(self.menu_tipoTracto)
            self.ui.btn_CajaPorta.clicked.connect(self.menu_cajaporta)
            self.ui.btn_Tractos.clicked.connect(self.menu_tracto)

            # BOTONES TIPOS DE TRACTOS
            self.ui.btn_tiptrac_regresar.clicked.connect(self.datos_menu_tractos)
            self.ui.btnBuscarTipoTracto.clicked.connect(self.gotoBuscarTipoTracto)
            self.ui.BuscarlineEditTipoTracto.returnPressed.connect(self.gotoBuscarTipoTracto)
            # self.ui.btnEliminarTipoTracto.clicked.connect(self.gotoeliminarTipoTracto)
            # self.ui.btnNuevoTipoTracto.clicked.connect(self.gotoNuevoTipoTracto)
            self.ui.btn_refrescarTipoTracto.clicked.connect(self.gotoRefrescarTipoTracto)
            # self.ui.btnActualizarTipoTracto.clicked.connect(self.gotoActualizarTipoTracto)

            # BOTONES CAJA/PORTACONTENEDOR
            self.ui.btn_porta_regresar.clicked.connect(self.datos_menu_tractos)
            self.ui.btnBuscarCajaPorta.clicked.connect(self.gotoBuscarCajaPorta)
            self.ui.BuscarlineEditCajaPorta.returnPressed.connect(self.gotoBuscarCajaPorta)
            # self.ui.btnEliminarCajaPorta.clicked.connect(self.gotoeliminarCajaPorta)
            self.ui.btnNuevoCajaPorta.clicked.connect(self.gotoNuevoCajaPorta)
            self.ui.btn_refrescarCajaPorta.clicked.connect(self.gotoRefrescarCajaPorta)
            self.ui.btnActualizarCajaPorta.clicked.connect(self.gotoActualizarCajaPorta)

            # BOTONES TRACTOS
            self.ui.btn_tracto_regresar.clicked.connect(self.datos_menu_tractos)
            self.ui.btnBuscarTracto.clicked.connect(self.gotoBuscarTracto)
            self.ui.BuscarlineEditTracto.returnPressed.connect(self.gotoBuscarTracto)
            # self.ui.btnEliminarTracto.clicked.connect(self.gotoeliminarTracto)
            self.ui.btnNuevoTracto.clicked.connect(self.gotoNuevoTracto)
            self.ui.btn_refrescarTracto.clicked.connect(self.gotoRefrescarTracto)
            self.ui.btnActualizarTracto.clicked.connect(self.gotoActualizarTracto)

            # BOTONES DESTINOS
            self.ui.btn_back_menudatos.clicked.connect(self.datos_menu)
            self.ui.btnDestinoventas.clicked.connect(self.menu_destinoventas)
            self.ui.btnSolas.clicked.connect(self.menu_destinosolas)
            self.ui.btnSucursal.clicked.connect(self.menu_destinosucursal)
            self.ui.btnSifon.clicked.connect(self.menu_sifon)

            # BOTONES DESTINOS ==> DESTINO VENTAS
            self.ui.btn_destinovtas_regresar.clicked.connect(self.datos_menu_destinos)
            self.ui.btnBuscarDestinoVta.clicked.connect(self.gotoBuscarDestinoVta)
            self.ui.BuscarlineEditDestinoVta.returnPressed.connect(self.gotoBuscarDestinoVta)
            self.ui.btnEliminarDestinovta.clicked.connect(self.gotoeliminardestinovta)
            self.ui.btnNuevoDestinovta.clicked.connect(self.gotoNuevodestinovta)
            self.ui.btn_refrescarDestinovta.clicked.connect(self.gotoRefrescarDestinovta)
            self.ui.btnActualizarDestinovta.clicked.connect(self.gotoActualizarDestinovta)

            # BOTONES DESTINOS ==> DESTINO SOLAS
            self.ui.btn_destinosolas_regresar.clicked.connect(self.datos_menu_destinos)
            self.ui.btnBuscarDestinoSolas.clicked.connect(self.gotoBuscarDestinoSolas)
            self.ui.BuscarlineEditDestinoSolas.returnPressed.connect(self.gotoBuscarDestinoSolas)
            self.ui.btnEliminarDestinosolas.clicked.connect(self.gotoeliminardestinoSolas)
            self.ui.btnNuevoDestinosolas.clicked.connect(self.gotoNuevodestinoSolas)
            self.ui.btn_refrescarDestinosolas.clicked.connect(self.gotoRefrescarDestinoSolas)
            self.ui.btnActualizarDestinosolas.clicked.connect(self.gotoActualizarDestinoSolas)

            # BOTONES DESTINOS ==> DESTINO SUCURSAL
            self.ui.btn_destinosucursal_regresar.clicked.connect(self.datos_menu_destinos)
            self.ui.btnBuscarDestinoSucursal.clicked.connect(self.gotoBuscarDestinoSucursal)
            self.ui.BuscarlineEditDestinoSucursal.returnPressed.connect(self.gotoBuscarDestinoSucursal)
            self.ui.btnEliminarDestinoSucursal.clicked.connect(self.gotoeliminardestinoSucursal)
            self.ui.btnNuevoDestinoSucursal.clicked.connect(self.gotoNuevodestinoSucursal)
            self.ui.btn_refrescarDestinoSucursal.clicked.connect(self.gotoRefrescarDestinoSucursal)
            self.ui.btnActualizarDestinoSucursal.clicked.connect(self.gotoActualizarDestinoSucursal)

            # BOTONES DESTINOS ==> DESTINO BODEGA/SIFON/MAQUILA
            self.ui.btn_destinosifon_regresar.clicked.connect(self.datos_menu_destinos)
            self.ui.btnBuscarDestinoSifon.clicked.connect(self.gotoBuscarDestinoSifon)
            self.ui.BuscarlineEditDestinoSifon.returnPressed.connect(self.gotoBuscarDestinoSifon)
            self.ui.btnEliminarDestinoSifon.clicked.connect(self.gotoeliminardestinoSifon)
            self.ui.btnNuevoDestinoSifon.clicked.connect(self.gotoNuevodestinoSifon)
            self.ui.btn_refrescarDestinoSifon.clicked.connect(self.gotoRefrescarDestinoSifon)
            self.ui.btnActualizarDestinoSifon.clicked.connect(self.gotoActualizarDestinoSifon)

            # BOTONES MENU CONTENEDORES
            self.ui.btn_crudContenedor.clicked.connect(self.menu_crudcontenedor)
            self.ui.btn_tipoContenedor.clicked.connect(self.menu_tipocontenedor)

            # BOTONOTES MENU CONTENEDORES ==> TIPO DE CONTENEDORES
            self.ui.btn_TipoCon_regresar.clicked.connect(self.menu_contenedor)
            self.ui.btnBuscarTipoCont.clicked.connect(self.gotoBuscarTipoCont)
            self.ui.BuscarlineEditTipoCont.returnPressed.connect(self.gotoBuscarTipoCont)
            # self.ui.btnEliminarTipoCont.clicked.connect(self.gotoEliminarTipoCont)
            self.ui.btnNuevoTipoCont.clicked.connect(self.gotoNuevoTipoCont)
            self.ui.btn_refrescarTipoCont.clicked.connect(self.gotoRefrescarTipoCont)
            self.ui.btnActualizarTipoCont.clicked.connect(self.gotoActualizarTipoCont)

            # BOTONES MENU CONTENEDORES ==> CRUD CONTENEDORES
            self.ui.btn_CrudCont_regresar.clicked.connect(self.menu_contenedor)
            self.ui.btnBuscarContenedor.clicked.connect(self.gotoBuscarContenedor)
            self.ui.BuscarlineEditContenedor.returnPressed.connect(self.gotoBuscarContenedor)
            # self.ui.btnEliminarContenedor.clicked.connect(self.gotoEliminarContenedor)
            self.ui.btnNuevoContenedor.clicked.connect(self.gotoNuevoContenedor)
            self.ui.btn_refrescarContenedor.clicked.connect(self.gotoRefrescarContenedor)
            self.ui.btnActualizarContenedor.clicked.connect(self.gotoActualizarContenedor)

            # BOTONES SEGUNDA PESADA
            self.ui.btn_analisisSegundaPesada.clicked.connect(self.analizaSegundaPesada)
            self.ui.btn_ActualizaTablaSegunda.clicked.connect(self.actualizaTablaSegundaPesada)

            # BOTONES DESTARE
            self.ui.btn_actualizarDestare.clicked.connect(self.actualizaTablaDestare)
            self.ui.btn_destarar.clicked.connect(self.analizaDestare)
            self.ui.btn_calcular.clicked.connect(self.registrarDestare)
            self.ui.btn_regresarTablaDestare.clicked.connect(self.btn_regresarTablaDestare)

            # BOTONES CANCELACIONES
            self.ui.btn_cancela.clicked.connect(self.analizaticketacancelar)
            self.ui.ticket_cancela.returnPressed.connect(self.analizaticketacancelar)

            # BOTONES RE IMPRESION
            self.ui.btn_reimpresion.clicked.connect(self.analizaticketreimpresion)
            self.ui.ticket_reimpresion.returnPressed.connect(self.analizaticketreimpresion)

            # BOTONES REPORTES
            self.ui.btn_ToExcel.clicked.connect(self.reportToExcel)

            # BOTONES SACO-TARIMA
            self.ui.btn_tarimas.clicked.connect(self.menu_sacotarima)
            self.ui.btn_refrescarSacoTarima.clicked.connect(self.gotoRefrescarSacoTarima)
            self.ui.btnActualizaSacoTarima.clicked.connect(self.gotoActualizaSacoTarima)

        except Exception as e:
            logger.debug(e)

        ## ==> END ##

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('SIPCASMO')
        ## ==> END ##

        ## ==> COMPANY
        try:
            self.cur.execute("SELECT * FROM totalco_info_gral")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("User: {}".format(self.row_authenticate[2]))
            UIFunctions.labelTitle(self, '{}'.format(self.row_authenticate[2]))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))
        ## ==> END ##

        ## ==> USER
        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("User: {}".format(self.row_authenticate[5]))
            UIFunctions.labelDescription(self, 'Usuario: {}'.format(self.row_authenticate[5]))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

        ## ==> END ##
        # System
        # print('Sistema: ' + platform.system())
        # print('Version: ' +platform.release())

        self.sistema = platform.system()
        self.version = platform.release()
        self.ui.label_credits.setText(self.sistema + ' ' + self.version)


        #UIFunctions.labelDescription(self, 'User')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "PRIMERA PESADA", "page_1a_pesada", "url(:/24x24/icons/24x24/ct-romana1.png)", True)
        UIFunctions.addNewMenu(self, "SEGUNDA PESADA", "btn_2a_pesada", "url(:/24x24/icons/24x24/ct-romana2.png)", True)
        UIFunctions.addNewMenu(self, "DESTARE", "btn_destare", "url(:/24x24/icons/24x24/ct-destare5.png)", True)
        UIFunctions.addNewMenu(self, "RE IMPRESION", "btn_impresion", "url(:/24x24/icons/24x24/ct-impresion.png)", True)
        UIFunctions.addNewMenu(self, "REPORTES", "btn_report", "url(:/24x24/icons/24x24/ct-reporte.png)", True)
        UIFunctions.addNewMenu(self, "CANCELACIONES", "btn_cancela", "url(:/24x24/icons/24x24/ct-cancela.png)", True)
        UIFunctions.addNewMenu(self, "DATOS", "btn_data", "url(:/24x24/icons/24x24/ct-datos.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_report")
        ## ==> END ##

        ## ==> START PAGE
        ## ==> CHANGE TO REPORTS
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_reportes)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, " ", "", True)
        ## ==> END ##

        ###

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DATABASE CONECCT
    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    ## ==> END ##

    ## REPORTE ##
    def reportToExcel(self):
        logger.debug("Reporte a Excel")
        from Operador_Reporte_Excel import operadorCreateExcel
        goto = operadorCreateExcel()
        goto.exec_()

    ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE 1A PESADA
        if btnWidget.objectName() == "page_1a_pesada":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1a_pesada)
            UIFunctions.resetStyle(self, "page_1a_pesada")
            UIFunctions.labelPage(self, "1a Pesada")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE 2A PESADA
        if btnWidget.objectName() == "btn_2a_pesada":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2a_pesada)
            UIFunctions.resetStyle(self, "btn_2a_pesada")
            UIFunctions.labelPage(self, "2a Pesada")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            try:
                self.cur.execute("SELECT id_bol_entra,peso_e,identifica_pedido_tipo,id_tractor,fecha_e,hora_e,solas,id_portacontenedor,cancelado FROM `totalco_boleto_ent` WHERE completo = '0' AND cancelado IS Null ORDER BY `id_bol_entra` ASC")
                self.resultados = self.cur.fetchall()
                self.ui.table_2a.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        if resultado[8] == None:
                            def pedido1():
                                self.tipoPedido = str("Compra")
                            def pedido2():
                                if resultado[6] == 0:
                                    self.tipoPedido = str("Venta")
                                else:
                                    self.tipoPedido = str("Exportación SOLAS")
                            def pedido3():
                                self.tipoPedido = str("Movimiento Interno")
                            def pedido4():
                                self.tipoPedido = str("Traspaso entre Sucursales")
                            def pedido5():
                                self.tipoPedido = str("Devolución a Proveedor")
                            def pedido6():
                                self.tipoPedido = str("Devolución de Cliente")

                            # Python switch
                            pedido = resultado[2]
                            options = {1: pedido1,
                                       2: pedido2,
                                       3: pedido3,
                                       4: pedido4,
                                       5: pedido5,
                                       6: pedido6,
                                       }
                            options[pedido]()

                            if resultado[7] != None:
                                logger.debug("Diferente de NULL es un trailer, puede ser caja o porta contenedor {} {}".format(resultado[7], resultado[0]))
                                self.id_contenedor = resultado[7]
                                logger.debug("Id Contenedor: {}".format(self.id_contenedor))
                                try:
                                    self.cur.execute("SELECT * FROM totalco_portacontenedor WHERE id_portacontenedor ='" + str(self.id_contenedor) + "'")
                                    self.row = self.cur.fetchone()
                                    self.placas = self.row[1]
                                    self.caja_porta = self.row[2]
                                    logger.debug("Placas Caja/Porta: {}".format(self.placas))
                                    # logger.debug("Caja o Porta contendor: {}".format(self.caja_porta))
                                    if self.caja_porta == 0:
                                        logger.debug("Caja")
                                    else:
                                        logger.debug("Portacontenedor")
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("En un Torton")
                                self.id_tracto = resultado[3]
                                logger.debug("Id tracto: {}".format(self.id_tracto))
                                # self.placas = str("Torton")
                                try:
                                    self.cur.execute("SELECT * FROM totalco_tractor WHERE id_tractor ='" + str(self.id_tracto) + "'")
                                    self.row = self.cur.fetchone()
                                    self.placas = self.row[3]
                                    self.caja_porta = 2
                                    logger.debug("Placas Torton: {}".format(self.placas))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                            self.ui.table_2a.setRowCount(fila + 1)
                            self.ui.table_2a.setColumnHidden(0, True)
                            self.ui.table_2a.setColumnHidden(7, True)
                            self.ui.table_2a.setColumnHidden(8, True)
                            self.ui.table_2a.setItem(fila, 0, QTableWidgetItem(str(resultado[2])))
                            self.ui.table_2a.setItem(fila, 1, QTableWidgetItem(str(resultado[0])))
                            self.ui.table_2a.setItem(fila, 2, QTableWidgetItem(str(resultado[1])))
                            self.ui.table_2a.setItem(fila, 3, QTableWidgetItem(str(self.tipoPedido)))
                            self.ui.table_2a.setItem(fila, 4, QTableWidgetItem(str(self.placas)))
                            self.ui.table_2a.setItem(fila, 5, QTableWidgetItem(str(resultado[4])))
                            self.ui.table_2a.setItem(fila, 6, QTableWidgetItem(str(resultado[5])))
                            self.ui.table_2a.setItem(fila, 7, QTableWidgetItem(str(resultado[6])))
                            self.ui.table_2a.setItem(fila, 8, QTableWidgetItem(str(self.caja_porta)))
                            fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

        # PAGE DESTARE
        if btnWidget.objectName() == "btn_destare":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_destare)
            UIFunctions.resetStyle(self, "btn_destare")
            UIFunctions.labelPage(self, "DESTARE")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            # self.ui.tabla_destare.clearContents()
            try:
                self.cur.execute(
                    "SELECT pri.id_bol_entra AS ticket, pri.peso_e AS PE, pri.identifica_pedido_tipo AS PedidoTipo, pri.id_tractor AS Tractor, pri.fecha_e AS FEntrada, pri.hora_e AS HEntrada, pri.solas AS TSolas, pri.id_portacontenedor AS Portacontenedor, pri.cancelado AS CanceladoPri, seg.peso_tara AS PS, seg.peso_neto AS PN, seg.cancelado AS CanceladoSegunda from totalco_boleto_ent pri INNER JOIN totalco_boleto_sal seg ON (pri.id_bol_entra = seg.id_bol_sal) WHERE pri.cancelado IS Null AND seg.cancelado IS Null AND seg.destare IS Null")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_destare.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        if resultado[8] == None:
                            def pedido1():
                                self.tipoPedido = str("Compra")

                            def pedido2():
                                if resultado[6] == 0:
                                    self.tipoPedido = str("Venta")
                                else:
                                    self.tipoPedido = str("Exportación SOLAS")

                            def pedido3():
                                self.tipoPedido = str("Movimiento Interno")

                            def pedido4():
                                self.tipoPedido = str("Traspaso entre Sucursales")

                            def pedido5():
                                self.tipoPedido = str("Devolución a Proveedor")

                            def pedido6():
                                self.tipoPedido = str("Devolución de Cliente")

                            # Python switch
                            pedido = resultado[2]
                            options = {1: pedido1,
                                       2: pedido2,
                                       3: pedido3,
                                       4: pedido4,
                                       5: pedido5,
                                       6: pedido6,
                                       }
                            options[int(pedido)]()

                            if resultado[7] != None:
                                logger.debug(
                                    "Diferente de NULL es un trailer, puede ser caja o porta contenedor {} {}".format(
                                        resultado[7], resultado[0]))
                                self.id_contenedor = resultado[7]
                                logger.debug("Id Contenedor: {}".format(self.id_contenedor))
                                try:
                                    self.cur.execute("SELECT * FROM totalco_portacontenedor WHERE id_portacontenedor ='" + str(self.id_contenedor) + "'")
                                    self.row = self.cur.fetchone()
                                    self.placas = self.row[1]
                                    self.caja_porta = self.row[2]
                                    logger.debug("Placas Caja/Porta: {}".format(self.placas))
                                    # logger.debug("Caja o Porta contendor: {}".format(self.caja_porta))
                                    if self.caja_porta == 0:
                                        logger.debug("Caja")
                                    else:
                                        logger.debug("Portacontenedor")
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("En un Torton")
                                self.id_tracto = resultado[3]
                                logger.debug("Id tracto: {}".format(self.id_tracto))
                                # self.placas = str("Torton")
                                try:
                                    self.cur.execute(
                                        "SELECT * FROM totalco_tractor WHERE id_tractor ='" + str(self.id_tracto) + "'")
                                    self.row = self.cur.fetchone()
                                    self.placas = self.row[3]
                                    self.caja_porta = 2
                                    logger.debug("Placas Torton: {}".format(self.placas))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                            self.ui.tabla_destare.setRowCount(fila + 1)
                            self.ui.tabla_destare.setColumnHidden(6, True)
                            self.ui.tabla_destare.setColumnHidden(7, True)
                            self.ui.tabla_destare.setColumnHidden(8, True)
                            self.ui.tabla_destare.setColumnHidden(9, True)
                            self.ui.tabla_destare.setColumnHidden(10, True)
                            self.ui.tabla_destare.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_destare.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_destare.setItem(fila, 2, QTableWidgetItem(str(resultado[9])))
                            self.ui.tabla_destare.setItem(fila, 3, QTableWidgetItem(str(resultado[10])))
                            self.ui.tabla_destare.setItem(fila, 4, QTableWidgetItem(str(self.tipoPedido)))
                            self.ui.tabla_destare.setItem(fila, 5, QTableWidgetItem(str(self.placas)))
                            self.ui.tabla_destare.setItem(fila, 6, QTableWidgetItem(str(resultado[4])))
                            self.ui.tabla_destare.setItem(fila, 7, QTableWidgetItem(str(resultado[5])))
                            self.ui.tabla_destare.setItem(fila, 8, QTableWidgetItem(str(resultado[6])))
                            self.ui.tabla_destare.setItem(fila, 9, QTableWidgetItem(str(self.caja_porta)))
                            self.ui.tabla_destare.setItem(fila, 10, QTableWidgetItem(str(resultado[2])))

                            fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

        # PAGE RE IMPRESION
        if btnWidget.objectName() == "btn_impresion":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_impresion)
            UIFunctions.resetStyle(self, "btn_impresion")
            UIFunctions.labelPage(self, "RE IMPRESION")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            #Se limpia el campo de ticket
            self.ui.ticket_reimpresion.clear()
            # Ticket Re impresión
            r1 = self.ui.ticket_reimpresion
            r1.objectName()
            r1.setValidator(QIntValidator())

        # PAGE REPORTES
        if btnWidget.objectName() == "btn_report":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_reportes)
            UIFunctions.resetStyle(self, "btn_report")
            UIFunctions.labelPage(self, "REPORTES")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE CANCELACIONES
        if btnWidget.objectName() == "btn_cancela":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_cancelaciones)
            UIFunctions.resetStyle(self, "btn_cancela")
            UIFunctions.labelPage(self, "CANCELACIONES")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            # Se limpia el campo de ticket
            self.ui.ticket_cancela.clear()
            # Ticket Cancelaciones
            c1 = self.ui.ticket_cancela
            c1.objectName()
            c1.setValidator(QIntValidator())

        # PAGE DATOS
        if btnWidget.objectName() == "btn_data":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_datos)
            UIFunctions.resetStyle(self, "btn_data")
            UIFunctions.labelPage(self, "DATOS")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> PRIMERA PESADA
    def page_1a_pesada(self):
        logger.debug("Home 1a Pesada Torton/Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1a_pesada)
        UIFunctions.resetStyle(self, "page_1a_pesada")
        UIFunctions.labelPage(self, "1a Pesada")

    def primera_menu(self):
        logger.debug("Menu para primera pesada (Entrada/Salida/Interno/Devolucion/Cancelacion)")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_primera_menu)
        UIFunctions.labelPage(self, "Menú Primera Pesada")
        UIFunctions.labelPage(self, "1a Pesada")

    def menu_entrada(self):
        logger.debug("Menu Entrada")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menu_entrada)
        UIFunctions.labelPage(self, "Primera Pesada Entrada")
        UIFunctions.labelPage(self, "Entrada")

    def primera_menu_tracto_compra(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1a_compra_menu_Tracto)
        UIFunctions.labelPage(self, "Primera Pesada Compra ")
        UIFunctions.labelPage(self, "Compra")

    def primera_menu_tracto_traspaso(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1a_traspaso_menu_tracto)
        UIFunctions.labelPage(self, "Primera Pesada Traspaso")
        UIFunctions.labelPage(self, "Traspaso")

    def primera_menu_tracto_traspaso_salida(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1a_traspaso_menu_tracto_salida)
        UIFunctions.labelPage(self, "Primera Pesada Traspaso Salida")
        UIFunctions.labelPage(self, "Traspaso")

    def primera_menu_salida_venta_traspaso(self):
        logger.debug("Selecciona salida o traspaso")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menu_salida)
        UIFunctions.labelPage(self, "Primera Pesada Salida")
        UIFunctions.labelPage(self, "Salida")

    def primera_menu_tracto_salida(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_salida_selecciona_tracto)
        UIFunctions.labelPage(self, "Primera Pesada Salida")
        UIFunctions.labelPage(self, "Salida")

    def menu_movin(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_movin)
        UIFunctions.labelPage(self, "Movimiento Interno")
        UIFunctions.labelPage(self, "Movimiento Interno")

    def menu_devolucion(self):
        logger.debug("Selecciona de Cliente o A Proveedor")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menu_devolucion)
        UIFunctions.labelPage(self, "Devoluciones de Clientes o a Proveedor")
        UIFunctions.labelPage(self, "Menu Devoluciones")

    def menu_devolucion_Cliente_Torton_Trailer(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_devolucion_Cliente_TorTra)
        UIFunctions.labelPage(self, "Devoluciones de Clientes")
        UIFunctions.labelPage(self, "Torton o Trailer")

    def menu_devolucion_Proveedor_Torton_Trailer(self):
        logger.debug("Selecciona Torton o Trailer")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_devolucion_Proveedor_TorTra)
        UIFunctions.labelPage(self, "Devoluciones de Clientes")
        UIFunctions.labelPage(self, "Torton o Trailer")

    ## ==> END ##

    ## ==> RE IMPRESIONES
    def analizaticketreimpresion(self):
        logger.debug("Analiza ticket para reimpresión")
        self.ticketareimprimir = self.ui.ticket_reimpresion.displayText()
        logger.debug("Ticket: {}".format(self.ticketareimprimir))
        if self.ticketareimprimir:
            try:
                self.cur.execute("SELECT numero_ticket FROM `totalco_destare` WHERE numero_ticket ='" + str(
                    self.ticketareimprimir) + "'")
                self.row = self.cur.fetchone()

                logger.debug("ROW Tabla Destare: {}".format(self.row))

                if self.row is None:
                    logger.debug("NO Existe el ticket en el Destare: {}".format(self.ticketareimprimir))
                    try:
                        self.cur.execute(
                            "SELECT id_bol_sal, cancelado FROM `totalco_boleto_sal` WHERE id_bol_sal ='" + str(
                                self.ticketareimprimir) + "'")
                        self.row = self.cur.fetchone()
                        logger.debug("ROW Tabla 2a Pesada: {}".format(self.row))
                        if self.row is None:
                            logger.debug("No existe el ticket {} en la 2a pesada".format(self.ticketareimprimir))
                            try:
                                self.cur.execute(
                                    "SELECT id_bol_entra, cancelado FROM `totalco_boleto_ent` WHERE id_bol_entra ='" + str(
                                        self.ticketareimprimir) + "'")
                                self.row = self.cur.fetchone()
                                logger.debug("ROW Tabla 1a Pesada: {}".format(self.row))
                                if self.row is None:
                                    logger.debug("No existe el ticket {} en la 1a pesada".format(self.ticketareimprimir))
                                    QMessageBox.critical(self, "NO EXISTE",
                                                         "No existe el ticket {}".format(self.ticketareimprimir),
                                                         QMessageBox.Ok)
                                    self.ui.ticket_reimpresion.clear()
                                else:
                                    logger.debug("Si existe en la 1a Pesada")
                                    logger.debug("Se analiza si ya esta cancelado")
                                    try:
                                        self.cur.execute(
                                            "SELECT cancelado FROM `totalco_boleto_ent` WHERE id_bol_entra ='" + str(
                                                self.ticketareimprimir) + "'")
                                        self.row = self.cur.fetchone()
                                        logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                                        if self.row[0] is None:
                                            logger.debug("El valor es Null, NO esta cancelado")
                                            self.tabla_re = 1
                                            self.seleccionaReimprimir()
                                        else:
                                            QMessageBox.critical(self, "Mensaje",
                                                                 "El ticket {} está cancelado.".format(
                                                                     self.ticketareimprimir),
                                                                 QMessageBox.Ok)
                                            self.ui.ticket_reimpresion.clear()

                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                                    logger.debug("Listo para re imprimir el ticket(1aPesada)")

                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                        else:
                            logger.debug("Si existe en la Segunda Pesada")
                            logger.debug("Se analiza si ya esta cancelado")
                            try:
                                self.cur.execute(
                                    "SELECT cancelado FROM `totalco_boleto_sal` WHERE id_bol_sal ='" + str(
                                        self.ticketareimprimir) + "'")
                                self.row = self.cur.fetchone()
                                logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                                if self.row[0] is None:
                                    logger.debug("El valor es Null, NO esta cancelado")
                                    self.tabla_re = 2
                                    self.seleccionaReimprimir()
                                else:
                                    QMessageBox.critical(self, "Mensaje",
                                                         "El ticket {} está cancelado.".format(
                                                             self.ticketareimprimir),
                                                         QMessageBox.Ok)
                                    self.ui.ticket_reimpresion.clear()

                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                            logger.debug("Listo para re imprimir el ticket(2aPesada)")

                    except Exception as e:
                        logger.debug("Error: {}".format(e))
                else:
                    logger.debug("Si existe el ticket {} en el Desatare".format(self.ticketareimprimir))
                    logger.debug("Se analiza si ya esta cancelado")
                    try:
                        self.cur.execute("SELECT cancelado FROM `totalco_destare` WHERE numero_ticket ='" + str(
                            self.ticketareimprimir) + "'")
                        self.row = self.cur.fetchone()
                        logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                        if self.row[0] is None:
                            logger.debug("El valor es Null, NO esta cancelado")
                            self.tabla_re = 3
                            self.seleccionaReimprimir()
                        else:
                            QMessageBox.critical(self, "Mensaje",
                                                 "El ticket {} está cancelado.".format(self.ticketareimprimir),
                                                 QMessageBox.Ok)
                            self.ui.ticket_reimpresion.clear()

                    except Exception as e:
                        logger.debug("Error: {}".format(e))
                    logger.debug("Listo para re imprimir el ticket(DESTARE)")

            except Error as e:
                logger.debug("Error: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes ingresar el número de ticket.   ", QMessageBox.Ok)
            self.ui.ticket_reimpresion.setFocus()

    def seleccionaReimprimir(self):
        logger.debug("Seleccion Reimprimir")
        logger.debug("Ticket: {}".format(self.ticketareimprimir))
        logger.debug("Valor en tabla: {}".format(self.tabla_re))

        # Python switch
        def tablar1():
            logger.debug("Selecciona Reimprimir Primera Pesada")
            try:
                self.cur.execute("SELECT identifica_pedido_tipo, solas FROM `totalco_boleto_ent` WHERE id_bol_entra='" + str(self.ticketareimprimir) + "'")
                self.row = self.cur.fetchone()
                self.identifica_pedido_tipo_re = self.row[0]
                self.solas_rep = self.row[1]
                self.primeraticketareiimprimir()
            except Exception as e:
                logger.debug("Error: {}".format(e))

        def tablar2():
            logger.debug("Selecciona Reimprimir Segunda Pesada")
            try:
                self.cur.execute("SELECT identifica_pedido_tipo, solas FROM `totalco_boleto_sal` WHERE id_bol_entra='" + str(self.ticketareimprimir) + "'")
                self.row = self.cur.fetchone()
                self.identifica_pedido_tipo_re = self.row[0]
                self.solas_res = self.row[1]
                self.segundaticketareiimprimir()
            except Exception as e:
                logger.debug("Error: {}".format(e))

        def tablar3():
            logger.debug("Selecciona Reimprimir Destare")
            try:
                self.cur.execute("SELECT id_identifica_pedido_tipo, solas FROM `totalco_destare` WHERE numero_ticket='" + str(self.ticketareimprimir) + "'")
                self.row = self.cur.fetchone()
                self.identifica_pedido_tipo_re = self.row[0]
                if self.row[1] is None:
                    self.solas_red = 0
                else:
                    self.solas_red = 1
                self.destareticketareiimprimir()
            except Exception as e:
                logger.debug("Error Printer??: {}".format(e))

        options = {1: tablar1,
                   2: tablar2,
                   3: tablar3,
                   }
        options[int(self.tabla_re)]()

    def primeraticketareiimprimir(self):
        logger.debug("Primera Restribuye")
        logger.debug("Ticket: {}".format(self.ticketareimprimir))
        logger.debug("Tipo de Pedido: {}".format(self.identifica_pedido_tipo_re))
        logger.debug("Solas: {}".format(self.solas_rep))
        if self.solas_rep == 1:
            self.identifica_pedido_tipo_re = 7
        ticketrep = self.ticketareimprimir

        # Python switch
        def tablare1():
            logger.debug("Compra")
            from Operador_Reimprime_Compra import reimprimirCompra
            goto = reimprimirCompra(ticketrep)
            goto.exec_()

        def tablare2():
            logger.debug("Venta")
            from Operador_Reimprime_Venta import reimprimirVenta
            goto = reimprimirVenta(ticketrep)
            goto.exec_()

        def tablare3():
            logger.debug("Movimiento Interno")
            from Operador_Reimprime_MovInt import reimprimirMovInt
            goto = reimprimirMovInt(ticketrep)
            goto.exec_()

        def tablare4():
            logger.debug("Traspaso entre Sucursales¾")
            from Operador_Reimprime_Traspaso import reimprimirTraspaso
            goto = reimprimirTraspaso(ticketrep)
            goto.exec_()

        def tablare5():
            logger.debug("Devolución a proveedor")
            from Operador_Reimprime_DevProv import reimprimirDevProv
            goto = reimprimirDevProv(ticketrep)
            goto.exec_()

        def tablare6():
            logger.debug("Devolución de Cliente")
            from Operador_Reimprime_DevCli import reimprimirDevCli
            goto = reimprimirDevCli(ticketrep)
            goto.exec_()

        def tablare7():
            logger.debug("SOLAS")
            from Operador_Reimprime_SOLAS import reimprimirVentaSolas
            goto = reimprimirVentaSolas(ticketrep)
            goto.exec_()

        options = {1: tablare1,
                   2: tablare2,
                   3: tablare3,
                   4: tablare4,
                   5: tablare5,
                   6: tablare6,
                   7: tablare7,
                   }
        options[int(self.identifica_pedido_tipo_re)]()

    def segundaticketareiimprimir(self):
        logger.debug("Segunda Restribuye")
        logger.debug("2a Pesada Ticket: {}".format(self.ticketareimprimir))
        logger.debug("2a Pesada Tipo de Pedido: {}".format(self.identifica_pedido_tipo_re))
        logger.debug("2a Pesada Solas: {}".format(self.solas_res))
        if self.solas_res == 1:
            self.identifica_pedido_tipo_re = 7
        ticketres = self.ticketareimprimir

        # Python switch
        def tablares1():
            logger.debug("2a Pesada Compra")
            from Operador_Reimprime_Segunda_Compra import reimprimirCompraSegunda
            goto = reimprimirCompraSegunda(ticketres)
            goto.exec_()

        def tablares2():
            logger.debug("Venta")
            from Operador_Reimprime_Segunda_Venta import reimprimirVentaSegunda
            goto = reimprimirVentaSegunda(ticketres)
            goto.exec_()

        def tablares3():
            logger.debug("Movimiento Interno")
            from Operador_Reimprime_Segunda_MovInt import reimprimirMovIntSegunda
            goto = reimprimirMovIntSegunda(ticketres)
            goto.exec_()

        def tablares4():
            logger.debug("Traspaso entre Sucursales")
            from Operador_Reimprime_Segunda_Traspaso import reimprimirTraspasoSegunda
            goto = reimprimirTraspasoSegunda(ticketres)
            goto.exec_()

        def tablares5():
            logger.debug("Devolución a proveedor")
            from Operador_Reimprime_Segunda_DevPro import reimprimirDevProSegunda
            goto = reimprimirDevProSegunda(ticketres)
            goto.exec_()

        def tablares6():
            logger.debug("Devolución de Cliente")
            from Operador_Reimprime_Segunda_DevCli import reimprimirDevCliSegunda
            goto = reimprimirDevCliSegunda(ticketres)
            goto.exec_()

        def tablares7():
            logger.debug("SOLAS")
            from Operador_Reimprime_Segunda_Venta_SOLAS import reimprimirVentaSolasSegunda
            goto = reimprimirVentaSolasSegunda(ticketres)
            goto.exec_()

        options = {1: tablares1,
                   2: tablares2,
                   3: tablares3,
                   4: tablares4,
                   5: tablares5,
                   6: tablares6,
                   7: tablares7,
                   }
        options[int(self.identifica_pedido_tipo_re)]()

    def destareticketareiimprimir(self):
        logger.debug("Tercera Restribuye")
        logger.debug("Ticket: {}".format(self.ticketareimprimir))
        logger.debug("Tipo de Pedido: {}".format(self.identifica_pedido_tipo_re))
        logger.debug("Solas: {}".format(self.solas_red))
        if self.solas_red == 1:
            self.identifica_pedido_tipo_re = 7
        ticketred = self.ticketareimprimir

        # Python switch
        def tablared1():
            logger.debug("Compra")
            from Operador_Reimprime_Destare_Compra import reimprimirCompraDestare
            goto = reimprimirCompraDestare(ticketred)
            goto.exec_()

        def tablared2():
            logger.debug("Venta")
            from Operador_Reimprime_Destare_Venta import reimprimirVentaDestare
            goto = reimprimirVentaDestare(ticketred)
            goto.exec_()

        def tablared3():
            logger.debug("Movimiento Interno")
            from Operador_Reimprime_Destare_MovInt import reimprimirMovIntDestare
            goto = reimprimirMovIntDestare(ticketred)
            goto.exec_()

        def tablared4():
            logger.debug("Traspaso de Sucursal")
            from Operador_Reimprime_Destare_Traspaso import reimprimirTraspasoDestare
            goto = reimprimirTraspasoDestare(ticketred)
            goto.exec_()

        def tablared5():
            logger.debug("Devolución a proveedor")
            from Operador_Reimprime_Destare_DevProv import reimprimirDevProvDestare
            goto = reimprimirDevProvDestare(ticketred)
            goto.exec_()

        def tablared6():
            logger.debug("Devolución de Cliente")
            from Operador_Reimprime_Destare_DevCli import reimprimirDevCliDestare
            goto = reimprimirDevCliDestare(ticketred)
            goto.exec_()

        def tablared7():
            logger.debug("SOLAS")
            from Operador_Reimprime_Destare_Venta_SOLAS import reimprimirVentaSolasDestare
            goto = reimprimirVentaSolasDestare(ticketred)
            goto.exec_()


        options = {1: tablared1,
                   2: tablared2,
                   3: tablared3,
                   4: tablared4,
                   5: tablared5,
                   6: tablared6,
                   7: tablared7,
                   }
        options[int(self.identifica_pedido_tipo_re)]()

    ## ==> END ##

    ## ==> CANCELACIONES ##
    def analizaticketacancelar(self):
        logger.debug("Analiza ticket a cancelar")
        self.ticketacancelar = self.ui.ticket_cancela.displayText()
        logger.debug("Ticket: {}".format(self.ticketacancelar))
        if self.ticketacancelar:
            try:
                self.cur.execute("SELECT numero_ticket FROM `totalco_destare` WHERE numero_ticket ='" + str(self.ticketacancelar) + "'")
                self.row = self.cur.fetchone()

                logger.debug("ROW Tabla Destare: {}".format(self.row))

                if self.row is None:
                    logger.debug("NO Existe el ticket en el Destare: {}".format(self.ticketacancelar))
                    try:
                        self.cur.execute("SELECT id_bol_sal, cancelado FROM `totalco_boleto_sal` WHERE id_bol_sal ='" + str(self.ticketacancelar) + "'")
                        self.row = self.cur.fetchone()
                        logger.debug("ROW Tabla 2a Pesada: {}".format(self.row))
                        if self.row is None:
                            logger.debug("No existe el ticket {} en la 2a pesada".format(self.ticketacancelar))
                            try:
                                self.cur.execute(
                                    "SELECT id_bol_entra, cancelado FROM `totalco_boleto_ent` WHERE id_bol_entra ='" + str(
                                        self.ticketacancelar) + "'")
                                self.row = self.cur.fetchone()
                                logger.debug("ROW Tabla 1a Pesada: {}".format(self.row))
                                if self.row is None:
                                    logger.debug("No existe el ticket {} en la 1a pesada".format(self.ticketacancelar))
                                    QMessageBox.critical(self, "NO EXISTE", "No existe el ticket {}".format(self.ticketacancelar),
                                                         QMessageBox.Ok)
                                    self.ui.ticket_cancela.clear()
                                else:
                                    logger.debug("Si existe en la 1a Pesada")
                                    logger.debug("Se analiza si ya esta cancelado")
                                    try:
                                        self.cur.execute(
                                            "SELECT cancelado FROM `totalco_boleto_ent` WHERE id_bol_entra ='" + str(
                                                self.ticketacancelar) + "'")
                                        self.row = self.cur.fetchone()
                                        logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                                        if self.row[0] is None:
                                            logger.debug("El valor es Null, NO esta cancelado")
                                            self.tabla = 1
                                            self.seleccionaCancelar()
                                        else:
                                            QMessageBox.critical(self, "Mensaje",
                                                                 "El ticket {} ya esta cancelado.".format(
                                                                     self.ticketacancelar),
                                                                 QMessageBox.Ok)
                                            self.ui.ticket_cancela.clear()

                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                                    logger.debug("Listo para cancelar el ticket(1aPesada)")

                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                        else:
                            logger.debug("Si existe en la Segunda Pesada")
                            logger.debug("Se analiza si ya esta cancelado")
                            try:
                                self.cur.execute(
                                    "SELECT cancelado FROM `totalco_boleto_sal` WHERE id_bol_sal ='" + str(
                                        self.ticketacancelar) + "'")
                                self.row = self.cur.fetchone()
                                logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                                if self.row[0] is None:
                                    logger.debug("El valor es Null, NO esta cancelado")
                                    self.tabla = 2
                                    self.seleccionaCancelar()
                                else:
                                    QMessageBox.critical(self, "Mensaje",
                                                         "El ticket {} ya esta cancelado.".format(
                                                             self.ticketacancelar),
                                                         QMessageBox.Ok)
                                    self.ui.ticket_cancela.clear()

                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                            logger.debug("Listo para cancelar el ticket(2aPesada)")

                    except Exception as e:
                        logger.debug("Error: {}".format(e))
                else:
                    logger.debug("Si existe el ticket {} en el Desatare".format(self.ticketacancelar))
                    logger.debug("Se analiza si ya esta cancelado")
                    try:
                        self.cur.execute("SELECT cancelado FROM `totalco_destare` WHERE numero_ticket ='" + str(self.ticketacancelar) + "'")
                        self.row = self.cur.fetchone()
                        logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
                        if self.row[0] is None:
                            logger.debug("El valor es Null, NO esta cancelado")
                            self.tabla = 3
                            self.seleccionaCancelar()
                        else:
                            QMessageBox.critical(self, "Mensaje", "El ticket {} ya esta cancelado.".format(self.ticketacancelar),
                                                 QMessageBox.Ok)
                            self.ui.ticket_cancela.clear()

                    except Exception as e:
                        logger.debug("Error: {}".format(e))
                    logger.debug("Listo para cancelar el ticket(DESTARE)")

            except Error as e:
                logger.debug("Error: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes ingresar el número de ticket.   ", QMessageBox.Ok)
            self.ui.ticket_cancela.setFocus()

    def seleccionaCancelar(self):
        logger.debug("Selecciona Cancelar")
        logger.debug("Ticket: {}".format(self.ticketacancelar))
        logger.debug("Tabla en la que se encuentra es: {}".format(self.tabla))
        ticketc = self.ticketacancelar

        # Python switch
        def tabla1():
            logger.debug("Primera Pesada")
            from Operador_Cancela_EnPrimera import operadorCancelaEnPrimera
            goto = operadorCancelaEnPrimera(ticketc)
            goto.exec_()

        def tabla2():
            logger.debug("Segunda Pesada")
            from Operador_Cancela_EnSegunda import operadorCancelaEnSegunda
            goto = operadorCancelaEnSegunda(ticketc)
            goto.exec_()

        def tabla3():
            logger.debug("Destare")
            from Operador_Cancela_EnDestare import operadorCancelaEnDestare
            goto = operadorCancelaEnDestare(ticketc)
            goto.exec_()

        options = {1: tabla1,
                   2: tabla2,
                   3: tabla3,
                   }
        options[int(self.tabla)]()


    ## ==> END ##

    ## ==> DESTARE ##
    def actualizaTablaDestare(self):
        logger.debug("Actualiza la tabla")
        try:
            self.cur.execute(
                "SELECT pri.id_bol_entra AS ticket, pri.peso_e AS PE, pri.identifica_pedido_tipo AS PedidoTipo, pri.id_tractor AS Tractor, pri.fecha_e AS FEntrada, pri.hora_e AS HEntrada, pri.solas AS TSolas, pri.id_portacontenedor AS Portacontenedor, pri.cancelado AS CanceladoPri, seg.peso_tara AS PS, seg.peso_neto AS PN, seg.cancelado AS CanceladoSegunda from totalco_boleto_ent pri INNER JOIN totalco_boleto_sal seg ON (pri.id_bol_entra = seg.id_bol_sal) WHERE pri.cancelado IS Null AND seg.cancelado IS Null AND seg.destare IS Null")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_destare.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    if resultado[8] == None:
                        def pedido1():
                            self.tipoPedido = str("Compra")

                        def pedido2():
                            if resultado[6] == 0:
                                self.tipoPedido = str("Venta")
                            else:
                                self.tipoPedido = str("Exportación SOLAS")

                        def pedido3():
                            self.tipoPedido = str("Movimiento Interno")

                        def pedido4():
                            self.tipoPedido = str("Traspaso entre Sucursales")

                        def pedido5():
                            self.tipoPedido = str("Devolución a Proveedor")

                        def pedido6():
                            self.tipoPedido = str("Devolución de Cliente")

                        # Python switch
                        pedido = resultado[2]
                        options = {1: pedido1,
                                   2: pedido2,
                                   3: pedido3,
                                   4: pedido4,
                                   5: pedido5,
                                   6: pedido6,
                                   }
                        options[int(pedido)]()

                        if resultado[7] != None:
                            logger.debug(
                                "Diferente de NULL es un trailer, puede ser caja o porta contenedor {} {}".format(
                                    resultado[7], resultado[0]))
                            self.id_contenedor = resultado[7]
                            logger.debug("Id Contenedor: {}".format(self.id_contenedor))
                            try:
                                self.cur.execute(
                                    "SELECT * FROM totalco_portacontenedor WHERE id_portacontenedor ='" + str(
                                        self.id_contenedor) + "'")
                                self.row = self.cur.fetchone()
                                self.placas = self.row[1]
                                self.caja_porta = self.row[2]
                                logger.debug("Placas Caja/Porta: {}".format(self.placas))
                                # logger.debug("Caja o Porta contendor: {}".format(self.caja_porta))
                                if self.caja_porta == 0:
                                    logger.debug("Caja")
                                else:
                                    logger.debug("Portacontenedor")
                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                        else:
                            logger.debug("En un Torton")
                            self.id_tracto = resultado[3]
                            logger.debug("Id tracto: {}".format(self.id_tracto))
                            # self.placas = str("Torton")
                            try:
                                self.cur.execute(
                                    "SELECT * FROM totalco_tractor WHERE id_tractor ='" + str(self.id_tracto) + "'")
                                self.row = self.cur.fetchone()
                                self.placas = self.row[3]
                                self.caja_porta = 2
                                logger.debug("Placas Torton: {}".format(self.placas))
                            except Exception as e:
                                logger.debug("Error: {}".format(e))

                        self.ui.tabla_destare.setRowCount(fila + 1)
                        self.ui.tabla_destare.setColumnHidden(6, True)
                        self.ui.tabla_destare.setColumnHidden(7, True)
                        self.ui.tabla_destare.setColumnHidden(8, True)
                        self.ui.tabla_destare.setColumnHidden(9, True)
                        self.ui.tabla_destare.setColumnHidden(10, True)
                        self.ui.tabla_destare.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_destare.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_destare.setItem(fila, 2, QTableWidgetItem(str(resultado[9])))
                        self.ui.tabla_destare.setItem(fila, 3, QTableWidgetItem(str(resultado[10])))
                        self.ui.tabla_destare.setItem(fila, 4, QTableWidgetItem(str(self.tipoPedido)))
                        self.ui.tabla_destare.setItem(fila, 5, QTableWidgetItem(str(self.placas)))
                        self.ui.tabla_destare.setItem(fila, 6, QTableWidgetItem(str(resultado[4])))
                        self.ui.tabla_destare.setItem(fila, 7, QTableWidgetItem(str(resultado[5])))
                        self.ui.tabla_destare.setItem(fila, 8, QTableWidgetItem(str(resultado[6])))
                        self.ui.tabla_destare.setItem(fila, 9, QTableWidgetItem(str(self.caja_porta)))
                        self.ui.tabla_destare.setItem(fila, 10, QTableWidgetItem(str(resultado[2])))
                        fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def analizaDestare(self):
        logger.debug("Analiza tabla de destare")
        self.filaSeleccionada = self.ui.tabla_destare.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                ticket = self.ui.tabla_destare.item(indiceFila, 0).text()
                pesoEntrada = self.ui.tabla_destare.item(indiceFila, 1).text()
                pesoSalida = self.ui.tabla_destare.item(indiceFila, 2).text()
                pesoNeto = self.ui.tabla_destare.item(indiceFila, 3).text()

                logger.debug("Ticket: {}".format(ticket))
                logger.debug("Primera Pesada: {}".format(pesoEntrada))
                logger.debug("Segunda Pesada: {}".format(pesoSalida))
                logger.debug("Peso Neto: {}".format(pesoNeto))

                self.calcularDestare(ticket, pesoEntrada, pesoSalida, pesoNeto)
            else:
                QMessageBox.critical(self, "Destarar Tcket", "Primero seleccione una ticket.   ", QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    def calcularDestare(self, ticket, pesoEntrada, pesoSalida, pesoNeto):
        logger.debug("Calcular Destare")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_calcular_destare)
        UIFunctions.labelPage(self, "MENU CALCULAR DESTARE")

        logger.debug("Ticket: {}".format(ticket))
        logger.debug("Primera Pesada: {}".format(pesoEntrada))
        logger.debug("Segunda Pesada: {}".format(pesoSalida))
        logger.debug("Peso Neto: {}".format(pesoNeto))

        self.ui.lcdNumber_ticket.display(ticket)
        self.ui.lcdNumber_1p.display(pesoEntrada)
        self.ui.lcdNumber_2p.display(pesoSalida)
        self.ui.lcdNumber_pn.display(pesoNeto)

        self.ui.yute.clear()
        self.ui.propileno.clear()
        self.ui.raspa.clear()
        self.ui.saco.clear()
        self.ui.saco10.clear()
        self.ui.tarima.clear()
        self.ui.chep.clear()
        self.ui.treforzada.clear()

        # Sacos Yute
        e1 = self.ui.yute
        e1.objectName()
        e1.setValidator(QIntValidator())

        # Sacos Propileno
        e2 = self.ui.propileno
        e2.objectName()
        e2.setValidator(QIntValidator())

        # Sacos raspa
        e3 = self.ui.raspa
        e3.objectName()
        e3.setValidator(QIntValidator())

        # Super Saco 3 Kg
        e4 = self.ui.saco
        e4.objectName()
        e4.setValidator(QIntValidator())

        # Super Saco 10 Kg
        e5 = self.ui.saco10
        e5.objectName()
        e5.setValidator(QIntValidator())

        # Tarima
        e6 = self.ui.tarima
        e6.objectName()
        e6.setValidator(QIntValidator())

        # Tarima Azul chep
        e7 = self.ui.chep
        e7.objectName()
        e7.setValidator(QIntValidator())

        # Tarima reforzada
        e8 = self.ui.treforzada
        e8.objectName()
        e8.setValidator(QIntValidator())

        # Saco especial
        e9 = self.ui.sacoesp
        e9.objectName()
        e9.setValidator(QIntValidator())

        # Tarima especial
        e10 = self.ui.tarimaesp
        e10.objectName()
        e10.setValidator(QIntValidator())

    def registrarDestare(self):

        destarar_ticket = int(self.ui.lcdNumber_ticket.value())
        logger.debug("Ticket: {}".format(destarar_ticket))
        self.ticketPesoNeto = destarar_ticket

        destarar_primeraPesada = int(self.ui.lcdNumber_1p.value())
        logger.debug("Primera Pesada: {}".format(destarar_primeraPesada))

        destarar_segundaPesada = int(self.ui.lcdNumber_2p.value())
        logger.debug("Segunda Pesada: {}".format(destarar_segundaPesada))

        destarar_pesoNeto = int(self.ui.lcdNumber_pn.value())
        logger.debug("Peso Neto: {}".format(destarar_pesoNeto))

        pyute = self.ui.yute.displayText()
        logger.debug("Yute: {}".format(pyute))

        ppropileno = self.ui.propileno.displayText()
        logger.debug("Propileno: {}".format(ppropileno))

        praspa = self.ui.raspa.displayText()
        logger.debug("Raspa: {}".format(praspa))

        psaco = self.ui.saco.displayText()
        logger.debug("Super Saco: {}".format(psaco))

        psaco10 = self.ui.saco10.displayText()
        logger.debug("Super Saco: {}".format(psaco10))

        ptarima = self.ui.tarima.displayText()
        logger.debug("Tarima: {}".format(ptarima))

        pchep = self.ui.chep.displayText()
        logger.debug("Tarima chep: {}".format(pchep))

        ptreforzada = self.ui.treforzada.displayText()
        logger.debug("Tarima reforzada: {}".format(ptreforzada))

        psacoesp = self.ui.sacoesp.displayText()
        logger.debug("Saco especial: {}".format(psacoesp))

        ptarimaesp = self.ui.tarimaesp.displayText()
        logger.debug("Tarima especial: {}".format(ptarimaesp))

        if pyute:
            self.yute = pyute
            logger.debug("Valor de yute: {}".format(pyute))
        else:
            self.yute = 0
            logger.debug("Valor de yute vacío: {}".format(self.yute))

        if ppropileno:
            self.propileno = ppropileno
            logger.debug("Valor de propileno: {}".format(ppropileno))
        else:
            self.propileno = 0
            logger.debug("Valor de propileno vacío: {}".format(self.propileno))

        if praspa:
            self.raspa = praspa
            logger.debug("Valor de saco raspa: {}".format(praspa))
        else:
            self.raspa = 0
            logger.debug("Valor de propileno vacío: {}".format(self.raspa))

        if psaco:
            self.saco = psaco
            logger.debug("Valor del saco: {}".format(psaco))
        else:
            self.saco = 0
            logger.debug("Valor de saco vacío: {}".format(self.saco))

        if psaco10:
            self.saco10 = psaco10
            logger.debug("Valor del forro de contenedor: {}".format(psaco10))
        else:
            self.saco10 = 0
            logger.debug("Valor del forro de contenedor: {}".format(self.saco10))

        if ptarima:
            self.tarima = ptarima
            logger.debug("Valor de tarima: {}".format(ptarima))
        else:
            self.tarima = 0
            logger.debug("Valor de tarima vacío: {}".format(self.tarima))

        if pchep:
            self.chep = pchep
            logger.debug("Valor de tarima chep: {}".format(pchep))
        else:
            self.chep = 0
            logger.debug("Valor de tarima chep vacío: {}".format(self.chep))

        if ptreforzada:
            self.treforzada = ptreforzada
            logger.debug("Valor de tarima reforzada: {}".format(ptreforzada))
        else:
            self.treforzada = 0
            logger.debug("Valor de tarima reforzada vacío: {}".format(self.treforzada))

        if psacoesp:
            self.sacoesp = psacoesp
            logger.debug("Valor de saco especial: {}".format(self.sacoesp))
        else:
            self.sacoesp = 0
            logger.debug("Valor del saco vacío: {}".format(self.sacoesp))

        if ptarimaesp:
            self.tarimaesp = ptarimaesp
            logger.debug("Valor de tarima especial: {}".format(ptarimaesp))
        else:
            self.tarimaesp = 0
            logger.debug("Valor de tarima especial vacío: {}".format(self.tarimaesp))

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


        self.ResPesoYute = int(self.yute) * int(self.pesoYute)
        logger.debug("Peso Total Yute: {}".format(self.ResPesoYute))

        self.ResPesoPropi = float(self.propileno) * float(self.pesoPropileno)
        logger.debug("Peso Total Propileno: {}".format(self.ResPesoPropi))

        self.ResPesoRaspa = float(self.raspa) * float(self.pesoRaspa)
        logger.debug("Peso Total Raspa: {}".format(self.ResPesoRaspa))

        self.ResSaco = int(self.saco) * int(self.pesoSuperSaco)
        logger.debug("Peso Total Super Saco: {}".format(self.ResSaco))

        self.ResSaco10 = int(self.saco10) * int(self.pesoSuperSaco10)
        logger.debug("Peso Total Forro contenedor: {}".format(self.ResSaco10))

        self.ResTarima = int(self.tarima) * int(self.pesoTarima)
        logger.debug("Peso Total Tarima: {}".format(self.ResTarima))

        self.ResChep = int(self.chep) * int(self.pesoTarimaChep)
        logger.debug("Peso Total Tarima Chep: {}".format(self.ResChep))

        self.ResTarimaReforzada = int(self.treforzada) * int(self.pesoTarimaReforzada)
        logger.debug("Peso Total Tarima Reforzada: {}".format(self.ResTarimaReforzada))

        logger.debug("Numero de sacos: {}".format(self.sacoesp))
        logger.debug("Peso de saco especial: {}".format(self.peso_saco_especial))
        self.ResSacoEspecial = float(self.sacoesp) * float(round(self.peso_saco_especial,3))
        logger.debug("Multiplicacion: {} x {} = {}".format(self.sacoesp, self.peso_saco_especial, self.ResSacoEspecial))

        logger.debug("Peso Total Saco Especial: {}".format(self.ResSacoEspecial))

        self.ResTarimaEspecial = float(self.tarimaesp) * float(self.peso_tarima_especial)
        logger.debug("Peso Total Tarima Especial: {}".format(self.ResTarimaEspecial))

        self.ResTotal = self.ResPesoYute + self.ResPesoPropi + self.ResPesoRaspa + self.ResSaco + self.ResSaco10 + self.ResTarima + self.ResChep + self.ResTarimaReforzada + self.ResSacoEspecial + self.ResTarimaEspecial

        try:
            self.cur.execute("SELECT peso_neto FROM `totalco_boleto_sal` WHERE id_bol_entra ='" + str(self.ticketPesoNeto) + "'")
            self.row = self.cur.fetchone()
            self.pesoNeto2a = self.row[0]
            logger.debug("Peso Neto 2a: {}".format(self.pesoNeto2a))

            if self.ResTotal > self.pesoNeto2a:
                logger.debug("Peso de embalaje: {}".format(self.ResTotal))
                logger.debug("Error, el embalaje no puede ser mayor al peso neto")
                reply = QMessageBox.question(self, "Mensaje", "El peso del embalaje no puede ser mayor al peso neto", QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return
            else:
                try:
                    self.cur.execute("SELECT status FROM `totalco_destare` WHERE numero_ticket ='" + str(destarar_ticket) + "'")
                    self.row = self.cur.fetchone()
                    if self.row is None:
                        logger.debug("Inicia el registro del Destare")
                        try:
                            self.cur.execute(
                                "SELECT identifica_pedido_tipo, solas FROM `totalco_boleto_ent` WHERE id_bol_entra ='" + str(
                                    destarar_ticket) + "'")
                            self.row = self.cur.fetchone()
                            pedido = self.row[0]
                            solas = self.row[1]
                            logger.debug("Pedido: {}".format(pedido))
                            logger.debug("Solas: {}".format(solas))
                        except Exception as e:
                            logger.debug("Error: {}".format(e))

                        if int(solas) == 1:
                            logger.debug("Es SOLAS")
                            from Operador_Imprimir_Destare_SOLAS import imprimirDestareVentaSOLAS
                            goto = imprimirDestareVentaSOLAS(destarar_ticket, destarar_primeraPesada,
                                                             destarar_segundaPesada,
                                                             destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                            goto.exec_()
                        else:
                            logger.debug("No es SOLAS")

                            def pedido1():
                                logger.debug("Compra")

                                from Operador_Imprimir_Destare_Compra import imprimirDestareCompra
                                goto = imprimirDestareCompra(destarar_ticket, destarar_primeraPesada,
                                                             destarar_segundaPesada,
                                                             destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            def pedido2():
                                logger.debug("Venta")
                                from Operador_Imprimir_Destare_Venta import imprimirDestareVenta
                                goto = imprimirDestareVenta(destarar_ticket, destarar_primeraPesada,
                                                            destarar_segundaPesada,
                                                            destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            def pedido3():
                                logger.debug("Movimiento Interno")
                                from Operador_Imprimir_Destare_Interno import imprimirDestareInterno
                                goto = imprimirDestareInterno(destarar_ticket, destarar_primeraPesada,
                                                              destarar_segundaPesada,
                                                              destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            def pedido4():
                                logger.debug("Traspaso entre Sucursales")
                                from Operador_Imprimir_Destare_Traspaso import imprimirDestareTraspaso
                                goto = imprimirDestareTraspaso(destarar_ticket, destarar_primeraPesada,
                                                               destarar_segundaPesada,
                                                               destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            def pedido5():
                                logger.debug("Devolución a Proveedor")
                                from Operador_Imprimir_Destare_DevProveedor import imprimirDestareDevProveedor
                                goto = imprimirDestareDevProveedor(destarar_ticket, destarar_primeraPesada,
                                                                   destarar_segundaPesada,
                                                                   destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            def pedido6():
                                logger.debug("Devolución de Cliente")
                                from Operador_Imprimir_Destare_DevCliente import imprimirDestareDevCliente
                                goto = imprimirDestareDevCliente(destarar_ticket, destarar_primeraPesada,
                                                                 destarar_segundaPesada,
                                                                 destarar_pesoNeto, pyute, ppropileno, praspa, psaco, psaco10, ptarima, pchep, ptreforzada, psacoesp, ptarimaesp)
                                goto.exec_()

                            # Python switch
                            options = {1: pedido1,
                                       2: pedido2,
                                       3: pedido3,
                                       4: pedido4,
                                       5: pedido5,
                                       6: pedido6,
                                       }
                            options[int(pedido)]()
                    else:
                        logger.debug("Regresa a la tabla")
                        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destare)
                        self.actualizaTablaDestare()
                except Exception as e:
                    logger.debug("Error: {}".format(e))

        except Exception as e:
            logger.debug("Error: {}".format(e))

    def btn_regresarTablaDestare(self):
        logger.debug("Boton Regresar a la tabla de Destare")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destare)
        self.actualizaTablaDestare()

    ## ==> END ##

    ## ==> SEGUNDA PESADA ##
    def actualizaTablaSegundaPesada(self):
        logger.debug("Actualiza la tabla")
        try:
            self.cur.execute(
                "SELECT id_bol_entra,peso_e,identifica_pedido_tipo,id_tractor,fecha_e,hora_e,solas,id_portacontenedor,cancelado FROM `totalco_boleto_ent` WHERE completo = '0' AND cancelado IS Null ORDER BY `id_bol_entra` ASC")
            self.resultados = self.cur.fetchall()
            self.ui.table_2a.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    if resultado[8] == None:
                        def pedido1():
                            self.tipoPedido = str("Compra")

                        def pedido2():
                            if resultado[6] == 0:
                                self.tipoPedido = str("Venta")
                            else:
                                self.tipoPedido = str("Exportación SOLAS")

                        def pedido3():
                            self.tipoPedido = str("Movimiento Interno")

                        def pedido4():
                            self.tipoPedido = str("Traspaso entre Sucursales")

                        def pedido5():
                            self.tipoPedido = str("Devolución a Proveedor")

                        def pedido6():
                            self.tipoPedido = str("Devolución de Cliente")

                        # Python switch
                        pedido = resultado[2]
                        options = {1: pedido1,
                                   2: pedido2,
                                   3: pedido3,
                                   4: pedido4,
                                   5: pedido5,
                                   6: pedido6,
                                   }
                        options[pedido]()

                        if resultado[7] != None:
                            logger.debug(
                                "Diferente de NULL es un trailer, puede ser caja o porta contenedor {} {}".format(
                                    resultado[7], resultado[0]))
                            self.id_contenedor = resultado[7]
                            logger.debug("Id Contenedor: {}".format(self.id_contenedor))
                            try:
                                self.cur.execute(
                                    "SELECT * FROM totalco_portacontenedor WHERE id_portacontenedor ='" + str(
                                        self.id_contenedor) + "'")
                                self.row = self.cur.fetchone()
                                self.placas = self.row[1]
                                self.caja_porta = self.row[2]
                                logger.debug("Placas Caja/Porta: {}".format(self.placas))
                                # logger.debug("Caja o Porta contendor: {}".format(self.caja_porta))
                                if self.caja_porta == 0:
                                    logger.debug("Caja")
                                else:
                                    logger.debug("Portacontenedor")
                            except Exception as e:
                                logger.debug("Error: {}".format(e))
                        else:
                            logger.debug("En un Torton")
                            self.id_tracto = resultado[3]
                            logger.debug("Id tracto: {}".format(self.id_tracto))
                            # self.placas = str("Torton")
                            try:
                                self.cur.execute(
                                    "SELECT * FROM totalco_tractor WHERE id_tractor ='" + str(self.id_tracto) + "'")
                                self.row = self.cur.fetchone()
                                self.placas = self.row[3]
                                self.caja_porta = 2
                                logger.debug("Placas Torton: {}".format(self.placas))
                            except Exception as e:
                                logger.debug("Error: {}".format(e))

                        self.ui.table_2a.setRowCount(fila + 1)
                        self.ui.table_2a.setColumnHidden(0, True)
                        self.ui.table_2a.setColumnHidden(7, True)
                        self.ui.table_2a.setColumnHidden(8, True)
                        self.ui.table_2a.setItem(fila, 0, QTableWidgetItem(str(resultado[2])))
                        self.ui.table_2a.setItem(fila, 1, QTableWidgetItem(str(resultado[0])))
                        self.ui.table_2a.setItem(fila, 2, QTableWidgetItem(str(resultado[1])))
                        self.ui.table_2a.setItem(fila, 3, QTableWidgetItem(str(self.tipoPedido)))
                        self.ui.table_2a.setItem(fila, 4, QTableWidgetItem(str(self.placas)))
                        self.ui.table_2a.setItem(fila, 5, QTableWidgetItem(str(resultado[4])))
                        self.ui.table_2a.setItem(fila, 6, QTableWidgetItem(str(resultado[5])))
                        self.ui.table_2a.setItem(fila, 7, QTableWidgetItem(str(resultado[6])))
                        self.ui.table_2a.setItem(fila, 8, QTableWidgetItem(str(self.caja_porta)))
                        fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def analizaSegundaPesada(self):
        logger.debug("Analiza Segunda Pesada")
        self.filaSeleccionada = self.ui.table_2a.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                pedido = self.ui.table_2a.item(indiceFila, 0).text()
                ticket = self.ui.table_2a.item(indiceFila, 1).text()
                solas = self.ui.table_2a.item(indiceFila, 7).text()
                tipo_torcajporta = self.ui.table_2a.item(indiceFila, 8).text()
                logger.debug("Tipo de pedido: {}".format(pedido))
                logger.debug("Ticket número: {}".format(ticket))
                logger.debug("SOLAS: {}".format(solas))
                logger.debug("Torton, Caja, Porta: {}".format(tipo_torcajporta))
                logger.debug("Se analiza numero de ticket")

                try:
                    logger.debug("Issue18: Determinar si ya se realizó la segunda pesada")
                    self.cur.execute("SELECT completo FROM `totalco_boleto_sal` WHERE id_bol_entra ='" + str(ticket) + "'")
                    self.row = self.cur.fetchone()
                    if self.row is None:
                        logger.debug("No se ha realizado la segunda pesada")

                        def pedido1():
                            self.tipoPedido = str("Compra")
                            logger.debug("Pedido: {}".format(self.tipoPedido))
                            if int(tipo_torcajporta) == 2:
                                logger.debug("Es un Torton")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("COMPRA Segunda Pesada Manual de un Torton")
                                            from Operador_Segunda_Compra_Torton_Manual import registraSegundaPesadaCompraTortonManual
                                            goto = registraSegundaPesadaCompraTortonManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("COMPRA Segunda Pesada Automatica de un Torton")
                                            from Operador_Segunda_Compra_Torton_Automatica import registraSegundaPesadaCompraTortonAutomatica
                                            goto = registraSegundaPesadaCompraTortonAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("Es un trailer")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("COMPRA Segunda Pesada Manual de un trailer")
                                            from Operador_Segunda_Compra_Trailer_Manual import registraSegundaPesadaCompraTrailerManual
                                            goto = registraSegundaPesadaCompraTrailerManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("COMPRA Segunda Pesada Automatica de un trailer")
                                            from Operador_Segunda_Compra_Trailer_Automatica import registraSegundaPesadaCompraTrailerAutomatica
                                            goto = registraSegundaPesadaCompraTrailerAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                        def pedido2():
                            if int(solas) == 0:
                                self.tipoPedido = str("Venta")
                                logger.debug("Pedido: {}".format(self.tipoPedido))
                                if int(tipo_torcajporta) == 2:
                                    logger.debug("Es un Torton")
                                    try:
                                        self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                        self.row = self.cur.fetchone()
                                        self.tipo_pesada = self.row[0]
                                        logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                        if int(self.tipo_pesada) != 0:
                                            logger.debug("El valor lo ingresa el usuario")
                                            try:
                                                logger.debug("VENTA Segunda Pesada Manual de un Torton")
                                                from Operador_Segunda_Venta_Torton_Manual import registraSegundaPesadaVentaTortonManual
                                                goto = registraSegundaPesadaVentaTortonManual(ticket)
                                                goto.exec_()
                                            except Exception as e:
                                                logger.debug("Error: {}".format(e))
                                        else:
                                            logger.debug("El valor es ingresado a través del indicador")
                                            try:
                                                logger.debug("VENTA Segunda Pesada Automatica de un Torton")
                                                from Operador_Segunda_Venta_Torton_Automatica import registraSegundaPesadaVentaTortonAutomatica
                                                goto = registraSegundaPesadaVentaTortonAutomatica(ticket)
                                                goto.exec_()
                                            except Exception as e:
                                                logger.debug("Error: {}".format(e))
                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                                else:
                                    logger.debug("Es un trailer")
                                    try:
                                        self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                        self.row = self.cur.fetchone()
                                        self.tipo_pesada = self.row[0]
                                        logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                        if int(self.tipo_pesada) != 0:
                                            logger.debug("El valor lo ingresa el usuario")
                                            try:
                                                logger.debug("VENTA Segunda Pesada Manual de un trailer")
                                                from Operador_Segunda_Venta_Trailer_Manual import registraSegundaPesadaVentaTrailerManual
                                                goto = registraSegundaPesadaVentaTrailerManual(ticket)
                                                goto.exec_()
                                            except Exception as e:
                                                logger.debug("Error: {}".format(e))
                                        else:
                                            logger.debug("El valor es ingresado a través del indicador")
                                            try:
                                                logger.debug("VENTA Segunda Pesada Automatica de un trailer")
                                                from Operador_Segunda_Venta_Trailer_Automatica import registraSegundaPesadaVentaTrailerAutomatica
                                                goto = registraSegundaPesadaVentaTrailerAutomatica(ticket)
                                                goto.exec_()
                                            except Exception as e:
                                                logger.debug("Error: {}".format(e))
                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                            else:
                                self.tipoPedido = str("Exportación SOLAS")
                                logger.debug("Pedido: {}".format(self.tipoPedido))
                                logger.debug("Es un portacontenedor")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario Aqui")
                                        QMessageBox.critical(self, "Mensaje", "Pesada SOLAS se deben realizar con INDICADOR.",
                                                             QMessageBox.Ok)
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("SOLAS Segunda Pesada Automatica  SOLAS")
                                            from Operador_Segunda_SOLAS_Trailer_Automatica import registraSegundaPesadaSolas
                                            goto = registraSegundaPesadaSolas(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                        def pedido3():
                            self.tipoPedido = str("Movimiento Interno")
                            logger.debug("Pedido: {}".format(self.tipoPedido))
                            logger.debug("Es un torton o volteo")
                            try:
                                self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                self.row = self.cur.fetchone()
                                self.tipo_pesada = self.row[0]
                                logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                if int(self.tipo_pesada) != 0:
                                    logger.debug("El valor lo ingresa el usuario")
                                    try:
                                        logger.debug("MOV INTERNO Segunda Pesada Manual de un Torton/Volteo")
                                        from Operador_Segunda_Interno_Torton_Manual import registraSegundaPesadaInternoTortonManual
                                        goto = registraSegundaPesadaInternoTortonManual(ticket)
                                        goto.exec_()
                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                                else:
                                    logger.debug("El valor es ingresado a través del indicador")
                                    try:
                                        logger.debug("MOV INTERNO Segunda Pesada Automatica de un Torton/Volteo")
                                        from Operador_Segunda_Interno_Torton_Automatica import registraSegundaPesadaInternoTortonAutomatica
                                        goto = registraSegundaPesadaInternoTortonAutomatica(ticket)
                                        goto.exec_()
                                    except Exception as e:
                                        logger.debug("Error: {}".format(e))
                            except Exception as e:
                                logger.debug("Error: {}".format(e))

                        def pedido4():
                            self.tipoPedido = str("Traspaso entre Sucursales")
                            logger.debug("Pedido: {}".format(self.tipoPedido))
                            if int(tipo_torcajporta) == 2:
                                logger.debug("Es un torton")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("Traspaso entre Sucursales Segunda Pesada Manual de Torton")
                                            from Operador_Segunda_Traspaso_Torton_Manual import registraSegundaPesadaTraspasoTortonManual
                                            goto = registraSegundaPesadaTraspasoTortonManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("Traspaso entre Sucursales Segunda Pesada Automatica de un Torton")
                                            from Operador_Segunda_Traspaso_Torton_Automatica import registraSegundaPesadaTraspasoTortonAutomatica
                                            goto = registraSegundaPesadaTraspasoTortonAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("Es un trailer")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("Traspaso entre Sucursales Segunda Pesada Manual de un trailer")
                                            from Operador_Segunda_Traspaso_Trailer_Manual import registraSegundaPesadaTraspasoTrailerManual
                                            goto = registraSegundaPesadaTraspasoTrailerManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("Traspaso entre Sucursales Segunda Pesada Automatica de un trailer")
                                            from Operador_Segunda_Traspaso_Trailer_Automatica import \
                                                registraSegundaPesadaTraspasoTrailerAutomatica
                                            goto = registraSegundaPesadaTraspasoTrailerAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                        def pedido5():
                            self.tipoPedido = str("Devolución a Proveedor")
                            logger.debug("Pedido: {}".format(self.tipoPedido))
                            if int(tipo_torcajporta) == 2:
                                logger.debug("Es un torton")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("DEV A PROVEEDOR Segunda Pesada Manual de un Torton")
                                            from Operador_Segunda_DevProv_Torton_Manual import registraSegundaPesadaDevProvTortonManual
                                            goto = registraSegundaPesadaDevProvTortonManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("DEV A PROVEEDOR Segunda Pesada Automatica de un Torton")
                                            from Operador_Segunda_DevProv_Torton_Automatica import registraSegundaPesadaDevProvTortonAutomatica
                                            goto = registraSegundaPesadaDevProvTortonAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("Es un trailer")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("DEV A PROVEEDOR Segunda Pesada Manual de un trailer")
                                            from Operador_Segunda_DevProv_Trailer_Manual import registraSegundaPesadaDevProvTrailerManual
                                            goto = registraSegundaPesadaDevProvTrailerManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("DEV A PROVEEDOR Segunda Pesada Automatica de un trailer")
                                            from Operador_Segunda_DevProv_Trailer_Automatica import registraSegundaPesadaDevProvTrailerAutomatica
                                            goto = registraSegundaPesadaDevProvTrailerAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                        def pedido6():
                            self.tipoPedido = str("Devolución de Cliente")
                            logger.debug("Pedido: {}".format(self.tipoPedido))
                            if int(tipo_torcajporta) == 2:
                                logger.debug("Es un torton")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("DEV DE CLIENTE Segunda Pesada Manual de un Torton")
                                            from Operador_Segunda_DevCliente_Torton_Manual import registraSegundaPesadaDevClienteTortonManual
                                            goto = registraSegundaPesadaDevClienteTortonManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("DEV DE CLIENTE Segunda Pesada Automatica de un Torton")
                                            from Operador_Segunda_DevCliente_Torton_Automatica import registraSegundaPesadaDevClienteTortonAutomatica
                                            goto = registraSegundaPesadaDevClienteTortonAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))
                            else:
                                logger.debug("Es un trailer")
                                try:
                                    self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
                                    self.row = self.cur.fetchone()
                                    self.tipo_pesada = self.row[0]
                                    logger.debug("Tipo de pesada: {}".format(self.tipo_pesada))
                                    if int(self.tipo_pesada) != 0:
                                        logger.debug("El valor lo ingresa el usuario")
                                        try:
                                            logger.debug("DEV DE CLIENTE Segunda Pesada Manual de un trailer")
                                            from Operador_Segunda_DevCliente_Trailer_Manual import registraSegundaPesadaDevClienteTrailerManual
                                            goto = registraSegundaPesadaDevClienteTrailerManual(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                    else:
                                        logger.debug("El valor es ingresado a través del indicador")
                                        try:
                                            logger.debug("DEV DE CLIENTE Segunda Pesada Automatica de un trailer")
                                            from Operador_Segunda_DevCliente_Trailer_Automatica import registraSegundaPesadaDevClienteTrailerAutomatica
                                            goto = registraSegundaPesadaDevClienteTrailerAutomatica(ticket)
                                            goto.exec_()
                                        except Exception as e:
                                            logger.debug("Error: {}".format(e))
                                except Exception as e:
                                    logger.debug("Error: {}".format(e))

                        # Python switch
                        options = {1: pedido1,
                                   2: pedido2,
                                   3: pedido3,
                                   4: pedido4,
                                   5: pedido5,
                                   6: pedido6,
                                   }
                        options[int(pedido)]()
                    else:
                        logger.debug("Regresa a la tabla")
                        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2a_pesada)
                        self.actualizaTablaSegundaPesada()

                except Exception as e:
                    logger.debug("Error en el analisis de la segunda pesada")

            else:
                QMessageBox.critical(self, "Terminar Pesada", "Primero seleccione una ticket.   ", QMessageBox.Ok)

        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    ## ==> PRIMERA PESADA COMPRA
    def primeraPesadaCompraTorton(self):
        logger.debug("Primera Pesada Compra Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                try:
                    from Operador_Primera_Compra_Torton_Manual import registraPrimeraCompraTortonManual
                    goto = registraPrimeraCompraTortonManual()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Compra_Torton_Automatica import registraPrimeraCompraTortonAutomatica
                    goto = registraPrimeraCompraTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaCompraTrailer(self):
        logger.debug("Primera Pesada Compra Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_Compra_Trailer_Manual import registraPrimeraCompraTrailerManual
                goto = registraPrimeraCompraTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Compra_Trailer_Automatica import registraPrimeraCompraTrailerAutomatica
                    goto = registraPrimeraCompraTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))


    ## == END ##

    ## ==> PRIMERA PESADA ENTRADA TRASPASO
    def primeraPesadaTraspasoTorton(self):
        logger.debug("Primera Pesada Traspaso Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_Traspaso_Torton_Manual import registraPrimeraTraspasoTortonManual
                goto = registraPrimeraTraspasoTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Traspaso_Torton_Automatica import registraPrimeraTraspasoTortonAutomatica
                    goto = registraPrimeraTraspasoTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaTraspasoTrailer(self):
        logger.debug("Primera Pesada Traspaso Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_Traspaso_Trailer_Manual import registraPrimeraTraspasoTrailerManual
                goto = registraPrimeraTraspasoTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Traspaso_Trailer_Automatica import registraPrimeraTraspasoTrailerAutomatica
                    goto = registraPrimeraTraspasoTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ## ==> PRIMERA PESADA SALIDA TRASPASO
    def primeraPesadaSalidaTraspasoTorton(self):
        logger.debug("Primera Pesada Salida Traspaso Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_Traspaso_Salida_Torton_Manual import registraPrimeraTraspasoSalidaTortonManual
                goto = registraPrimeraTraspasoSalidaTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Traspaso_Salida_Torton_Automatica import registraPrimeraTraspasoSalidaTortonAutomatica
                    goto = registraPrimeraTraspasoSalidaTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaSalidaTraspasoTrailer(self):
        logger.debug("Primera Pesada Traspaso Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_Traspaso_Salida_Trailer_Manual import registraPrimeraTraspasoSalidaTrailerManual
                goto = registraPrimeraTraspasoSalidaTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Traspaso_Salida_Trailer_Automatica import registraPrimeraTraspasoSalidaTrailerAutomatica
                    goto = registraPrimeraTraspasoSalidaTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ##########################
    ##########################

    ## ==> PRIMERA PESADA SALIDA
    def primeraPesadaSalidaTorton(self):
        logger.debug("Primera Pesada Salida Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_Salida_Torton_Manual import registraPrimeraSalidaTortonManual
                goto = registraPrimeraSalidaTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Salida_Torton_Automatica import registraPrimeraSalidaTortonAutomatica
                    goto = registraPrimeraSalidaTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaSalidaTrailer(self):
        logger.debug("Primera Pesada Salida Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_Salida_Trailer_Manual import registraPrimeraSalidaTrailerManual
                goto = registraPrimeraSalidaTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Salida_Trailer_Automatica import registraPrimeraSalidaTrailerAutomatica
                    goto = registraPrimeraSalidaTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ## == PRIMERA PESADA DEVOLUCION DE CLIENTE

    def primeraPesadaDevClienteTorton(self):
        logger.debug("Primera Pesada Devolucion Cliente Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_DevCliente_Torton_Manual import registraPrimeraDevClientTortonManual
                goto = registraPrimeraDevClientTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_DevCliente_Torton_Automatica import registraPrimeraDevClientTortonAutomatica
                    goto = registraPrimeraDevClientTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaDevClienteTrailer(self):
        logger.debug("Primera Pesada Devolucion Cliente Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_DevCliente_Trailer_Manual import registraPrimeraDevClientTrailerManual
                goto = registraPrimeraDevClientTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_DevCliente_Trailer_Automatica import registraPrimeraDevClientTrailerAutomatica
                    goto = registraPrimeraDevClientTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ## == PRIMERA PESADA DEVOLUCION A PROVEEDOR

    def primeraPesadaDevProvTorton(self):
        logger.debug("Primera Pesada Devolucion a Proveedor Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_DevProv_Torton_Manual import registraPrimeraDevProvTortonManual
                goto = registraPrimeraDevProvTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_DevProv_Torton_Automatica import registraPrimeraDevProvTortonAutomatica
                    goto = registraPrimeraDevProvTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def primeraPesadaDevProvTrailer(self):
        logger.debug("Primera Pesada Devolucion a Proveedor Trailer")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                from Operador_Primera_DevProv_Trailer_Manual import registraPrimeraDevProvTrailerManual
                goto = registraPrimeraDevProvTrailerManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_DevProv_Trailer_Automatica import registraPrimeraDevProvTrailerAutomatica
                    goto = registraPrimeraDevProvTrailerAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ## ==> PRIMERA PESADA SOLAS

    def primeraPesadaSOLAS(self):
        logger.debug("Primera Pesada SOLAS")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario Aqui")
                QMessageBox.critical(self, "Mensaje", "Pesada SOLAS se deben realizar con INDICADOR.", QMessageBox.Ok)
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Pesada_SOLAS_Automatica import registraPrimeraPesadaSolasAutomatica
                    goto = registraPrimeraPesadaSolasAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    ## PRIMERA PESADA MOVIMIENTO INTERNO

    def primeraPesadaInternoTorton(self):
        logger.debug("Primera Pesada Movimiento Interno Torton")
        logger.debug("Query para saber si es pesada manual o automática")
        try:
            self.cur.execute("SELECT * FROM `totalco_pesada_manual`")
            self.row = self.cur.fetchone()
            self.tipo_pesada = self.row[0]
            if self.tipo_pesada != 0:
                logger.debug("El valor lo ingresa el usuario")
                from Operador_Primera_Interno_Torton_Manual import registraPrimeraInternoTortonManual
                goto = registraPrimeraInternoTortonManual()
                goto.exec_()
            else:
                logger.debug("El valor es ingresado a través del indicador")
                try:
                    logger.debug("Abriendo Indicador")
                    from Operador_Primera_Interno_Torton_Automatica import registraPrimeraInternoTortonAutomatica
                    goto = registraPrimeraInternoTortonAutomatica()
                    goto.exec_()
                except Exception as e:
                    logger.debug("Error: {}".format(e))
        except Exception as e:
            logger.debug("Error: {}".format(e))

    ## == END ##

    #########################
    ##########################

    ## EVENT ==> FUNCIONES DE RE IMPRESION

    ## ==> END ##

    ## EVENT ==> FUNCIONES DE REPORTES

    ## ==> END ##

    ## EVENT ==> FUNCIONES DE DATOS
    def datos_menu_destinos(self):
        logger.debug("Menú destinos")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menudestinos)
        UIFunctions.labelPage(self, "Menú Destinos")

    def datos_menu(self):
        logger.debug("Regresar a menu datos")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_datos)
        UIFunctions.labelPage(self, "DATOS")

    def datos_menu_tractos(self):
        logger.debug("Menú tractos")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menutractos)
        UIFunctions.labelPage(self, "MENU TRACTOS")

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> ADUANA
    #####
    def menu_aduana(self):
        logger.debug("Menu Aduana")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_aduana)
        UIFunctions.labelPage(self, "MENU ADUANA")
        try:
            self.cur.execute("SELECT * FROM totalco_agencia_aduanal ORDER BY id_aduana DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla.setRowCount(fila + 1)
                    self.ui.tabla.setColumnHidden(0, True)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarAduana(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditAduana.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_agencia_aduanal WHERE nombre LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla.setRowCount(fila + 1)
                            self.ui.tabla.setColumnHidden(0, True)
                            self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ", QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_agencia_aduanal ORDER BY id_aduana DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla.setRowCount(fila + 1)
                                self.ui.tabla.setColumnHidden(0, True)
                                self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_agencia_aduanal ORDER BY id_aduana DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla.setRowCount(fila + 1)
                        self.ui.tabla.setColumnHidden(0, True)
                        self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaAduana(self):
        logger.debug("Elimina Aduana")
        # self.filaSeleccionada = self.ui.tabla.currentItem().text()
        self.filaSeleccionada = self.ui.tabla.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla.item(indiceFila, 1).text()
                    logger.debug("id Aduana: {}".format(self.idItem))
                    logger.debug("Nombre Aduana: {}".format(nombreItem))
                    self.ui.tabla.removeRow(indiceFila)
                    self.ui.tabla.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_agencia_aduanal WHERE id_aduana = %s LIMIT 1 """
                        row = (self.idItem, )
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevaAduana(self):
        from Operador_Aduana_Create import operadorCreateAduana
        goto = operadorCreateAduana()
        goto.exec_()

    def gotoRefrescar(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_agencia_aduanal ORDER BY id_aduana DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla.setRowCount(fila + 1)
                    self.ui.tabla.setColumnHidden(0, True)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaAduana(self):
        logger.debug("Actualiza Aduana")
        self.filaSeleccionada = self.ui.tabla.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla.item(indiceFila, 1).text()
                logger.debug("Id Aduana en el CRUD: {}".format(idItem))
                logger.debug("Nombre de Auana: {}".format(nombreItem))

                from Operador_Aduana_Update import operadorUpdateAduana
                goto = operadorUpdateAduana(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                         QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))


    ## ==> END ADUANA ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> CLIENTE
    #####
    def menu_cliente(self):
        logger.debug("Funcion Cliente")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cliente)
        UIFunctions.labelPage(self, "MENU CLIENTE")
        try:
            self.cur.execute("SELECT * FROM totalco_cliente ORDER BY id_cliente DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_cl.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_cl.setRowCount(fila + 1)
                    self.ui.tabla_cl.setColumnHidden(0, True)
                    self.ui.tabla_cl.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_cl.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_cl.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarCliente(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditCliente.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_cliente WHERE nombre_cliente LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_cl.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_cl.setRowCount(fila + 1)
                            self.ui.tabla_cl.setColumnHidden(0, True)
                            self.ui.tabla_cl.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_cl.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_cl.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_cliente ORDER BY id_cliente DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_cl.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_cl.setRowCount(fila + 1)
                                self.ui.tabla_cl.setColumnHidden(0, True)
                                self.ui.tabla_cl.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_cl.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_cl.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_cliente ORDER BY id_cliente DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_cl.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_cl.setRowCount(fila + 1)
                        self.ui.tabla_cl.setColumnHidden(0, True)
                        self.ui.tabla_cl.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_cl.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_cl.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaCliente(self):
        logger.debug("Elimina Cliente")
        # self.filaSeleccionada = self.ui.tabla_cl.currentItem().text()
        self.filaSeleccionada = self.ui.tabla_cl.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_cl.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_cl.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_cl.removeRow(indiceFila)
                    self.ui.tabla_cl.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_cliente WHERE id_cliente = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoCliente(self):
        logger.debug("Funcion nuevo cliente")
        from Operador_Cliente_Create import operadorCreateCliente
        goto = operadorCreateCliente()
        goto.exec_()

    def gotoRefrescarCliente(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_cliente ORDER BY id_cliente DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_cl.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_cl.setRowCount(fila + 1)
                    self.ui.tabla_cl.setColumnHidden(0, True)
                    self.ui.tabla_cl.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_cl.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_cl.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaCliente(self):
        logger.debug("Actualiza Cliente")
        self.filaSeleccionada = self.ui.tabla_cl.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_cl.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_cl.item(indiceFila, 1).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Cliente_Update import operadorUpdateCliente
                goto = operadorUpdateCliente(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))
    ## ==> END CLIENTE ##

    ## EVENT ==> FUNCIONES DE DATOS ==> MENU CONTENEDOR
    #####
    def menu_contenedor(self):
        logger.debug("Funcion Menu Contenedor")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_menuContenedor)
        UIFunctions.labelPage(self, "MENU CONTENEDOR")

    ## ==> END CONTENEDOR ##


    ## EVENT ==> FUNCIONES DE DATOS ==> MENU CONTENEDOR ==> TIPO DE CONTENEDOR
    #####
    def menu_tipocontenedor(self):
        logger.debug("Funcion Menu Tipo de contenedor")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_tiposcontenedor)
        UIFunctions.labelPage(self, "MENU TIPO DE CONTENEDOR")
        try:
            self.cur.execute("SELECT * FROM totalco_contenedor_tipo ORDER BY id_contenedor_tipo ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tcon.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tcon.setRowCount(fila + 1)
                    self.ui.tabla_tcon.setColumnHidden(0, True)
                    self.ui.tabla_tcon.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tcon.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarTipoCont(self):
        logger.debug("Buscar tipo de contenedores")
        self.textoBuscar = self.ui.BuscarlineEditTipoCont.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_contenedor_tipo WHERE contenedor_tipo LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tcon.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_tcon.setRowCount(fila + 1)
                            self.ui.tabla_tcon.setColumnHidden(0, True)
                            self.ui.tabla_tcon.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_tcon.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_contenedor_tipo ORDER BY id_contenedor_tipo ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_tcon.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_tcon.setRowCount(fila + 1)
                                self.ui.tabla_tcon.setColumnHidden(0, True)
                                self.ui.tabla_tcon.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_tcon.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_contenedor_tipo ORDER BY id_contenedor_tipo ASC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tcon.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_tcon.setRowCount(fila + 1)
                        self.ui.tabla_tcon.setColumnHidden(0, True)
                        self.ui.tabla_tcon.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_tcon.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminarTipoCont(self):
        logger.debug("Eliminar tipo de contenedor")
        self.filaSeleccionada = self.ui.tabla_tcon.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_tcon.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_tcon.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_tcon.removeRow(indiceFila)
                    self.ui.tabla_tcon.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_contenedor_tipo WHERE id_contenedor_tipo = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoTipoCont(self):
        logger.debug("Nuevo tipo de contenedor")
        from Operador_TipoCont_Create import operadorCreateTipoCont
        goto = operadorCreateTipoCont()
        goto.exec_()

    def gotoRefrescarTipoCont(self):
        logger.debug("Refrescar tabla de tipos de contenedores")
        try:
            self.cur.execute("SELECT * FROM totalco_contenedor_tipo ORDER BY id_contenedor_tipo ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tcon.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tcon.setRowCount(fila + 1)
                    self.ui.tabla_tcon.setColumnHidden(0, True)
                    self.ui.tabla_tcon.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tcon.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarTipoCont(self):
        logger.debug("Actualizar tipo de contenedor")
        self.filaSeleccionada = self.ui.tabla_tcon.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_tcon.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_tcon.item(indiceFila, 1).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_TipoCont_Update import operadorUpdateTipoCont
                goto = operadorUpdateTipoCont(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END CONTENEDOR ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> MENU CONTENEDOR ==> CONTENEDOR
    #####
    def menu_crudcontenedor(self):
        logger.debug("Funcion Menu Contenedor")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_contenedor)
        UIFunctions.labelPage(self, "MENU CONTENEDOR")
        # id clave tipo placasTracto PlacasPorta Linea
        try:
            self.cur.execute("SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo)")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_con.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_con.setRowCount(fila + 1)
                    self.ui.tabla_con.setColumnHidden(0, True)
                    self.ui.tabla_con.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_con.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_con.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_con.setItem(fila, 3, QTableWidgetItem(str(resultado[4])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarContenedor(self):
        logger.debug("Buscar Contenedor")
        self.textoBuscar = self.ui.BuscarlineEditContenedor.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo) AND (cont.id_clave_conte LIKE '%" + self.textoBuscar + "%')")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_con.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_con.setRowCount(fila + 1)
                            self.ui.tabla_con.setColumnHidden(0, True)
                            self.ui.tabla_con.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_con.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_con.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_con.setItem(fila, 3, QTableWidgetItem(str(resultado[4])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo)")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_con.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_con.setRowCount(fila + 1)
                                self.ui.tabla_con.setColumnHidden(0, True)
                                self.ui.tabla_con.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_con.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                self.ui.tabla_con.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_con.setItem(fila, 3, QTableWidgetItem(str(resultado[4])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo)")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_con.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_con.setRowCount(fila + 1)
                        self.ui.tabla_con.setColumnHidden(0, True)
                        self.ui.tabla_con.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_con.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_con.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_con.setItem(fila, 3, QTableWidgetItem(str(resultado[4])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminarContenedor(self):
        logger.debug("Eliminar Contenedor")
        self.filaSeleccionada = self.ui.tabla_con.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_con.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_con.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_con.removeRow(indiceFila)
                    self.ui.tabla_con.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_contenedor WHERE id_contenedor = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoContenedor(self):
        logger.debug("Nuevo Contenedor")

        from Operador_Contenedor_Create import operadorCreateContenedor
        goto = operadorCreateContenedor()
        goto.exec_()

    def gotoRefrescarContenedor(self):
        logger.debug("Refrescar tabla de contenedores")
        try:
            self.cur.execute(
                "SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo)")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_con.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_con.setRowCount(fila + 1)
                    self.ui.tabla_con.setColumnHidden(0, True)
                    self.ui.tabla_con.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_con.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_con.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_con.setItem(fila, 3, QTableWidgetItem(str(resultado[4])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoActualizarContenedor(self):
        logger.debug("Actualizar contenedor")
        self.filaSeleccionada = self.ui.tabla_con.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_con.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_con.item(indiceFila, 1).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Contenedor_Update import operadorUpdateContenedor
                goto = operadorUpdateContenedor(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))


    ## ==> END CONTENEDOR ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> TRASNPORTISTA
    #####
    def menu_transportista(self):
        logger.debug("Funcion Trasportista")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_transportista)
        UIFunctions.labelPage(self, "MENU TRANSPORTISTA")
        try:
            self.cur.execute("SELECT * FROM totalco_transporte ORDER BY id_transporte DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tr.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tr.setRowCount(fila + 1)
                    self.ui.tabla_tr.setColumnHidden(0, True)
                    self.ui.tabla_tr.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tr.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarTransportista(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditTransportista.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_transporte WHERE linea LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tr.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_tr.setRowCount(fila + 1)
                            self.ui.tabla_tr.setColumnHidden(0, True)
                            self.ui.tabla_tr.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_tr.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ", QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_transporte ORDER BY id_transporte DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_tr.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_tr.setRowCount(fila + 1)
                                self.ui.tabla_tr.setColumnHidden(0, True)
                                self.ui.tabla_tr.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_tr.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_transporte ORDER BY id_transporte DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tr.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_tr.setRowCount(fila + 1)
                        self.ui.tabla_tr.setColumnHidden(0, True)
                        self.ui.tabla_tr.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_tr.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaTransportista(self):
        logger.debug("Elimina Transportista")
        # self.filaSeleccionada = self.ui.tabla.currentItem().text()
        self.filaSeleccionada = self.ui.tabla_tr.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_tr.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_tr.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_tr.removeRow(indiceFila)
                    self.ui.tabla_tr.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_transporte WHERE id_transporte = %s LIMIT 1 """
                        row = (self.idItem, )
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevaLinea(self):
        logger.debug("Nueva linea")
        from Operador_Transportista_Create import operadorCreateTransportista
        goto = operadorCreateTransportista()
        goto.exec_()

    def gotoRefrescarTransportista(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_transporte ORDER BY id_transporte DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tr.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tr.setRowCount(fila + 1)
                    self.ui.tabla_tr.setColumnHidden(0, True)
                    self.ui.tabla_tr.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tr.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaTransportista(self):
        logger.debug("Actualiza Transportista")
        self.filaSeleccionada = self.ui.tabla_tr.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_tr.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_tr.item(indiceFila, 1).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Transportista_Update import operadorUpdateTransportista
                goto = operadorUpdateTransportista(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END TRASNPORTISTA ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> OPERADOR
    #####
    def menu_operador(self):
        logger.debug("Funcion Operador")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_operador)
        UIFunctions.labelPage(self, "MENU OPERADOR")
        try:
            self.cur.execute("SELECT * FROM totalco_operadores ORDER BY id_operador DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_op.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_op.setRowCount(fila + 1)
                    self.ui.tabla_op.setColumnHidden(0, True)
                    self.ui.tabla_op.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_op.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_op.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_op.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    self.ui.tabla_op.setItem(fila, 4, QTableWidgetItem(str(resultado[4])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarOperador(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditOperador.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_operadores WHERE nombre LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_op.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_op.setRowCount(fila + 1)
                            self.ui.tabla_op.setColumnHidden(0, True)
                            self.ui.tabla_op.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_op.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_op.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_op.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                            self.ui.tabla_op.setItem(fila, 4, QTableWidgetItem(str(resultado[4])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_operadores ORDER BY id_operador DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_op.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_op.setRowCount(fila + 1)
                                self.ui.tabla_op.setColumnHidden(0, True)
                                self.ui.tabla_op.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_op.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                self.ui.tabla_op.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_op.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                                self.ui.tabla_op.setItem(fila, 4, QTableWidgetItem(str(resultado[4])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_operadores ORDER BY id_operador DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_op.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_op.setRowCount(fila + 1)
                        self.ui.tabla_op.setColumnHidden(0, True)
                        self.ui.tabla_op.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_op.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_op.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_op.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                        self.ui.tabla_op.setItem(fila, 4, QTableWidgetItem(str(resultado[4])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaOperador(self):
        logger.debug("Elimina Operador")
        # self.filaSeleccionada = self.ui.tabla.currentItem().text()
        self.filaSeleccionada = self.ui.tabla_op.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_op.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_op.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_op.removeRow(indiceFila)
                    self.ui.tabla_op.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_operadores WHERE id_operador = %s LIMIT 1 """
                        row = (self.idItem, )
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoOperador(self):
        logger.debug("Nuevo Operador")
        from Operador_Chofer_Create import operadorCreateChofer
        goto = operadorCreateChofer()
        goto.exec_()

    def gotoRefrescarOperador(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_operadores ORDER BY id_operador DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_op.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_op.setRowCount(fila + 1)
                    self.ui.tabla_op.setColumnHidden(0, True)
                    self.ui.tabla_op.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_op.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_op.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_op.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    self.ui.tabla_op.setItem(fila, 4, QTableWidgetItem(str(resultado[4])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaOperador(self):
        logger.debug("Actualiza Operador")
        self.filaSeleccionada = self.ui.tabla_op.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_op.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_op.item(indiceFila, 1).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Chofer_Update import operadorUpdateChofer
                goto = operadorUpdateChofer(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))
    ## ==> END OPERADOR ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> PRODUCTO
    #####
    def menu_producto(self):
        logger.debug("Funcion Producto")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_producto)
        UIFunctions.labelPage(self, "MENU PRODUCTO")
        try:
            self.cur.execute("SELECT * FROM totalco_producto ORDER BY id_producto DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_pro.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_pro.setRowCount(fila + 1)
                    self.ui.tabla_pro.setColumnHidden(0, True)
                    self.ui.tabla_pro.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_pro.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_pro.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_pro.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarProducto(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditProducto.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_producto WHERE nombre_producto LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_pro.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_pro.setRowCount(fila + 1)
                            self.ui.tabla_pro.setColumnHidden(0, True)
                            self.ui.tabla_pro.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_pro.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_pro.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_pro.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_producto ORDER BY id_producto DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_pro.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_pro.setRowCount(fila + 1)
                                self.ui.tabla_pro.setColumnHidden(0, True)
                                self.ui.tabla_pro.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_pro.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                self.ui.tabla_pro.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_pro.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_producto ORDER BY id_producto DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_pro.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_pro.setRowCount(fila + 1)
                        self.ui.tabla_pro.setColumnHidden(0, True)
                        self.ui.tabla_pro.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_pro.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_pro.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_pro.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaProducto(self):
        logger.debug("Elimina Producto")
        # self.filaSeleccionada = self.ui.tabla.currentItem().text()
        self.filaSeleccionada = self.ui.tabla_pro.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_pro.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_pro.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_pro.removeRow(indiceFila)
                    self.ui.tabla_pro.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_producto WHERE id_producto = %s LIMIT 1 """
                        row = (self.idItem, )
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoProducto(self):
        logger.debug("Nuevo Producto")
        from Operador_Producto_Create import operadorCreateProducto
        goto = operadorCreateProducto()
        goto.exec_()

    def gotoRefrescarProducto(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_producto ORDER BY id_producto DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_pro.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_pro.setRowCount(fila + 1)
                    self.ui.tabla_pro.setColumnHidden(0, True)
                    self.ui.tabla_pro.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_pro.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_pro.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_pro.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaProducto(self):
        logger.debug("Actualiza Producto")
        self.filaSeleccionada = self.ui.tabla_pro.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_pro.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_pro.item(indiceFila, 2).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Producto_Update import operadorUpdateProducto
                goto = operadorUpdateProducto(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END PRODUCTO ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> PROVEEDOR
    #####
    def menu_proveedor(self):
        logger.debug("Funcion Proveedor")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_proveedor)
        UIFunctions.labelPage(self, "MENU PROVEEDOR")
        try:
            self.cur.execute("SELECT * FROM totalco_proveedor ORDER BY id_proveedor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_prov.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_prov.setRowCount(fila + 1)
                    self.ui.tabla_prov.setColumnHidden(0, True)
                    self.ui.tabla_prov.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_prov.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_prov.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarProveedor(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditProveedor.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_proveedor WHERE nombre_proveedor LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_prov.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_prov.setRowCount(fila + 1)
                            self.ui.tabla_prov.setColumnHidden(0, True)
                            self.ui.tabla_prov.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_prov.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_prov.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_proveedor ORDER BY id_proveedor DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_prov.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_prov.setRowCount(fila + 1)
                                self.ui.tabla_prov.setColumnHidden(0, True)
                                self.ui.tabla_prov.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_prov.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_prov.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_proveedor ORDER BY id_proveedor DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_prov.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_prov.setRowCount(fila + 1)
                        self.ui.tabla_prov.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_prov.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_prov.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoEliminaProveedor(self):
        logger.debug("Elimina Producto")
        # self.filaSeleccionada = self.ui.tabla.currentItem().text()
        self.filaSeleccionada = self.ui.tabla_prov.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_prov.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_prov.item(indiceFila, 1).text()
                    logger.debug("id item: {}".format(self.idItem))
                    logger.debug("Nombre item: {}".format(nombreItem))
                    self.ui.tabla_prov.removeRow(indiceFila)
                    self.ui.tabla_prov.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_proveedor WHERE id_proveedor = %s LIMIT 1 """
                        row = (self.idItem, )
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoProveedor(self):
        logger.debug("Nuevo Proveedor")
        from Operador_Proveedor_Create import operadorCreateProveedor
        goto = operadorCreateProveedor()
        goto.exec_()

    def gotoRefrescarProveedor(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_proveedor ORDER BY id_proveedor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_prov.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_prov.setRowCount(fila + 1)
                    self.ui.tabla_prov.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_prov.setItem(fila, 1, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_prov.setItem(fila, 2, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaProveedor(self):
        logger.debug("Actualiza Proveedor")
        self.filaSeleccionada = self.ui.tabla_prov.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_prov.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_prov.item(indiceFila, 2).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))

                from Operador_Proveedor_Update import operadorUpdateProveedor
                goto = operadorUpdateProveedor(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END PROVEEDOR ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> SUCURSAL
    #####
    def menu_sucursal(self):
        logger.debug("Funcion Sucursal")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sucursal)
        UIFunctions.labelPage(self, "MENU SUCURSAL")
        try:
            self.cur.execute("SELECT * FROM totalco_sucursales WHERE id_sucursal > 0 ORDER BY id_sucursal DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_su.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_su.setRowCount(fila + 1)
                    self.ui.tabla_su.setColumnHidden(0, True)
                    self.ui.tabla_su.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_su.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarSucursal(self):
        logger.debug("Buscar Sucursal")
        self.textoBuscar = self.ui.BuscarlineEditSucursal.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_sucursales WHERE sucursal LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_su.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_su.setRowCount(fila + 1)
                            self.ui.tabla_su.setColumnHidden(0, True)
                            self.ui.tabla_su.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_su.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_sucursales WHERE id_sucursal > 0 ORDER BY id_sucursal DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_su.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_su.setRowCount(fila + 1)
                                self.ui.tabla_su.setColumnHidden(0, True)
                                self.ui.tabla_su.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_su.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_sucursales WHERE id_sucursal > 0 ORDER BY id_sucursal DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_su.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_su.setRowCount(fila + 1)
                        self.ui.tabla_su.setColumnHidden(0, True)
                        self.ui.tabla_su.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_su.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminarSucursal(self):
        logger.debug("Eliminar Sucursal")
        self.filaSeleccionada = self.ui.tabla_su.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_su.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_su.item(indiceFila, 1).text()
                    logger.debug("id Sucursal: {}".format(self.idItem))
                    logger.debug("Nombre Sucursal: {}".format(nombreItem))
                    self.ui.tabla_su.removeRow(indiceFila)
                    self.ui.tabla_su.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_sucursales WHERE id_sucursal = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoSucursal(self):
        logger.debug("Nueva Sucursal")
        from Operador_Sucursal_Create import operadorCreateSucursal
        goto = operadorCreateSucursal()
        goto.exec_()

    def gotoRefrescarSucursal(self):
        logger.debug("Refrescar tabla sucursal")
        try:
            self.cur.execute("SELECT * FROM totalco_sucursales WHERE id_sucursal > 0 ORDER BY id_sucursal DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_su.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_su.setRowCount(fila + 1)
                    self.ui.tabla_su.setColumnHidden(0, True)
                    self.ui.tabla_su.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_su.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarSucursal(self):
        logger.debug("Actualizar Datos de Sucursal")
        self.filaSeleccionada = self.ui.tabla_su.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_su.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_su.item(indiceFila, 1).text()
                logger.debug("Id Sucursal en el CRUD: {}".format(idItem))
                logger.debug("Nombre de Sucursal: {}".format(nombreItem))

                from Operador_Sucursal_Update import operadorUpdateSucursal
                goto = operadorUpdateSucursal(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END SUCURSAL ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> TRACTOS ==> TIPOS DE TRACTOS
    #####
    def menu_tipoTracto(self):
        logger.debug("Funcion Tipo Tracto")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_tipostractos)
        UIFunctions.labelPage(self, "MENU TIPOS DE TRACTOS")
        try:
            self.cur.execute("SELECT * FROM totalco_tipo_tracto ORDER BY id_tipo_tracto DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tiptrac.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tiptrac.setRowCount(fila + 1)
                    self.ui.tabla_tiptrac.setColumnHidden(0, True)
                    self.ui.tabla_tiptrac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tiptrac.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarTipoTracto(self):
        logger.debug("Buscar Tipo de tracto")
        self.textoBuscar = self.ui.BuscarlineEditTipoTracto.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_tipo_tracto WHERE tipo_tracto LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tiptrac.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_tiptrac.setRowCount(fila + 1)
                            self.ui.tabla_tiptrac.setColumnHidden(0, True)
                            self.ui.tabla_tiptrac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_tiptrac.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute(
                            "SELECT * FROM totalco_tipo_tracto ORDER BY id_tipo_tracto DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_tiptrac.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_tiptrac.setRowCount(fila + 1)
                                self.ui.tabla_tiptrac.setColumnHidden(0, True)
                                self.ui.tabla_tiptrac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_tiptrac.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_tipo_tracto ORDER BY id_tipo_tracto DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_tiptrac.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_tiptrac.setRowCount(fila + 1)
                        self.ui.tabla_tiptrac.setColumnHidden(0, True)
                        self.ui.tabla_tiptrac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_tiptrac.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminarTipoTracto(self):
        logger.debug("Eliminar Tipo de Tracto")
        self.filaSeleccionada = self.ui.tabla_tiptrac.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_tiptrac.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_tiptrac.item(indiceFila, 1).text()
                    logger.debug("id Tipo: {}".format(self.idItem))
                    logger.debug("Nombre Tipo: {}".format(nombreItem))
                    self.ui.tabla_tiptrac.removeRow(indiceFila)
                    self.ui.tabla_tiptrac.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_tipo_tracto WHERE id_tipo_tracto = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoTipoTracto(self):
        logger.debug("Nuevo Tipo de Tracto")
        from Operador_TipoTracto_Create import operadorCreateTipoTracto
        goto = operadorCreateTipoTracto()
        goto.exec_()

    def gotoRefrescarTipoTracto(self):
        logger.debug("Refrescar tabla Tipo de Tracto")
        try:
            self.cur.execute("SELECT * FROM totalco_tipo_tracto ORDER BY id_tipo_tracto DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_tiptrac.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_tiptrac.setRowCount(fila + 1)
                    self.ui.tabla_tiptrac.setColumnHidden(0, True)
                    self.ui.tabla_tiptrac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_tiptrac.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarTipoTracto(self):
        logger.debug("Actualizar Tipo de Tracto")
        self.filaSeleccionada = self.ui.tabla_tiptrac.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_tiptrac.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_tiptrac.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo de Tracto: {}".format(nombreItem))

                from Operador_TipoTracto_Update import operadorUpdateTipoTracto
                goto = operadorUpdateTipoTracto(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> TRACTOS ==> CAJA-PORTA
    #####
    def menu_cajaporta(self):
        logger.debug("Funcion Caja - Porta")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cajaporta)
        UIFunctions.labelPage(self, "MENU CAJA PORTACONTENEDOR")
        try:
            self.cur.execute("SELECT porta.id_portacontenedor AS id, porta.placas AS placas, cajaporta.caja_porta AS tipo, trans.linea AS linea FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) ORDER BY id_portacontenedor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_porta.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_porta.setRowCount(fila + 1)
                    self.ui.tabla_porta.setColumnHidden(0, True)
                    self.ui.tabla_porta.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_porta.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_porta.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_porta.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarCajaPorta(self):
        logger.debug("Buscar Caja Porta")
        self.textoBuscar = self.ui.BuscarlineEditCajaPorta.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT porta.id_portacontenedor AS id, porta.placas AS placas, cajaporta.caja_porta AS tipo, trans.linea AS linea FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) WHERE placas LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_porta.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_porta.setRowCount(fila + 1)
                            self.ui.tabla_porta.setColumnHidden(0, True)
                            self.ui.tabla_porta.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_porta.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_porta.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                            self.ui.tabla_porta.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT porta.id_portacontenedor AS id, porta.placas AS placas, cajaporta.caja_porta AS tipo, trans.linea AS linea FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) ORDER BY id_portacontenedor DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_porta.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_porta.setRowCount(fila + 1)
                                self.ui.tabla_porta.setColumnHidden(0, True)
                                self.ui.tabla_porta.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_porta.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                self.ui.tabla_porta.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                                self.ui.tabla_porta.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT porta.id_portacontenedor AS id, porta.placas AS placas, cajaporta.caja_porta AS tipo, trans.linea AS linea FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) ORDER BY id_portacontenedor DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_porta.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_porta.setRowCount(fila + 1)
                        self.ui.tabla_porta.setColumnHidden(0, True)
                        self.ui.tabla_porta.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_porta.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_porta.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                        self.ui.tabla_porta.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminarCajaPorta(self):
        logger.debug("Eliminar Caja Porta")
        self.filaSeleccionada = self.ui.tabla_porta.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_porta.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_porta.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_porta.removeRow(indiceFila)
                    self.ui.tabla_porta.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_portacontenedor WHERE id_portacontenedor = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoCajaPorta(self):
        logger.debug("Nueva Caja Porta")

        from Operador_CajaPorta_Create import operadorCreateCajaPorta
        goto = operadorCreateCajaPorta()
        goto.exec_()

    def gotoRefrescarCajaPorta(self):
        logger.debug("Refrescar Tabla")
        try:
            self.cur.execute("SELECT porta.id_portacontenedor AS id, porta.placas AS placas, cajaporta.caja_porta AS tipo, trans.linea AS linea FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) ORDER BY id_portacontenedor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_porta.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_porta.setRowCount(fila + 1)
                    self.ui.tabla_porta.setColumnHidden(0, True)
                    self.ui.tabla_porta.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_porta.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_porta.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    self.ui.tabla_porta.setItem(fila, 3, QTableWidgetItem(str(resultado[3])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarCajaPorta(self):
        logger.debug("Actualizar Caja Porta")
        self.filaSeleccionada = self.ui.tabla_porta.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_porta.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_porta.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_CajaPorta_Update import operadorUpdateCajaPorta
                goto = operadorUpdateCajaPorta(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> TRACTOS ==> TRACTO
    #####
    def menu_tracto(self):
        logger.debug("Funcion Tracto")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_tractos)
        UIFunctions.labelPage(self, "MENU TRACTO")
        try:
            self.cur.execute("SELECT * FROM totalco_tractor ORDER BY id_tractor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_trac.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_trac.setRowCount(fila + 1)
                    self.ui.tabla_trac.setColumnHidden(0, True)
                    self.ui.tabla_trac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_trac.setItem(fila, 1, QTableWidgetItem(str(resultado[3])))
                    self.ui.tabla_trac.setItem(fila, 2, QTableWidgetItem(str(resultado[4])))
                    self.ui.tabla_trac.setItem(fila, 3, QTableWidgetItem(str(resultado[7])))
                    self.ui.tabla_trac.setItem(fila, 4, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_trac.setItem(fila, 5, QTableWidgetItem(str(resultado[8])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarTracto(self):
        logger.debug("Buscar Tracto")
        self.textoBuscar = self.ui.BuscarlineEditTracto.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_tractor WHERE placas LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_trac.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_trac.setRowCount(fila + 1)
                            self.ui.tabla_trac.setColumnHidden(0, True)
                            self.ui.tabla_trac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_trac.setItem(fila, 1, QTableWidgetItem(str(resultado[3])))
                            self.ui.tabla_trac.setItem(fila, 2, QTableWidgetItem(str(resultado[4])))
                            self.ui.tabla_trac.setItem(fila, 3, QTableWidgetItem(str(resultado[7])))
                            self.ui.tabla_trac.setItem(fila, 4, QTableWidgetItem(str(resultado[1])))
                            self.ui.tabla_trac.setItem(fila, 5, QTableWidgetItem(str(resultado[8])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute("ELECT * FROM totalco_tractor ORDER BY id_tractor DESC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_trac.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_trac.setRowCount(fila + 1)
                                self.ui.tabla_trac.setColumnHidden(0, True)
                                self.ui.tabla_trac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_trac.setItem(fila, 1, QTableWidgetItem(str(resultado[3])))
                                self.ui.tabla_trac.setItem(fila, 2, QTableWidgetItem(str(resultado[4])))
                                self.ui.tabla_trac.setItem(fila, 3, QTableWidgetItem(str(resultado[7])))
                                self.ui.tabla_trac.setItem(fila, 4, QTableWidgetItem(str(resultado[1])))
                                self.ui.tabla_trac.setItem(fila, 5, QTableWidgetItem(str(resultado[8])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_tractor ORDER BY id_tractor DESC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_trac.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_trac.setRowCount(fila + 1)
                        self.ui.tabla_trac.setColumnHidden(0, True)
                        self.ui.tabla_trac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_trac.setItem(fila, 1, QTableWidgetItem(str(resultado[3])))
                        self.ui.tabla_trac.setItem(fila, 2, QTableWidgetItem(str(resultado[4])))
                        self.ui.tabla_trac.setItem(fila, 3, QTableWidgetItem(str(resultado[7])))
                        self.ui.tabla_trac.setItem(fila, 4, QTableWidgetItem(str(resultado[1])))
                        self.ui.tabla_trac.setItem(fila, 5, QTableWidgetItem(str(resultado[8])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminarTracto(self):
        logger.debug("Eliminar Tracto")
        self.filaSeleccionada = self.ui.tabla_trac.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_trac.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_trac.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_trac.removeRow(indiceFila)
                    self.ui.tabla_trac.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_tractor WHERE id_tractor = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevoTracto(self):
        logger.debug("Nuevo Tracto")

        from Operador_Tracto_Create import operadorCreateTracto
        goto = operadorCreateTracto()
        goto.exec_()

    def gotoRefrescarTracto(self):
        logger.debug("Refrescar Tabla Tracto")
        try:
            self.cur.execute("SELECT * FROM totalco_tractor ORDER BY id_tractor DESC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_trac.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_trac.setRowCount(fila + 1)
                    self.ui.tabla_trac.setColumnHidden(0, True)
                    self.ui.tabla_trac.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_trac.setItem(fila, 1, QTableWidgetItem(str(resultado[3])))
                    self.ui.tabla_trac.setItem(fila, 2, QTableWidgetItem(str(resultado[4])))
                    self.ui.tabla_trac.setItem(fila, 3, QTableWidgetItem(str(resultado[7])))
                    self.ui.tabla_trac.setItem(fila, 4, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_trac.setItem(fila, 5, QTableWidgetItem(str(resultado[8])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoActualizarTracto(self):
        logger.debug("Actualizar Tracto")
        self.filaSeleccionada = self.ui.tabla_trac.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_trac.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_trac.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_Tracto_Update import operadorUpdateTracto
                goto = operadorUpdateTracto(idItem, nombreItem)
                goto.exec_()
            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))
    ## ==> END ##

    #####
    ## EVENT ==> FUNCIONES DE MENÚ DESTINOS ==> DESTINO VENTAS
    #####
    def menu_destinoventas(self):
        logger.debug("Funcion Menu Destino ventas")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destinoventas)
        UIFunctions.labelPage(self, "MENU DESTINO VENTAS")
        try:
            self.cur.execute("SELECT * FROM totalco_destino_vta WHERE id_destino_vta > 0 ORDER BY id_destino_vta ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_dv.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_dv.setRowCount(fila + 1)
                    self.ui.tabla_dv.setColumnHidden(0, True)
                    self.ui.tabla_dv.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_dv.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarDestinoVta(self):
        logger.debug("Boton Buscar")
        self.textoBuscar = self.ui.BuscarlineEditDestinoVta.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM totalco_destino_vta WHERE destino_vta LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_dv.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_dv.setRowCount(fila + 1)
                            self.ui.tabla_dv.setColumnHidden(0, True)
                            self.ui.tabla_dv.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_dv.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ", QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT * FROM totalco_destino_vta WHERE id_destino_vta > 0 ORDER BY id_destino_vta ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_dv.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_dv.setRowCount(fila + 1)
                                self.ui.tabla_dv.setColumnHidden(0, True)
                                self.ui.tabla_dv.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_dv.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT * FROM totalco_destino_vta WHERE id_destino_vta > 0 ORDER BY id_destino_vta ASC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_dv.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_dv.setRowCount(fila + 1)
                        self.ui.tabla_dv.setColumnHidden(0, True)
                        self.ui.tabla_dv.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_dv.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminardestinovta(self):
        logger.debug("Eliminar Destino Venta")
        self.filaSeleccionada = self.ui.tabla_dv.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_dv.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_dv.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_dv.removeRow(indiceFila)
                    self.ui.tabla_dv.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_destino_vta WHERE id_destino_vta = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevodestinovta(self):
        logger.debug("Boton Nuevo Destino Venta")

        from Operador_Destinovta_Create import operadorCreateDestinovta
        goto = operadorCreateDestinovta()
        goto.exec_()

    def gotoRefrescarDestinovta(self):
        logger.debug("Boton Refescar tabla destino venta")
        try:
            self.cur.execute("SELECT * FROM totalco_destino_vta WHERE id_destino_vta > 0 ORDER BY id_destino_vta ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_dv.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_dv.setRowCount(fila + 1)
                    self.ui.tabla_dv.setColumnHidden(0, True)
                    self.ui.tabla_dv.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_dv.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarDestinovta(self):
        logger.debug("Boton Actualizar Destino Venta")
        self.filaSeleccionada = self.ui.tabla_dv.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_dv.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_dv.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_Destinovta_Update import operadorUpdateDestinovta
                goto = operadorUpdateDestinovta(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    #####
    ## EVENT ==> FUNCIONES DE MENÚ DESTINOS ==> DESTINO VENTAS
    #####
    def menu_destinosolas(self):
        logger.debug("Funcion Menu Destino Ventas SOLAS")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destinosolas)
        UIFunctions.labelPage(self, "MENU DESTINO SOLAS")
        try:
            self.cur.execute("SELECT * FROM totalco_destino_vta_solas WHERE id_destino_vta_solas > 0 ORDER BY id_destino_vta_solas ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_dsol.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_dsol.setRowCount(fila + 1)
                    self.ui.tabla_dsol.setColumnHidden(0, True)
                    self.ui.tabla_dsol.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_dsol.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarDestinoSolas(self):
        logger.debug("Buscar Destino Solas")
        self.textoBuscar = self.ui.BuscarlineEditDestinoSolas.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino_vta_solas WHERE destino_vta_solas LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_dsol.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_dsol.setRowCount(fila + 1)
                            self.ui.tabla_dsol.setColumnHidden(0, True)
                            self.ui.tabla_dsol.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_dsol.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute(
                            "SELECT * FROM totalco_destino_vta_solas WHERE id_destino_vta_solas > 0 ORDER BY id_destino_vta_solas ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_dsol.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_dsol.setRowCount(fila + 1)
                                self.ui.tabla_dsol.setColumnHidden(0, True)
                                self.ui.tabla_dsol.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_dsol.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino_vta_solas WHERE id_destino_vta_solas > 0 ORDER BY id_destino_vta_solas ASC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_dsol.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_dsol.setRowCount(fila + 1)
                        self.ui.tabla_dsol.setColumnHidden(0, True)
                        self.ui.tabla_dsol.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_dsol.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminardestinoSolas(self):
        logger.debug("Eliminar Destino Solas")
        self.filaSeleccionada = self.ui.tabla_dsol.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_dsol.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_dsol.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_dsol.removeRow(indiceFila)
                    self.ui.tabla_dsol.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_destino_vta_solas WHERE id_destino_vta_solas = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevodestinoSolas(self):
        logger.debug("Nuevo Destino Solas")
        from Operador_DestinovtaSolas_Create import operadorCreateDestinovtaSolas
        goto = operadorCreateDestinovtaSolas()
        goto.exec_()

    def gotoRefrescarDestinoSolas(self):
        logger.debug("Refrescar Destino Solas")
        try:
            self.cur.execute("SELECT * FROM totalco_destino_vta_solas WHERE id_destino_vta_solas > 0 ORDER BY id_destino_vta_solas ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_dsol.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_dsol.setRowCount(fila + 1)
                    self.ui.tabla_dsol.setColumnHidden(0, True)
                    self.ui.tabla_dsol.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_dsol.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarDestinoSolas(self):
        logger.debug("Actualizar Destino Solas")
        self.filaSeleccionada = self.ui.tabla_dsol.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_dsol.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_dsol.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_DestinovtaSolas_Update import operadorUpdateDestinovtaSolas
                goto = operadorUpdateDestinovtaSolas(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##
    #####

    ## EVENT ==> FUNCIONES DE MENÚ DESTINOS ==> DESTINO SUCURSAL
    #####
    def menu_destinosucursal(self):
        logger.debug("Funcion Menu Destino Ventas SUCURSAL")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destinosucursal)
        UIFunctions.labelPage(self, "MENU DESTINO SUCURSAL")
        try:
            self.cur.execute(
                "SELECT * FROM totalco_destino_sucursal WHERE id_destino_sucursal > 0 ORDER BY id_destino_sucursal ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_suc.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_suc.setRowCount(fila + 1)
                    self.ui.tabla_suc.setColumnHidden(0, True)
                    self.ui.tabla_suc.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_suc.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarDestinoSucursal(self):
        logger.debug("Buscar Sucursal")
        self.textoBuscar = self.ui.BuscarlineEditDestinoSucursal.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino_sucursal WHERE destino_sucursal LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_suc.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_suc.setRowCount(fila + 1)
                            self.ui.tabla_suc.setColumnHidden(0, True)
                            self.ui.tabla_suc.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_suc.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute(
                            "SELECT * FROM totalco_destino_sucursal WHERE id_destino_sucursal > 0 ORDER BY id_destino_sucursal ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_suc.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_suc.setRowCount(fila + 1)
                                self.ui.tabla_suc.setColumnHidden(0, True)
                                self.ui.tabla_suc.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_suc.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino_sucursal WHERE id_destino_sucursal > 0 ORDER BY id_destino_sucursal ASC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_suc.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_suc.setRowCount(fila + 1)
                        self.ui.tabla_suc.setColumnHidden(0, True)
                        self.ui.tabla_suc.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_suc.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminardestinoSucursal(self):
        logger.debug("Eliminar Sucursal")
        self.filaSeleccionada = self.ui.tabla_suc.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_suc.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_suc.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_suc.removeRow(indiceFila)
                    self.ui.tabla_suc.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_destino_sucursal WHERE id_destino_sucursal = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevodestinoSucursal(self):
        logger.debug("Nueva Sucursal")
        from Operador_DestinoSucursal_Create import operadorCreateSucursal
        goto = operadorCreateSucursal()
        goto.exec_()

    def gotoRefrescarDestinoSucursal(self):
        logger.debug("Refrescar tabla Sucursal")
        try:
            self.cur.execute("SELECT * FROM totalco_destino_sucursal WHERE id_destino_sucursal > 0 ORDER BY id_destino_sucursal ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_suc.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_suc.setRowCount(fila + 1)
                    self.ui.tabla_suc.setColumnHidden(0, True)
                    self.ui.tabla_suc.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_suc.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarDestinoSucursal(self):
        logger.debug("Actualizar Sucursal")
        self.filaSeleccionada = self.ui.tabla_suc.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_suc.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_suc.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_DestinoSucursal_Update import operadorUpdateSucursal
                goto = operadorUpdateSucursal(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    ## EVENT ==> FUNCIONES DE MENÚ DESTINOS ==> DESTINO SUCURSAL
    #####
    def menu_sifon(self):
        logger.debug("Funcion Menu Destino Ventas BODEGA/SIFON/MAQUILA")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_destinosifon)
        UIFunctions.labelPage(self, "MENU DESTINO BODEGA/SIFON/MAQUILA")
        try:
            self.cur.execute(
                "SELECT * FROM totalco_destino WHERE id_destino > 0 ORDER BY id_destino ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_sif.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_sif.setRowCount(fila + 1)
                    self.ui.tabla_sif.setColumnHidden(0, True)
                    self.ui.tabla_sif.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_sif.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoBuscarDestinoSifon(self):
        logger.debug("Buscar sifon/bodega/maquila")
        self.textoBuscar = self.ui.BuscarlineEditDestinoSifon.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino WHERE destino LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_sif.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.tabla_sif.setRowCount(fila + 1)
                            self.ui.tabla_sif.setColumnHidden(0, True)
                            self.ui.tabla_sif.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.tabla_sif.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ",
                                            QMessageBox.Ok)
                    try:
                        self.cur.execute(
                            "SELECT * FROM totalco_destino WHERE id_destino > 0 ORDER BY id_destino ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.tabla_sif.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.tabla_sif.setRowCount(fila + 1)
                                self.ui.tabla_sif.setColumnHidden(0, True)
                                self.ui.tabla_sif.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.tabla_sif.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute(
                    "SELECT * FROM totalco_destino WHERE id_destino > 0 ORDER BY id_destino ASC")
                self.resultados = self.cur.fetchall()
                self.ui.tabla_sif.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.tabla_sif.setRowCount(fila + 1)
                        self.ui.tabla_sif.setColumnHidden(0, True)
                        self.ui.tabla_sif.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.tabla_sif.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def gotoeliminardestinoSifon(self):
        logger.debug("Eliminar sifon/bodega/maquila")
        self.filaSeleccionada = self.ui.tabla_sif.selectedItems()
        try:
            if self.filaSeleccionada:
                reply = QMessageBox.question(
                    self, "Mensaje",
                    "¿Estás completamente seguro de borrarlo del sistema?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if reply == QMessageBox.Ok:
                    logger.debug("Fila seleccionada: {}".format(self.filaSeleccionada))
                    indiceFila = self.filaSeleccionada[0].row()
                    logger.debug("indice de fila: {}".format(indiceFila))
                    self.idItem = self.ui.tabla_sif.item(indiceFila, 0).text()
                    nombreItem = self.ui.tabla_sif.item(indiceFila, 1).text()
                    logger.debug("id: {}".format(self.idItem))
                    logger.debug("Nombre: {}".format(nombreItem))
                    self.ui.tabla_sif.removeRow(indiceFila)
                    self.ui.tabla_sif.clearSelection()
                    try:
                        logger.debug("Borrar en BD")
                        sql = """ DELETE FROM totalco_destino WHERE id_destino = %s LIMIT 1 """
                        row = (self.idItem,)
                        self.cur.execute(sql, row)
                        self.conn.commit()
                    except Exception as e:
                        logger.debug("Error al eliminar: {}".format(e))
                    QMessageBox.information(self, "Éxito", "Se eliminó con Éxito.   ",
                                            QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Eliminar", "Primero seleccione una fila.",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error: {}".format(e))

    def gotoNuevodestinoSifon(self):
        logger.debug("Nuevo sifon/bodega/maquila")
        from Operador_DestinoSifon_Create import operadorCreateDestinoSifon
        goto = operadorCreateDestinoSifon()
        goto.exec_()

    def gotoRefrescarDestinoSifon(self):
        logger.debug("Refrescar tabla sifon/bodega/maquila")
        try:
            self.cur.execute("SELECT * FROM totalco_destino WHERE id_destino > 0 ORDER BY id_destino ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_sif.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_sif.setRowCount(fila + 1)
                    self.ui.tabla_sif.setColumnHidden(0, True)
                    self.ui.tabla_sif.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_sif.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizarDestinoSifon(self):
        logger.debug("Actualizar sifon/bodega/maquia")
        self.filaSeleccionada = self.ui.tabla_sif.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_sif.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_sif.item(indiceFila, 1).text()
                logger.debug("Id en el CRUD: {}".format(idItem))
                logger.debug("Tipo: {}".format(nombreItem))

                from Operador_DestinoSifon_Update import operadorUpdateSifon
                goto = operadorUpdateSifon(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))

    ## ==> END ##

    #####
    ## EVENT ==> FUNCIONES DE DATOS ==> SACO-TARIMA
    #####
    def menu_sacotarima(self):
        logger.debug("Funcion SacoTarima")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sacotarima)
        UIFunctions.labelPage(self, "MENU SACO-TARIMA")
        try:
            self.cur.execute("SELECT * FROM totalco_saco_tarima  ORDER BY id_st ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_sacotarima.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_sacotarima.setRowCount(fila + 1)
                    self.ui.tabla_sacotarima.setColumnHidden(0, True)
                    self.ui.tabla_sacotarima.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_sacotarima.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_sacotarima.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    fila += 1
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def gotoRefrescarSacoTarima(self):
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT * FROM totalco_saco_tarima  ORDER BY id_st ASC")
            self.resultados = self.cur.fetchall()
            self.ui.tabla_sacotarima.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.tabla_sacotarima.setRowCount(fila + 1)
                    self.ui.tabla_sacotarima.setColumnHidden(0, True)
                    self.ui.tabla_sacotarima.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.tabla_sacotarima.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    self.ui.tabla_sacotarima.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))

    def gotoActualizaSacoTarima(self):
        logger.debug("Actualiza Saco Tarima")
        self.filaSeleccionada = self.ui.tabla_sacotarima.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.tabla_sacotarima.item(indiceFila, 0).text()
                nombreItem = self.ui.tabla_sacotarima.item(indiceFila, 1).text()
                pesoItem = self.ui.tabla_sacotarima.item(indiceFila, 2).text()
                logger.debug("Id item en el CRUD: {}".format(idItem))
                logger.debug("Nombre de item: {}".format(nombreItem))
                logger.debug("Peso de item: {}".format(pesoItem))

                from Operador_SacoTarima_Update import operadorUpdateSacoTarima
                goto = operadorUpdateSacoTarima(idItem, nombreItem, pesoItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))
    ## ==> END SACO-TARIMA ##

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        if event.key() == Qt.Key_Escape:
            logger.debug("Key Scape")
            self.close()
    ## ==> END ##

    ## Close window
    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de salir?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            logger.debug("Close")
            # Identify User
            try:
                self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
                self.row_authenticate = self.cur.fetchone()
                # logger.debug("Query: {}".format(self.cur))
                # logger.debug("Result row_authenticate: {}".format(self.row_authenticate))
                # logger.debug("Result 4: {}".format(self.row_authenticate))
                if self.row_authenticate is None:
                    logger.debug("No hay usuario en el sistema")
                else:
                    logger.debug("Identifica")
                    sql = """ UPDATE usuarios SET autenticado = %s WHERE id_usuario = %s """
                    row = (0, self.row_authenticate[0])
                    self.cur.execute(sql, row)
                    self.conn.commit()
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
            finally:
                self.cur.close()
            # Authenticate Update
        else:
            logger.debug("Cancel")
            event.ignore()

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(Window2, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

class MainWindow(QMainWindow):

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        #Buttons and Fields
        btn = self.window.findChild(QPushButton, 'ButtonLogin')
        btn.clicked.connect(self.window2)
        field_pass = self.window.findChild(QLineEdit, 'password')
        field_pass.returnPressed.connect(self.window2)
        btn2 = self.window.findChild(QPushButton, 'btn_desbloqueo')
        btn2.clicked.connect(self.window3)


        self.window.show()
        self.DB_Connect()


    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def window3(self):
        logger.debug("Desbloqueo")

        # Inicia login
        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row_authenticate = self.cur.fetchone()
            if self.row_authenticate is None:
                logger.debug("NO Esta bloqueado")
                QMessageBox.information(self, "Mensaje", "El sistema no esta bloqueado", QMessageBox.Ok)
                pass
            else:
                logger.debug("Esta bloqueado")
                self.id_usuario = self.row_authenticate[0]
                self.nombre = self.row_authenticate[5]
                logger.debug("Id de usuario bloqueado: {}".format(self.id_usuario))
                logger.debug("Nombre de usuario: {}".format(self.nombre))
                self.autenticado = 0
                try:
                    query = """ UPDATE usuarios SET autenticado = %s WHERE id_usuario = %s """
                    data = (str(self.autenticado), self.id_usuario)
                    self.cur.execute(query, data)
                    self.conn.commit()
                    QMessageBox.information(self, "Éxito", "Se desbloqueo el sistema exitosamente", QMessageBox.Ok)
                    logger.debug("Desbloqueado el sistema")
                except Exception as e:
                    logger.debug("Error en el update de desbloqueo de usuario: {}".format(e))
        except Exception as e:
            logger.exception("Error Query Usuario: {}".format(e))


    def window2(self):
        logger.debug("Login Button")
        get_user = self.window.findChild(QLineEdit, 'user')
        username = get_user.text()
        # print('Print Usuario: ' + str(user))
        logger.debug("Usuario: {}".format(str(username)))
        get_password = self.window.findChild(QLineEdit, 'password')
        password = get_password.text()
        logger.debug("Password: {}".format(password))
        # print('Password: ' + str(password))

        # Inicia login
        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("Query: {}".format(self.cur))
            logger.debug("Result row_authenticate: {}".format(self.row_authenticate))
            logger.debug("Result 4: {}".format(self.row_authenticate))
            if self.row_authenticate is None:
                try:
                    self.cur.execute(
                        "SELECT * FROM usuarios WHERE usuario='" + username + "' AND password='" + password + "'")
                    self.row = self.cur.fetchone()
                    logger.debug("Query: {}".format(self.cur))
                    logger.debug("Result: {}".format(self.row))
                except Exception as e:
                    logger.exception("Error Query Usuario: {}".format(e))

                if self.row is not None:
                    logger.debug("User level: {}".format(self.row[3]))

                    def level1():
                        logger.debug("Hi level 1")
                        sql = """ UPDATE usuarios SET autenticado = %s WHERE id_usuario = %s """
                        row = (1, self.row[0])
                        self.cur.execute(sql, row)
                        self.conn.commit()
                        self.Operador()

                    def level2():
                        logger.debug("Hi level 2")

                    def level3():
                        logger.debug("Hi level 3")

                    # Python switch
                    level = self.row[3]
                    options = {1: level1,
                               2: level2,
                               3: level3,
                               }
                    options[level]()
                else:
                    logger.debug("Usuario o password incorrecto/vacio")
                    Q = QMessageBox()
                    Q = QMessageBox.information(Q, 'Error',
                                                'Usuario o password incorrecto/vacio.',
                                                QMessageBox.Ok)
            else:
                logger.debug("Hay un usuario en el sistema")
                Q = QMessageBox()
                Q = QMessageBox.information(Q, 'Error',
                                            'El sistema ya esta siendo utilizado.',
                                            QMessageBox.Ok)
        except Exception as e:
            logger.exception("Error Query Usuario: {}".format(e))

    def Operador(self):
        logger.debug("Operador")
        self.w = Window2()
        self.w.show()
        # self.window.hide()
        self.window.close()
        self.cur.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('icons/company/16x16.png', QtCore.QSize(16, 16))
    app_icon.addFile('icons/company/24x24.png', QtCore.QSize(24, 24))
    app_icon.addFile('icons/company/32x32.png', QtCore.QSize(32, 32))
    app_icon.addFile('icons/company/48x48.png', QtCore.QSize(48, 48))
    app_icon.addFile('icons/company/256x256.png', QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow('login.ui')
    sys.exit(app.exec_())