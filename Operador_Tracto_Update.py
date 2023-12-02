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


class operadorUpdateTracto(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(operadorUpdateTracto, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Tracto_Update.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        logger.debug("Placas: {}".format(nombreItem))
        self.id = idItem
        self.placas = nombreItem

        try:
            self.cur.execute("SELECT * FROM totalco_tractor WHERE id_tractor='" + idItem + "'")
            self.row = self.cur.fetchone()
            self.clave = self.row[2]
            self.marca = self.row[4]
            self.modelo = self.row[5]
            self.colortracto = self.row[6]
            self.economico = self.row[7]
            self.linea = self.row[8]
            self.idlinea = self.row[9]

            logger.debug("After Query Linea: {}".format(self.linea))
            logger.debug("After Query Id Linea: {}".format(self.idlinea))
        except Error as e:
            logger.debug("Query Error: {}".format(e))
        # TIPO DE TRACTO
        try:
            self.cur.execute("SELECT * FROM `totalco_tractor` WHERE id_tractor ='" + idItem + "'")
            self.row = self.cur.fetchone()
            self.tipo = self.row[1]

            logger.debug("After Query Tipo: {}".format(self.tipo))
        except Error as e:
            logger.debug("Query Error: {}".format(e))

        # COMBOBOX LÍNEA
        self.comboBoxLinea.addItem(str(self.linea), int(self.idlinea))
        try:
            self.cur.execute("SELECT * FROM totalco_transporte")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[1] != self.linea:
                    self.comboBoxLinea.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        # COMBOBOX TIPOS
        self.comboBox_Tipo.addItem(str(self.tipo))
        try:
            self.cur.execute("SELECT * FROM totalco_tipo_tracto")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[1] != self.tipo:
                    self.comboBox_Tipo.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        self.lineEditUpdatePlacas.setText(str(self.placas))
        self.lineEditclave.setText(str(self.clave))
        self.lineEditmarca.setText(str(self.marca))
        self.lineEditmodelo.setText(str(self.modelo))
        self.lineEditcolor.setText(str(self.colortracto))
        self.lineEditeconomico.setText(str(self.economico))

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

        if self.placas:
            logger.debug("Actualizar Datos")
            logger.debug("Placas en el Update: {}".format(self.placas))
            logger.debug("Placas Caja: {}".format(self.placas))

            self.clave = self.lineEditclave.displayText()
            logger.debug("Clave: {}".format(self.clave))
            self.marca = self.lineEditmarca.displayText()
            logger.debug("Marca: {}".format(self.marca))
            self.modelo = self.lineEditmodelo.displayText()
            logger.debug("Modelo: {}".format(self.modelo))
            self.colortracto = self.lineEditcolor.displayText()
            logger.debug("Color: {}".format(self.colortracto))
            self.economico = self.lineEditeconomico.displayText()
            logger.debug("Economico: {}".format(self.economico))

            self.id_linea = self.comboBoxLinea.itemData(self.comboBoxLinea.currentIndex())
            self.linea = self.comboBoxLinea.currentText()
            logger.debug("ID Linea: {}".format(self.id_linea))
            logger.debug("Linea: {}".format(self.linea))

            self.tipo = self.comboBox_Tipo.currentText()
            logger.debug("Tipo: {}".format(self.tipo))
            try:
                query = """ UPDATE totalco_tractor SET tipo = %s, clave= %s, placas= %s, marca_tractor= %s, modelo= %s, color= %s, economico= %s, linea= %s, id_transporte= %s WHERE id_tractor = %s """
                data = (str(self.tipo), str(self.clave), str(self.placas), str(self.marca), str(self.modelo), str(self.colortracto), str(self.economico), str(self.linea), str(self.id_linea), self.id)
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
