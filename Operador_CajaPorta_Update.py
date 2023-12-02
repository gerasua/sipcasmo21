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


class operadorUpdateCajaPorta(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(operadorUpdateCajaPorta, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_CajaPorta_Update.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        logger.debug("Placas: {}".format(nombreItem))
        self.id = idItem

        self.cur.execute("SELECT porta.placas AS placas, cajaporta.caja_porta AS tipo, porta.caja_porta AS idPC, trans.linea AS linea, trans.id_transporte AS idTransporte FROM totalco_portacontenedor porta INNER JOIN totalco_caja_porta cajaporta INNER JOIN totalco_transporte trans ON (porta.caja_porta = cajaporta.id_caja_porta) AND (porta.id_transporte = trans.id_transporte) WHERE porta.id_portacontenedor ='" + idItem + "'")
        self.row = self.cur.fetchone()

        self.placas = self.row[0]
        self.tipo = self.row[1]
        self.idPC = self.row[2]
        self.linea = self.row[3]
        self.id_linea = self.row[4]

        logger.debug("After Query Placas: {}".format(self.placas))
        logger.debug("After Query Tipo: {}".format(self.tipo))
        logger.debug("After Query id Tipo Caja or Porta: {}".format(self.idPC))
        logger.debug("Id Línea transportista: {}".format(self.id_linea))
        logger.debug("Linea Transportista: {}".format(self.linea))

        self.lineEditUpdatePlacas.setText(str(self.placas))
        self.comboBox_Tipo.addItem(str(self.tipo), int(self.idPC))

        # COMBOBOX TIPOS
        try:
            self.cur.execute("SELECT * FROM totalco_caja_porta")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[1] != self.tipo:
                    self.comboBox_Tipo.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        # COMBOBOX LÍNEA
        self.comboBoxLinea.addItem(str(self.linea), int(self.id_linea))
        try:
            self.cur.execute("SELECT * FROM totalco_transporte")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[1] != self.linea:
                    self.comboBoxLinea.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnActualizar.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        self.placas = self.lineEditUpdatePlacas.displayText()
        logger.debug("Placas Caja: {}".format(self.placas))
        if self.placas:
            logger.debug("Actualizar Datos")
            logger.debug("Placas en el Update: {}".format(self.placas))
            self.id_tipo = self.comboBox_Tipo.itemData(self.comboBox_Tipo.currentIndex())
            self.tipo = self.comboBox_Tipo.currentText()
            logger.debug("ID Tipo: {}".format(self.id_tipo))
            logger.debug("Tipo: {}".format(self.tipo))
            self.id_linea = self.comboBoxLinea.itemData(self.comboBoxLinea.currentIndex())
            logger.debug("Id Línea Transportista: {}".format(self.id_linea))
            try:
                query = """ UPDATE totalco_portacontenedor SET placas = %s, caja_porta = %s, id_transporte= %s WHERE id_portacontenedor = %s """
                data = (str(self.placas), str(self.id_tipo), str(self.id_linea), self.id)
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
