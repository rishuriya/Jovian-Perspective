from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, File):
        global fname
        fname=File[0]
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 782, 582))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.greet = QtWidgets.QPushButton(self.frame)
        self.greet.setGeometry(QtCore.QRect(320, 90, 121, 41))
        self.greet.setObjectName("greet")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Z003")
        font.setPointSize(27)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.go = QtWidgets.QPushButton(self.frame)
        self.go.setGeometry(QtCore.QRect(570, 514, 161, 51))
        self.go.setObjectName("go")
        self.Image = QtWidgets.QLabel(self.frame)
        self.Image.setGeometry(QtCore.QRect(80, 140, 601, 351))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setGeometry(QtCore.QRect(-5, -19, 801, 601))
        self.treeView.setObjectName("treeView")
        self.treeView.raise_()
        self.label.raise_()
        self.greet.raise_()
        self.go.raise_()
        self.Image.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.greet.setText(_translate("Form", "Select Image"))
        self.label.setText(_translate("Form", "Explore Jovian System"))
        self.go.setText(_translate("Form", "Lets Goo -->"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
