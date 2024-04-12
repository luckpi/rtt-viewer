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
    Signal,
    Slot,
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
        self.last_connect_jlink = []
        self.jlink_is_need_connect = False

        self.actionopen.triggered.connect(self.open_file_dialog)
        self.switch_device.clicked.connect(self.set_debug_device)
        self.jlink_enable.clicked.connect(self.connect)
        self.jlink_list.activated.connect(self.switch_jlink)
        self.recv_clean.clicked.connect(self.recv_window_clear)
        self.setup_thread()

    def open_file_dialog(self):
        options = QFileDialog.Option()
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "打开文件",
            "",
            "C Files (*.h);All Files (*);",
            options=options,
        )

    def switch_jlink(self):
        self.jlink_connect = False

    def set_debug_device(self):
        device_name = self.rtt.switch_device()
        self.debug_device_name.setText(device_name)

    def connect(self):
        self.rtt.set_connect_mode(self.mode_list.currentText())
        speed = self.speed_list.currentText()
        if speed != "auto" and speed != "adaptive":
            speed = int(re.findall(r"\d+", speed)[0])
        self.rtt.connect(self.debug_device_name.displayText(), speed)
        if self.rtt.is_connected() == False:
            raise Exception("connect failed")
        self.rtt.start(self.rtt_address.displayText())

    def setup_thread(self):
        self.rtt_thread = rtt_thread(self.rtt)
        self.rtt_thread.start()
        self.rtt_thread.recv_add_signal.connect(self.rtt_recv_add)
        self.rtt_thread.update_jlink_list_signal.connect(self.update_jlink_list)
        self.rtt_thread.connect_jlink_signal.connect(self.connect_jlink)

    def recv_window_clear(self):
        self.recv_window.clear()
        self.recv_window.clearHistory()
        self.recv_window.clearFocus()

    @Slot(str)
    def rtt_recv_add(self, string):
        self.recv_window.append(string)
        self.recv_window.ensureCursorVisible()

    @Slot(list)
    def update_jlink_list(self, jlink_list):
        self.jlink_list.clear()
        self.jlink_list.addItems(jlink_list)
        for index in range(len(jlink_list)):
            if jlink_list[index] == self.last_connect_jlink:
                self.jlink_list.setCurrentIndex(index)

    @Slot(str)
    def connect_jlink(self, sn):
        self.jlink_connect = True
        self.last_connect_jlink = sn
        print("connect jlink: ", sn)

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()


class rtt_thread(QThread):
    recv_add_signal = Signal(str)
    update_jlink_list_signal = Signal(list)
    connect_jlink_signal = Signal(str)

    def __init__(self, rtt: rtt.RTT):
        super(rtt_thread, self).__init__()
        self.rtt = rtt
        self.last_jlink_list = list

    def check_jlink(self):
        jlink_list = self.rtt.get_jlink_list()
        if jlink_list != self.last_jlink_list:
            self.update_jlink_list_signal.emit(jlink_list)
        self.last_jlink_list = jlink_list

    def connect_jlink(self):
        if (
            self.rtt.is_connected() == False or _win.jlink_connect == False
        ) and _win.jlink_list.currentText() != "":
            connect_jlink_sn = _win.jlink_list.currentText()
            self.rtt.open(connect_jlink_sn)
            self.connect_jlink_signal.emit(connect_jlink_sn)

    def rtt_read(self):
        if self.rtt.target_connected() == True:
            string = bytes(self.rtt.read(0, 128)).decode("ascii")
            self.recv_add_signal.emit(string)

    def run(self):
        while True:
            self.check_jlink()
            self.connect_jlink()
            self.rtt_read()
            self.msleep(1)


def _ui():
    global _win

    app = QApplication(sys.argv)
    _win = MainForm()
    _win.show()
    sys.exit(app.exec())
