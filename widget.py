# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from Home import Home
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QDialog, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Start(QWidget):
    global fname
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        self.button1 = self.findChild(QPushButton,"greet")
        self.button1.clicked.connect(self.open_dialog)
        self.button1 = self.findChild(QPushButton,"go")
        self.button1.clicked.connect(self.open_home)
        ui_file.close()
    def open_home(self):
        self.window=QMainWindow()
        self.ui=Home()
        self.ui.load_ui(self.window)
        widget.hide()
        self.window.show()
    def open_dialog(self):

               fname= QFileDialog.getOpenFileName(
                    self,
                    "Open File",
                    "${HOME}",
                    "PNG Files (*.png);;JPG Files (*.jpg);; JPEG Files (*.jpeg);;All Files (*)",
                )
               label=self.findChild(QLabel,"Image")
               pixmap = QPixmap(fname[0])
               print(pixmap)
               label.setPixmap(pixmap)
               label.setScaledContents(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Start()
    widget.show()
    sys.exit(app.exec())

