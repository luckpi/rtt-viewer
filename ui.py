"""
Copyright 2023-2023 The jdh99 Authors. All rights reserved.
UI模块
Authors: jdh99 <jdh821@163.com>
"""

from PySide6.QtGui import QCloseEvent
from qt_ui import Ui_MainWindow
import sys
import rtt

from PySide6.QtCore import (
    QThread,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
)


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.rtt = rtt.RTT()

        self.actionopen.triggered.connect(self.open_file_dialog)
        self.switch_device.clicked.connect(self.set_debug_device)
        self.jlink_enable.clicked.connect(self.connect)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "打开文件",
            "",
            "C Files (*.h);All Files (*);",
            options=options,
        )

    def set_enable(self):
        self.rtt.open()

    def set_debug_device(self):
        self.rtt.open()
        device_name = self.rtt.jlink_switch_device()
        self.debug_device_name.setText(device_name)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.rtt.close()
        event.accept()

    def connect(self):
        self.rtt.connect_mode(self.mode_list.currentText())
        self.rtt.connect(self.debug_device_name.displayText(), self.speed_list.currentText())
        print(self.rtt.info())


class update_jlink_list_thread(QThread):
    def __init__(self):
        super(update_jlink_list_thread, self).__init__()

    def run(self):
        last_jlink_list = []
        while True:
            jlink_list = _win.rtt.get_jlink_list()
            if jlink_list != last_jlink_list:
                _win.jlink_list.clear()
                _win.jlink_list.addItems(jlink_list)
            last_jlink_list = jlink_list
            self.msleep(100)


class jlink_connect_thread(QThread):
    def __init__(self):
        super(jlink_connect_thread, self).__init__()

    def run(self):
        while True:
            if _win.rtt.is_connected() == False and _win.jlink_list.currentText() != "":
                print(_win.rtt.is_connected())
                _win.rtt.open(_win.jlink_list.currentText())
            self.msleep(100)


def _ui():
    global _win

    app = QApplication(sys.argv)
    _win = MainForm()
    thread1 = update_jlink_list_thread()
    thread1.start()
    thread2 = jlink_connect_thread()
    thread2.start()
    _win.show()
    sys.exit(app.exec())
