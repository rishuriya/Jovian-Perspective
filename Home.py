from PyQt6 import QtCore, QtGui, QtWidgets
from sharpness import Ui_Sharpness
from edge import Ui_edge
from colour import Ui_colour
from brightness import Ui_brightness

class Ui_Form(object):
    def setupUi(self, Form,File):
        Form.setObjectName("Form")
        Form.resize(1397, 726)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1401, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("*{\n"
"border:none;\n"
"background-color:#fff;\n"
"color:#fff;\n"
"}\n"
"#ui{\n"
"background-color:rgb(97, 53, 131)\n"
"}\n"
"QPushButton{\n"
"background-color:#071e26;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.original = QtWidgets.QLabel(self.frame)
        self.original.setGeometry(QtCore.QRect(210, 90, 451, 501))
        self.original.setText("")
        self.original.setObjectName("original")

        global fname
        fname=File[0]
        pixmap = QtGui.QPixmap(fname)
        print(pixmap)
        self.original.setPixmap(pixmap)
        self.original.setScaledContents(True)

        self.change = QtWidgets.QLabel(self.frame)
        self.change.setGeometry(QtCore.QRect(770, 90, 451, 501))
        self.change.setText("")
        self.change.setObjectName("change")
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(1220, 10, 121, 41))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.discard = QtWidgets.QPushButton(self.frame)
        self.discard.setGeometry(QtCore.QRect(1070, 10, 121, 41))
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.discard.setIcon(icon)
        self.discard.setObjectName("discard")
        self.ui = QtWidgets.QFrame(self.frame)
        self.ui.setGeometry(QtCore.QRect(-10, -10, 201, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.sizePolicy().hasHeightForWidth())
        self.ui.setSizePolicy(sizePolicy)
        self.ui.setStyleSheet("*{\n"
"border:none;\n"
"background-color:rgb(97, 53, 131);\n"
"color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color:#071e26;\n"
"}")
        self.ui.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ui.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui.setObjectName("ui")
        self.auto_2 = QtWidgets.QPushButton(self.ui)
        self.auto_2.setGeometry(QtCore.QRect(40, 130, 121, 61))
        self.auto_2.setObjectName("auto_2")
        self.sharpness = QtWidgets.QPushButton(self.ui)
        self.sharpness.setGeometry(QtCore.QRect(40, 220, 121, 61))
        self.sharpness.setObjectName("sharpness")
        self.sharpness.clicked.connect(self.open_Sharpness)
        self.edge = QtWidgets.QPushButton(self.ui)
        self.edge.setGeometry(QtCore.QRect(40, 310, 121, 61))
        self.edge.setObjectName("edge")
        self.edge.clicked.connect(self.open_Edge)
        self.brightness = QtWidgets.QPushButton(self.ui)
        self.brightness.setGeometry(QtCore.QRect(40, 390, 121, 61))
        self.brightness.setObjectName("brightness")
        self.brightness.clicked.connect(self.open_Brightness)
        self.colour = QtWidgets.QPushButton(self.ui)
        self.colour.setGeometry(QtCore.QRect(40, 480, 121, 61))
        self.colour.setObjectName("colour")
        self.colour.clicked.connect(self.open_Colour)
        self.logo = QtWidgets.QLabel(self.ui)
        self.logo.setGeometry(QtCore.QRect(36, 36, 141, 71))
        self.logo.setText("")
        self.logo.setObjectName("logo")

        pixmap_logo = QtGui.QPixmap("ImageSet/85539b9ed619c9423eec9476d970b93c.jpg")
        print(pixmap)
        self.logo.setPixmap(pixmap_logo)
        self.logo.setScaledContents(True)

        self.ui.raise_()
        self.original.raise_()
        self.change.raise_()
        self.save.raise_()
        self.discard.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open_Sharpness(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Sharpness()
        self.ui.setupUi(self.window,fname)
        self.window.show()
    def open_Brightness(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_brightness()
        self.ui.setupUi(self.window,fname)
        self.window.show()
    def open_Edge(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_edge()
        self.ui.setupUi(self.window,fname)
        self.window.show()
    def open_Colour(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_colour()
        self.ui.setupUi(self.window,fname)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save.setText(_translate("Form", "Save"))
        self.discard.setText(_translate("Form", "Discard"))
        self.auto_2.setText(_translate("Form", "Auto_Enchance"))
        self.sharpness.setText(_translate("Form", "Sharpness"))
        self.edge.setText(_translate("Form", "Edge"))
        self.brightness.setText(_translate("Form", "Brightness"))
        self.colour.setText(_translate("Form", "Colour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
