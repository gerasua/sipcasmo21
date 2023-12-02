from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)

# Logging and console
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


class operadorCreateContenedor(QDialog):
    def __init__(self, parent=None):
        super(operadorCreateContenedor, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Contenedor_Create.ui', self)
        logger.debug("Ventana agregar Contenedor")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        # COMBOBOX TIPO DE CONTENEDOR
        try:
            self.cur.execute("SELECT * FROM totalco_contenedor_tipo")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBoxTipoCont.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        # COMBOBOX PLACA PORTACONTENEDOR
        try:
            self.cur.execute("SELECT * FROM totalco_portacontenedor WHERE caja_porta =1")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBoxPlacasPorta.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.clave = self.lineEditClave.displayText()
        logger.debug("Clave: {}".format(self.clave))

        # TIPO DE CONTENEDOR
        self.id_tipo_contenedor = self.comboBoxTipoCont.itemData(self.comboBoxTipoCont.currentIndex())
        self.tipo_contenedor = self.comboBoxTipoCont.currentText()
        logger.debug("Tipo contenedor ID: {}".format(self.id_tipo_contenedor))
        logger.debug("Tipo de Contenedor: {}".format(self.tipo_contenedor))

        # PLACAS PORTA CONTENEDOR
        self.id_placasPorta = self.comboBoxPlacasPorta.itemData(self.comboBoxPlacasPorta.currentIndex())
        self.placasPorta = self.comboBoxPlacasPorta.currentText()
        logger.debug("Placas Portacontenedor ID: {}".format(self.id_placasPorta))
        logger.debug("Placas Portacontenedor: {}".format(self.placasPorta))

        if self.clave:
            logger.debug("No esta vacío")
            try:
                query = "INSERT INTO `totalco_contenedor` (`id_clave_conte`, `id_tipo_contenedor`, `id_portacontenedor`) VALUES ('{}', '{}', '{}')".format(
                    self.clave, self.id_tipo_contenedor, self.id_placasPorta)
                self.cur.execute(query)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Clave.   ", QMessageBox.Ok)
            self.lineEditClave.setFocus()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de cancelar?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            logger.debug("Close")
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
