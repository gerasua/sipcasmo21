from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QDate
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIntValidator
from datetime import datetime


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


class operadorUpdateChofer(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(operadorUpdateChofer, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Chofer_Update.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        logger.debug("Nombre Item: {}".format(nombreItem))

        self.cur.execute("SELECT * FROM totalco_operadores WHERE id_operador='" + idItem + "'")
        self.row = self.cur.fetchone()

        self.nombre = nombreItem
        self.licencia = self.row[2]
        self.vigencia = self.row[3]
        self.celular = self.row[4]
        logger.debug("Query: {}".format(self.cur))
        logger.debug("Result: {}".format(self.row))
        logger.debug("Licencia: {}".format(self.licencia))
        logger.debug("Vigencia: {}".format(self.vigencia))
        logger.debug("Celular: {}".format(self.celular))

        e1 = self.lineEditLicencia
        e1.objectName()
        e1.setValidator(QIntValidator())

        e2 = self.lineEditCelular
        e2.objectName()
        e2.setValidator(QIntValidator())

        self.id = idItem
        self.lineEditChofer.setText(str(self.nombre))
        self.lineEditLicencia.setText(str(self.licencia))
        self.lineEditCelular.setText(str(self.celular))

        # Obtener la fecha para meterla en Widget Calendar
        formato = "%Y-%m-%d"
        # vigencia = "2023-06-18"
        fecha = datetime.strptime(str(self.vigencia), formato)
        logger.debug(fecha)
        año = fecha.year
        mes = fecha.month
        dia = fecha.day
        logger.debug("{}, {}, {}".format(año, mes, dia))
        self.vigenciadate.setSelectedDate(QDate(año, mes, dia))


        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnActualizar.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        self.nombre = self.lineEditChofer.displayText()
        logger.debug("Nombre: {}".format(self.nombre))
        self.licencia = self.lineEditLicencia.displayText()
        logger.debug("Licencia: {}".format(self.licencia))
        self.vigencia = self.vigenciadate.selectedDate().toString("yyyy-MM-dd")
        logger.debug("Vigencia Licencia: {}".format(self.vigencia))
        self.celular = self.lineEditCelular.displayText()
        logger.debug("Celular: {}".format(self.celular))

        if self.nombre:
            logger.debug("No esta vacío")
            try:
                query = """ UPDATE totalco_operadores SET nombre = %s, licencia = %s, vigencia = %s, celular = %s WHERE id_operador = %s """
                data = (str(self.nombre), str(self.licencia), str(self.vigencia), str(self.celular), self.id)
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
            self.lineEditChofer.setFocus()

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
