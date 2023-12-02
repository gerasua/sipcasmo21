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


class operadorCreateCajaPorta(QDialog):
    def __init__(self, parent=None):
        super(operadorCreateCajaPorta, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_CajaPorta_Create.ui', self)
        logger.debug("Ventana agregar Caja/Porta")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        # COMBOBOX TIPOS
        try:
            self.cur.execute("SELECT * FROM totalco_caja_porta")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBox_Tipo.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))
        # COMBOBOX LINEA TRANSPORTISTA
        try:
            self.cur.execute("SELECT * FROM totalco_transporte")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                self.comboBoxLinea.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.placas = self.lineEditCreate.displayText()
        logger.debug("Placas: {}".format(self.placas))

        # Tipo Contenedor ID
        self.id_tipo_caja_porta = self.comboBox_Tipo.itemData(self.comboBox_Tipo.currentIndex())
        self.tipo_caja_porta = self.comboBox_Tipo.currentText()
        logger.debug("Tipo Contenedor ID: {}".format(self.id_tipo_caja_porta))
        logger.debug("Tipo Contenedor: {}".format(self.tipo_caja_porta))

        # Línea Transportista
        self.id_linea = self.comboBoxLinea.itemData(self.comboBoxLinea.currentIndex())
        self.linea = self.comboBoxLinea.currentText()
        logger.debug("Línea ID: {}".format(self.id_linea))
        logger.debug("Línea: {}".format(self.linea))

        if self.placas:
            logger.debug("No esta vacío")
            try:
                query = "INSERT INTO `totalco_portacontenedor` (`id_portacontenedor`, `placas`, `caja_porta`, `id_transporte`) VALUES (NULL, '{}', '{}', '{}')".format(
                    self.placas, self.id_tipo_caja_porta, self.id_linea)
                self.cur.execute(query)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Placas.   ", QMessageBox.Ok)
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
