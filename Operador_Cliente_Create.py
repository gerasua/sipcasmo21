from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIntValidator

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


class operadorCreateCliente(QDialog):
    def __init__(self, parent=None):
        super(operadorCreateCliente, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Cliente_Create.ui', self)
        logger.debug("Ventana agregar Cliente")
        self.DB_Connect()

        # BOTONES
        self.btnCancelarCliente.clicked.connect(self.cancelar)
        self.btnAgregarCliente.clicked.connect(self.agregar)

        e1 = self.lineEditSAP
        e1.objectName()
        e1.setValidator(QIntValidator())

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.clave = self.lineEditClave.displayText()
        logger.debug("Clave: {}".format(self.clave))

        self.nombre = self.lineEditNombre.displayText()
        logger.debug("Nombre de cliente: {}".format(self.nombre))

        self.sap = self.lineEditSAP.displayText()
        logger.debug("SAP: {}".format(self.sap))


        if self.nombre:
            logger.debug("No esta vacío")
            try:
                query = "INSERT INTO `totalco_cliente` (`id_cliente`, `clave_cliente`, `nombre_cliente`, `clave_cliente_sap`) VALUES (NULL, '{}', '{}', '{}')".format(
                    self.clave, self.nombre, self.sap)
                logger.debug("Query: {}".format(query))
                # args = (self.clave, self.nombre, self.sap)
                # self.cur.execute(query, args)
                self.cur.execute(query)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Nombre.   ", QMessageBox.Ok)
            self.lineEditNombre.setFocus()

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
