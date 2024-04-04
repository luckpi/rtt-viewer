# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 588)
        self.actiondhgdfh = QAction(MainWindow)
        self.actiondhgdfh.setObjectName(u"actiondhgdfh")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.jlink_enable = QPushButton(self.widget)
        self.jlink_enable.setObjectName(u"jlink_enable")
        self.jlink_enable.setGeometry(QRect(30, 220, 151, 31))
        self.recv_window = QTextBrowser(self.widget)
        self.recv_window.setObjectName(u"recv_window")
        self.recv_window.setGeometry(QRect(210, 10, 601, 341))
        self.recv_window.setMinimumSize(QSize(0, 160))
        self.jlink_list = QComboBox(self.widget)
        self.jlink_list.setObjectName(u"jlink_list")
        self.jlink_list.setGeometry(QRect(90, 20, 91, 22))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 23, 54, 16))
        self.mode_list = QComboBox(self.widget)
        self.mode_list.addItem("")
        self.mode_list.addItem("")
        self.mode_list.setObjectName(u"mode_list")
        self.mode_list.setGeometry(QRect(90, 60, 91, 22))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_list.sizePolicy().hasHeightForWidth())
        self.mode_list.setSizePolicy(sizePolicy)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 63, 54, 16))
        self.speed_list = QComboBox(self.widget)
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.setObjectName(u"speed_list")
        self.speed_list.setGeometry(QRect(90, 100, 91, 22))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 103, 54, 16))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 143, 54, 16))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 183, 54, 16))
        self.send_window = QTextBrowser(self.widget)
        self.send_window.setObjectName(u"send_window")
        self.send_window.setGeometry(QRect(210, 370, 521, 151))
        self.send = QPushButton(self.widget)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(740, 370, 75, 24))
        self.send_clean = QPushButton(self.widget)
        self.send_clean.setObjectName(u"send_clean")
        self.send_clean.setGeometry(QRect(740, 410, 75, 24))
        self.recv_clean = QPushButton(self.widget)
        self.recv_clean.setObjectName(u"recv_clean")
        self.recv_clean.setGeometry(QRect(740, 450, 75, 24))
        self.rtt_address = QLineEdit(self.widget)
        self.rtt_address.setObjectName(u"rtt_address")
        self.rtt_address.setGeometry(QRect(90, 180, 91, 21))
        self.debug_device_name = QLineEdit(self.widget)
        self.debug_device_name.setObjectName(u"debug_device_name")
        self.debug_device_name.setGeometry(QRect(90, 140, 91, 21))
        self.switch_device = QPushButton(self.widget)
        self.switch_device.setObjectName(u"switch_device")
        self.switch_device.setGeometry(QRect(187, 139, 21, 24))
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionsave_as)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RTT Viewer", None))
        self.actiondhgdfh.setText(QCoreApplication.translate("MainWindow", u"dhgdfh", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.jlink_enable.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u5668", None))
        self.mode_list.setItemText(0, QCoreApplication.translate("MainWindow", u"JTAG", None))
        self.mode_list.setItemText(1, QCoreApplication.translate("MainWindow", u"SWD", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65b9\u5f0f", None))
        self.speed_list.setItemText(0, QCoreApplication.translate("MainWindow", u"auto", None))
        self.speed_list.setItemText(1, QCoreApplication.translate("MainWindow", u"5 kHz", None))
        self.speed_list.setItemText(2, QCoreApplication.translate("MainWindow", u"10 kHz", None))
        self.speed_list.setItemText(3, QCoreApplication.translate("MainWindow", u"20 kHz", None))
        self.speed_list.setItemText(4, QCoreApplication.translate("MainWindow", u"30 kHz", None))
        self.speed_list.setItemText(5, QCoreApplication.translate("MainWindow", u"50 kHz", None))

        self.speed_list.setCurrentText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5\u8bbe\u5907", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RTT \u5730\u5740", None))
        self.send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.send_clean.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6e05\u7a7a", None))
        self.recv_clean.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u6e05\u7a7a", None))
        self.rtt_address.setText("")
        self.debug_device_name.setText("")
#if QT_CONFIG(tooltip)
        self.switch_device.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.switch_device.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

