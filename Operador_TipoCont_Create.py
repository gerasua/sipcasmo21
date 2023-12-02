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


class operadorCreateTipoCont(QDialog):
    def __init__(self, parent=None):
        super(operadorCreateTipoCont, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_TipoCont_Create.ui', self)
        logger.debug("Ventana agregar Tipo Contenedor")
        self.DB_Connect()

        # BOTONES
        self.btnCancelarAduana.clicked.connect(self.cancelar)
        self.btnAgregarAduana.clicked.connect(self.agregar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.nombre = self.lineEditCreate.displayText()
        logger.debug("Nombre: {}".format(self.nombre))
        if self.nombre:
            logger.debug("No esta vacío")
            try:
                query = "INSERT INTO `totalco_contenedor_tipo` (`id_contenedor_tipo`, `contenedor_tipo`) VALUES (NULL, '{}')".format(
                    self.nombre)
                args = (self.nombre)
                self.cur.execute(query, args)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Nombre.   ", QMessageBox.Ok)
            self.lineEditCreate.setFocus()

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
