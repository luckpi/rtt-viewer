"""
Copyright 2024 The gumy Authors. All rights reserved.
UI模块
Authors: gumy <ojbk@msn.com>
"""

from qt_ui import Ui_MainWindow
import sys
import rtt
import re

from PySide6.QtGui import (
    QCloseEvent,
    QTextCursor,
)

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

        self.rtt = rtt_object()
        self.last_connect_jlink = ""
        self.jlink_is_need_connect = False
        self.jlink_connect = False

        self.actionopen.triggered.connect(self.open_file_dialog)
        self.switch_device.clicked.connect(self.set_debug_device)
        self.jlink_enable.clicked.connect(self.connect)
        self.jlink_list.activated.connect(self.switch_jlink)
        self.recv_clean.clicked.connect(self.recv_window_clear)
        self.recv_stop.clicked.connect(self.recv_stop_func)
        self.setup_thread()

    def open_file_dialog(self):
        pass

    def switch_jlink(self, index):
        self.rtt.jlink_open_trigger = True
        self.rtt.open_jlink_sn = self.jlink_list.itemText(index)

    def set_debug_device(self):
        self.rtt.jlink_target_switch_device_trigger = True

    def connect(self):
        self.rtt.jlink_target_port = self.mode_list.currentText()

        speed = self.speed_list.currentText()
        if speed != "auto" and speed != "adaptive":
            self.rtt.jlink_target_speed = int(re.findall(r"\d+", speed)[0])
        else:
            self.rtt.jlink_target_speed = speed

        self.rtt.jlink_target_device = self.debug_device_name.text()
        self.rtt.jlink_target_rtt_address = self.rtt_address.displayText()
        self.rtt.jlink_connect_trigger = True
        self.rtt.rtt_recv_enable = True

    def setup_thread(self):
        self.rtt_thread = rtt_thread(self.rtt)
        self.rtt_thread.start()
        self.rtt_thread.recv_add_signal.connect(self.rtt_recv_add)
        self.rtt_thread.update_jlink_list_signal.connect(self.update_jlink_list)
        self.rtt_thread.connect_jlink_signal.connect(self.connect_jlink)
        self.rtt_thread.switch_device_signal.connect(self.switch_device_func)

    def recv_window_clear(self):
        self.recv_window.clear()

    def recv_stop_func(self):
        self.rtt.rtt_recv_enable = not self.rtt.rtt_recv_enable
        self.recv_stop.setText("暂停" if self.rtt.rtt_recv_enable == True else "继续")

    @Slot(str)
    def rtt_recv_add(self, data):
        if self.rtt.rtt_recv_enable == False:
            return
        if self.hex_type.isChecked() == True:
            string = " ".join("{:02x}".format(c) for c in data)
        else:
            string = bytes(data).decode("ascii")

        self.recv_window.append(string)
        if self.auto_scroll.isChecked() == True:
            self.recv_window.moveCursor(self.recv_window.textCursor().MoveOperation.End)

    @Slot(list)
    def update_jlink_list(self, jlink_list, index):
        self.jlink_list.clear()
        self.jlink_list.addItems(jlink_list)
        self.jlink_list.setCurrentIndex(index)

    @Slot(str)
    def connect_jlink(self, sn):
        print("connect jlink: ", sn)

    @Slot(str)
    def switch_device_func(self, device_name):
        self.debug_device_name.setText(device_name)

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()


class rtt_object:
    def __init__(self):
        self.rtt = rtt.RTT()
        self.rtt_recv_enable = False
        self.last_open_jlink_sn = ""
        self.open_jlink_sn = ""
        self.jlink_open_trigger = True
        self.jlink_connect_trigger = False
        self.jlink_target_switch_device_trigger = False
        self.jlink_target_port = ""
        self.jlink_target_speed = ""
        self.jlink_target_rtt_address = ""
        self.jlink_target_device = ""
        self.target_is_connected = False

    def open(self, sn):
        self.rtt.open(sn)

    def get_jlink_list(self):
        return self.rtt.get_jlink_list()

    def connect(self, device, speed):
        self.rtt.connect(device, speed)
    
    def disconnect(self):
        self.rtt.close()

    def start(self, buff_addr):
        self.rtt.start(buff_addr)

    def stop(self):
        self.rtt.stop()

    def is_connected(self):
        return self.rtt.is_connected()

    def set_port(self, port):
        self.rtt.set_connect_mode(port)

    def target_connected(self):
        self.target_is_connected = self.rtt.target_connected()
        return self.target_is_connected

    def read(self, address, size):
        return self.rtt.read(address, size)

    def switch_device(self):
        return self.rtt.switch_device()


class rtt_thread(QThread):
    recv_add_signal = Signal(list)
    update_jlink_list_signal = Signal(list, int)
    connect_jlink_signal = Signal(str)
    switch_device_signal = Signal(str)

    def __init__(self, rtt: rtt_object):
        super(rtt_thread, self).__init__()
        self.rtt = rtt
        self.last_jlink_list = []

    def check_jlink(self):
        jlink_list = self.rtt.get_jlink_list()
        if jlink_list == self.last_jlink_list:
            return
        index = 0
        for index in range(len(jlink_list)):
            if self.rtt.last_open_jlink_sn == "":
                break
            if jlink_list[index] == self.rtt.last_open_jlink_sn:
                break
        self.last_jlink_list = jlink_list
        self.update_jlink_list_signal.emit(jlink_list, index)

    def open_jlink(self):
        if (
            (self.rtt.is_connected() == False or self.rtt.jlink_open_trigger == True)
            and _win.jlink_list.currentText() != ""
            and self.last_jlink_list != []
        ):
            if self.rtt.open_jlink_sn == "" or self.rtt.open_jlink_sn not in self.last_jlink_list:
                self.rtt.open_jlink_sn = self.last_jlink_list[0]
            self.rtt.open(self.rtt.open_jlink_sn)
            self.rtt.last_open_jlink_sn = self.rtt.open_jlink_sn
            self.connect_jlink_signal.emit(self.rtt.open_jlink_sn)

        self.rtt.jlink_open_trigger = False

    def connect_jlink(self):
        if self.rtt.is_connected() == False or self.rtt.jlink_connect_trigger == False:
            self.rtt.jlink_connect_trigger = False
            return
        self.rtt.jlink_connect_trigger = False

        if self.rtt.target_connected() == True:
            self.rtt.stop()
        
        self.rtt.set_port(self.rtt.jlink_target_port)
        self.rtt.connect(self.rtt.jlink_target_device, self.rtt.jlink_target_speed)
        self.rtt.start(self.rtt.jlink_target_rtt_address)

    def switch_device(self):
        if self.rtt.is_connected() == False or self.rtt.jlink_target_switch_device_trigger == False:
            self.rtt.jlink_target_switch_device_trigger = False
            return
        self.rtt.jlink_target_switch_device_trigger = False
        device_name = self.rtt.switch_device()
        self.switch_device_signal.emit(device_name)

    def rtt_read(self):
        if self.rtt.target_connected() == True and self.rtt.rtt_recv_enable == True:
            data = self.rtt.read(0, 4096)
            if len(data) == 0:
                return
            self.recv_add_signal.emit(data)

    def rtt_write(self):
        pass

    def run(self):
        while True:
            self.check_jlink()
            self.open_jlink()
            self.switch_device()
            self.connect_jlink()
            self.rtt_read()
            self.usleep(1)


def _ui():
    global _win

    app = QApplication(sys.argv)
    _win = MainForm()
    _win.show()
    sys.exit(app.exec())
