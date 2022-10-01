from PyQt6 import QtCore, QtGui, QtWidgets
from sharpness import Ui_Sharpness
from edge import Ui_edge
from colour import Ui_colour
from brightness import Ui_brightness
class Url:
    def sharpness(self,Form,name,counter):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Sharpness()
        self.ui.setupUi(self.window,name,counter)
        Form.hide()
        self.window.show()
    def edge(self,Form,name,counter):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_edge()
        self.ui.setupUi(self.window,name,counter)
        Form.hide()
        self.window.show()
    def brightness(self,Form,name,counter):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_brightness()
        self.ui.setupUi(self.window,name,counter)
        Form.hide()
        self.window.show()
    def colour(self,Form,name,counter):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_colour()
        self.ui.setupUi(self.window,name,counter)
        Form.hide()
        self.window.show()