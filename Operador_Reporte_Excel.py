from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtWidgets import QDialog
import time
import os
import platform
import subprocess
from xlsxwriter.workbook import Workbook
from openpyxl import Workbook


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


class operadorCreateExcel(QDialog):
    def __init__(self, parent=None):
        super(operadorCreateExcel, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('Operador_Reporte_Excel.ui', self)
        logger.debug("Ventana crear archivo de Excel")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btn_exportar.clicked.connect(self.crear)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def crear(self):
        logger.debug("Crear archivo de Excel")

        try:
            self.cur.execute("SELECT * FROM totalco_info_gral")
            self.row = self.cur.fetchone()
            self.sucursal = self.row[3]

        except Exception as e:
            logger.debug("Error: {}".format(e))

        path_de_reportes = 'reportes_' + self.sucursal + '/'
        open_path_ = 'reportes_' + self.sucursal
        logger.debug("Directorio: {}".format(path_de_reportes))
        SAVE_PATH = path_de_reportes
        # OPEN_PATH = "C:\\Users\\Bascula Totalco\\PycharmProjects\\SIPCASMO21\\reportes"
        OPEN_PATH = open_path_
        logger.debug("OPEN PATH: {}".format(OPEN_PATH))

        self.fecha1 = self.calendar1.selectedDate().toString("yyyy-MM-dd")
        logger.debug("Fecha 1: {}".format(self.fecha1))

        self.fecha2 = self.calendar2.selectedDate().toString("yyyy-MM-dd")
        logger.debug("Fecha 2: {}".format(self.fecha2))

        if self.fecha2 < self.fecha1:
            logger.debug("La fecha 2 no puede ser menor a la fecha 1")
            QMessageBox.information(self, "Cuidado", "La segunda fecha no puede ser mayor a la primera", QMessageBox.Ok)
        else:
            logger.debug("Se inicia la creación del archivo")
            logger.debug("Query para archivo de excel")
            try:
                self.cur.execute("SELECT numero_ticket AS TICKET,cliente AS CLIENTE,proveedor AS PROVEEDOR, sucursal AS SUCURSAL,usuario_primera AS PESADOR_ENTRADA,producto AS PRODUCTO,fecha_primera AS FECHA_ENTRADA,hora_primera AS HORA_ENTRADA,placas AS PLACAS,placas_portacontenedor AS CAJA_CONTENEDOR,operador_entrada AS CHOFER_ENTRADA,primera_pesada AS PRIMERA_PESADA,observaciones_entrada AS OBSERVACIONES_ENTRADA,fecha_segunda AS FECHA_SALIDA,hora_segunda AS HORA_SALIDA,segunda_pesada AS SEGUNDA_PESADA,peso_neto_embalaje AS PESO_NETO,peso_neto_sin_embalaje_redondeo AS KG_NETOS, yute AS SACO_YUTE, propileno AS SACO_PROPILENO, supersaco AS SUPER_SACO, tarimas AS TARIMA, raspa AS SACO_RASPA, super_saco10 AS FORRO_CONTENEDOR, tarimas_chep AS TARIMA_CHEP, tarimas_reforzada AS TARIMA_REFORZADA, sacos_especiales AS SACO_ESPECIAL, tarimas_especiales AS TARIMA_ESPECIAL, total_embalaje AS PESO_EMBALAJE,observaciones_salida AS OBSERVACIONES,operador_salida AS CHOFER_SALIDA,usuario_segunda AS PESADOR_SALIDA,linea_trasnportista AS LINEA,maniobra AS MANIOBRA, identifica_pedido_tipo AS TIPO, cancela_status AS CANCELADO FROM totalco_destare WHERE fecHa_primera >='" + self.fecha1 + "' AND fecha_segunda <='" + self.fecha2 + "'")
                wb = Workbook()
                table_name = self.sucursal
                self.results = self.cur.fetchall()
                logger.debug(self.results)
                ws = wb.create_sheet(index=0)
                ws.title = table_name
                ws.append(self.cur.column_names)
                for row in self.results:
                    ws.append(row)
                workbook_name = table_name
                wb.save(SAVE_PATH + workbook_name + str(time.strftime("_%d_%m_%Y_%H_%M")) + ".xlsx")

                if platform.system() == "Windows":
                    os.system("explorer " + OPEN_PATH)
                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", SAVE_PATH])
                else:
                    subprocess.Popen(["xdg-open", SAVE_PATH])
                self.hide()

            except Error as e:
                logger.debug("ERROR: {}".format(e))

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
