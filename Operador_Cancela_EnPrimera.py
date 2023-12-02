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


class operadorCancelaEnPrimera(QDialog):
    def __init__(self, ticketc, parent=None):
        super(operadorCancelaEnPrimera, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Cancela_EnPrimera.ui', self)
        logger.debug("Ventana Cancelar Ticket")
        self.DB_Connect()
        self.tickeacancelar = ticketc
        logger.debug("Ticket Numero: {}".format(self.tickeacancelar))

        # BOTONES
        self.btnr.clicked.connect(self.cancelar)
        self.btn_guardar.clicked.connect(self.agregar)

        logger.debug("Se obtienen los pesos a mostrar como refrerencia")
        try:
            self.cur.execute("SELECT `peso_e` FROM totalco_boleto_ent WHERE id_bol_entra  ='" + str(self.tickeacancelar) + "'")
            self.row = self.cur.fetchone()
            logger.debug("Valor del ROW Cancelado: {}".format(self.row[0]))
            self.primera_pesada = self.row[0]
            self.segunda_pesada = 0
            self.peso_neto_embalaje = 0
            self.peso_neto_sin_embalaje = 0
            self.peso_neto_sin_embalaje_redondeo = 0

        except Exception as e:
            logger.debug("Error: {}".format(e))

        self.lcdNumber_9.display(self.tickeacancelar)
        self.lcdNumber_3.display(self.primera_pesada)
        self.lcdNumber_7.display(self.segunda_pesada)
        self.lcdNumber_1.display(self.peso_neto_embalaje)
        self.lcdNumber_4.display(self.peso_neto_sin_embalaje)
        self.lcdNumber_6.display(self.peso_neto_sin_embalaje_redondeo)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.InsertarObservacionesCancelar = self.ObservacionesCancelar.toPlainText()
        self.cancelado = 1

        if self.InsertarObservacionesCancelar:
            logger.debug("No esta vacío")
            # Identify User
            try:
                self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
                self.row_authenticate = self.cur.fetchone()
                self.id_usuario = self.row_authenticate[0]
                self.nombre_usuario = self.row_authenticate[5]
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

            try:
                query = """ UPDATE totalco_boleto_ent SET cancelado = %s, observaciones_cancelado = %s, id_usuario_cancela = %s, nombre_usuario_cancela = %s WHERE id_bol_entra = %s """
                data = (str(self.cancelado), str(self.InsertarObservacionesCancelar), str(self.id_usuario), str(self.nombre_usuario), str(self.tickeacancelar))
                self.cur.execute(query, data)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se canceló el ticket {}".format(self.tickeacancelar), QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error en el update: {}".format(e))

        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Observaciones.   ", QMessageBox.Ok)
            self.ObservacionesCancelar.setFocus()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de salir?",
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