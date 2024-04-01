"""
Copyright 2023-2023 The jdh99 Authors. All rights reserved.
UI模块
Authors: jdh99 <jdh821@163.com>
"""

import os
import threading

import re
import threading

import sys
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
    QFileDialog,
    QTableWidgetItem,
    QTextBrowser,
    QLineEdit,
)

from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
    QTextDocument,
    QTextCursor,
    QTextCharFormat,
)

from qt_ui import Ui_MainWindow
import sys

from datetime import datetime

_win = None


def parse_c_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    pattern = r"#define\s+(\w+)\s+(.*)"
    matches = re.findall(pattern, content)
    params = {name: value for name, value in matches}
    return params


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.actionopen.triggered.connect(self.open_file_dialog)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "打开文件",
            "",
            "C Files (*.h);All Files (*);",
            options=options,
        )
        if fileName:
            params = parse_c_file(fileName)
            print(params)


def _ui():
    global _win

    app = QApplication(sys.argv)
    _win = MainForm()
    _win.show()
    sys.exit(app.exec())
