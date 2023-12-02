# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_158 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	\n"
"	image: url(:/48x48/icons/48x48/logo_tomari.png);\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(240, 100))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_1a_pesada = QWidget()
        self.page_1a_pesada.setObjectName(u"page_1a_pesada")
        self.verticalLayout_10 = QVBoxLayout(self.page_1a_pesada)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.page_1a_pesada)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_1a_pesada)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(60)
        self.formLayout_2.setVerticalSpacing(60)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.btn_1a = QPushButton(self.frame_5)
        self.btn_1a.setObjectName(u"btn_1a")
        self.btn_1a.setMinimumSize(QSize(300, 100))
        self.btn_1a.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/ct-caja_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_1a.setIcon(icon3)
        self.btn_1a.setIconSize(QSize(300, 100))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.btn_1a)

        self.btn_1a_solas = QPushButton(self.frame_5)
        self.btn_1a_solas.setObjectName(u"btn_1a_solas")
        self.btn_1a_solas.setMinimumSize(QSize(300, 100))
        self.btn_1a_solas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/ct-solas_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_1a_solas.setIcon(icon4)
        self.btn_1a_solas.setIconSize(QSize(300, 100))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.btn_1a_solas)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(300, 0))
        self.label_6.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(300, 0))
        self.label_7.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_8)


        self.verticalLayout_18.addLayout(self.formLayout_2)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_1a_pesada)
        self.page_primera_menu = QWidget()
        self.page_primera_menu.setObjectName(u"page_primera_menu")
        self.verticalLayout_20 = QVBoxLayout(self.page_primera_menu)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_6 = QFrame(self.page_primera_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 70))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_10)


        self.verticalLayout_21.addLayout(self.verticalLayout_25)


        self.verticalLayout_20.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.page_primera_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_4.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_4.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_4.setHorizontalSpacing(60)
        self.formLayout_4.setVerticalSpacing(60)
        self.formLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.btn_entrada = QPushButton(self.frame_7)
        self.btn_entrada.setObjectName(u"btn_entrada")
        self.btn_entrada.setMinimumSize(QSize(300, 100))
        self.btn_entrada.setMaximumSize(QSize(300, 16777215))
        self.btn_entrada.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/80x80/icons/80x80/ct-entrada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_entrada.setIcon(icon5)
        self.btn_entrada.setIconSize(QSize(80, 80))

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.btn_entrada)

        self.btn_salida = QPushButton(self.frame_7)
        self.btn_salida.setObjectName(u"btn_salida")
        self.btn_salida.setMinimumSize(QSize(300, 100))
        self.btn_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/80x80/icons/80x80/ct-salida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salida.setIcon(icon6)
        self.btn_salida.setIconSize(QSize(80, 80))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.btn_salida)

        self.btn_interno = QPushButton(self.frame_7)
        self.btn_interno.setObjectName(u"btn_interno")
        self.btn_interno.setMinimumSize(QSize(300, 100))
        self.btn_interno.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/80x80/icons/80x80/ct-interno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_interno.setIcon(icon7)
        self.btn_interno.setIconSize(QSize(80, 80))

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.btn_interno)

        self.btn_devoluciones = QPushButton(self.frame_7)
        self.btn_devoluciones.setObjectName(u"btn_devoluciones")
        self.btn_devoluciones.setMinimumSize(QSize(300, 100))
        self.btn_devoluciones.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/80x80/icons/80x80/ct-devolucion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_devoluciones.setIcon(icon8)
        self.btn_devoluciones.setIconSize(QSize(80, 80))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.btn_devoluciones)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_4.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)


        self.verticalLayout_22.addLayout(self.formLayout_4)


        self.verticalLayout_20.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page_primera_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_back_1p = QPushButton(self.frame_8)
        self.btn_back_1p.setObjectName(u"btn_back_1p")
        self.btn_back_1p.setMinimumSize(QSize(200, 70))
        self.btn_back_1p.setMaximumSize(QSize(200, 70))
        self.btn_back_1p.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/80x80/icons/80x80/ct-regresar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_1p.setIcon(icon9)
        self.btn_back_1p.setIconSize(QSize(80, 70))

        self.horizontalLayout_13.addWidget(self.btn_back_1p)


        self.verticalLayout_24.addLayout(self.horizontalLayout_13)


        self.verticalLayout_20.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_primera_menu)
        self.page_menu_entrada = QWidget()
        self.page_menu_entrada.setObjectName(u"page_menu_entrada")
        self.verticalLayout_16 = QVBoxLayout(self.page_menu_entrada)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.page_menu_entrada)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_11)


        self.verticalLayout_23.addLayout(self.verticalLayout_29)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_menu_entrada)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(60)
        self.formLayout_3.setVerticalSpacing(60)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.btn_1a_compra = QPushButton(self.frame_10)
        self.btn_1a_compra.setObjectName(u"btn_1a_compra")
        self.btn_1a_compra.setMinimumSize(QSize(300, 100))
        self.btn_1a_compra.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_1a_compra.setIcon(icon5)
        self.btn_1a_compra.setIconSize(QSize(80, 80))

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.btn_1a_compra)

        self.btn_1a_traspaso = QPushButton(self.frame_10)
        self.btn_1a_traspaso.setObjectName(u"btn_1a_traspaso")
        self.btn_1a_traspaso.setMinimumSize(QSize(300, 100))
        self.btn_1a_traspaso.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/80x80/icons/80x80/ct-traspaso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_1a_traspaso.setIcon(icon10)
        self.btn_1a_traspaso.setIconSize(QSize(80, 80))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.btn_1a_traspaso)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_4)


        self.verticalLayout_26.addLayout(self.formLayout_3)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.page_menu_entrada)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 100))
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_11)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_back_1p_menu = QPushButton(self.frame_11)
        self.btn_back_1p_menu.setObjectName(u"btn_back_1p_menu")
        self.btn_back_1p_menu.setMinimumSize(QSize(200, 70))
        self.btn_back_1p_menu.setMaximumSize(QSize(200, 70))
        self.btn_back_1p_menu.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_1p_menu.setIcon(icon9)
        self.btn_back_1p_menu.setIconSize(QSize(80, 70))

        self.horizontalLayout_14.addWidget(self.btn_back_1p_menu)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_menu_entrada)
        self.page_menu_salida = QWidget()
        self.page_menu_salida.setObjectName(u"page_menu_salida")
        self.verticalLayout_146 = QVBoxLayout(self.page_menu_salida)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.frame_141 = QFrame(self.page_menu_salida)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMinimumSize(QSize(0, 70))
        self.frame_141.setMaximumSize(QSize(16777215, 70))
        self.frame_141.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_58 = QLabel(self.frame_141)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.label_58)


        self.horizontalLayout_155.addLayout(self.horizontalLayout_156)


        self.verticalLayout_146.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.page_menu_salida)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.formLayout_15.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_15.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_15.setHorizontalSpacing(60)
        self.formLayout_15.setVerticalSpacing(60)
        self.btn_menu_salida = QPushButton(self.frame_142)
        self.btn_menu_salida.setObjectName(u"btn_menu_salida")
        self.btn_menu_salida.setMinimumSize(QSize(300, 100))
        self.btn_menu_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_menu_salida.setIcon(icon6)
        self.btn_menu_salida.setIconSize(QSize(80, 80))

        self.formLayout_15.setWidget(1, QFormLayout.LabelRole, self.btn_menu_salida)

        self.btn_menu_salida_traspaso = QPushButton(self.frame_142)
        self.btn_menu_salida_traspaso.setObjectName(u"btn_menu_salida_traspaso")
        self.btn_menu_salida_traspaso.setMinimumSize(QSize(300, 100))
        self.btn_menu_salida_traspaso.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_menu_salida_traspaso.setIcon(icon10)
        self.btn_menu_salida_traspaso.setIconSize(QSize(80, 80))

        self.formLayout_15.setWidget(1, QFormLayout.FieldRole, self.btn_menu_salida_traspaso)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_15.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_29)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_15.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_30)


        self.horizontalLayout_159.addLayout(self.formLayout_15)


        self.verticalLayout_146.addWidget(self.frame_142)

        self.frame_143 = QFrame(self.page_menu_salida)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(0, 100))
        self.frame_143.setMaximumSize(QSize(16777215, 100))
        self.frame_143.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.btn_regresar_menu_salida = QPushButton(self.frame_143)
        self.btn_regresar_menu_salida.setObjectName(u"btn_regresar_menu_salida")
        self.btn_regresar_menu_salida.setMinimumSize(QSize(200, 70))
        self.btn_regresar_menu_salida.setMaximumSize(QSize(200, 70))
        self.btn_regresar_menu_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_regresar_menu_salida.setIcon(icon9)
        self.btn_regresar_menu_salida.setIconSize(QSize(80, 70))

        self.horizontalLayout_160.addWidget(self.btn_regresar_menu_salida)


        self.horizontalLayout_161.addLayout(self.horizontalLayout_160)


        self.verticalLayout_146.addWidget(self.frame_143)

        self.stackedWidget.addWidget(self.page_menu_salida)
        self.page_1a_compra_menu_Tracto = QWidget()
        self.page_1a_compra_menu_Tracto.setObjectName(u"page_1a_compra_menu_Tracto")
        self.verticalLayout_30 = QVBoxLayout(self.page_1a_compra_menu_Tracto)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_12 = QFrame(self.page_1a_compra_menu_Tracto)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 70))
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_12)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)


        self.verticalLayout_30.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_1a_compra_menu_Tracto)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_5.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_5.setHorizontalSpacing(60)
        self.formLayout_5.setVerticalSpacing(60)
        self.btnPrimeraPesadaCompraTorton = QPushButton(self.frame_13)
        self.btnPrimeraPesadaCompraTorton.setObjectName(u"btnPrimeraPesadaCompraTorton")
        self.btnPrimeraPesadaCompraTorton.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaCompraTorton.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaCompraTorton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/80x80/icons/80x80/ct-torton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrimeraPesadaCompraTorton.setIcon(icon11)
        self.btnPrimeraPesadaCompraTorton.setIconSize(QSize(80, 80))

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.btnPrimeraPesadaCompraTorton)

        self.btnPrimeraPesadaCompraTrailer = QPushButton(self.frame_13)
        self.btnPrimeraPesadaCompraTrailer.setObjectName(u"btnPrimeraPesadaCompraTrailer")
        self.btnPrimeraPesadaCompraTrailer.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaCompraTrailer.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaCompraTrailer.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/80x80/icons/80x80/ct-trailer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrimeraPesadaCompraTrailer.setIcon(icon12)
        self.btnPrimeraPesadaCompraTrailer.setIconSize(QSize(80, 80))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.btnPrimeraPesadaCompraTrailer)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_6)


        self.horizontalLayout_15.addLayout(self.formLayout_5)


        self.verticalLayout_30.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.page_1a_compra_menu_Tracto)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setMaximumSize(QSize(16777215, 100))
        self.frame_14.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_14)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_back_1p_menu_entrada = QPushButton(self.frame_14)
        self.btn_back_1p_menu_entrada.setObjectName(u"btn_back_1p_menu_entrada")
        self.btn_back_1p_menu_entrada.setMinimumSize(QSize(200, 70))
        self.btn_back_1p_menu_entrada.setMaximumSize(QSize(200, 70))
        self.btn_back_1p_menu_entrada.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_1p_menu_entrada.setIcon(icon9)
        self.btn_back_1p_menu_entrada.setIconSize(QSize(80, 70))

        self.horizontalLayout_16.addWidget(self.btn_back_1p_menu_entrada)


        self.verticalLayout_34.addLayout(self.horizontalLayout_16)


        self.verticalLayout_30.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_1a_compra_menu_Tracto)
        self.page_1a_traspaso_menu_tracto = QWidget()
        self.page_1a_traspaso_menu_tracto.setObjectName(u"page_1a_traspaso_menu_tracto")
        self.verticalLayout_37 = QVBoxLayout(self.page_1a_traspaso_menu_tracto)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_15 = QFrame(self.page_1a_traspaso_menu_tracto)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 70))
        self.frame_15.setMaximumSize(QSize(16777215, 70))
        self.frame_15.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_14)


        self.verticalLayout_38.addLayout(self.verticalLayout_39)


        self.verticalLayout_37.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_1a_traspaso_menu_tracto)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_7.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_7.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_7.setHorizontalSpacing(60)
        self.formLayout_7.setVerticalSpacing(60)
        self.btnPrimeraPesadaTraspasoTorton = QPushButton(self.frame_16)
        self.btnPrimeraPesadaTraspasoTorton.setObjectName(u"btnPrimeraPesadaTraspasoTorton")
        self.btnPrimeraPesadaTraspasoTorton.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTorton.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTorton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaTraspasoTorton.setIcon(icon11)
        self.btnPrimeraPesadaTraspasoTorton.setIconSize(QSize(80, 80))

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.btnPrimeraPesadaTraspasoTorton)

        self.btnPrimeraPesadaTraspasoTrailer = QPushButton(self.frame_16)
        self.btnPrimeraPesadaTraspasoTrailer.setObjectName(u"btnPrimeraPesadaTraspasoTrailer")
        self.btnPrimeraPesadaTraspasoTrailer.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTrailer.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTrailer.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaTraspasoTrailer.setIcon(icon12)
        self.btnPrimeraPesadaTraspasoTrailer.setIconSize(QSize(80, 80))

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.btnPrimeraPesadaTraspasoTrailer)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_7.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_11)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_7.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_12)


        self.horizontalLayout_19.addLayout(self.formLayout_7)


        self.verticalLayout_37.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.page_1a_traspaso_menu_tracto)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 100))
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.btn_back_1p_menu_entrada_3 = QPushButton(self.frame_17)
        self.btn_back_1p_menu_entrada_3.setObjectName(u"btn_back_1p_menu_entrada_3")
        self.btn_back_1p_menu_entrada_3.setMinimumSize(QSize(200, 70))
        self.btn_back_1p_menu_entrada_3.setMaximumSize(QSize(200, 70))
        self.btn_back_1p_menu_entrada_3.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_1p_menu_entrada_3.setIcon(icon9)
        self.btn_back_1p_menu_entrada_3.setIconSize(QSize(80, 70))

        self.horizontalLayout_20.addWidget(self.btn_back_1p_menu_entrada_3)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)


        self.verticalLayout_37.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.page_1a_traspaso_menu_tracto)
        self.page_1a_traspaso_menu_tracto_salida = QWidget()
        self.page_1a_traspaso_menu_tracto_salida.setObjectName(u"page_1a_traspaso_menu_tracto_salida")
        self.verticalLayout_159 = QVBoxLayout(self.page_1a_traspaso_menu_tracto_salida)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.frame_144 = QFrame(self.page_1a_traspaso_menu_tracto_salida)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(0, 70))
        self.frame_144.setMaximumSize(QSize(16777215, 70))
        self.frame_144.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_144)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_160 = QVBoxLayout()
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.label_59 = QLabel(self.frame_144)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_160.addWidget(self.label_59)


        self.verticalLayout_161.addLayout(self.verticalLayout_160)


        self.verticalLayout_159.addWidget(self.frame_144)

        self.frame_145 = QFrame(self.page_1a_traspaso_menu_tracto_salida)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_145)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.formLayout_16.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_16.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_16.setHorizontalSpacing(60)
        self.formLayout_16.setVerticalSpacing(60)
        self.btnPrimeraPesadaTraspasoTorton_salida = QPushButton(self.frame_145)
        self.btnPrimeraPesadaTraspasoTorton_salida.setObjectName(u"btnPrimeraPesadaTraspasoTorton_salida")
        self.btnPrimeraPesadaTraspasoTorton_salida.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTorton_salida.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTorton_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaTraspasoTorton_salida.setIcon(icon11)
        self.btnPrimeraPesadaTraspasoTorton_salida.setIconSize(QSize(80, 80))

        self.formLayout_16.setWidget(1, QFormLayout.LabelRole, self.btnPrimeraPesadaTraspasoTorton_salida)

        self.btnPrimeraPesadaTraspasoTrailer_salida = QPushButton(self.frame_145)
        self.btnPrimeraPesadaTraspasoTrailer_salida.setObjectName(u"btnPrimeraPesadaTraspasoTrailer_salida")
        self.btnPrimeraPesadaTraspasoTrailer_salida.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTrailer_salida.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaTraspasoTrailer_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaTraspasoTrailer_salida.setIcon(icon12)
        self.btnPrimeraPesadaTraspasoTrailer_salida.setIconSize(QSize(80, 80))

        self.formLayout_16.setWidget(1, QFormLayout.FieldRole, self.btnPrimeraPesadaTraspasoTrailer_salida)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_16.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_31)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_16.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_32)


        self.horizontalLayout.addLayout(self.formLayout_16)


        self.verticalLayout_159.addWidget(self.frame_145)

        self.frame_146 = QFrame(self.page_1a_traspaso_menu_tracto_salida)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(0, 100))
        self.frame_146.setMaximumSize(QSize(16777215, 100))
        self.frame_146.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_146)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.btn_regresar_menu_traspaso_salida = QPushButton(self.frame_146)
        self.btn_regresar_menu_traspaso_salida.setObjectName(u"btn_regresar_menu_traspaso_salida")
        self.btn_regresar_menu_traspaso_salida.setMinimumSize(QSize(200, 70))
        self.btn_regresar_menu_traspaso_salida.setMaximumSize(QSize(200, 70))
        self.btn_regresar_menu_traspaso_salida.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_regresar_menu_traspaso_salida.setIcon(icon9)
        self.btn_regresar_menu_traspaso_salida.setIconSize(QSize(80, 70))

        self.horizontalLayout_158.addWidget(self.btn_regresar_menu_traspaso_salida)


        self.verticalLayout_164.addLayout(self.horizontalLayout_158)


        self.verticalLayout_159.addWidget(self.frame_146)

        self.stackedWidget.addWidget(self.page_1a_traspaso_menu_tracto_salida)
        self.page_salida_selecciona_tracto = QWidget()
        self.page_salida_selecciona_tracto.setObjectName(u"page_salida_selecciona_tracto")
        self.verticalLayout_27 = QVBoxLayout(self.page_salida_selecciona_tracto)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_18 = QFrame(self.page_salida_selecciona_tracto)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 70))
        self.frame_18.setMaximumSize(QSize(16777215, 70))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_18)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 70))
        self.label_13.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_13)


        self.verticalLayout_35.addLayout(self.verticalLayout_33)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.page_salida_selecciona_tracto)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_6.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_6.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_6.setHorizontalSpacing(60)
        self.formLayout_6.setVerticalSpacing(60)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_6.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_9)

        self.btnPrimeraPesadaSalidaTorton = QPushButton(self.frame_19)
        self.btnPrimeraPesadaSalidaTorton.setObjectName(u"btnPrimeraPesadaSalidaTorton")
        self.btnPrimeraPesadaSalidaTorton.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaSalidaTorton.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaSalidaTorton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaSalidaTorton.setIcon(icon11)
        self.btnPrimeraPesadaSalidaTorton.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.btnPrimeraPesadaSalidaTorton)

        self.btnPrimeraPesadaSalidaTrailer = QPushButton(self.frame_19)
        self.btnPrimeraPesadaSalidaTrailer.setObjectName(u"btnPrimeraPesadaSalidaTrailer")
        self.btnPrimeraPesadaSalidaTrailer.setMinimumSize(QSize(300, 100))
        self.btnPrimeraPesadaSalidaTrailer.setMaximumSize(QSize(300, 100))
        self.btnPrimeraPesadaSalidaTrailer.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnPrimeraPesadaSalidaTrailer.setIcon(icon12)
        self.btnPrimeraPesadaSalidaTrailer.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.btnPrimeraPesadaSalidaTrailer)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_6.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_10)


        self.horizontalLayout_17.addLayout(self.formLayout_6)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)


        self.verticalLayout_27.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.page_salida_selecciona_tracto)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 100))
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.frame_20.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_back_1p_menu_salida_tracto = QPushButton(self.frame_20)
        self.btn_back_1p_menu_salida_tracto.setObjectName(u"btn_back_1p_menu_salida_tracto")
        self.btn_back_1p_menu_salida_tracto.setMinimumSize(QSize(200, 70))
        self.btn_back_1p_menu_salida_tracto.setMaximumSize(QSize(200, 70))
        self.btn_back_1p_menu_salida_tracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_1p_menu_salida_tracto.setIcon(icon9)
        self.btn_back_1p_menu_salida_tracto.setIconSize(QSize(80, 70))

        self.horizontalLayout_22.addWidget(self.btn_back_1p_menu_salida_tracto)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)


        self.verticalLayout_27.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_salida_selecciona_tracto)
        self.page_impresion = QWidget()
        self.page_impresion.setObjectName(u"page_impresion")
        self.verticalLayout_6 = QVBoxLayout(self.page_impresion)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_impresion)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 70))
        self.label_8.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_impresion)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_reimpresion = QPushButton(self.frame_2)
        self.btn_reimpresion.setObjectName(u"btn_reimpresion")
        self.btn_reimpresion.setMinimumSize(QSize(300, 100))
        self.btn_reimpresion.setMaximumSize(QSize(300, 100))
        self.btn_reimpresion.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/80x80/icons/80x80/ct-producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reimpresion.setIcon(icon13)
        self.btn_reimpresion.setIconSize(QSize(80, 80))

        self.gridLayout_4.addWidget(self.btn_reimpresion, 3, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_15, 4, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.ticket_reimpresion = QLineEdit(self.frame_2)
        self.ticket_reimpresion.setObjectName(u"ticket_reimpresion")
        self.ticket_reimpresion.setMinimumSize(QSize(300, 50))
        self.ticket_reimpresion.setMaximumSize(QSize(300, 50))
        self.ticket_reimpresion.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.ticket_reimpresion.setAlignment(Qt.AlignCenter)
        self.ticket_reimpresion.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.ticket_reimpresion, 2, 1, 1, 1)

        self.label_51 = QLabel(self.frame_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_51, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_19, 2, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_20, 2, 2, 1, 1)


        self.horizontalLayout_146.addLayout(self.gridLayout_4)


        self.horizontalLayout_147.addLayout(self.horizontalLayout_146)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_impresion)
        self.page_reportes = QWidget()
        self.page_reportes.setObjectName(u"page_reportes")
        self.verticalLayout_11 = QVBoxLayout(self.page_reportes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_3 = QFrame(self.page_reportes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 70))
        self.label_9.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)


        self.verticalLayout_15.addLayout(self.verticalLayout_13)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_27 = QFrame(self.page_reportes)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setVerticalSpacing(10)
        self.pushButton_4 = QPushButton(self.frame_27)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_27)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_5.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_27)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_27)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_5.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.btn_ToExcel = QPushButton(self.frame_27)
        self.btn_ToExcel.setObjectName(u"btn_ToExcel")
        self.btn_ToExcel.setMinimumSize(QSize(240, 100))
        self.btn_ToExcel.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/16x16/icons/16x16/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ToExcel.setIcon(icon14)
        self.btn_ToExcel.setIconSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.btn_ToExcel, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_27)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_5.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_27)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_5.addWidget(self.pushButton_6, 1, 2, 1, 1)


        self.horizontalLayout_148.addLayout(self.gridLayout_5)


        self.horizontalLayout_149.addLayout(self.horizontalLayout_148)


        self.verticalLayout_11.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.page_reportes)
        self.page_2a_pesada = QWidget()
        self.page_2a_pesada.setObjectName(u"page_2a_pesada")
        self.verticalLayout_12 = QVBoxLayout(self.page_2a_pesada)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_21 = QFrame(self.page_2a_pesada)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 70))
        self.frame_21.setMaximumSize(QSize(16777215, 70))
        self.frame_21.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_21)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_2 = QLabel(self.frame_21)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_2)


        self.verticalLayout_40.addLayout(self.verticalLayout_36)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_130 = QFrame(self.page_2a_pesada)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(0, 100))
        self.frame_130.setMaximumSize(QSize(16777215, 100))
        self.frame_130.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_130)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.btn_analisisSegundaPesada = QPushButton(self.frame_130)
        self.btn_analisisSegundaPesada.setObjectName(u"btn_analisisSegundaPesada")
        self.btn_analisisSegundaPesada.setMinimumSize(QSize(200, 70))
        self.btn_analisisSegundaPesada.setMaximumSize(QSize(200, 70))
        self.btn_analisisSegundaPesada.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/48x48/icons/48x48/ct-romana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analisisSegundaPesada.setIcon(icon15)
        self.btn_analisisSegundaPesada.setIconSize(QSize(80, 80))

        self.horizontalLayout_138.addWidget(self.btn_analisisSegundaPesada)

        self.btn_ActualizaTablaSegunda = QPushButton(self.frame_130)
        self.btn_ActualizaTablaSegunda.setObjectName(u"btn_ActualizaTablaSegunda")
        self.btn_ActualizaTablaSegunda.setMinimumSize(QSize(200, 70))
        self.btn_ActualizaTablaSegunda.setMaximumSize(QSize(200, 70))
        self.btn_ActualizaTablaSegunda.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/24x24/icons/24x24/ct-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ActualizaTablaSegunda.setIcon(icon16)
        self.btn_ActualizaTablaSegunda.setIconSize(QSize(80, 80))

        self.horizontalLayout_138.addWidget(self.btn_ActualizaTablaSegunda)


        self.verticalLayout_139.addLayout(self.horizontalLayout_138)


        self.verticalLayout_12.addWidget(self.frame_130)

        self.frame_22 = QFrame(self.page_2a_pesada)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_137 = QVBoxLayout()
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.table_2a = QTableWidget(self.frame_22)
        if (self.table_2a.columnCount() < 9):
            self.table_2a.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_2a.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_2a.setObjectName(u"table_2a")
        self.table_2a.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_137.addWidget(self.table_2a)


        self.horizontalLayout_24.addLayout(self.verticalLayout_137)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_2a_pesada)
        self.page_destare = QWidget()
        self.page_destare.setObjectName(u"page_destare")
        self.verticalLayout_14 = QVBoxLayout(self.page_destare)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_23 = QFrame(self.page_destare)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 70))
        self.frame_23.setMaximumSize(QSize(16777215, 70))
        self.frame_23.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_23)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_3)


        self.verticalLayout_42.addLayout(self.verticalLayout_41)


        self.verticalLayout_14.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.page_destare)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 100))
        self.frame_24.setMaximumSize(QSize(16777215, 100))
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_24)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.btn_destarar = QPushButton(self.frame_24)
        self.btn_destarar.setObjectName(u"btn_destarar")
        self.btn_destarar.setMinimumSize(QSize(200, 70))
        self.btn_destarar.setMaximumSize(QSize(200, 70))
        self.btn_destarar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/24x24/icons/24x24/ct-destare5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_destarar.setIcon(icon17)
        self.btn_destarar.setIconSize(QSize(80, 80))

        self.horizontalLayout_26.addWidget(self.btn_destarar)

        self.btn_actualizarDestare = QPushButton(self.frame_24)
        self.btn_actualizarDestare.setObjectName(u"btn_actualizarDestare")
        self.btn_actualizarDestare.setMinimumSize(QSize(200, 70))
        self.btn_actualizarDestare.setMaximumSize(QSize(200, 70))
        self.btn_actualizarDestare.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_actualizarDestare.setIcon(icon16)
        self.btn_actualizarDestare.setIconSize(QSize(80, 80))

        self.horizontalLayout_26.addWidget(self.btn_actualizarDestare)


        self.verticalLayout_141.addLayout(self.horizontalLayout_26)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.frame_131 = QFrame(self.page_destare)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_131)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_138 = QVBoxLayout()
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.tabla_destare = QTableWidget(self.frame_131)
        if (self.tabla_destare.columnCount() < 11):
            self.tabla_destare.setColumnCount(11)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_destare.setHorizontalHeaderItem(10, __qtablewidgetitem19)
        self.tabla_destare.setObjectName(u"tabla_destare")
        self.tabla_destare.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_138.addWidget(self.tabla_destare)


        self.verticalLayout_140.addLayout(self.verticalLayout_138)


        self.verticalLayout_14.addWidget(self.frame_131)

        self.stackedWidget.addWidget(self.page_destare)
        self.page_calcular_destare = QWidget()
        self.page_calcular_destare.setObjectName(u"page_calcular_destare")
        self.verticalLayout_143 = QVBoxLayout(self.page_calcular_destare)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.frame_132 = QFrame(self.page_calcular_destare)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 50))
        self.frame_132.setMaximumSize(QSize(16777215, 70))
        self.frame_132.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_132)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_142 = QVBoxLayout()
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.label_4 = QLabel(self.frame_132)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_142.addWidget(self.label_4)


        self.verticalLayout_144.addLayout(self.verticalLayout_142)


        self.verticalLayout_143.addWidget(self.frame_132)

        self.frame_133 = QFrame(self.page_calcular_destare)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 40))
        self.frame_133.setMaximumSize(QSize(16777215, 70))
        self.frame_133.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_5 = QLabel(self.frame_133)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_139.addWidget(self.label_5)

        self.lcdNumber_ticket = QLCDNumber(self.frame_133)
        self.lcdNumber_ticket.setObjectName(u"lcdNumber_ticket")
        self.lcdNumber_ticket.setMinimumSize(QSize(500, 20))
        self.lcdNumber_ticket.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_139.addWidget(self.lcdNumber_ticket)


        self.horizontalLayout_140.addLayout(self.horizontalLayout_139)


        self.verticalLayout_143.addWidget(self.frame_133)

        self.frame_134 = QFrame(self.page_calcular_destare)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMinimumSize(QSize(0, 100))
        self.frame_134.setMaximumSize(QSize(16777215, 180))
        self.frame_134.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.frame_134)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.lcdNumber_1p = QLCDNumber(self.frame_134)
        self.lcdNumber_1p.setObjectName(u"lcdNumber_1p")
        self.lcdNumber_1p.setMinimumSize(QSize(500, 30))
        self.lcdNumber_1p.setMaximumSize(QSize(16777215, 50))
        self.lcdNumber_1p.setStyleSheet(u"color: rgb(0, 255, 0)")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lcdNumber_1p)

        self.label_16 = QLabel(self.frame_134)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.lcdNumber_2p = QLCDNumber(self.frame_134)
        self.lcdNumber_2p.setObjectName(u"lcdNumber_2p")
        self.lcdNumber_2p.setMinimumSize(QSize(500, 30))
        self.lcdNumber_2p.setMaximumSize(QSize(16777215, 50))
        self.lcdNumber_2p.setStyleSheet(u"color: rgb(0, 0, 255)")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lcdNumber_2p)

        self.label_17 = QLabel(self.frame_134)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.lcdNumber_pn = QLCDNumber(self.frame_134)
        self.lcdNumber_pn.setObjectName(u"lcdNumber_pn")
        self.lcdNumber_pn.setMinimumSize(QSize(500, 30))
        self.lcdNumber_pn.setMaximumSize(QSize(16777215, 50))
        self.lcdNumber_pn.setStyleSheet(u"color: rgb(255, 255, 0)")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lcdNumber_pn)


        self.horizontalLayout_141.addLayout(self.formLayout)


        self.verticalLayout_143.addWidget(self.frame_134)

        self.frame_135 = QFrame(self.page_calcular_destare)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_18 = QLabel(self.frame_135)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.yute = QLineEdit(self.frame_135)
        self.yute.setObjectName(u"yute")
        self.yute.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.yute)

        self.label_19 = QLabel(self.frame_135)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.propileno = QLineEdit(self.frame_135)
        self.propileno.setObjectName(u"propileno")
        self.propileno.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.propileno)

        self.label_54 = QLabel(self.frame_135)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_54)

        self.raspa = QLineEdit(self.frame_135)
        self.raspa.setObjectName(u"raspa")
        self.raspa.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.raspa)

        self.label_20 = QLabel(self.frame_135)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.label_20)

        self.saco = QLineEdit(self.frame_135)
        self.saco.setObjectName(u"saco")
        self.saco.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.saco)

        self.label_55 = QLabel(self.frame_135)
        self.label_55.setObjectName(u"label_55")

        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.label_55)

        self.saco10 = QLineEdit(self.frame_135)
        self.saco10.setObjectName(u"saco10")
        self.saco10.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.saco10)

        self.label_48 = QLabel(self.frame_135)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_9.setWidget(5, QFormLayout.LabelRole, self.label_48)

        self.tarima = QLineEdit(self.frame_135)
        self.tarima.setObjectName(u"tarima")
        self.tarima.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(5, QFormLayout.FieldRole, self.tarima)

        self.label_49 = QLabel(self.frame_135)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_9.setWidget(6, QFormLayout.LabelRole, self.label_49)

        self.chep = QLineEdit(self.frame_135)
        self.chep.setObjectName(u"chep")
        self.chep.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(6, QFormLayout.FieldRole, self.chep)

        self.label_52 = QLabel(self.frame_135)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_9.setWidget(7, QFormLayout.LabelRole, self.label_52)

        self.treforzada = QLineEdit(self.frame_135)
        self.treforzada.setObjectName(u"treforzada")
        self.treforzada.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(7, QFormLayout.FieldRole, self.treforzada)

        self.label_53 = QLabel(self.frame_135)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_9.setWidget(8, QFormLayout.LabelRole, self.label_53)

        self.sacoesp = QLineEdit(self.frame_135)
        self.sacoesp.setObjectName(u"sacoesp")
        self.sacoesp.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(8, QFormLayout.FieldRole, self.sacoesp)

        self.label_56 = QLabel(self.frame_135)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_9.setWidget(9, QFormLayout.LabelRole, self.label_56)

        self.tarimaesp = QLineEdit(self.frame_135)
        self.tarimaesp.setObjectName(u"tarimaesp")
        self.tarimaesp.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.formLayout_9.setWidget(9, QFormLayout.FieldRole, self.tarimaesp)


        self.horizontalLayout_143.addLayout(self.formLayout_9)


        self.verticalLayout_143.addWidget(self.frame_135)

        self.frame_136 = QFrame(self.page_calcular_destare)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_136)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.btn_calcular = QPushButton(self.frame_136)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setMinimumSize(QSize(200, 50))
        self.btn_calcular.setMaximumSize(QSize(200, 70))
        self.btn_calcular.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_calcular.setIcon(icon13)
        self.btn_calcular.setIconSize(QSize(40, 40))

        self.horizontalLayout_142.addWidget(self.btn_calcular)

        self.btn_regresarTablaDestare = QPushButton(self.frame_136)
        self.btn_regresarTablaDestare.setObjectName(u"btn_regresarTablaDestare")
        self.btn_regresarTablaDestare.setMinimumSize(QSize(200, 50))
        self.btn_regresarTablaDestare.setMaximumSize(QSize(200, 70))
        self.btn_regresarTablaDestare.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_regresarTablaDestare.setIcon(icon9)
        self.btn_regresarTablaDestare.setIconSize(QSize(40, 40))

        self.horizontalLayout_142.addWidget(self.btn_regresarTablaDestare)


        self.verticalLayout_145.addLayout(self.horizontalLayout_142)


        self.verticalLayout_143.addWidget(self.frame_136)

        self.stackedWidget.addWidget(self.page_calcular_destare)
        self.page_datos = QWidget()
        self.page_datos.setObjectName(u"page_datos")
        self.verticalLayout_43 = QVBoxLayout(self.page_datos)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_25 = QFrame(self.page_datos)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 70))
        self.frame_25.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_25)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 70))
        self.label_21.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_21)


        self.verticalLayout_45.addLayout(self.verticalLayout_44)


        self.verticalLayout_43.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.page_datos)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setVerticalSpacing(10)
        self.btn_tracto = QPushButton(self.frame_26)
        self.btn_tracto.setObjectName(u"btn_tracto")
        self.btn_tracto.setMinimumSize(QSize(240, 100))
        self.btn_tracto.setMaximumSize(QSize(240, 100))
        self.btn_tracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_tracto.setIcon(icon12)
        self.btn_tracto.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_tracto, 2, 1, 1, 1)

        self.btn_cliente = QPushButton(self.frame_26)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setMinimumSize(QSize(240, 100))
        self.btn_cliente.setMaximumSize(QSize(240, 100))
        self.btn_cliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/80x80/icons/80x80/ct-cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cliente.setIcon(icon18)
        self.btn_cliente.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_cliente, 0, 1, 1, 1)

        self.btn_proveedor = QPushButton(self.frame_26)
        self.btn_proveedor.setObjectName(u"btn_proveedor")
        self.btn_proveedor.setMinimumSize(QSize(240, 100))
        self.btn_proveedor.setMaximumSize(QSize(240, 100))
        self.btn_proveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/80x80/icons/80x80/ct-proveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_proveedor.setIcon(icon19)
        self.btn_proveedor.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_proveedor, 2, 0, 1, 1)

        self.btn_contenedor = QPushButton(self.frame_26)
        self.btn_contenedor.setObjectName(u"btn_contenedor")
        self.btn_contenedor.setMinimumSize(QSize(240, 100))
        self.btn_contenedor.setMaximumSize(QSize(240, 100))
        self.btn_contenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/80x80/icons/80x80/ct-contenedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_contenedor.setIcon(icon20)
        self.btn_contenedor.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_contenedor, 0, 2, 1, 1)

        self.btn_producto = QPushButton(self.frame_26)
        self.btn_producto.setObjectName(u"btn_producto")
        self.btn_producto.setMinimumSize(QSize(240, 100))
        self.btn_producto.setMaximumSize(QSize(240, 100))
        self.btn_producto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_producto.setIcon(icon13)
        self.btn_producto.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_producto, 1, 2, 1, 1)

        self.btn_aduana = QPushButton(self.frame_26)
        self.btn_aduana.setObjectName(u"btn_aduana")
        self.btn_aduana.setMinimumSize(QSize(240, 100))
        self.btn_aduana.setMaximumSize(QSize(240, 100))
        self.btn_aduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/80x80/icons/80x80/ct-aduana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_aduana.setIcon(icon21)
        self.btn_aduana.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_aduana, 0, 0, 1, 1)

        self.btn_operador = QPushButton(self.frame_26)
        self.btn_operador.setObjectName(u"btn_operador")
        self.btn_operador.setMinimumSize(QSize(240, 100))
        self.btn_operador.setMaximumSize(QSize(240, 100))
        self.btn_operador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/80x80/icons/80x80/ct-operador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_operador.setIcon(icon22)
        self.btn_operador.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_operador, 1, 1, 1, 1)

        self.btn_transportista = QPushButton(self.frame_26)
        self.btn_transportista.setObjectName(u"btn_transportista")
        self.btn_transportista.setMinimumSize(QSize(240, 100))
        self.btn_transportista.setMaximumSize(QSize(240, 100))
        self.btn_transportista.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/80x80/icons/80x80/ct-transportista.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_transportista.setIcon(icon23)
        self.btn_transportista.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_transportista, 1, 0, 1, 1)

        self.btn_destinos = QPushButton(self.frame_26)
        self.btn_destinos.setObjectName(u"btn_destinos")
        self.btn_destinos.setMinimumSize(QSize(240, 100))
        self.btn_destinos.setMaximumSize(QSize(240, 100))
        self.btn_destinos.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/80x80/icons/80x80/ct-destino.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_destinos.setIcon(icon24)
        self.btn_destinos.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_destinos, 3, 0, 1, 1)

        self.btn_sucursal = QPushButton(self.frame_26)
        self.btn_sucursal.setObjectName(u"btn_sucursal")
        self.btn_sucursal.setMinimumSize(QSize(240, 100))
        self.btn_sucursal.setMaximumSize(QSize(240, 100))
        self.btn_sucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_sucursal.setIcon(icon21)
        self.btn_sucursal.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.btn_sucursal, 2, 2, 1, 1)

        self.btn_tarimas = QPushButton(self.frame_26)
        self.btn_tarimas.setObjectName(u"btn_tarimas")
        self.btn_tarimas.setMinimumSize(QSize(240, 100))
        self.btn_tarimas.setMaximumSize(QSize(240, 100))
        self.btn_tarimas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_tarimas.setIcon(icon13)
        self.btn_tarimas.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.btn_tarimas, 3, 1, 1, 1)


        self.horizontalLayout_25.addLayout(self.gridLayout_3)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_25)


        self.verticalLayout_43.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.page_datos)
        self.page_sacotarima = QWidget()
        self.page_sacotarima.setObjectName(u"page_sacotarima")
        self.verticalLayout_147 = QVBoxLayout(self.page_sacotarima)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.frame_137 = QFrame(self.page_sacotarima)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(0, 70))
        self.frame_137.setMaximumSize(QSize(16777215, 70))
        self.frame_137.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_137)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_148 = QVBoxLayout()
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.label_57 = QLabel(self.frame_137)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_148.addWidget(self.label_57)


        self.verticalLayout_149.addLayout(self.verticalLayout_148)


        self.verticalLayout_147.addWidget(self.frame_137)

        self.frame_138 = QFrame(self.page_sacotarima)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 130))
        self.frame_138.setMaximumSize(QSize(16777215, 130))
        self.frame_138.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.btnActualizaSacoTarima = QPushButton(self.frame_138)
        self.btnActualizaSacoTarima.setObjectName(u"btnActualizaSacoTarima")
        self.btnActualizaSacoTarima.setMinimumSize(QSize(300, 0))
        self.btnActualizaSacoTarima.setMaximumSize(QSize(300, 100))
        self.btnActualizaSacoTarima.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/80x80/icons/80x80/ct-producto-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizaSacoTarima.setIcon(icon25)
        self.btnActualizaSacoTarima.setIconSize(QSize(80, 80))

        self.horizontalLayout_150.addWidget(self.btnActualizaSacoTarima)


        self.horizontalLayout_151.addLayout(self.horizontalLayout_150)


        self.verticalLayout_147.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.page_sacotarima)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setLayoutDirection(Qt.LeftToRight)
        self.frame_139.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.tabla_sacotarima = QTableWidget(self.frame_139)
        if (self.tabla_sacotarima.columnCount() < 3):
            self.tabla_sacotarima.setColumnCount(3)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_sacotarima.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_sacotarima.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_sacotarima.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        self.tabla_sacotarima.setObjectName(u"tabla_sacotarima")
        self.tabla_sacotarima.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_154.addWidget(self.tabla_sacotarima)


        self.verticalLayout_147.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.page_sacotarima)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(0, 60))
        self.frame_140.setMaximumSize(QSize(16777215, 60))
        self.frame_140.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_21)

        self.btn_refrescarSacoTarima = QPushButton(self.frame_140)
        self.btn_refrescarSacoTarima.setObjectName(u"btn_refrescarSacoTarima")
        self.btn_refrescarSacoTarima.setMinimumSize(QSize(80, 30))
        self.btn_refrescarSacoTarima.setMaximumSize(QSize(80, 30))
        self.btn_refrescarSacoTarima.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarSacoTarima.setIcon(icon16)

        self.horizontalLayout_152.addWidget(self.btn_refrescarSacoTarima)


        self.horizontalLayout_153.addLayout(self.horizontalLayout_152)


        self.verticalLayout_147.addWidget(self.frame_140)

        self.stackedWidget.addWidget(self.page_sacotarima)
        self.page_menudestinos = QWidget()
        self.page_menudestinos.setObjectName(u"page_menudestinos")
        self.verticalLayout_46 = QVBoxLayout(self.page_menudestinos)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_28 = QFrame(self.page_menudestinos)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 70))
        self.frame_28.setMaximumSize(QSize(16777215, 70))
        self.frame_28.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_28)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_22 = QLabel(self.frame_28)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_22)


        self.verticalLayout_48.addLayout(self.verticalLayout_47)


        self.verticalLayout_46.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.page_menudestinos)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_29)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_8.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_8.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_8.setHorizontalSpacing(60)
        self.formLayout_8.setVerticalSpacing(60)
        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_8.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_18)

        self.btnDestinoventas = QPushButton(self.frame_29)
        self.btnDestinoventas.setObjectName(u"btnDestinoventas")
        self.btnDestinoventas.setMinimumSize(QSize(300, 100))
        self.btnDestinoventas.setMaximumSize(QSize(300, 100))
        self.btnDestinoventas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/80x80/icons/80x80/ct-destinos-ventas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDestinoventas.setIcon(icon26)
        self.btnDestinoventas.setIconSize(QSize(80, 80))

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.btnDestinoventas)

        self.btnSolas = QPushButton(self.frame_29)
        self.btnSolas.setObjectName(u"btnSolas")
        self.btnSolas.setMinimumSize(QSize(300, 100))
        self.btnSolas.setMaximumSize(QSize(300, 100))
        self.btnSolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/80x80/icons/80x80/ct-destino-solas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSolas.setIcon(icon27)
        self.btnSolas.setIconSize(QSize(80, 80))

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.btnSolas)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_8.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_17)

        self.btnSifon = QPushButton(self.frame_29)
        self.btnSifon.setObjectName(u"btnSifon")
        self.btnSifon.setMinimumSize(QSize(300, 100))
        self.btnSifon.setMaximumSize(QSize(300, 100))
        self.btnSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/80x80/icons/80x80/ct-destino-sifon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSifon.setIcon(icon28)
        self.btnSifon.setIconSize(QSize(80, 80))

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.btnSifon)

        self.btnSucursal = QPushButton(self.frame_29)
        self.btnSucursal.setObjectName(u"btnSucursal")
        self.btnSucursal.setMinimumSize(QSize(300, 100))
        self.btnSucursal.setMaximumSize(QSize(300, 100))
        self.btnSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/80x80/icons/80x80/ct-destino-sucursal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSucursal.setIcon(icon29)
        self.btnSucursal.setIconSize(QSize(80, 80))

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.btnSucursal)


        self.verticalLayout_51.addLayout(self.formLayout_8)


        self.verticalLayout_46.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.page_menudestinos)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 100))
        self.frame_30.setMaximumSize(QSize(16777215, 100))
        self.frame_30.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_30)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_back_menudatos = QPushButton(self.frame_30)
        self.btn_back_menudatos.setObjectName(u"btn_back_menudatos")
        self.btn_back_menudatos.setMinimumSize(QSize(200, 70))
        self.btn_back_menudatos.setMaximumSize(QSize(200, 70))
        self.btn_back_menudatos.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_menudatos.setIcon(icon9)
        self.btn_back_menudatos.setIconSize(QSize(80, 70))

        self.horizontalLayout_9.addWidget(self.btn_back_menudatos)


        self.verticalLayout_50.addLayout(self.horizontalLayout_9)


        self.verticalLayout_46.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.page_menudestinos)
        self.page_menutractos = QWidget()
        self.page_menutractos.setObjectName(u"page_menutractos")
        self.verticalLayout_49 = QVBoxLayout(self.page_menutractos)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_31 = QFrame(self.page_menutractos)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 70))
        self.frame_31.setMaximumSize(QSize(16777215, 70))
        self.frame_31.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_31)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_23 = QLabel(self.frame_31)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_23)


        self.verticalLayout_53.addLayout(self.verticalLayout_52)


        self.verticalLayout_49.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.page_menutractos)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.btn_CajaPorta = QPushButton(self.frame_32)
        self.btn_CajaPorta.setObjectName(u"btn_CajaPorta")
        self.btn_CajaPorta.setMinimumSize(QSize(240, 100))
        self.btn_CajaPorta.setMaximumSize(QSize(240, 100))
        self.btn_CajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/80x80/icons/80x80/ct-portacontenedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CajaPorta.setIcon(icon30)
        self.btn_CajaPorta.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.btn_CajaPorta, 0, 1, 1, 1)

        self.btn_Tractos = QPushButton(self.frame_32)
        self.btn_Tractos.setObjectName(u"btn_Tractos")
        self.btn_Tractos.setMinimumSize(QSize(240, 100))
        self.btn_Tractos.setMaximumSize(QSize(240, 100))
        self.btn_Tractos.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_Tractos.setIcon(icon12)
        self.btn_Tractos.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.btn_Tractos, 0, 0, 1, 1)

        self.btn_TipoTracto = QPushButton(self.frame_32)
        self.btn_TipoTracto.setObjectName(u"btn_TipoTracto")
        self.btn_TipoTracto.setMinimumSize(QSize(240, 100))
        self.btn_TipoTracto.setMaximumSize(QSize(240, 100))
        self.btn_TipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_TipoTracto.setIcon(icon12)
        self.btn_TipoTracto.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.btn_TipoTracto, 0, 2, 1, 1)


        self.horizontalLayout_29.addLayout(self.gridLayout)


        self.verticalLayout_49.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.page_menutractos)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 100))
        self.frame_33.setMaximumSize(QSize(16777215, 100))
        self.frame_33.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_back_menutracto = QPushButton(self.frame_33)
        self.btn_back_menutracto.setObjectName(u"btn_back_menutracto")
        self.btn_back_menutracto.setMinimumSize(QSize(200, 70))
        self.btn_back_menutracto.setMaximumSize(QSize(200, 70))
        self.btn_back_menutracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_menutracto.setIcon(icon9)
        self.btn_back_menutracto.setIconSize(QSize(80, 70))

        self.horizontalLayout_12.addWidget(self.btn_back_menutracto)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_12)


        self.verticalLayout_49.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.page_menutractos)
        self.page_aduana = QWidget()
        self.page_aduana.setObjectName(u"page_aduana")
        self.verticalLayout_54 = QVBoxLayout(self.page_aduana)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_34 = QFrame(self.page_aduana)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 70))
        self.frame_34.setMaximumSize(QSize(16777215, 70))
        self.frame_34.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_34)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_24 = QLabel(self.frame_34)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_24)


        self.verticalLayout_55.addLayout(self.verticalLayout_56)


        self.verticalLayout_54.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.page_aduana)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 70))
        self.frame_35.setMaximumSize(QSize(16777215, 70))
        self.frame_35.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.BuscarlineEditAduana = QLineEdit(self.frame_35)
        self.BuscarlineEditAduana.setObjectName(u"BuscarlineEditAduana")
        self.BuscarlineEditAduana.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditAduana.setMaximumSize(QSize(16777215, 30))
        self.BuscarlineEditAduana.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditAduana.setClearButtonEnabled(True)

        self.horizontalLayout_31.addWidget(self.BuscarlineEditAduana)

        self.btnBuscarAduana = QPushButton(self.frame_35)
        self.btnBuscarAduana.setObjectName(u"btnBuscarAduana")
        self.btnBuscarAduana.setMinimumSize(QSize(100, 40))
        self.btnBuscarAduana.setMaximumSize(QSize(100, 40))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.btnBuscarAduana.setFont(font5)
        self.btnBuscarAduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon31 = QIcon()
        icon31.addFile(u":/16x16/icons/16x16/ct-buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBuscarAduana.setIcon(icon31)

        self.horizontalLayout_31.addWidget(self.btnBuscarAduana)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)


        self.verticalLayout_54.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.page_aduana)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 120))
        self.frame_36.setMaximumSize(QSize(16777215, 120))
        self.frame_36.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btnNuevaAduana = QPushButton(self.frame_36)
        self.btnNuevaAduana.setObjectName(u"btnNuevaAduana")
        self.btnNuevaAduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon32 = QIcon()
        icon32.addFile(u":/80x80/icons/80x80/ct-aduana-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevaAduana.setIcon(icon32)
        self.btnNuevaAduana.setIconSize(QSize(80, 80))

        self.horizontalLayout_33.addWidget(self.btnNuevaAduana)

        self.btnActualizaAduana = QPushButton(self.frame_36)
        self.btnActualizaAduana.setObjectName(u"btnActualizaAduana")
        self.btnActualizaAduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon33 = QIcon()
        icon33.addFile(u":/80x80/icons/80x80/ct-aduana-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizaAduana.setIcon(icon33)
        self.btnActualizaAduana.setIconSize(QSize(80, 80))

        self.horizontalLayout_33.addWidget(self.btnActualizaAduana)

        self.btnEliminarAduana = QPushButton(self.frame_36)
        self.btnEliminarAduana.setObjectName(u"btnEliminarAduana")
        self.btnEliminarAduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon34 = QIcon()
        icon34.addFile(u":/80x80/icons/80x80/ct-aduana-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarAduana.setIcon(icon34)
        self.btnEliminarAduana.setIconSize(QSize(80, 80))

        self.horizontalLayout_33.addWidget(self.btnEliminarAduana)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)


        self.verticalLayout_54.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.page_aduana)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.tabla = QTableWidget(self.frame_37)
        if (self.tabla.columnCount() < 2):
            self.tabla.setColumnCount(2)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        icon35 = QIcon()
        icon35.addFile(u":/16x16/icons/16x16/ct-aduana16.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem24.setIcon(icon35);
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.tabla.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_34.addWidget(self.tabla)


        self.verticalLayout_54.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.page_aduana)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 60))
        self.frame_38.setMaximumSize(QSize(16777215, 60))
        self.frame_38.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_16)

        self.btn_refrescarAduana = QPushButton(self.frame_38)
        self.btn_refrescarAduana.setObjectName(u"btn_refrescarAduana")
        self.btn_refrescarAduana.setMinimumSize(QSize(80, 30))
        self.btn_refrescarAduana.setMaximumSize(QSize(80, 16777215))
        self.btn_refrescarAduana.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarAduana.setIcon(icon16)

        self.horizontalLayout_35.addWidget(self.btn_refrescarAduana)


        self.horizontalLayout_126.addLayout(self.horizontalLayout_35)


        self.verticalLayout_54.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.page_aduana)
        self.page_cliente = QWidget()
        self.page_cliente.setObjectName(u"page_cliente")
        self.verticalLayout_57 = QVBoxLayout(self.page_cliente)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_39 = QFrame(self.page_cliente)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 70))
        self.frame_39.setMaximumSize(QSize(16777215, 70))
        self.frame_39.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_39)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_25 = QLabel(self.frame_39)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.label_25)


        self.verticalLayout_59.addLayout(self.verticalLayout_58)


        self.verticalLayout_57.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.page_cliente)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 70))
        self.frame_40.setMaximumSize(QSize(16777215, 70))
        self.frame_40.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.BuscarlineEditCliente = QLineEdit(self.frame_40)
        self.BuscarlineEditCliente.setObjectName(u"BuscarlineEditCliente")
        self.BuscarlineEditCliente.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditCliente.setMaximumSize(QSize(16777215, 30))
        self.BuscarlineEditCliente.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditCliente.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.BuscarlineEditCliente)

        self.btnBuscarCliente = QPushButton(self.frame_40)
        self.btnBuscarCliente.setObjectName(u"btnBuscarCliente")
        self.btnBuscarCliente.setMinimumSize(QSize(100, 40))
        self.btnBuscarCliente.setMaximumSize(QSize(100, 40))
        self.btnBuscarCliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarCliente.setIcon(icon31)

        self.horizontalLayout_11.addWidget(self.btnBuscarCliente)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_11)


        self.verticalLayout_57.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.page_cliente)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 120))
        self.frame_41.setMaximumSize(QSize(16777215, 120))
        self.frame_41.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.btnNuevoCliente = QPushButton(self.frame_41)
        self.btnNuevoCliente.setObjectName(u"btnNuevoCliente")
        self.btnNuevoCliente.setMinimumSize(QSize(0, 100))
        self.btnNuevoCliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon36 = QIcon()
        icon36.addFile(u":/80x80/icons/80x80/ct-cliente-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoCliente.setIcon(icon36)
        self.btnNuevoCliente.setIconSize(QSize(80, 80))

        self.horizontalLayout_37.addWidget(self.btnNuevoCliente)

        self.btnActualizarCliente = QPushButton(self.frame_41)
        self.btnActualizarCliente.setObjectName(u"btnActualizarCliente")
        self.btnActualizarCliente.setMinimumSize(QSize(0, 100))
        self.btnActualizarCliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon37 = QIcon()
        icon37.addFile(u":/80x80/icons/80x80/ct-cliente-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarCliente.setIcon(icon37)
        self.btnActualizarCliente.setIconSize(QSize(80, 80))

        self.horizontalLayout_37.addWidget(self.btnActualizarCliente)

        self.btnEliminarCliente = QPushButton(self.frame_41)
        self.btnEliminarCliente.setObjectName(u"btnEliminarCliente")
        self.btnEliminarCliente.setMinimumSize(QSize(0, 100))
        self.btnEliminarCliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon38 = QIcon()
        icon38.addFile(u":/80x80/icons/80x80/ct-cliente-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarCliente.setIcon(icon38)
        self.btnEliminarCliente.setIconSize(QSize(80, 80))

        self.horizontalLayout_37.addWidget(self.btnEliminarCliente)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_37)


        self.verticalLayout_57.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.page_cliente)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.tabla_cl = QTableWidget(self.frame_42)
        if (self.tabla_cl.columnCount() < 3):
            self.tabla_cl.setColumnCount(3)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_cl.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_cl.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_cl.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        self.tabla_cl.setObjectName(u"tabla_cl")
        self.tabla_cl.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_41.addWidget(self.tabla_cl)


        self.verticalLayout_57.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.page_cliente)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 60))
        self.frame_43.setMaximumSize(QSize(16777215, 60))
        self.frame_43.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer)

        self.btn_refrescarCliente = QPushButton(self.frame_43)
        self.btn_refrescarCliente.setObjectName(u"btn_refrescarCliente")
        self.btn_refrescarCliente.setMinimumSize(QSize(80, 30))
        self.btn_refrescarCliente.setMaximumSize(QSize(80, 16777215))
        self.btn_refrescarCliente.setLayoutDirection(Qt.LeftToRight)
        self.btn_refrescarCliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarCliente.setIcon(icon16)

        self.horizontalLayout_40.addWidget(self.btn_refrescarCliente)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_40)


        self.verticalLayout_57.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_cliente)
        self.page_contenedor = QWidget()
        self.page_contenedor.setObjectName(u"page_contenedor")
        self.verticalLayout_60 = QVBoxLayout(self.page_contenedor)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_44 = QFrame(self.page_contenedor)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 70))
        self.frame_44.setMaximumSize(QSize(16777215, 70))
        self.frame_44.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_44)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_26 = QLabel(self.frame_44)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.label_26)


        self.verticalLayout_62.addLayout(self.verticalLayout_61)


        self.verticalLayout_60.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.page_contenedor)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 70))
        self.frame_45.setMaximumSize(QSize(16777215, 70))
        self.frame_45.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.BuscarlineEditContenedor = QLineEdit(self.frame_45)
        self.BuscarlineEditContenedor.setObjectName(u"BuscarlineEditContenedor")
        self.BuscarlineEditContenedor.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditContenedor.setMaximumSize(QSize(16777215, 30))
        self.BuscarlineEditContenedor.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditContenedor.setClearButtonEnabled(True)

        self.horizontalLayout_42.addWidget(self.BuscarlineEditContenedor)

        self.btnBuscarContenedor = QPushButton(self.frame_45)
        self.btnBuscarContenedor.setObjectName(u"btnBuscarContenedor")
        self.btnBuscarContenedor.setMinimumSize(QSize(100, 40))
        self.btnBuscarContenedor.setMaximumSize(QSize(100, 40))
        self.btnBuscarContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarContenedor.setIcon(icon31)

        self.horizontalLayout_42.addWidget(self.btnBuscarContenedor)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_42)


        self.verticalLayout_60.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.page_contenedor)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 120))
        self.frame_46.setMaximumSize(QSize(16777215, 120))
        self.frame_46.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.btnNuevoContenedor = QPushButton(self.frame_46)
        self.btnNuevoContenedor.setObjectName(u"btnNuevoContenedor")
        self.btnNuevoContenedor.setMinimumSize(QSize(0, 100))
        self.btnNuevoContenedor.setMaximumSize(QSize(16777215, 100))
        self.btnNuevoContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon39 = QIcon()
        icon39.addFile(u":/80x80/icons/80x80/ct-contenedor-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoContenedor.setIcon(icon39)
        self.btnNuevoContenedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_44.addWidget(self.btnNuevoContenedor)

        self.btnActualizarContenedor = QPushButton(self.frame_46)
        self.btnActualizarContenedor.setObjectName(u"btnActualizarContenedor")
        self.btnActualizarContenedor.setMinimumSize(QSize(0, 100))
        self.btnActualizarContenedor.setMaximumSize(QSize(16777215, 100))
        self.btnActualizarContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon40 = QIcon()
        icon40.addFile(u":/80x80/icons/80x80/ct-contenedor-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarContenedor.setIcon(icon40)
        self.btnActualizarContenedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_44.addWidget(self.btnActualizarContenedor)

        self.btnEliminarContenedor = QPushButton(self.frame_46)
        self.btnEliminarContenedor.setObjectName(u"btnEliminarContenedor")
        self.btnEliminarContenedor.setMinimumSize(QSize(0, 100))
        self.btnEliminarContenedor.setMaximumSize(QSize(16777215, 100))
        self.btnEliminarContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon41 = QIcon()
        icon41.addFile(u":/80x80/icons/80x80/ct-contenedor-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarContenedor.setIcon(icon41)
        self.btnEliminarContenedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_44.addWidget(self.btnEliminarContenedor)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_44)


        self.verticalLayout_60.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.page_contenedor)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_47)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.tabla_con = QTableWidget(self.frame_47)
        if (self.tabla_con.columnCount() < 4):
            self.tabla_con.setColumnCount(4)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_con.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_con.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_con.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_con.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        self.tabla_con.setObjectName(u"tabla_con")
        self.tabla_con.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_121.addWidget(self.tabla_con)


        self.verticalLayout_60.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.page_contenedor)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 60))
        self.frame_48.setMaximumSize(QSize(16777215, 60))
        self.frame_48.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_2)

        self.btn_CrudCont_regresar = QPushButton(self.frame_48)
        self.btn_CrudCont_regresar.setObjectName(u"btn_CrudCont_regresar")
        self.btn_CrudCont_regresar.setMinimumSize(QSize(80, 30))
        self.btn_CrudCont_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon42 = QIcon()
        icon42.addFile(u":/16x16/icons/16x16/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CrudCont_regresar.setIcon(icon42)

        self.horizontalLayout_46.addWidget(self.btn_CrudCont_regresar)

        self.btn_refrescarContenedor = QPushButton(self.frame_48)
        self.btn_refrescarContenedor.setObjectName(u"btn_refrescarContenedor")
        self.btn_refrescarContenedor.setMinimumSize(QSize(80, 30))
        self.btn_refrescarContenedor.setMaximumSize(QSize(80, 30))
        self.btn_refrescarContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarContenedor.setIcon(icon16)

        self.horizontalLayout_46.addWidget(self.btn_refrescarContenedor)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_46)


        self.verticalLayout_60.addWidget(self.frame_48)

        self.stackedWidget.addWidget(self.page_contenedor)
        self.page_transportista = QWidget()
        self.page_transportista.setObjectName(u"page_transportista")
        self.verticalLayout_63 = QVBoxLayout(self.page_transportista)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_49 = QFrame(self.page_transportista)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 70))
        self.frame_49.setMaximumSize(QSize(16777215, 70))
        self.frame_49.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_49)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_27 = QLabel(self.frame_49)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_27)


        self.verticalLayout_65.addLayout(self.verticalLayout_64)


        self.verticalLayout_63.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.page_transportista)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 70))
        self.frame_50.setMaximumSize(QSize(16777215, 70))
        self.frame_50.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.BuscarlineEditTransportista = QLineEdit(self.frame_50)
        self.BuscarlineEditTransportista.setObjectName(u"BuscarlineEditTransportista")
        self.BuscarlineEditTransportista.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditTransportista.setMaximumSize(QSize(16777215, 30))
        self.BuscarlineEditTransportista.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditTransportista.setClearButtonEnabled(True)

        self.horizontalLayout_48.addWidget(self.BuscarlineEditTransportista)

        self.btnBuscarTransportista = QPushButton(self.frame_50)
        self.btnBuscarTransportista.setObjectName(u"btnBuscarTransportista")
        self.btnBuscarTransportista.setMinimumSize(QSize(100, 40))
        self.btnBuscarTransportista.setMaximumSize(QSize(100, 40))
        self.btnBuscarTransportista.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarTransportista.setIcon(icon31)

        self.horizontalLayout_48.addWidget(self.btnBuscarTransportista)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_48)


        self.verticalLayout_63.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.page_transportista)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 120))
        self.frame_51.setMaximumSize(QSize(16777215, 120))
        self.frame_51.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.btnNuevaLinea = QPushButton(self.frame_51)
        self.btnNuevaLinea.setObjectName(u"btnNuevaLinea")
        self.btnNuevaLinea.setMinimumSize(QSize(0, 100))
        self.btnNuevaLinea.setMaximumSize(QSize(16777215, 100))
        self.btnNuevaLinea.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon43 = QIcon()
        icon43.addFile(u":/80x80/icons/80x80/ct-transportista-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevaLinea.setIcon(icon43)
        self.btnNuevaLinea.setIconSize(QSize(80, 80))

        self.horizontalLayout_50.addWidget(self.btnNuevaLinea)

        self.btnActualizarTransportista = QPushButton(self.frame_51)
        self.btnActualizarTransportista.setObjectName(u"btnActualizarTransportista")
        self.btnActualizarTransportista.setMinimumSize(QSize(0, 100))
        self.btnActualizarTransportista.setMaximumSize(QSize(16777215, 100))
        self.btnActualizarTransportista.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon44 = QIcon()
        icon44.addFile(u":/80x80/icons/80x80/ct-transportistas-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarTransportista.setIcon(icon44)
        self.btnActualizarTransportista.setIconSize(QSize(80, 80))

        self.horizontalLayout_50.addWidget(self.btnActualizarTransportista)

        self.btnEliminarTransportista = QPushButton(self.frame_51)
        self.btnEliminarTransportista.setObjectName(u"btnEliminarTransportista")
        self.btnEliminarTransportista.setMinimumSize(QSize(0, 100))
        self.btnEliminarTransportista.setMaximumSize(QSize(16777215, 100))
        self.btnEliminarTransportista.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon45 = QIcon()
        icon45.addFile(u":/80x80/icons/80x80/ct-transportistas-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarTransportista.setIcon(icon45)
        self.btnEliminarTransportista.setIconSize(QSize(80, 80))

        self.horizontalLayout_50.addWidget(self.btnEliminarTransportista)


        self.horizontalLayout_51.addLayout(self.horizontalLayout_50)


        self.verticalLayout_63.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.page_transportista)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_52)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.tabla_tr = QTableWidget(self.frame_52)
        if (self.tabla_tr.columnCount() < 2):
            self.tabla_tr.setColumnCount(2)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_tr.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setIcon(icon12);
        self.tabla_tr.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        self.tabla_tr.setObjectName(u"tabla_tr")
        self.tabla_tr.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_103.addWidget(self.tabla_tr)


        self.verticalLayout_63.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.page_transportista)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 60))
        self.frame_53.setMaximumSize(QSize(16777215, 60))
        self.frame_53.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_3)

        self.btn_refrescarTransportista = QPushButton(self.frame_53)
        self.btn_refrescarTransportista.setObjectName(u"btn_refrescarTransportista")
        self.btn_refrescarTransportista.setMinimumSize(QSize(80, 30))
        self.btn_refrescarTransportista.setMaximumSize(QSize(80, 30))
        self.btn_refrescarTransportista.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarTransportista.setIcon(icon16)

        self.horizontalLayout_52.addWidget(self.btn_refrescarTransportista)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_52)


        self.verticalLayout_63.addWidget(self.frame_53)

        self.stackedWidget.addWidget(self.page_transportista)
        self.page_operador = QWidget()
        self.page_operador.setObjectName(u"page_operador")
        self.verticalLayout_66 = QVBoxLayout(self.page_operador)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_54 = QFrame(self.page_operador)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 70))
        self.frame_54.setMaximumSize(QSize(16777215, 70))
        self.frame_54.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_54)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_28 = QLabel(self.frame_54)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_28)


        self.verticalLayout_69.addLayout(self.verticalLayout_68)


        self.verticalLayout_66.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.page_operador)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 70))
        self.frame_55.setMaximumSize(QSize(16777215, 70))
        self.frame_55.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.BuscarlineEditOperador = QLineEdit(self.frame_55)
        self.BuscarlineEditOperador.setObjectName(u"BuscarlineEditOperador")
        self.BuscarlineEditOperador.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditOperador.setMaximumSize(QSize(16777215, 30))
        self.BuscarlineEditOperador.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditOperador.setClearButtonEnabled(True)

        self.horizontalLayout_54.addWidget(self.BuscarlineEditOperador)

        self.btnBuscarOperador = QPushButton(self.frame_55)
        self.btnBuscarOperador.setObjectName(u"btnBuscarOperador")
        self.btnBuscarOperador.setMinimumSize(QSize(100, 40))
        self.btnBuscarOperador.setMaximumSize(QSize(100, 40))
        self.btnBuscarOperador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarOperador.setIcon(icon31)

        self.horizontalLayout_54.addWidget(self.btnBuscarOperador)


        self.horizontalLayout_55.addLayout(self.horizontalLayout_54)


        self.verticalLayout_66.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.page_operador)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 120))
        self.frame_56.setMaximumSize(QSize(16777215, 120))
        self.frame_56.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.btnNuevoOperador = QPushButton(self.frame_56)
        self.btnNuevoOperador.setObjectName(u"btnNuevoOperador")
        self.btnNuevoOperador.setMinimumSize(QSize(0, 100))
        self.btnNuevoOperador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon46 = QIcon()
        icon46.addFile(u":/80x80/icons/80x80/ct-operador-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoOperador.setIcon(icon46)
        self.btnNuevoOperador.setIconSize(QSize(80, 80))

        self.horizontalLayout_56.addWidget(self.btnNuevoOperador)

        self.btnActualizarOperador = QPushButton(self.frame_56)
        self.btnActualizarOperador.setObjectName(u"btnActualizarOperador")
        self.btnActualizarOperador.setMinimumSize(QSize(0, 100))
        self.btnActualizarOperador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon47 = QIcon()
        icon47.addFile(u":/80x80/icons/80x80/ct-operador-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarOperador.setIcon(icon47)
        self.btnActualizarOperador.setIconSize(QSize(80, 80))

        self.horizontalLayout_56.addWidget(self.btnActualizarOperador)

        self.btnEliminarOperador = QPushButton(self.frame_56)
        self.btnEliminarOperador.setObjectName(u"btnEliminarOperador")
        self.btnEliminarOperador.setMinimumSize(QSize(0, 100))
        self.btnEliminarOperador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon48 = QIcon()
        icon48.addFile(u":/80x80/icons/80x80/ct-operador-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarOperador.setIcon(icon48)
        self.btnEliminarOperador.setIconSize(QSize(80, 80))

        self.horizontalLayout_56.addWidget(self.btnEliminarOperador)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_56)


        self.verticalLayout_66.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.page_operador)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_57)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.tabla_op = QTableWidget(self.frame_57)
        if (self.tabla_op.columnCount() < 5):
            self.tabla_op.setColumnCount(5)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_op.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setIcon(icon22);
        self.tabla_op.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_op.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabla_op.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabla_op.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        self.tabla_op.setObjectName(u"tabla_op")
        self.tabla_op.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_104.addWidget(self.tabla_op)


        self.verticalLayout_66.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.page_operador)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 60))
        self.frame_58.setMaximumSize(QSize(16777215, 60))
        self.frame_58.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_4)

        self.btn_refrescarOperador = QPushButton(self.frame_58)
        self.btn_refrescarOperador.setObjectName(u"btn_refrescarOperador")
        self.btn_refrescarOperador.setMinimumSize(QSize(80, 30))
        self.btn_refrescarOperador.setMaximumSize(QSize(80, 30))
        self.btn_refrescarOperador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarOperador.setIcon(icon16)

        self.horizontalLayout_58.addWidget(self.btn_refrescarOperador)


        self.horizontalLayout_59.addLayout(self.horizontalLayout_58)


        self.verticalLayout_66.addWidget(self.frame_58)

        self.stackedWidget.addWidget(self.page_operador)
        self.page_producto = QWidget()
        self.page_producto.setObjectName(u"page_producto")
        self.verticalLayout_70 = QVBoxLayout(self.page_producto)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_59 = QFrame(self.page_producto)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 70))
        self.frame_59.setMaximumSize(QSize(16777215, 70))
        self.frame_59.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_59)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_29 = QLabel(self.frame_59)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.label_29)


        self.verticalLayout_72.addLayout(self.verticalLayout_71)


        self.verticalLayout_70.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.page_producto)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 70))
        self.frame_60.setMaximumSize(QSize(16777215, 70))
        self.frame_60.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.BuscarlineEditProducto = QLineEdit(self.frame_60)
        self.BuscarlineEditProducto.setObjectName(u"BuscarlineEditProducto")
        self.BuscarlineEditProducto.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditProducto.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditProducto.setClearButtonEnabled(True)

        self.horizontalLayout_60.addWidget(self.BuscarlineEditProducto)

        self.btnBuscarProducto = QPushButton(self.frame_60)
        self.btnBuscarProducto.setObjectName(u"btnBuscarProducto")
        self.btnBuscarProducto.setMinimumSize(QSize(100, 40))
        self.btnBuscarProducto.setMaximumSize(QSize(100, 40))
        self.btnBuscarProducto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarProducto.setIcon(icon31)

        self.horizontalLayout_60.addWidget(self.btnBuscarProducto)


        self.horizontalLayout_61.addLayout(self.horizontalLayout_60)


        self.verticalLayout_70.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.page_producto)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 120))
        self.frame_61.setMaximumSize(QSize(16777215, 120))
        self.frame_61.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.btnNuevoProducto = QPushButton(self.frame_61)
        self.btnNuevoProducto.setObjectName(u"btnNuevoProducto")
        self.btnNuevoProducto.setMinimumSize(QSize(0, 100))
        self.btnNuevoProducto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon49 = QIcon()
        icon49.addFile(u":/80x80/icons/80x80/ct-producto-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoProducto.setIcon(icon49)
        self.btnNuevoProducto.setIconSize(QSize(80, 80))

        self.horizontalLayout_62.addWidget(self.btnNuevoProducto)

        self.btnActualizarProducto = QPushButton(self.frame_61)
        self.btnActualizarProducto.setObjectName(u"btnActualizarProducto")
        self.btnActualizarProducto.setMinimumSize(QSize(0, 100))
        self.btnActualizarProducto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnActualizarProducto.setIcon(icon25)
        self.btnActualizarProducto.setIconSize(QSize(80, 80))

        self.horizontalLayout_62.addWidget(self.btnActualizarProducto)

        self.btnEliminarProducto = QPushButton(self.frame_61)
        self.btnEliminarProducto.setObjectName(u"btnEliminarProducto")
        self.btnEliminarProducto.setMinimumSize(QSize(0, 100))
        self.btnEliminarProducto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon50 = QIcon()
        icon50.addFile(u":/80x80/icons/80x80/ct-producto-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarProducto.setIcon(icon50)
        self.btnEliminarProducto.setIconSize(QSize(80, 80))

        self.horizontalLayout_62.addWidget(self.btnEliminarProducto)


        self.horizontalLayout_63.addLayout(self.horizontalLayout_62)


        self.verticalLayout_70.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.page_producto)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_62)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.tabla_pro = QTableWidget(self.frame_62)
        if (self.tabla_pro.columnCount() < 4):
            self.tabla_pro.setColumnCount(4)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabla_pro.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabla_pro.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabla_pro.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabla_pro.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        self.tabla_pro.setObjectName(u"tabla_pro")
        self.tabla_pro.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_105.addWidget(self.tabla_pro)


        self.verticalLayout_70.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.page_producto)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 60))
        self.frame_63.setMaximumSize(QSize(16777215, 60))
        self.frame_63.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_5)

        self.btn_refrescarProducto = QPushButton(self.frame_63)
        self.btn_refrescarProducto.setObjectName(u"btn_refrescarProducto")
        self.btn_refrescarProducto.setMinimumSize(QSize(80, 30))
        self.btn_refrescarProducto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarProducto.setIcon(icon16)

        self.horizontalLayout_64.addWidget(self.btn_refrescarProducto)


        self.horizontalLayout_65.addLayout(self.horizontalLayout_64)


        self.verticalLayout_70.addWidget(self.frame_63)

        self.stackedWidget.addWidget(self.page_producto)
        self.page_proveedor = QWidget()
        self.page_proveedor.setObjectName(u"page_proveedor")
        self.verticalLayout_73 = QVBoxLayout(self.page_proveedor)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.frame_64 = QFrame(self.page_proveedor)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 70))
        self.frame_64.setMaximumSize(QSize(16777215, 70))
        self.frame_64.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_64)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_30 = QLabel(self.frame_64)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.label_30)


        self.verticalLayout_75.addLayout(self.verticalLayout_74)


        self.verticalLayout_73.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.page_proveedor)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 70))
        self.frame_65.setMaximumSize(QSize(16777215, 70))
        self.frame_65.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.BuscarlineEditProveedor = QLineEdit(self.frame_65)
        self.BuscarlineEditProveedor.setObjectName(u"BuscarlineEditProveedor")
        self.BuscarlineEditProveedor.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditProveedor.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditProveedor.setClearButtonEnabled(True)

        self.horizontalLayout_66.addWidget(self.BuscarlineEditProveedor)

        self.btnBuscarProveedor = QPushButton(self.frame_65)
        self.btnBuscarProveedor.setObjectName(u"btnBuscarProveedor")
        self.btnBuscarProveedor.setMinimumSize(QSize(100, 40))
        self.btnBuscarProveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarProveedor.setIcon(icon31)

        self.horizontalLayout_66.addWidget(self.btnBuscarProveedor)


        self.horizontalLayout_67.addLayout(self.horizontalLayout_66)


        self.verticalLayout_73.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.page_proveedor)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 120))
        self.frame_66.setMaximumSize(QSize(16777215, 120))
        self.frame_66.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.btnNuevoProveedor = QPushButton(self.frame_66)
        self.btnNuevoProveedor.setObjectName(u"btnNuevoProveedor")
        self.btnNuevoProveedor.setMinimumSize(QSize(0, 100))
        self.btnNuevoProveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon51 = QIcon()
        icon51.addFile(u":/80x80/icons/80x80/ct-proveedor-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoProveedor.setIcon(icon51)
        self.btnNuevoProveedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_68.addWidget(self.btnNuevoProveedor)

        self.btnActualizarProveedor = QPushButton(self.frame_66)
        self.btnActualizarProveedor.setObjectName(u"btnActualizarProveedor")
        self.btnActualizarProveedor.setMinimumSize(QSize(0, 100))
        self.btnActualizarProveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon52 = QIcon()
        icon52.addFile(u":/80x80/icons/80x80/ct-proveedor-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarProveedor.setIcon(icon52)
        self.btnActualizarProveedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_68.addWidget(self.btnActualizarProveedor)

        self.btnEliminarProveedor = QPushButton(self.frame_66)
        self.btnEliminarProveedor.setObjectName(u"btnEliminarProveedor")
        self.btnEliminarProveedor.setMinimumSize(QSize(0, 100))
        self.btnEliminarProveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon53 = QIcon()
        icon53.addFile(u":/80x80/icons/80x80/ct-proveedor-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarProveedor.setIcon(icon53)
        self.btnEliminarProveedor.setIconSize(QSize(80, 80))

        self.horizontalLayout_68.addWidget(self.btnEliminarProveedor)


        self.horizontalLayout_69.addLayout(self.horizontalLayout_68)


        self.verticalLayout_73.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.page_proveedor)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_67)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.tabla_prov = QTableWidget(self.frame_67)
        if (self.tabla_prov.columnCount() < 3):
            self.tabla_prov.setColumnCount(3)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabla_prov.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabla_prov.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabla_prov.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        self.tabla_prov.setObjectName(u"tabla_prov")
        self.tabla_prov.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_106.addWidget(self.tabla_prov)


        self.verticalLayout_73.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.page_proveedor)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 60))
        self.frame_68.setMaximumSize(QSize(16777215, 60))
        self.frame_68.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_6)

        self.btn_refrescarProveedor = QPushButton(self.frame_68)
        self.btn_refrescarProveedor.setObjectName(u"btn_refrescarProveedor")
        self.btn_refrescarProveedor.setMinimumSize(QSize(80, 30))
        self.btn_refrescarProveedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarProveedor.setIcon(icon16)

        self.horizontalLayout_70.addWidget(self.btn_refrescarProveedor)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_70)


        self.verticalLayout_73.addWidget(self.frame_68)

        self.stackedWidget.addWidget(self.page_proveedor)
        self.page_sucursal = QWidget()
        self.page_sucursal.setObjectName(u"page_sucursal")
        self.verticalLayout_76 = QVBoxLayout(self.page_sucursal)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.frame_69 = QFrame(self.page_sucursal)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 70))
        self.frame_69.setMaximumSize(QSize(16777215, 70))
        self.frame_69.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_69)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_77 = QVBoxLayout()
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_31 = QLabel(self.frame_69)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_31)


        self.verticalLayout_78.addLayout(self.verticalLayout_77)


        self.verticalLayout_76.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.page_sucursal)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 70))
        self.frame_70.setMaximumSize(QSize(16777215, 70))
        self.frame_70.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.BuscarlineEditSucursal = QLineEdit(self.frame_70)
        self.BuscarlineEditSucursal.setObjectName(u"BuscarlineEditSucursal")
        self.BuscarlineEditSucursal.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditSucursal.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditSucursal.setClearButtonEnabled(True)

        self.horizontalLayout_72.addWidget(self.BuscarlineEditSucursal)

        self.btnBuscarSucursal = QPushButton(self.frame_70)
        self.btnBuscarSucursal.setObjectName(u"btnBuscarSucursal")
        self.btnBuscarSucursal.setMinimumSize(QSize(100, 40))
        self.btnBuscarSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarSucursal.setIcon(icon31)

        self.horizontalLayout_72.addWidget(self.btnBuscarSucursal)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_72)


        self.verticalLayout_76.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.page_sucursal)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 120))
        self.frame_71.setMaximumSize(QSize(16777215, 120))
        self.frame_71.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.btnNuevoSucursal = QPushButton(self.frame_71)
        self.btnNuevoSucursal.setObjectName(u"btnNuevoSucursal")
        self.btnNuevoSucursal.setMinimumSize(QSize(0, 100))
        self.btnNuevoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon54 = QIcon()
        icon54.addFile(u":/80x80/icons/80x80/ct-sucursal-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoSucursal.setIcon(icon54)
        self.btnNuevoSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_74.addWidget(self.btnNuevoSucursal)

        self.btnActualizarSucursal = QPushButton(self.frame_71)
        self.btnActualizarSucursal.setObjectName(u"btnActualizarSucursal")
        self.btnActualizarSucursal.setMinimumSize(QSize(0, 100))
        self.btnActualizarSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon55 = QIcon()
        icon55.addFile(u":/80x80/icons/80x80/ct-sucursal-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarSucursal.setIcon(icon55)
        self.btnActualizarSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_74.addWidget(self.btnActualizarSucursal)

        self.btnEliminarSucursal = QPushButton(self.frame_71)
        self.btnEliminarSucursal.setObjectName(u"btnEliminarSucursal")
        self.btnEliminarSucursal.setMinimumSize(QSize(0, 100))
        self.btnEliminarSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon56 = QIcon()
        icon56.addFile(u":/80x80/icons/80x80/ct-sucursal-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarSucursal.setIcon(icon56)
        self.btnEliminarSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_74.addWidget(self.btnEliminarSucursal)


        self.horizontalLayout_75.addLayout(self.horizontalLayout_74)


        self.verticalLayout_76.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.page_sucursal)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_72)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.tabla_su = QTableWidget(self.frame_72)
        if (self.tabla_su.columnCount() < 2):
            self.tabla_su.setColumnCount(2)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabla_su.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tabla_su.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        self.tabla_su.setObjectName(u"tabla_su")
        self.tabla_su.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_107.addWidget(self.tabla_su)


        self.verticalLayout_76.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.page_sucursal)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 60))
        self.frame_73.setMaximumSize(QSize(16777215, 60))
        self.frame_73.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_7)

        self.btn_refrescarSucursal = QPushButton(self.frame_73)
        self.btn_refrescarSucursal.setObjectName(u"btn_refrescarSucursal")
        self.btn_refrescarSucursal.setMinimumSize(QSize(80, 30))
        self.btn_refrescarSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarSucursal.setIcon(icon16)

        self.horizontalLayout_76.addWidget(self.btn_refrescarSucursal)


        self.horizontalLayout_77.addLayout(self.horizontalLayout_76)


        self.verticalLayout_76.addWidget(self.frame_73)

        self.stackedWidget.addWidget(self.page_sucursal)
        self.page_tractos = QWidget()
        self.page_tractos.setObjectName(u"page_tractos")
        self.verticalLayout_67 = QVBoxLayout(self.page_tractos)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.frame_74 = QFrame(self.page_tractos)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(0, 70))
        self.frame_74.setMaximumSize(QSize(16777215, 70))
        self.frame_74.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_74)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_79 = QVBoxLayout()
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_32 = QLabel(self.frame_74)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.label_32)


        self.verticalLayout_80.addLayout(self.verticalLayout_79)


        self.verticalLayout_67.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.page_tractos)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 70))
        self.frame_75.setMaximumSize(QSize(16777215, 70))
        self.frame_75.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.BuscarlineEditTracto = QLineEdit(self.frame_75)
        self.BuscarlineEditTracto.setObjectName(u"BuscarlineEditTracto")
        self.BuscarlineEditTracto.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditTracto.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditTracto.setClearButtonEnabled(True)

        self.horizontalLayout_78.addWidget(self.BuscarlineEditTracto)

        self.btnBuscarTracto = QPushButton(self.frame_75)
        self.btnBuscarTracto.setObjectName(u"btnBuscarTracto")
        self.btnBuscarTracto.setMinimumSize(QSize(100, 40))
        self.btnBuscarTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarTracto.setIcon(icon31)

        self.horizontalLayout_78.addWidget(self.btnBuscarTracto)


        self.horizontalLayout_79.addLayout(self.horizontalLayout_78)


        self.verticalLayout_67.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.page_tractos)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 120))
        self.frame_76.setMaximumSize(QSize(16777215, 120))
        self.frame_76.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_76)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.btnNuevoTracto = QPushButton(self.frame_76)
        self.btnNuevoTracto.setObjectName(u"btnNuevoTracto")
        self.btnNuevoTracto.setMinimumSize(QSize(0, 100))
        self.btnNuevoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon57 = QIcon()
        icon57.addFile(u":/80x80/icons/80x80/ct-tracto-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoTracto.setIcon(icon57)
        self.btnNuevoTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_80.addWidget(self.btnNuevoTracto)

        self.btnActualizarTracto = QPushButton(self.frame_76)
        self.btnActualizarTracto.setObjectName(u"btnActualizarTracto")
        self.btnActualizarTracto.setMinimumSize(QSize(0, 100))
        self.btnActualizarTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon58 = QIcon()
        icon58.addFile(u":/80x80/icons/80x80/ct-tracto-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarTracto.setIcon(icon58)
        self.btnActualizarTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_80.addWidget(self.btnActualizarTracto)

        self.btnEliminarTracto = QPushButton(self.frame_76)
        self.btnEliminarTracto.setObjectName(u"btnEliminarTracto")
        self.btnEliminarTracto.setMinimumSize(QSize(0, 100))
        self.btnEliminarTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon59 = QIcon()
        icon59.addFile(u":/80x80/icons/80x80/ct-tracto-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarTracto.setIcon(icon59)
        self.btnEliminarTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_80.addWidget(self.btnEliminarTracto)


        self.verticalLayout_102.addLayout(self.horizontalLayout_80)


        self.verticalLayout_67.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.page_tractos)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_77)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.tabla_trac = QTableWidget(self.frame_77)
        if (self.tabla_trac.columnCount() < 6):
            self.tabla_trac.setColumnCount(6)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tabla_trac.setHorizontalHeaderItem(5, __qtablewidgetitem53)
        self.tabla_trac.setObjectName(u"tabla_trac")
        self.tabla_trac.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_110.addWidget(self.tabla_trac)


        self.verticalLayout_67.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.page_tractos)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 60))
        self.frame_78.setMaximumSize(QSize(16777215, 60))
        self.frame_78.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_8)

        self.btn_tracto_regresar = QPushButton(self.frame_78)
        self.btn_tracto_regresar.setObjectName(u"btn_tracto_regresar")
        self.btn_tracto_regresar.setMinimumSize(QSize(80, 30))
        self.btn_tracto_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_tracto_regresar.setIcon(icon42)

        self.horizontalLayout_81.addWidget(self.btn_tracto_regresar)

        self.btn_refrescarTracto = QPushButton(self.frame_78)
        self.btn_refrescarTracto.setObjectName(u"btn_refrescarTracto")
        self.btn_refrescarTracto.setMinimumSize(QSize(80, 30))
        self.btn_refrescarTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarTracto.setIcon(icon16)

        self.horizontalLayout_81.addWidget(self.btn_refrescarTracto)


        self.horizontalLayout_82.addLayout(self.horizontalLayout_81)


        self.verticalLayout_67.addWidget(self.frame_78)

        self.stackedWidget.addWidget(self.page_tractos)
        self.page_cajaporta = QWidget()
        self.page_cajaporta.setObjectName(u"page_cajaporta")
        self.verticalLayout_81 = QVBoxLayout(self.page_cajaporta)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_79 = QFrame(self.page_cajaporta)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 70))
        self.frame_79.setMaximumSize(QSize(16777215, 70))
        self.frame_79.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_79)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_82 = QVBoxLayout()
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.label_33 = QLabel(self.frame_79)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.label_33)


        self.verticalLayout_83.addLayout(self.verticalLayout_82)


        self.verticalLayout_81.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.page_cajaporta)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 70))
        self.frame_80.setMaximumSize(QSize(16777215, 70))
        self.frame_80.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.BuscarlineEditCajaPorta = QLineEdit(self.frame_80)
        self.BuscarlineEditCajaPorta.setObjectName(u"BuscarlineEditCajaPorta")
        self.BuscarlineEditCajaPorta.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditCajaPorta.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditCajaPorta.setClearButtonEnabled(True)

        self.horizontalLayout_83.addWidget(self.BuscarlineEditCajaPorta)

        self.btnBuscarCajaPorta = QPushButton(self.frame_80)
        self.btnBuscarCajaPorta.setObjectName(u"btnBuscarCajaPorta")
        self.btnBuscarCajaPorta.setMinimumSize(QSize(100, 40))
        self.btnBuscarCajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarCajaPorta.setIcon(icon31)

        self.horizontalLayout_83.addWidget(self.btnBuscarCajaPorta)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_83)


        self.verticalLayout_81.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.page_cajaporta)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 120))
        self.frame_81.setMaximumSize(QSize(16777215, 120))
        self.frame_81.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.btnNuevoCajaPorta = QPushButton(self.frame_81)
        self.btnNuevoCajaPorta.setObjectName(u"btnNuevoCajaPorta")
        self.btnNuevoCajaPorta.setMinimumSize(QSize(0, 100))
        self.btnNuevoCajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon60 = QIcon()
        icon60.addFile(u":/80x80/icons/80x80/ct-porta-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoCajaPorta.setIcon(icon60)
        self.btnNuevoCajaPorta.setIconSize(QSize(80, 80))

        self.horizontalLayout_85.addWidget(self.btnNuevoCajaPorta)

        self.btnActualizarCajaPorta = QPushButton(self.frame_81)
        self.btnActualizarCajaPorta.setObjectName(u"btnActualizarCajaPorta")
        self.btnActualizarCajaPorta.setMinimumSize(QSize(0, 100))
        self.btnActualizarCajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon61 = QIcon()
        icon61.addFile(u":/80x80/icons/80x80/ct-porta-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarCajaPorta.setIcon(icon61)
        self.btnActualizarCajaPorta.setIconSize(QSize(80, 80))

        self.horizontalLayout_85.addWidget(self.btnActualizarCajaPorta)

        self.btnEliminarCajaPorta = QPushButton(self.frame_81)
        self.btnEliminarCajaPorta.setObjectName(u"btnEliminarCajaPorta")
        self.btnEliminarCajaPorta.setMinimumSize(QSize(0, 100))
        self.btnEliminarCajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon62 = QIcon()
        icon62.addFile(u":/80x80/icons/80x80/ct-porta-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarCajaPorta.setIcon(icon62)
        self.btnEliminarCajaPorta.setIconSize(QSize(80, 80))

        self.horizontalLayout_85.addWidget(self.btnEliminarCajaPorta)


        self.horizontalLayout_86.addLayout(self.horizontalLayout_85)


        self.verticalLayout_81.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.page_cajaporta)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_82)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.tabla_porta = QTableWidget(self.frame_82)
        if (self.tabla_porta.columnCount() < 4):
            self.tabla_porta.setColumnCount(4)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tabla_porta.setHorizontalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tabla_porta.setHorizontalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tabla_porta.setHorizontalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tabla_porta.setHorizontalHeaderItem(3, __qtablewidgetitem57)
        self.tabla_porta.setObjectName(u"tabla_porta")
        self.tabla_porta.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_109.addWidget(self.tabla_porta)


        self.verticalLayout_81.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.page_cajaporta)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 60))
        self.frame_83.setMaximumSize(QSize(16777215, 60))
        self.frame_83.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_9)

        self.btn_porta_regresar = QPushButton(self.frame_83)
        self.btn_porta_regresar.setObjectName(u"btn_porta_regresar")
        self.btn_porta_regresar.setMinimumSize(QSize(80, 30))
        self.btn_porta_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_porta_regresar.setIcon(icon42)

        self.horizontalLayout_87.addWidget(self.btn_porta_regresar)

        self.btn_refrescarCajaPorta = QPushButton(self.frame_83)
        self.btn_refrescarCajaPorta.setObjectName(u"btn_refrescarCajaPorta")
        self.btn_refrescarCajaPorta.setMinimumSize(QSize(80, 30))
        self.btn_refrescarCajaPorta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarCajaPorta.setIcon(icon16)

        self.horizontalLayout_87.addWidget(self.btn_refrescarCajaPorta)


        self.horizontalLayout_88.addLayout(self.horizontalLayout_87)


        self.verticalLayout_81.addWidget(self.frame_83)

        self.stackedWidget.addWidget(self.page_cajaporta)
        self.page_tipostractos = QWidget()
        self.page_tipostractos.setObjectName(u"page_tipostractos")
        self.verticalLayout_84 = QVBoxLayout(self.page_tipostractos)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_84 = QFrame(self.page_tipostractos)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 70))
        self.frame_84.setMaximumSize(QSize(16777215, 70))
        self.frame_84.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_84)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_85 = QVBoxLayout()
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.label_34 = QLabel(self.frame_84)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_34)


        self.verticalLayout_86.addLayout(self.verticalLayout_85)


        self.verticalLayout_84.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.page_tipostractos)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 70))
        self.frame_85.setMaximumSize(QSize(16777215, 70))
        self.frame_85.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.BuscarlineEditTipoTracto = QLineEdit(self.frame_85)
        self.BuscarlineEditTipoTracto.setObjectName(u"BuscarlineEditTipoTracto")
        self.BuscarlineEditTipoTracto.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditTipoTracto.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditTipoTracto.setClearButtonEnabled(True)

        self.horizontalLayout_89.addWidget(self.BuscarlineEditTipoTracto)

        self.btnBuscarTipoTracto = QPushButton(self.frame_85)
        self.btnBuscarTipoTracto.setObjectName(u"btnBuscarTipoTracto")
        self.btnBuscarTipoTracto.setMinimumSize(QSize(100, 40))
        self.btnBuscarTipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarTipoTracto.setIcon(icon31)

        self.horizontalLayout_89.addWidget(self.btnBuscarTipoTracto)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_89)


        self.verticalLayout_84.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.page_tipostractos)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 120))
        self.frame_86.setMaximumSize(QSize(16777215, 120))
        self.frame_86.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.btnNuevoTipoTracto = QPushButton(self.frame_86)
        self.btnNuevoTipoTracto.setObjectName(u"btnNuevoTipoTracto")
        self.btnNuevoTipoTracto.setMinimumSize(QSize(0, 100))
        self.btnNuevoTipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnNuevoTipoTracto.setIcon(icon57)
        self.btnNuevoTipoTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_91.addWidget(self.btnNuevoTipoTracto)

        self.btnActualizarTipoTracto = QPushButton(self.frame_86)
        self.btnActualizarTipoTracto.setObjectName(u"btnActualizarTipoTracto")
        self.btnActualizarTipoTracto.setMinimumSize(QSize(0, 100))
        self.btnActualizarTipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnActualizarTipoTracto.setIcon(icon58)
        self.btnActualizarTipoTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_91.addWidget(self.btnActualizarTipoTracto)

        self.btnEliminarTipoTracto = QPushButton(self.frame_86)
        self.btnEliminarTipoTracto.setObjectName(u"btnEliminarTipoTracto")
        self.btnEliminarTipoTracto.setMinimumSize(QSize(0, 100))
        self.btnEliminarTipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnEliminarTipoTracto.setIcon(icon59)
        self.btnEliminarTipoTracto.setIconSize(QSize(80, 80))

        self.horizontalLayout_91.addWidget(self.btnEliminarTipoTracto)


        self.horizontalLayout_92.addLayout(self.horizontalLayout_91)


        self.verticalLayout_84.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.page_tipostractos)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_87)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.tabla_tiptrac = QTableWidget(self.frame_87)
        if (self.tabla_tiptrac.columnCount() < 2):
            self.tabla_tiptrac.setColumnCount(2)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tabla_tiptrac.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tabla_tiptrac.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        self.tabla_tiptrac.setObjectName(u"tabla_tiptrac")
        self.tabla_tiptrac.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_108.addWidget(self.tabla_tiptrac)


        self.verticalLayout_84.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.page_tipostractos)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 60))
        self.frame_88.setMaximumSize(QSize(16777215, 60))
        self.frame_88.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_10)

        self.btn_tiptrac_regresar = QPushButton(self.frame_88)
        self.btn_tiptrac_regresar.setObjectName(u"btn_tiptrac_regresar")
        self.btn_tiptrac_regresar.setMinimumSize(QSize(80, 30))
        self.btn_tiptrac_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_tiptrac_regresar.setIcon(icon42)

        self.horizontalLayout_93.addWidget(self.btn_tiptrac_regresar)

        self.btn_refrescarTipoTracto = QPushButton(self.frame_88)
        self.btn_refrescarTipoTracto.setObjectName(u"btn_refrescarTipoTracto")
        self.btn_refrescarTipoTracto.setMinimumSize(QSize(80, 30))
        self.btn_refrescarTipoTracto.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarTipoTracto.setIcon(icon16)

        self.horizontalLayout_93.addWidget(self.btn_refrescarTipoTracto)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_93)


        self.verticalLayout_84.addWidget(self.frame_88)

        self.stackedWidget.addWidget(self.page_tipostractos)
        self.page_destinoventas = QWidget()
        self.page_destinoventas.setObjectName(u"page_destinoventas")
        self.verticalLayout_87 = QVBoxLayout(self.page_destinoventas)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_89 = QFrame(self.page_destinoventas)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 70))
        self.frame_89.setMaximumSize(QSize(16777215, 70))
        self.frame_89.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_89)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_88 = QVBoxLayout()
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_35 = QLabel(self.frame_89)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.label_35)


        self.verticalLayout_89.addLayout(self.verticalLayout_88)


        self.verticalLayout_87.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.page_destinoventas)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 70))
        self.frame_90.setMaximumSize(QSize(16777215, 70))
        self.frame_90.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.BuscarlineEditDestinoVta = QLineEdit(self.frame_90)
        self.BuscarlineEditDestinoVta.setObjectName(u"BuscarlineEditDestinoVta")
        self.BuscarlineEditDestinoVta.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditDestinoVta.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditDestinoVta.setClearButtonEnabled(True)

        self.horizontalLayout_96.addWidget(self.BuscarlineEditDestinoVta)

        self.btnBuscarDestinoVta = QPushButton(self.frame_90)
        self.btnBuscarDestinoVta.setObjectName(u"btnBuscarDestinoVta")
        self.btnBuscarDestinoVta.setMinimumSize(QSize(100, 40))
        self.btnBuscarDestinoVta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarDestinoVta.setIcon(icon31)

        self.horizontalLayout_96.addWidget(self.btnBuscarDestinoVta)


        self.horizontalLayout_97.addLayout(self.horizontalLayout_96)


        self.verticalLayout_87.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.page_destinoventas)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 120))
        self.frame_91.setMaximumSize(QSize(16777215, 120))
        self.frame_91.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.btnNuevoDestinovta = QPushButton(self.frame_91)
        self.btnNuevoDestinovta.setObjectName(u"btnNuevoDestinovta")
        self.btnNuevoDestinovta.setMinimumSize(QSize(0, 100))
        self.btnNuevoDestinovta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon63 = QIcon()
        icon63.addFile(u":/80x80/icons/80x80/ct-destino-vta-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoDestinovta.setIcon(icon63)
        self.btnNuevoDestinovta.setIconSize(QSize(80, 80))

        self.horizontalLayout_98.addWidget(self.btnNuevoDestinovta)

        self.btnActualizarDestinovta = QPushButton(self.frame_91)
        self.btnActualizarDestinovta.setObjectName(u"btnActualizarDestinovta")
        self.btnActualizarDestinovta.setMinimumSize(QSize(0, 100))
        self.btnActualizarDestinovta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon64 = QIcon()
        icon64.addFile(u":/80x80/icons/80x80/ct-destino-vta-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarDestinovta.setIcon(icon64)
        self.btnActualizarDestinovta.setIconSize(QSize(80, 80))

        self.horizontalLayout_98.addWidget(self.btnActualizarDestinovta)

        self.btnEliminarDestinovta = QPushButton(self.frame_91)
        self.btnEliminarDestinovta.setObjectName(u"btnEliminarDestinovta")
        self.btnEliminarDestinovta.setMinimumSize(QSize(0, 100))
        self.btnEliminarDestinovta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon65 = QIcon()
        icon65.addFile(u":/80x80/icons/80x80/ct-destino-vta-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarDestinovta.setIcon(icon65)
        self.btnEliminarDestinovta.setIconSize(QSize(80, 80))

        self.horizontalLayout_98.addWidget(self.btnEliminarDestinovta)


        self.horizontalLayout_99.addLayout(self.horizontalLayout_98)


        self.verticalLayout_87.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.page_destinoventas)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_92)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.tabla_dv = QTableWidget(self.frame_92)
        if (self.tabla_dv.columnCount() < 2):
            self.tabla_dv.setColumnCount(2)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tabla_dv.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tabla_dv.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        self.tabla_dv.setObjectName(u"tabla_dv")
        self.tabla_dv.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_111.addWidget(self.tabla_dv)


        self.verticalLayout_87.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.page_destinoventas)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(0, 60))
        self.frame_93.setMaximumSize(QSize(16777215, 60))
        self.frame_93.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_11)

        self.btn_destinovtas_regresar = QPushButton(self.frame_93)
        self.btn_destinovtas_regresar.setObjectName(u"btn_destinovtas_regresar")
        self.btn_destinovtas_regresar.setMinimumSize(QSize(80, 30))
        self.btn_destinovtas_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_destinovtas_regresar.setIcon(icon42)

        self.horizontalLayout_100.addWidget(self.btn_destinovtas_regresar)

        self.btn_refrescarDestinovta = QPushButton(self.frame_93)
        self.btn_refrescarDestinovta.setObjectName(u"btn_refrescarDestinovta")
        self.btn_refrescarDestinovta.setMinimumSize(QSize(80, 30))
        self.btn_refrescarDestinovta.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarDestinovta.setIcon(icon16)

        self.horizontalLayout_100.addWidget(self.btn_refrescarDestinovta)


        self.horizontalLayout_101.addLayout(self.horizontalLayout_100)


        self.verticalLayout_87.addWidget(self.frame_93)

        self.stackedWidget.addWidget(self.page_destinoventas)
        self.page_destinosolas = QWidget()
        self.page_destinosolas.setObjectName(u"page_destinosolas")
        self.verticalLayout_90 = QVBoxLayout(self.page_destinosolas)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_94 = QFrame(self.page_destinosolas)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 70))
        self.frame_94.setMaximumSize(QSize(16777215, 70))
        self.frame_94.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_94)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_91 = QVBoxLayout()
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_36 = QLabel(self.frame_94)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.label_36)


        self.verticalLayout_92.addLayout(self.verticalLayout_91)


        self.verticalLayout_90.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.page_destinosolas)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(0, 70))
        self.frame_95.setMaximumSize(QSize(16777215, 70))
        self.frame_95.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.BuscarlineEditDestinoSolas = QLineEdit(self.frame_95)
        self.BuscarlineEditDestinoSolas.setObjectName(u"BuscarlineEditDestinoSolas")
        self.BuscarlineEditDestinoSolas.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditDestinoSolas.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditDestinoSolas.setClearButtonEnabled(True)

        self.horizontalLayout_102.addWidget(self.BuscarlineEditDestinoSolas)

        self.btnBuscarDestinoSolas = QPushButton(self.frame_95)
        self.btnBuscarDestinoSolas.setObjectName(u"btnBuscarDestinoSolas")
        self.btnBuscarDestinoSolas.setMinimumSize(QSize(100, 40))
        self.btnBuscarDestinoSolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarDestinoSolas.setIcon(icon31)

        self.horizontalLayout_102.addWidget(self.btnBuscarDestinoSolas)


        self.horizontalLayout_103.addLayout(self.horizontalLayout_102)


        self.verticalLayout_90.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.page_destinosolas)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 120))
        self.frame_96.setMaximumSize(QSize(16777215, 120))
        self.frame_96.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.btnNuevoDestinosolas = QPushButton(self.frame_96)
        self.btnNuevoDestinosolas.setObjectName(u"btnNuevoDestinosolas")
        self.btnNuevoDestinosolas.setMinimumSize(QSize(0, 100))
        self.btnNuevoDestinosolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon66 = QIcon()
        icon66.addFile(u":/80x80/icons/80x80/ct-destino-solas-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoDestinosolas.setIcon(icon66)
        self.btnNuevoDestinosolas.setIconSize(QSize(80, 80))

        self.horizontalLayout_104.addWidget(self.btnNuevoDestinosolas)

        self.btnActualizarDestinosolas = QPushButton(self.frame_96)
        self.btnActualizarDestinosolas.setObjectName(u"btnActualizarDestinosolas")
        self.btnActualizarDestinosolas.setMinimumSize(QSize(0, 100))
        self.btnActualizarDestinosolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon67 = QIcon()
        icon67.addFile(u":/80x80/icons/80x80/ct-destino-solas-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarDestinosolas.setIcon(icon67)
        self.btnActualizarDestinosolas.setIconSize(QSize(80, 80))

        self.horizontalLayout_104.addWidget(self.btnActualizarDestinosolas)

        self.btnEliminarDestinosolas = QPushButton(self.frame_96)
        self.btnEliminarDestinosolas.setObjectName(u"btnEliminarDestinosolas")
        self.btnEliminarDestinosolas.setMinimumSize(QSize(0, 100))
        self.btnEliminarDestinosolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon68 = QIcon()
        icon68.addFile(u":/80x80/icons/80x80/ct-destino-solas-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarDestinosolas.setIcon(icon68)
        self.btnEliminarDestinosolas.setIconSize(QSize(80, 80))

        self.horizontalLayout_104.addWidget(self.btnEliminarDestinosolas)


        self.horizontalLayout_105.addLayout(self.horizontalLayout_104)


        self.verticalLayout_90.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.page_destinosolas)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_97)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.tabla_dsol = QTableWidget(self.frame_97)
        if (self.tabla_dsol.columnCount() < 2):
            self.tabla_dsol.setColumnCount(2)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tabla_dsol.setHorizontalHeaderItem(0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tabla_dsol.setHorizontalHeaderItem(1, __qtablewidgetitem63)
        self.tabla_dsol.setObjectName(u"tabla_dsol")
        self.tabla_dsol.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_112.addWidget(self.tabla_dsol)


        self.verticalLayout_90.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.page_destinosolas)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 60))
        self.frame_98.setMaximumSize(QSize(16777215, 60))
        self.frame_98.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_12)

        self.btn_destinosolas_regresar = QPushButton(self.frame_98)
        self.btn_destinosolas_regresar.setObjectName(u"btn_destinosolas_regresar")
        self.btn_destinosolas_regresar.setMinimumSize(QSize(80, 30))
        self.btn_destinosolas_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_destinosolas_regresar.setIcon(icon42)

        self.horizontalLayout_106.addWidget(self.btn_destinosolas_regresar)

        self.btn_refrescarDestinosolas = QPushButton(self.frame_98)
        self.btn_refrescarDestinosolas.setObjectName(u"btn_refrescarDestinosolas")
        self.btn_refrescarDestinosolas.setMinimumSize(QSize(80, 30))
        self.btn_refrescarDestinosolas.setBaseSize(QSize(2, 0))
        self.btn_refrescarDestinosolas.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarDestinosolas.setIcon(icon16)

        self.horizontalLayout_106.addWidget(self.btn_refrescarDestinosolas)


        self.horizontalLayout_107.addLayout(self.horizontalLayout_106)


        self.verticalLayout_90.addWidget(self.frame_98)

        self.stackedWidget.addWidget(self.page_destinosolas)
        self.page_destinosucursal = QWidget()
        self.page_destinosucursal.setObjectName(u"page_destinosucursal")
        self.verticalLayout_93 = QVBoxLayout(self.page_destinosucursal)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_99 = QFrame(self.page_destinosucursal)
        self.frame_99.setObjectName(u"frame_99")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(70)
        sizePolicy5.setHeightForWidth(self.frame_99.sizePolicy().hasHeightForWidth())
        self.frame_99.setSizePolicy(sizePolicy5)
        self.frame_99.setMaximumSize(QSize(16777215, 70))
        self.frame_99.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_99)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_94 = QVBoxLayout()
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.label_37 = QLabel(self.frame_99)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_37)


        self.verticalLayout_95.addLayout(self.verticalLayout_94)


        self.verticalLayout_93.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.page_destinosucursal)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 70))
        self.frame_100.setMaximumSize(QSize(16777215, 70))
        self.frame_100.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.BuscarlineEditDestinoSucursal = QLineEdit(self.frame_100)
        self.BuscarlineEditDestinoSucursal.setObjectName(u"BuscarlineEditDestinoSucursal")
        self.BuscarlineEditDestinoSucursal.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditDestinoSucursal.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditDestinoSucursal.setClearButtonEnabled(True)

        self.horizontalLayout_108.addWidget(self.BuscarlineEditDestinoSucursal)

        self.btnBuscarDestinoSucursal = QPushButton(self.frame_100)
        self.btnBuscarDestinoSucursal.setObjectName(u"btnBuscarDestinoSucursal")
        self.btnBuscarDestinoSucursal.setMinimumSize(QSize(100, 40))
        self.btnBuscarDestinoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarDestinoSucursal.setIcon(icon31)

        self.horizontalLayout_108.addWidget(self.btnBuscarDestinoSucursal)


        self.horizontalLayout_109.addLayout(self.horizontalLayout_108)


        self.verticalLayout_93.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.page_destinosucursal)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(0, 120))
        self.frame_101.setMaximumSize(QSize(16777215, 120))
        self.frame_101.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.btnNuevoDestinoSucursal = QPushButton(self.frame_101)
        self.btnNuevoDestinoSucursal.setObjectName(u"btnNuevoDestinoSucursal")
        self.btnNuevoDestinoSucursal.setMinimumSize(QSize(0, 100))
        self.btnNuevoDestinoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon69 = QIcon()
        icon69.addFile(u":/80x80/icons/80x80/ct-destino-sucursal-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoDestinoSucursal.setIcon(icon69)
        self.btnNuevoDestinoSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_110.addWidget(self.btnNuevoDestinoSucursal)

        self.btnActualizarDestinoSucursal = QPushButton(self.frame_101)
        self.btnActualizarDestinoSucursal.setObjectName(u"btnActualizarDestinoSucursal")
        self.btnActualizarDestinoSucursal.setMinimumSize(QSize(0, 100))
        self.btnActualizarDestinoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon70 = QIcon()
        icon70.addFile(u":/80x80/icons/80x80/ct-destino-sucursal-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarDestinoSucursal.setIcon(icon70)
        self.btnActualizarDestinoSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_110.addWidget(self.btnActualizarDestinoSucursal)

        self.btnEliminarDestinoSucursal = QPushButton(self.frame_101)
        self.btnEliminarDestinoSucursal.setObjectName(u"btnEliminarDestinoSucursal")
        self.btnEliminarDestinoSucursal.setMinimumSize(QSize(0, 100))
        self.btnEliminarDestinoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon71 = QIcon()
        icon71.addFile(u":/80x80/icons/80x80/ct-destino-sucursal-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarDestinoSucursal.setIcon(icon71)
        self.btnEliminarDestinoSucursal.setIconSize(QSize(80, 80))

        self.horizontalLayout_110.addWidget(self.btnEliminarDestinoSucursal)


        self.horizontalLayout_111.addLayout(self.horizontalLayout_110)


        self.verticalLayout_93.addWidget(self.frame_101)

        self.frame_102 = QFrame(self.page_destinosucursal)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_102)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.tabla_suc = QTableWidget(self.frame_102)
        if (self.tabla_suc.columnCount() < 2):
            self.tabla_suc.setColumnCount(2)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tabla_suc.setHorizontalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tabla_suc.setHorizontalHeaderItem(1, __qtablewidgetitem65)
        self.tabla_suc.setObjectName(u"tabla_suc")
        self.tabla_suc.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_113.addWidget(self.tabla_suc)


        self.verticalLayout_93.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.page_destinosucursal)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 60))
        self.frame_103.setMaximumSize(QSize(16777215, 60))
        self.frame_103.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_13)

        self.btn_destinosucursal_regresar = QPushButton(self.frame_103)
        self.btn_destinosucursal_regresar.setObjectName(u"btn_destinosucursal_regresar")
        self.btn_destinosucursal_regresar.setMinimumSize(QSize(80, 30))
        self.btn_destinosucursal_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_destinosucursal_regresar.setIcon(icon42)

        self.horizontalLayout_112.addWidget(self.btn_destinosucursal_regresar)

        self.btn_refrescarDestinoSucursal = QPushButton(self.frame_103)
        self.btn_refrescarDestinoSucursal.setObjectName(u"btn_refrescarDestinoSucursal")
        self.btn_refrescarDestinoSucursal.setMinimumSize(QSize(80, 30))
        self.btn_refrescarDestinoSucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarDestinoSucursal.setIcon(icon16)

        self.horizontalLayout_112.addWidget(self.btn_refrescarDestinoSucursal)


        self.horizontalLayout_113.addLayout(self.horizontalLayout_112)


        self.verticalLayout_93.addWidget(self.frame_103)

        self.stackedWidget.addWidget(self.page_destinosucursal)
        self.page_destinosifon = QWidget()
        self.page_destinosifon.setObjectName(u"page_destinosifon")
        self.verticalLayout_96 = QVBoxLayout(self.page_destinosifon)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.frame_104 = QFrame(self.page_destinosifon)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 70))
        self.frame_104.setMaximumSize(QSize(16777215, 70))
        self.frame_104.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_104)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_97 = QVBoxLayout()
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_38 = QLabel(self.frame_104)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.label_38)


        self.verticalLayout_98.addLayout(self.verticalLayout_97)


        self.verticalLayout_96.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.page_destinosifon)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 70))
        self.frame_105.setMaximumSize(QSize(16777215, 70))
        self.frame_105.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.BuscarlineEditDestinoSifon = QLineEdit(self.frame_105)
        self.BuscarlineEditDestinoSifon.setObjectName(u"BuscarlineEditDestinoSifon")
        self.BuscarlineEditDestinoSifon.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditDestinoSifon.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditDestinoSifon.setClearButtonEnabled(True)

        self.horizontalLayout_114.addWidget(self.BuscarlineEditDestinoSifon)

        self.btnBuscarDestinoSifon = QPushButton(self.frame_105)
        self.btnBuscarDestinoSifon.setObjectName(u"btnBuscarDestinoSifon")
        self.btnBuscarDestinoSifon.setMinimumSize(QSize(100, 40))
        self.btnBuscarDestinoSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarDestinoSifon.setIcon(icon31)

        self.horizontalLayout_114.addWidget(self.btnBuscarDestinoSifon)


        self.horizontalLayout_115.addLayout(self.horizontalLayout_114)


        self.verticalLayout_96.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.page_destinosifon)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 120))
        self.frame_106.setMaximumSize(QSize(16777215, 120))
        self.frame_106.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.btnNuevoDestinoSifon = QPushButton(self.frame_106)
        self.btnNuevoDestinoSifon.setObjectName(u"btnNuevoDestinoSifon")
        self.btnNuevoDestinoSifon.setMinimumSize(QSize(0, 100))
        self.btnNuevoDestinoSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon72 = QIcon()
        icon72.addFile(u":/80x80/icons/80x80/ct-destino-sifon-create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoDestinoSifon.setIcon(icon72)
        self.btnNuevoDestinoSifon.setIconSize(QSize(80, 80))

        self.horizontalLayout_116.addWidget(self.btnNuevoDestinoSifon)

        self.btnActualizarDestinoSifon = QPushButton(self.frame_106)
        self.btnActualizarDestinoSifon.setObjectName(u"btnActualizarDestinoSifon")
        self.btnActualizarDestinoSifon.setMinimumSize(QSize(0, 100))
        self.btnActualizarDestinoSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon73 = QIcon()
        icon73.addFile(u":/80x80/icons/80x80/ct-destino-sifon-update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarDestinoSifon.setIcon(icon73)
        self.btnActualizarDestinoSifon.setIconSize(QSize(80, 80))

        self.horizontalLayout_116.addWidget(self.btnActualizarDestinoSifon)

        self.btnEliminarDestinoSifon = QPushButton(self.frame_106)
        self.btnEliminarDestinoSifon.setObjectName(u"btnEliminarDestinoSifon")
        self.btnEliminarDestinoSifon.setMinimumSize(QSize(0, 100))
        self.btnEliminarDestinoSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon74 = QIcon()
        icon74.addFile(u":/80x80/icons/80x80/ct-destino-sifon-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEliminarDestinoSifon.setIcon(icon74)
        self.btnEliminarDestinoSifon.setIconSize(QSize(80, 80))

        self.horizontalLayout_116.addWidget(self.btnEliminarDestinoSifon)


        self.horizontalLayout_117.addLayout(self.horizontalLayout_116)


        self.verticalLayout_96.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.page_destinosifon)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_107)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.tabla_sif = QTableWidget(self.frame_107)
        if (self.tabla_sif.columnCount() < 2):
            self.tabla_sif.setColumnCount(2)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tabla_sif.setHorizontalHeaderItem(0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tabla_sif.setHorizontalHeaderItem(1, __qtablewidgetitem67)
        self.tabla_sif.setObjectName(u"tabla_sif")
        self.tabla_sif.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_119.addWidget(self.tabla_sif)


        self.verticalLayout_96.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.page_destinosifon)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 60))
        self.frame_108.setMaximumSize(QSize(16777215, 60))
        self.frame_108.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_118.addItem(self.horizontalSpacer_14)

        self.btn_destinosifon_regresar = QPushButton(self.frame_108)
        self.btn_destinosifon_regresar.setObjectName(u"btn_destinosifon_regresar")
        self.btn_destinosifon_regresar.setMinimumSize(QSize(80, 30))
        self.btn_destinosifon_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_destinosifon_regresar.setIcon(icon42)

        self.horizontalLayout_118.addWidget(self.btn_destinosifon_regresar)

        self.btn_refrescarDestinoSifon = QPushButton(self.frame_108)
        self.btn_refrescarDestinoSifon.setObjectName(u"btn_refrescarDestinoSifon")
        self.btn_refrescarDestinoSifon.setMinimumSize(QSize(80, 30))
        self.btn_refrescarDestinoSifon.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarDestinoSifon.setIcon(icon16)

        self.horizontalLayout_118.addWidget(self.btn_refrescarDestinoSifon)


        self.horizontalLayout_119.addLayout(self.horizontalLayout_118)


        self.verticalLayout_96.addWidget(self.frame_108)

        self.stackedWidget.addWidget(self.page_destinosifon)
        self.page_tiposcontenedor = QWidget()
        self.page_tiposcontenedor.setObjectName(u"page_tiposcontenedor")
        self.verticalLayout_99 = QVBoxLayout(self.page_tiposcontenedor)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.frame_109 = QFrame(self.page_tiposcontenedor)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 70))
        self.frame_109.setMaximumSize(QSize(16777215, 70))
        self.frame_109.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_109)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_100 = QVBoxLayout()
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.label_39 = QLabel(self.frame_109)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_39)


        self.verticalLayout_101.addLayout(self.verticalLayout_100)


        self.verticalLayout_99.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.page_tiposcontenedor)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(0, 70))
        self.frame_110.setMaximumSize(QSize(16777215, 70))
        self.frame_110.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.BuscarlineEditTipoCont = QLineEdit(self.frame_110)
        self.BuscarlineEditTipoCont.setObjectName(u"BuscarlineEditTipoCont")
        self.BuscarlineEditTipoCont.setMinimumSize(QSize(0, 30))
        self.BuscarlineEditTipoCont.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.BuscarlineEditTipoCont.setClearButtonEnabled(True)

        self.horizontalLayout_120.addWidget(self.BuscarlineEditTipoCont)

        self.btnBuscarTipoCont = QPushButton(self.frame_110)
        self.btnBuscarTipoCont.setObjectName(u"btnBuscarTipoCont")
        self.btnBuscarTipoCont.setMinimumSize(QSize(100, 40))
        self.btnBuscarTipoCont.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnBuscarTipoCont.setIcon(icon31)

        self.horizontalLayout_120.addWidget(self.btnBuscarTipoCont)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_120)


        self.verticalLayout_99.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.page_tiposcontenedor)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(0, 120))
        self.frame_111.setMaximumSize(QSize(16777215, 120))
        self.frame_111.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.btnNuevoTipoCont = QPushButton(self.frame_111)
        self.btnNuevoTipoCont.setObjectName(u"btnNuevoTipoCont")
        self.btnNuevoTipoCont.setMinimumSize(QSize(0, 100))
        self.btnNuevoTipoCont.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnNuevoTipoCont.setIcon(icon39)
        self.btnNuevoTipoCont.setIconSize(QSize(80, 80))

        self.horizontalLayout_122.addWidget(self.btnNuevoTipoCont)

        self.btnActualizarTipoCont = QPushButton(self.frame_111)
        self.btnActualizarTipoCont.setObjectName(u"btnActualizarTipoCont")
        self.btnActualizarTipoCont.setMinimumSize(QSize(0, 100))
        self.btnActualizarTipoCont.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnActualizarTipoCont.setIcon(icon40)
        self.btnActualizarTipoCont.setIconSize(QSize(80, 80))

        self.horizontalLayout_122.addWidget(self.btnActualizarTipoCont)

        self.btnEliminarTipoCont = QPushButton(self.frame_111)
        self.btnEliminarTipoCont.setObjectName(u"btnEliminarTipoCont")
        self.btnEliminarTipoCont.setMinimumSize(QSize(0, 100))
        self.btnEliminarTipoCont.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btnEliminarTipoCont.setIcon(icon41)
        self.btnEliminarTipoCont.setIconSize(QSize(80, 80))

        self.horizontalLayout_122.addWidget(self.btnEliminarTipoCont)


        self.horizontalLayout_123.addLayout(self.horizontalLayout_122)


        self.verticalLayout_99.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.page_tiposcontenedor)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_112)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.tabla_tcon = QTableWidget(self.frame_112)
        if (self.tabla_tcon.columnCount() < 2):
            self.tabla_tcon.setColumnCount(2)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tabla_tcon.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tabla_tcon.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        self.tabla_tcon.setObjectName(u"tabla_tcon")
        self.tabla_tcon.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_120.addWidget(self.tabla_tcon)


        self.verticalLayout_99.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.page_tiposcontenedor)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(0, 60))
        self.frame_113.setMaximumSize(QSize(16777215, 60))
        self.frame_113.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_124.addItem(self.horizontalSpacer_15)

        self.btn_TipoCon_regresar = QPushButton(self.frame_113)
        self.btn_TipoCon_regresar.setObjectName(u"btn_TipoCon_regresar")
        self.btn_TipoCon_regresar.setMinimumSize(QSize(80, 30))
        self.btn_TipoCon_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_TipoCon_regresar.setIcon(icon42)

        self.horizontalLayout_124.addWidget(self.btn_TipoCon_regresar)

        self.btn_refrescarTipoCont = QPushButton(self.frame_113)
        self.btn_refrescarTipoCont.setObjectName(u"btn_refrescarTipoCont")
        self.btn_refrescarTipoCont.setMinimumSize(QSize(80, 30))
        self.btn_refrescarTipoCont.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_refrescarTipoCont.setIcon(icon16)

        self.horizontalLayout_124.addWidget(self.btn_refrescarTipoCont)


        self.horizontalLayout_125.addLayout(self.horizontalLayout_124)


        self.verticalLayout_99.addWidget(self.frame_113)

        self.stackedWidget.addWidget(self.page_tiposcontenedor)
        self.page_menuContenedor = QWidget()
        self.page_menuContenedor.setObjectName(u"page_menuContenedor")
        self.verticalLayout_114 = QVBoxLayout(self.page_menuContenedor)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.frame_114 = QFrame(self.page_menuContenedor)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(0, 70))
        self.frame_114.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_114)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_115 = QVBoxLayout()
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.label_40 = QLabel(self.frame_114)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_115.addWidget(self.label_40)


        self.verticalLayout_116.addLayout(self.verticalLayout_115)


        self.verticalLayout_114.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.page_menuContenedor)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_115)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_117 = QVBoxLayout()
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_10.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_10.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_10.setHorizontalSpacing(60)
        self.formLayout_10.setVerticalSpacing(60)
        self.btn_crudContenedor = QPushButton(self.frame_115)
        self.btn_crudContenedor.setObjectName(u"btn_crudContenedor")
        self.btn_crudContenedor.setMinimumSize(QSize(300, 100))
        self.btn_crudContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon75 = QIcon()
        icon75.addFile(u":/images/images/ct-solas_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_crudContenedor.setIcon(icon75)
        self.btn_crudContenedor.setIconSize(QSize(300, 100))

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.btn_crudContenedor)

        self.btn_tipoContenedor = QPushButton(self.frame_115)
        self.btn_tipoContenedor.setObjectName(u"btn_tipoContenedor")
        self.btn_tipoContenedor.setMinimumSize(QSize(300, 100))
        self.btn_tipoContenedor.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_tipoContenedor.setIcon(icon4)
        self.btn_tipoContenedor.setIconSize(QSize(300, 100))

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.btn_tipoContenedor)

        self.label_41 = QLabel(self.frame_115)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(300, 0))
        self.label_41.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_41)

        self.label_42 = QLabel(self.frame_115)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(300, 0))
        self.label_42.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.label_42)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_10.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_19)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_10.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_20)


        self.verticalLayout_117.addLayout(self.formLayout_10)


        self.verticalLayout_118.addLayout(self.verticalLayout_117)


        self.verticalLayout_114.addWidget(self.frame_115)

        self.stackedWidget.addWidget(self.page_menuContenedor)
        self.page_movin = QWidget()
        self.page_movin.setObjectName(u"page_movin")
        self.verticalLayout_122 = QVBoxLayout(self.page_movin)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.frame_116 = QFrame(self.page_movin)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(0, 70))
        self.frame_116.setMaximumSize(QSize(16777215, 70))
        self.frame_116.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_116)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_123 = QVBoxLayout()
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.label_43 = QLabel(self.frame_116)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.label_43)


        self.verticalLayout_124.addLayout(self.verticalLayout_123)


        self.verticalLayout_122.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.page_movin)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_11.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_11.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_11.setHorizontalSpacing(60)
        self.formLayout_11.setVerticalSpacing(60)
        self.btn_movin_torton = QPushButton(self.frame_117)
        self.btn_movin_torton.setObjectName(u"btn_movin_torton")
        self.btn_movin_torton.setMinimumSize(QSize(300, 100))
        self.btn_movin_torton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_movin_torton.setIcon(icon11)
        self.btn_movin_torton.setIconSize(QSize(80, 80))

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.btn_movin_torton)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_11.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_21)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_11.setItem(2, QFormLayout.FieldRole, self.verticalSpacer_22)


        self.horizontalLayout_129.addLayout(self.formLayout_11)


        self.verticalLayout_122.addWidget(self.frame_117)

        self.frame_118 = QFrame(self.page_movin)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(0, 100))
        self.frame_118.setMaximumSize(QSize(16777215, 100))
        self.frame_118.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.btn_back_movin = QPushButton(self.frame_118)
        self.btn_back_movin.setObjectName(u"btn_back_movin")
        self.btn_back_movin.setMinimumSize(QSize(200, 70))
        self.btn_back_movin.setMaximumSize(QSize(200, 70))
        self.btn_back_movin.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_movin.setIcon(icon9)
        self.btn_back_movin.setIconSize(QSize(80, 70))

        self.horizontalLayout_95.addWidget(self.btn_back_movin)


        self.horizontalLayout_127.addLayout(self.horizontalLayout_95)


        self.verticalLayout_122.addWidget(self.frame_118)

        self.stackedWidget.addWidget(self.page_movin)
        self.page_menu_devolucion = QWidget()
        self.page_menu_devolucion.setObjectName(u"page_menu_devolucion")
        self.verticalLayout_125 = QVBoxLayout(self.page_menu_devolucion)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.frame_119 = QFrame(self.page_menu_devolucion)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 70))
        self.frame_119.setMaximumSize(QSize(16777215, 70))
        self.frame_119.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_119)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_126 = QVBoxLayout()
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.label_44 = QLabel(self.frame_119)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_44)


        self.verticalLayout_127.addLayout(self.verticalLayout_126)


        self.verticalLayout_125.addWidget(self.frame_119)

        self.frame_120 = QFrame(self.page_menu_devolucion)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_12.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_12.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_12.setHorizontalSpacing(60)
        self.formLayout_12.setVerticalSpacing(60)
        self.btn_dev_decliente = QPushButton(self.frame_120)
        self.btn_dev_decliente.setObjectName(u"btn_dev_decliente")
        self.btn_dev_decliente.setMinimumSize(QSize(300, 100))
        self.btn_dev_decliente.setMaximumSize(QSize(300, 100))
        self.btn_dev_decliente.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_dev_decliente.setIcon(icon8)
        self.btn_dev_decliente.setIconSize(QSize(80, 80))

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.btn_dev_decliente)

        self.btn_dev_aprov = QPushButton(self.frame_120)
        self.btn_dev_aprov.setObjectName(u"btn_dev_aprov")
        self.btn_dev_aprov.setMinimumSize(QSize(300, 100))
        self.btn_dev_aprov.setMaximumSize(QSize(300, 100))
        self.btn_dev_aprov.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_dev_aprov.setIcon(icon5)
        self.btn_dev_aprov.setIconSize(QSize(80, 80))

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.btn_dev_aprov)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_12.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_23)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_12.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_24)


        self.horizontalLayout_128.addLayout(self.formLayout_12)


        self.verticalLayout_125.addWidget(self.frame_120)

        self.frame_121 = QFrame(self.page_menu_devolucion)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(0, 100))
        self.frame_121.setMaximumSize(QSize(16777215, 100))
        self.frame_121.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.btn_back_devoluciones = QPushButton(self.frame_121)
        self.btn_back_devoluciones.setObjectName(u"btn_back_devoluciones")
        self.btn_back_devoluciones.setMinimumSize(QSize(200, 70))
        self.btn_back_devoluciones.setMaximumSize(QSize(200, 70))
        self.btn_back_devoluciones.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_back_devoluciones.setIcon(icon9)
        self.btn_back_devoluciones.setIconSize(QSize(80, 70))

        self.horizontalLayout_130.addWidget(self.btn_back_devoluciones)


        self.horizontalLayout_131.addLayout(self.horizontalLayout_130)


        self.verticalLayout_125.addWidget(self.frame_121)

        self.stackedWidget.addWidget(self.page_menu_devolucion)
        self.page_devolucion_Cliente_TorTra = QWidget()
        self.page_devolucion_Cliente_TorTra.setObjectName(u"page_devolucion_Cliente_TorTra")
        self.verticalLayout_128 = QVBoxLayout(self.page_devolucion_Cliente_TorTra)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.frame_122 = QFrame(self.page_devolucion_Cliente_TorTra)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 70))
        self.frame_122.setMaximumSize(QSize(16777215, 70))
        self.frame_122.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_122)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_130 = QVBoxLayout()
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.label_45 = QLabel(self.frame_122)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_130.addWidget(self.label_45)


        self.verticalLayout_131.addLayout(self.verticalLayout_130)


        self.verticalLayout_128.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.page_devolucion_Cliente_TorTra)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.formLayout_13 = QFormLayout()
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_13.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_13.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_13.setHorizontalSpacing(60)
        self.formLayout_13.setVerticalSpacing(60)
        self.btn_devclient_torton = QPushButton(self.frame_123)
        self.btn_devclient_torton.setObjectName(u"btn_devclient_torton")
        self.btn_devclient_torton.setMinimumSize(QSize(300, 100))
        self.btn_devclient_torton.setMaximumSize(QSize(300, 100))
        self.btn_devclient_torton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devclient_torton.setIcon(icon11)
        self.btn_devclient_torton.setIconSize(QSize(80, 80))

        self.formLayout_13.setWidget(1, QFormLayout.LabelRole, self.btn_devclient_torton)

        self.btn_devclient_trailer = QPushButton(self.frame_123)
        self.btn_devclient_trailer.setObjectName(u"btn_devclient_trailer")
        self.btn_devclient_trailer.setMinimumSize(QSize(300, 100))
        self.btn_devclient_trailer.setMaximumSize(QSize(300, 100))
        self.btn_devclient_trailer.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devclient_trailer.setIcon(icon12)
        self.btn_devclient_trailer.setIconSize(QSize(80, 80))

        self.formLayout_13.setWidget(1, QFormLayout.FieldRole, self.btn_devclient_trailer)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_13.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_25)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_13.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_26)


        self.horizontalLayout_132.addLayout(self.formLayout_13)


        self.verticalLayout_128.addWidget(self.frame_123)

        self.frame_124 = QFrame(self.page_devolucion_Cliente_TorTra)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(0, 100))
        self.frame_124.setMaximumSize(QSize(16777215, 100))
        self.frame_124.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.btn_devcliente_regresar = QPushButton(self.frame_124)
        self.btn_devcliente_regresar.setObjectName(u"btn_devcliente_regresar")
        self.btn_devcliente_regresar.setMinimumSize(QSize(0, 70))
        self.btn_devcliente_regresar.setMaximumSize(QSize(200, 70))
        self.btn_devcliente_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devcliente_regresar.setIcon(icon9)
        self.btn_devcliente_regresar.setIconSize(QSize(80, 70))

        self.horizontalLayout_133.addWidget(self.btn_devcliente_regresar)


        self.horizontalLayout_134.addLayout(self.horizontalLayout_133)


        self.verticalLayout_128.addWidget(self.frame_124)

        self.stackedWidget.addWidget(self.page_devolucion_Cliente_TorTra)
        self.page_devolucion_Proveedor_TorTra = QWidget()
        self.page_devolucion_Proveedor_TorTra.setObjectName(u"page_devolucion_Proveedor_TorTra")
        self.verticalLayout_129 = QVBoxLayout(self.page_devolucion_Proveedor_TorTra)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.frame_125 = QFrame(self.page_devolucion_Proveedor_TorTra)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(0, 70))
        self.frame_125.setMaximumSize(QSize(16777215, 70))
        self.frame_125.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_125)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_132 = QVBoxLayout()
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.label_46 = QLabel(self.frame_125)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_132.addWidget(self.label_46)


        self.verticalLayout_133.addLayout(self.verticalLayout_132)


        self.verticalLayout_129.addWidget(self.frame_125)

        self.frame_126 = QFrame(self.page_devolucion_Proveedor_TorTra)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.formLayout_14 = QFormLayout()
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.formLayout_14.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_14.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_14.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_14.setHorizontalSpacing(60)
        self.formLayout_14.setVerticalSpacing(60)
        self.btn_devprov_torton = QPushButton(self.frame_126)
        self.btn_devprov_torton.setObjectName(u"btn_devprov_torton")
        self.btn_devprov_torton.setMinimumSize(QSize(300, 100))
        self.btn_devprov_torton.setMaximumSize(QSize(300, 100))
        self.btn_devprov_torton.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devprov_torton.setIcon(icon11)
        self.btn_devprov_torton.setIconSize(QSize(80, 80))

        self.formLayout_14.setWidget(1, QFormLayout.LabelRole, self.btn_devprov_torton)

        self.btn_devprov_trailer = QPushButton(self.frame_126)
        self.btn_devprov_trailer.setObjectName(u"btn_devprov_trailer")
        self.btn_devprov_trailer.setMinimumSize(QSize(300, 100))
        self.btn_devprov_trailer.setMaximumSize(QSize(300, 100))
        self.btn_devprov_trailer.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devprov_trailer.setIcon(icon12)
        self.btn_devprov_trailer.setIconSize(QSize(80, 80))

        self.formLayout_14.setWidget(1, QFormLayout.FieldRole, self.btn_devprov_trailer)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_14.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_27)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_14.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_28)


        self.horizontalLayout_135.addLayout(self.formLayout_14)


        self.verticalLayout_129.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.page_devolucion_Proveedor_TorTra)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMinimumSize(QSize(0, 100))
        self.frame_127.setMaximumSize(QSize(16777215, 100))
        self.frame_127.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.btn_devprov_regresar = QPushButton(self.frame_127)
        self.btn_devprov_regresar.setObjectName(u"btn_devprov_regresar")
        self.btn_devprov_regresar.setMinimumSize(QSize(0, 70))
        self.btn_devprov_regresar.setMaximumSize(QSize(200, 70))
        self.btn_devprov_regresar.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_devprov_regresar.setIcon(icon9)
        self.btn_devprov_regresar.setIconSize(QSize(80, 70))

        self.horizontalLayout_136.addWidget(self.btn_devprov_regresar)


        self.horizontalLayout_137.addLayout(self.horizontalLayout_136)


        self.verticalLayout_129.addWidget(self.frame_127)

        self.stackedWidget.addWidget(self.page_devolucion_Proveedor_TorTra)
        self.page_cancelaciones = QWidget()
        self.page_cancelaciones.setObjectName(u"page_cancelaciones")
        self.verticalLayout_134 = QVBoxLayout(self.page_cancelaciones)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.frame_128 = QFrame(self.page_cancelaciones)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(0, 70))
        self.frame_128.setMaximumSize(QSize(16777215, 70))
        self.frame_128.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_128)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_135 = QVBoxLayout()
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.label_47 = QLabel(self.frame_128)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_135.addWidget(self.label_47)


        self.verticalLayout_136.addLayout(self.verticalLayout_135)


        self.verticalLayout_134.addWidget(self.frame_128)

        self.frame_129 = QFrame(self.page_cancelaciones)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_50 = QLabel(self.frame_129)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_50, 1, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 1, 0, 1, 1)

        self.ticket_cancela = QLineEdit(self.frame_129)
        self.ticket_cancela.setObjectName(u"ticket_cancela")
        self.ticket_cancela.setMinimumSize(QSize(300, 50))
        self.ticket_cancela.setMaximumSize(QSize(300, 50))
        self.ticket_cancela.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.ticket_cancela.setAlignment(Qt.AlignCenter)
        self.ticket_cancela.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.ticket_cancela, 2, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_13, 4, 1, 1, 1)

        self.btn_cancela = QPushButton(self.frame_129)
        self.btn_cancela.setObjectName(u"btn_cancela")
        self.btn_cancela.setMinimumSize(QSize(300, 100))
        self.btn_cancela.setMaximumSize(QSize(300, 100))
        self.btn_cancela.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon76 = QIcon()
        icon76.addFile(u":/80x80/icons/80x80/ct-cancelaciones.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancela.setIcon(icon76)
        self.btn_cancela.setIconSize(QSize(80, 80))

        self.gridLayout_2.addWidget(self.btn_cancela, 3, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_14, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 1, 2, 1, 1)


        self.horizontalLayout_145.addLayout(self.gridLayout_2)


        self.horizontalLayout_144.addLayout(self.horizontalLayout_145)


        self.verticalLayout_134.addWidget(self.frame_129)

        self.stackedWidget.addWidget(self.page_cancelaciones)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_158.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.btn_1a)
        QWidget.setTabOrder(self.btn_1a, self.btn_1a_solas)
        QWidget.setTabOrder(self.btn_1a_solas, self.btn_entrada)
        QWidget.setTabOrder(self.btn_entrada, self.btn_salida)
        QWidget.setTabOrder(self.btn_salida, self.btn_interno)
        QWidget.setTabOrder(self.btn_interno, self.btn_devoluciones)
        QWidget.setTabOrder(self.btn_devoluciones, self.btn_back_1p)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(31)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| SIPCASMO", None))
        self.label_user_icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRIMERA PESADA", None))
        self.btn_1a.setText("")
        self.btn_1a_solas.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TORTON/CAJA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CONTENEDORES", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PRIMERA PESADA", None))
        self.btn_entrada.setText(QCoreApplication.translate("MainWindow", u"Entrada ", None))
        self.btn_salida.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.btn_interno.setText(QCoreApplication.translate("MainWindow", u"Interno", None))
        self.btn_devoluciones.setText(QCoreApplication.translate("MainWindow", u"Devoluci\u00f3n", None))
        self.btn_back_1p.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da ENTRADA", None))
        self.btn_1a_compra.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        self.btn_1a_traspaso.setText(QCoreApplication.translate("MainWindow", u"Traspaso", None))
        self.btn_back_1p_menu.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da DE SALIDA", None))
        self.btn_menu_salida.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.btn_menu_salida_traspaso.setText(QCoreApplication.translate("MainWindow", u"Traspaso", None))
        self.btn_regresar_menu_salida.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SELECCIONA TRACTO PARA LA COMPRA", None))
        self.btnPrimeraPesadaCompraTorton.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btnPrimeraPesadaCompraTrailer.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_back_1p_menu_entrada.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SELECIONA TRACTO PARA EL TRASPASO DE SUCURSAL", None))
        self.btnPrimeraPesadaTraspasoTorton.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btnPrimeraPesadaTraspasoTrailer.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_back_1p_menu_entrada_3.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"SELECCIONA EL TRACTO PARA EL TRASPASO A SUCURSAL", None))
        self.btnPrimeraPesadaTraspasoTorton_salida.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btnPrimeraPesadaTraspasoTrailer_salida.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_regresar_menu_traspaso_salida.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SELECCIONA EL TRACTO VENTA A CLIENTE", None))
        self.btnPrimeraPesadaSalidaTorton.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btnPrimeraPesadaSalidaTrailer.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_back_1p_menu_salida_tracto.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RE IMPRESI\u00d3N", None))
        self.btn_reimpresion.setText(QCoreApplication.translate("MainWindow", u"RE IMPRESION", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"REPORTES", None))
        self.pushButton_4.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.pushButton_8.setText("")
        self.btn_ToExcel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.pushButton_9.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SEGUNDA PESADA", None))
        self.btn_analisisSegundaPesada.setText(QCoreApplication.translate("MainWindow", u"Terminar", None))
        self.btn_ActualizaTablaSegunda.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        ___qtablewidgetitem = self.table_2a.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_2a.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"# Ticket", None));
        ___qtablewidgetitem2 = self.table_2a.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PE", None));
        ___qtablewidgetitem3 = self.table_2a.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem4 = self.table_2a.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PLACAS", None));
        ___qtablewidgetitem5 = self.table_2a.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"FECHA", None));
        ___qtablewidgetitem6 = self.table_2a.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        ___qtablewidgetitem7 = self.table_2a.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SOLAS", None));
        ___qtablewidgetitem8 = self.table_2a.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TortonCajaPorta", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destare", None))
        self.btn_destarar.setText(QCoreApplication.translate("MainWindow", u"Destarar", None))
        self.btn_actualizarDestare.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        ___qtablewidgetitem9 = self.tabla_destare.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"# Ticket", None));
        ___qtablewidgetitem10 = self.tabla_destare.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"P. Entrada", None));
        ___qtablewidgetitem11 = self.tabla_destare.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"P. Salida", None));
        ___qtablewidgetitem12 = self.tabla_destare.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"P. Neto", None));
        ___qtablewidgetitem13 = self.tabla_destare.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem14 = self.tabla_destare.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Placas", None));
        ___qtablewidgetitem15 = self.tabla_destare.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem16 = self.tabla_destare.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem17 = self.tabla_destare.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"SOLAS", None));
        ___qtablewidgetitem18 = self.tabla_destare.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"TortonCajaPorta", None));
        ___qtablewidgetitem19 = self.tabla_destare.horizontalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Tipo int", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Calcular Destare", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Primera Pesada", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Segunda Pesada", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Peso Neto", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Yute 1 Kg", None))
        self.yute.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Propileno 0.20 Kg", None))
        self.propileno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Saco de raspa 0.70 Kg", None))
        self.raspa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Super Saco 3 Kg", None))
        self.saco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Forro contenedor 10 Kg", None))
        self.saco10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Tarima 5 Kg", None))
        self.tarima.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Tarima azul chep 25 Kg", None))
        self.chep.setText("")
        self.chep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Tarima reforzada 45 Kg", None))
        self.treforzada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Saco Especial", None))
        self.sacoesp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Tarima Especial", None))
        self.tarimaesp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.btn_regresarTablaDestare.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"DATOS", None))
        self.btn_tracto.setText(QCoreApplication.translate("MainWindow", u"Tracto", None))
        self.btn_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btn_proveedor.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.btn_contenedor.setText(QCoreApplication.translate("MainWindow", u"Contenedor", None))
        self.btn_producto.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.btn_aduana.setText(QCoreApplication.translate("MainWindow", u"Aduana", None))
        self.btn_operador.setText(QCoreApplication.translate("MainWindow", u"Operador", None))
        self.btn_transportista.setText(QCoreApplication.translate("MainWindow", u"Transportista", None))
        self.btn_destinos.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.btn_sucursal.setText(QCoreApplication.translate("MainWindow", u"Sucursal", None))
        self.btn_tarimas.setText(QCoreApplication.translate("MainWindow", u"Embalaje/Tarimas", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"SACOS / TARIMAS", None))
        self.btnActualizaSacoTarima.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        ___qtablewidgetitem20 = self.tabla_sacotarima.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem21 = self.tabla_sacotarima.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem22 = self.tabla_sacotarima.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Peso Kg", None));
        self.btn_refrescarSacoTarima.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da DESTINOS", None))
        self.btnDestinoventas.setText(QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.btnSolas.setText(QCoreApplication.translate("MainWindow", u"SOLAS", None))
        self.btnSifon.setText(QCoreApplication.translate("MainWindow", u"BODEGA/SIFON", None))
        self.btnSucursal.setText(QCoreApplication.translate("MainWindow", u"SUCURSAL", None))
        self.btn_back_menudatos.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da TRACTOS", None))
        self.btn_CajaPorta.setText(QCoreApplication.translate("MainWindow", u"CAJA/PORTA", None))
        self.btn_Tractos.setText(QCoreApplication.translate("MainWindow", u"TRACTOS", None))
        self.btn_TipoTracto.setText(QCoreApplication.translate("MainWindow", u"TIPOS", None))
        self.btn_back_menutracto.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ADUANA", None))
        self.BuscarlineEditAduana.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda de Agencia Aduanal", None))
        self.btnBuscarAduana.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevaAduana.setText(QCoreApplication.translate("MainWindow", u"NUEVO", None))
        self.btnActualizaAduana.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.btnEliminarAduana.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        ___qtablewidgetitem23 = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem24 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Aduana", None));
        self.btn_refrescarAduana.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.BuscarlineEditCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda de Clientes", None))
        self.btnBuscarCliente.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoCliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarCliente.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarCliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem25 = self.tabla_cl.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem26 = self.tabla_cl.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem27 = self.tabla_cl.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"SAP", None));
        self.btn_refrescarCliente.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CONTENEDORES", None))
        self.BuscarlineEditContenedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda de contenedores", None))
        self.btnBuscarContenedor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoContenedor.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarContenedor.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarContenedor.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem28 = self.tabla_con.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem29 = self.tabla_con.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem30 = self.tabla_con.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem31 = self.tabla_con.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Placas Porta", None));
        self.btn_CrudCont_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarContenedor.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TRANSPORTISTA", None))
        self.btnBuscarTransportista.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevaLinea.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarTransportista.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarTransportista.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem32 = self.tabla_tr.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem33 = self.tabla_tr.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.btn_refrescarTransportista.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"OPERADORES", None))
        self.btnBuscarOperador.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoOperador.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarOperador.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarOperador.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem34 = self.tabla_op.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem35 = self.tabla_op.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem36 = self.tabla_op.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Licencia", None));
        ___qtablewidgetitem37 = self.tabla_op.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Vigencia", None));
        ___qtablewidgetitem38 = self.tabla_op.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Celular", None));
        self.btn_refrescarOperador.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.btnBuscarProducto.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoProducto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarProducto.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarProducto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem39 = self.tabla_pro.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem40 = self.tabla_pro.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem41 = self.tabla_pro.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem42 = self.tabla_pro.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Clave SAP", None));
        self.btn_refrescarProducto.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"PROVEEDORES", None))
        self.btnBuscarProveedor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoProveedor.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarProveedor.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarProveedor.setText(QCoreApplication.translate("MainWindow", u"Elminiar", None))
        ___qtablewidgetitem43 = self.tabla_prov.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem44 = self.tabla_prov.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Clave SAP", None));
        ___qtablewidgetitem45 = self.tabla_prov.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.btn_refrescarProveedor.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"SUCURSALES", None))
        self.btnBuscarSucursal.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoSucursal.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarSucursal.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarSucursal.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem46 = self.tabla_su.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem47 = self.tabla_su.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Sucursal", None));
        self.btn_refrescarSucursal.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TRACTOS", None))
        self.btnBuscarTracto.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoTracto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarTracto.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarTracto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem48 = self.tabla_trac.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem49 = self.tabla_trac.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Placas", None));
        ___qtablewidgetitem50 = self.tabla_trac.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem51 = self.tabla_trac.horizontalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Econ\u00f3mico", None));
        ___qtablewidgetitem52 = self.tabla_trac.horizontalHeaderItem(4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem53 = self.tabla_trac.horizontalHeaderItem(5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"L\u00ednea", None));
        self.btn_tracto_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarTracto.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"CAJA / PORTACONTENEDOR", None))
        self.btnBuscarCajaPorta.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoCajaPorta.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarCajaPorta.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarCajaPorta.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem54 = self.tabla_porta.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem55 = self.tabla_porta.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Placas", None));
        ___qtablewidgetitem56 = self.tabla_porta.horizontalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem57 = self.tabla_porta.horizontalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"L\u00ednea Transportista", None));
        self.btn_porta_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarCajaPorta.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TIPOS DE TRACTOS", None))
        self.btnBuscarTipoTracto.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoTipoTracto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarTipoTracto.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarTipoTracto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem58 = self.tabla_tiptrac.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem59 = self.tabla_tiptrac.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        self.btn_tiptrac_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarTipoTracto.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"DESTINOS VENTAS", None))
        self.btnBuscarDestinoVta.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoDestinovta.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarDestinovta.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarDestinovta.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem60 = self.tabla_dv.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem61 = self.tabla_dv.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        self.btn_destinovtas_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarDestinovta.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"DESTINO SOLAS", None))
        self.btnBuscarDestinoSolas.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoDestinosolas.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarDestinosolas.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarDestinosolas.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem62 = self.tabla_dsol.horizontalHeaderItem(0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem63 = self.tabla_dsol.horizontalHeaderItem(1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        self.btn_destinosolas_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarDestinosolas.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"SUCURSAL", None))
        self.btnBuscarDestinoSucursal.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoDestinoSucursal.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarDestinoSucursal.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarDestinoSucursal.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem64 = self.tabla_suc.horizontalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem65 = self.tabla_suc.horizontalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Sucursal", None));
        self.btn_destinosucursal_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarDestinoSucursal.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"SUCURSAL/SIFON/MAQUILA/BODEGA", None))
        self.btnBuscarDestinoSifon.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoDestinoSifon.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarDestinoSifon.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarDestinoSifon.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem66 = self.tabla_sif.horizontalHeaderItem(0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem67 = self.tabla_sif.horizontalHeaderItem(1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        self.btn_destinosifon_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarDestinoSifon.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TIPOS DE CONTENEDOR", None))
        self.btnBuscarTipoCont.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnNuevoTipoCont.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnActualizarTipoCont.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnEliminarTipoCont.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem68 = self.tabla_tcon.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem69 = self.tabla_tcon.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        self.btn_TipoCon_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_refrescarTipoCont.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"MEN\u00da CONTENEDOR", None))
        self.btn_crudContenedor.setText("")
        self.btn_tipoContenedor.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"CONTENEDOR", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TIPO DE CONTENEDOR", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"MOVIMIENTO INTERNO", None))
        self.btn_movin_torton.setText(QCoreApplication.translate("MainWindow", u"Volteo/Torton", None))
        self.btn_back_movin.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Devoluciones Cliente/Proveedor", None))
        self.btn_dev_decliente.setText(QCoreApplication.translate("MainWindow", u"De Cliente", None))
        self.btn_dev_aprov.setText(QCoreApplication.translate("MainWindow", u"A Proveedor", None))
        self.btn_back_devoluciones.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Devoluci\u00f3n de Cliente", None))
        self.btn_devclient_torton.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btn_devclient_trailer.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_devcliente_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Devoluci\u00f3n a Proveedor", None))
        self.btn_devprov_torton.setText(QCoreApplication.translate("MainWindow", u"Torton", None))
        self.btn_devprov_trailer.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.btn_devprov_regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"CANCELACIONES", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.btn_cancela.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.1", None))
    # retranslateUi

