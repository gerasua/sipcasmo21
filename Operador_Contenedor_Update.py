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


class operadorUpdateContenedor(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(operadorUpdateContenedor, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Contenedor_Update.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        logger.debug("Placas: {}".format(nombreItem))
        self.id = idItem
        self.clave = nombreItem

        try:
            self.cur.execute("SELECT cont.id_contenedor AS idContenedor, cont.id_clave_conte AS ClaveContenedor, contTipo.contenedor_tipo AS TipoContenedor, contTipo.id_contenedor_tipo AS idTipoContenedor, porta.placas AS placasporta, porta.id_portacontenedor AS idPorta FROM totalco_contenedor cont INNER JOIN totalco_portacontenedor porta INNER JOIN totalco_contenedor_tipo contTipo ON (porta.id_portacontenedor = cont.id_portacontenedor) AND (cont.id_tipo_contenedor = contTipo.id_contenedor_tipo) WHERE id_contenedor ='" + str(self.id) + "'")
            self.row = self.cur.fetchone()
            self.clave = self.row[1]
            self.tipo_contenedor = self.row[2]
            self.id_tipo_contenedor = self.row[3]
            self.placas_Portacontenedor = self.row[4]
            self.id_portacontenedor = self.row[5]

            logger.debug("Id Tipo de contenedor: {}".format(self.id_tipo_contenedor))
            logger.debug("Tipo de contenedor: {}".format(self.tipo_contenedor))
            logger.debug("Id Portacontenedor: {}".format(self.id_portacontenedor))
            logger.debug("Placas Portacontenedor: {}".format(self.placas_Portacontenedor))

        except Error as e:
            logger.debug("Query Error: {}".format(e))

        # TIPO DE CONTENEDOR
        self.comboBoxTipoCont.addItem(str(self.tipo_contenedor), int(self.id_tipo_contenedor))
        try:
            self.cur.execute("SELECT * FROM totalco_contenedor_tipo")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[0] != self.id_tipo_contenedor:
                    self.comboBoxTipoCont.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        # PLACAS PORTACONTENEDOR
        self.comboBoxPlacasPorta.addItem(str(self.placas_Portacontenedor), int(self.id_portacontenedor))
        try:
            self.cur.execute("SELECT * FROM totalco_portacontenedor WHERE caja_porta =1")
            self.resultados = self.cur.fetchall()
            for resultado in self.resultados:
                if resultado[0] != self.id_portacontenedor:
                    self.comboBoxPlacasPorta.addItem(str(resultado[1]), int(resultado[0]))
        except Error as e:
            logger.debug("Error: {}".format(e))

        self.lineEditClave.setText(str(self.clave))

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnActualizar.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        self.clave = self.lineEditClave.displayText()

        if self.clave:
            logger.debug("Actualizar Datos")
            logger.debug("Clave en el Update: {}".format(self.clave))

            self.id_tipo_contenedor = self.comboBoxTipoCont.itemData(self.comboBoxTipoCont.currentIndex())
            logger.debug("Id Tipo de contenedor: {}".format(self.id_tipo_contenedor))

            self.id_portacontenedor = self.comboBoxPlacasPorta.itemData(self.comboBoxPlacasPorta.currentIndex())
            logger.debug("Id Placas Portacontenedor: {}".format(self.id_portacontenedor))

            try:
                query = """ UPDATE totalco_contenedor SET id_clave_conte = %s, id_tipo_contenedor= %s, id_portacontenedor= %s WHERE id_contenedor = %s """
                data = (str(self.clave), str(self.id_tipo_contenedor), str(self.id_portacontenedor), self.id)
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
