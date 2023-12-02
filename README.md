# SIPCASMO21

#Version PyESCPOS
En esta version la impresión es directa sin cable serial-USB
La lectura del indicador es directa sin cable serial-USB

# Instalacion de paquetes

SIP CASMO Sistema de pesadas para Cafés Tomari

Para su funcionamiento se deben agregar los siguientes paquetes:

pip install pyside2==5.15.2

pip install mysql-connector

pip install escpos

pip install PyESCPOS

pip install serial

pip install opencv-python

pip install pyserial

pip install pyqt5

pip install pyusb

pip install Pillow

pip install qrcode

pip install pywin32 (For windows machines)

pip install pyqt5-stubs==5.14.2.2

pip install --upgrade cx_Freeze

setup.py

import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["escpos"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None

if sys.platform == "win32":

    base = "Win32GUI"


setup(

    name = "sipcasmo",

    version = "0.1",

    description = "Sipcasmo",

    options = {"build_exe": build_exe_options},

    executables = [Executable("main.py", base=base)]

)


python setup.py build

Despues de modificar un archivo y moverlo a la carpeta, se debe construir(build) el main
nuevamente.


Variable name: ESCPOS_CAPABILITIES_FILE

Variables Value: C:\Users\Bascula Totalco\AppData\Local\Programs\Python\Python38\Lib\site-packages\escpos\capabilities.json

How to Make Windows 10 Accept File Paths Over 260 Characters

https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/

# Creacion de archivos Excel

pip install xlsxwriter

pip install openpyxl

# Crear archivo PY desde un UI

C:\Users\gerar\AppData\Local\Programs\Python\Python38\Scripts\pyside2-uic.exe ui_main.ui -o ui_main.py

C:\Users\Nombre de Usuario\AppData\Local\Programs\Python\Python38\Scripts\pyside2-uic.exe ui_main.ui -o ui_main.py

# Agregar imagenes para el QT Designer

C:\Users\gerar\AppData\Local\Programs\Python\Python38\Scripts\pyrcc5 imagenesv1.qrc -o imagenesv1_rc.py

# Crear PDF e imprimir

pip install reportlab
