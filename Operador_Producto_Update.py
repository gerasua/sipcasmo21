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


class operadorUpdateProducto(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(operadorUpdateProducto, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Producto_Update.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        logger.debug("Nombre Item: {}".format(nombreItem))

        self.cur.execute("SELECT * FROM totalco_producto WHERE id_producto='" + idItem + "'")
        self.row = self.cur.fetchone()

        self.claveProducto = self.row[1]
        self.codigosap = self.row[3]
        logger.debug("Query: {}".format(self.cur))
        logger.debug("Result: {}".format(self.row))
        logger.debug("Codigo SAP: {}".format(self.codigosap))

        self.id = idItem
        self.lineEditUpdateClave.setText(str(self.claveProducto))
        self.lineEditUpdateNombre.setText(str(nombreItem))
        self.lineEditUpdateSAP.setText(str(self.codigosap))

        e1 = self.lineEditUpdateSAP
        e1.objectName()
        e1.setValidator(QIntValidator())

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnActualizar.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        self.itemUpdate = self.lineEditUpdateNombre.displayText()
        self.claveProductoUpdate = self.lineEditUpdateClave.displayText()
        self.codigoSapUpdate = self.lineEditUpdateSAP.displayText()
        logger.debug("Nombre: {}".format(self.itemUpdate))
        if self.itemUpdate:
            logger.debug("No esta vacío")
            try:
                query = """ UPDATE totalco_producto SET nombre_producto = %s, clave_producto = %s, clave_sap = %s WHERE id_producto = %s """
                data = (str(self.itemUpdate), str(self.claveProductoUpdate), str(self.codigoSapUpdate), self.id)
                self.cur.execute(query, data)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Nombre.   ", QMessageBox.Ok)
            self.lineEditUpdateNombre.setFocus()

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
