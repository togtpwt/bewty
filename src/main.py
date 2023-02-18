"""
bewty - betty for war thunder
by togtpwt
"""

import json
import requests
import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import *

class Bewty(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("bewty")

        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.mode = QComboBox()
        self.text = QLabel('reehhe')

        self.mode.addItems(["Boeing 7X7", "F/A-18"])

        self.layout.addWidget(self.mode)
        self.layout.addWidget(self.text)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Bewty()
    window.show()

    app.exec()