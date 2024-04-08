"""
Copyright 2023-2023 The jdh99 Authors. All rights reserved.
UI模块
Authors: jdh99 <jdh821@163.com>
"""

from PySide6.QtGui import QCloseEvent
from qt_ui import Ui_MainWindow
import sys
import rtt
import re

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
        self.need_connect_jlink_sn = None

        self.actionopen.triggered.connect(self.open_file_dialog)
        self.switch_device.clicked.connect(self.set_debug_device)
        self.jlink_enable.clicked.connect(self.connect)
        self.jlink_list.activated.connect(self.switch_jlink)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "打开文件",
            "",
            "C Files (*.h);All Files (*);",
            options=options,
        )

    def switch_jlink(self):
        self.rtt.close()

    def set_debug_device(self):
        self.rtt.open()
        device_name = self.rtt.jlink_switch_device()
        self.debug_device_name.setText(device_name)

    def connect(self):
        self.rtt.connect_mode(self.mode_list.currentText())
        speed = self.speed_list.currentText()
        if speed != "auto" and speed != "adaptive":
            speed = int(re.findall(r"\d+", speed)[0])
        self.rtt.connect(self.debug_device_name.displayText(), speed)
        print(self.rtt.info())

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()


class jlink_connect_thread(QThread):
    def __init__(self):
        super(jlink_connect_thread, self).__init__()
        self.last_jlink_list = []
        self.last_connect_jlink = str

    def update_jlink_list(self):
        jlink_list = _win.rtt.get_jlink_list()
        if jlink_list != self.last_jlink_list:
            _win.jlink_list.clear()
            if len(jlink_list) == 0:
                _win.jlink_list.addItem("")
            else:
                _win.jlink_list.addItems(jlink_list)
                print(jlink_list)
                for i in range(len(jlink_list)):
                    if jlink_list[i] == self.last_connect_jlink:
                        print("set index", i)
                        _win.jlink_list.setCurrentIndex(i)
        self.last_jlink_list = jlink_list

    def connect_jlink(self):
        if _win.rtt.is_connected() == False and _win.jlink_list.currentText() != "":
            print("connect", _win.jlink_list.currentText())
            _win.rtt.open(_win.jlink_list.currentText())
            self.last_connect_jlink = _win.jlink_list.currentText()

    def run(self):
        while True:
            self.update_jlink_list()
            self.connect_jlink()
            self.msleep(100)


def _ui():
    global _win

    app = QApplication(sys.argv)
    _win = MainForm()
    thread1 = jlink_connect_thread()
    thread1.start()
    _win.show()
    sys.exit(app.exec())
