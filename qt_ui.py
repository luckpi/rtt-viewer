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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 450)
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
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.recv_window = QTextBrowser(self.widget)
        self.recv_window.setObjectName(u"recv_window")
        self.recv_window.setMinimumSize(QSize(400, 300))

        self.gridLayout.addWidget(self.recv_window, 0, 4, 16, 2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(71, 25))
        self.label_5.setMaximumSize(QSize(71, 25))

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(71, 25))
        self.label.setMaximumSize(QSize(71, 25))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.rtt_address = QLineEdit(self.widget)
        self.rtt_address.setObjectName(u"rtt_address")
        self.rtt_address.setMinimumSize(QSize(100, 25))
        self.rtt_address.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.rtt_address, 4, 1, 1, 2)

        self.send = QPushButton(self.widget)
        self.send.setObjectName(u"send")

        self.gridLayout.addWidget(self.send, 19, 5, 1, 1)

        self.send_clean = QPushButton(self.widget)
        self.send_clean.setObjectName(u"send_clean")

        self.gridLayout.addWidget(self.send_clean, 18, 5, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(71, 25))
        self.label_4.setMaximumSize(QSize(71, 25))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.debug_device_name = QLineEdit(self.widget)
        self.debug_device_name.setObjectName(u"debug_device_name")
        self.debug_device_name.setMinimumSize(QSize(100, 25))
        self.debug_device_name.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.debug_device_name, 3, 1, 1, 2)

        self.recv_clean = QPushButton(self.widget)
        self.recv_clean.setObjectName(u"recv_clean")

        self.gridLayout.addWidget(self.recv_clean, 17, 5, 1, 1)

        self.jlink_enable = QPushButton(self.widget)
        self.jlink_enable.setObjectName(u"jlink_enable")
        self.jlink_enable.setMinimumSize(QSize(177, 35))
        self.jlink_enable.setMaximumSize(QSize(177, 35))

        self.gridLayout.addWidget(self.jlink_enable, 5, 0, 1, 3)

        self.send_text = QTextEdit(self.widget)
        self.send_text.setObjectName(u"send_text")

        self.gridLayout.addWidget(self.send_text, 17, 4, 5, 1)

        self.jlink_list = QComboBox(self.widget)
        self.jlink_list.setObjectName(u"jlink_list")
        self.jlink_list.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.jlink_list, 0, 1, 1, 2)

        self.speed_list = QComboBox(self.widget)
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.addItem("")
        self.speed_list.setObjectName(u"speed_list")
        self.speed_list.setMinimumSize(QSize(100, 25))
        self.speed_list.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.speed_list, 2, 1, 1, 2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(71, 25))
        self.label_2.setMaximumSize(QSize(71, 25))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.switch_device = QPushButton(self.widget)
        self.switch_device.setObjectName(u"switch_device")
        self.switch_device.setMaximumSize(QSize(25, 25))

        self.gridLayout.addWidget(self.switch_device, 3, 3, 1, 1)

        self.port_list = QComboBox(self.widget)
        self.port_list.addItem("")
        self.port_list.addItem("")
        self.port_list.setObjectName(u"port_list")
        self.port_list.setMinimumSize(QSize(100, 25))
        self.port_list.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.port_list, 1, 1, 1, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(71, 25))
        self.label_3.setMaximumSize(QSize(71, 25))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(70, 25))
        self.label_6.setMaximumSize(QSize(70, 25))

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.auto_scroll = QCheckBox(self.widget)
        self.auto_scroll.setObjectName(u"auto_scroll")
        sizePolicy.setHeightForWidth(self.auto_scroll.sizePolicy().hasHeightForWidth())
        self.auto_scroll.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.auto_scroll)

        self.hex_type = QCheckBox(self.widget)
        self.hex_type.setObjectName(u"hex_type")
        sizePolicy.setHeightForWidth(self.hex_type.sizePolicy().hasHeightForWidth())
        self.hex_type.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.hex_type)


        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 1)

        self.recv_stop = QPushButton(self.widget)
        self.recv_stop.setObjectName(u"recv_stop")
        sizePolicy.setHeightForWidth(self.recv_stop.sizePolicy().hasHeightForWidth())
        self.recv_stop.setSizePolicy(sizePolicy)
        self.recv_stop.setMinimumSize(QSize(100, 50))
        self.recv_stop.setMaximumSize(QSize(100, 50))
        self.recv_stop.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.recv_stop, 7, 1, 1, 1)

        MainWindow.setCentralWidget(self.widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RTT \u5730\u5740", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u5668", None))
        self.rtt_address.setText("")
        self.send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.send_clean.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6e05\u7a7a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5\u8bbe\u5907", None))
        self.debug_device_name.setText("")
        self.recv_clean.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u6e05\u7a7a", None))
        self.jlink_enable.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.speed_list.setItemText(0, QCoreApplication.translate("MainWindow", u"auto", None))
        self.speed_list.setItemText(1, QCoreApplication.translate("MainWindow", u"5 kHz", None))
        self.speed_list.setItemText(2, QCoreApplication.translate("MainWindow", u"10 kHz", None))
        self.speed_list.setItemText(3, QCoreApplication.translate("MainWindow", u"20 kHz", None))
        self.speed_list.setItemText(4, QCoreApplication.translate("MainWindow", u"30 kHz", None))
        self.speed_list.setItemText(5, QCoreApplication.translate("MainWindow", u"50 kHz", None))

        self.speed_list.setCurrentText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65b9\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.switch_device.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.switch_device.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.port_list.setItemText(0, QCoreApplication.translate("MainWindow", u"SWD", None))
        self.port_list.setItemText(1, QCoreApplication.translate("MainWindow", u"JTAG", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u901f\u7387", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u8bbe\u7f6e\uff1a", None))
        self.auto_scroll.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6eda\u52a8", None))
        self.hex_type.setText(QCoreApplication.translate("MainWindow", u"\u5341\u516d\u8fdb\u5236", None))
        self.recv_stop.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

