from PyQt6 import QtCore, QtGui, QtWidgets

from Home import Ui_Form

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setGeometry(QtCore.QRect(-5, -9, 801, 601))
        self.treeView.setObjectName("treeView")
        self.greet = QtWidgets.QPushButton(self.frame)

        self.greet.clicked.connect(self.open_dialog)

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

        self.go.clicked.connect(self.open_home)

        self.go.setGeometry(QtCore.QRect(570, 514, 161, 51))
        self.go.setObjectName("go")
        self.Image = QtWidgets.QLabel(self.frame)
        self.Image.setGeometry(QtCore.QRect(80, 140, 601, 351))
        self.Image.setObjectName("Image")
        self.Image.setText("")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.greet.setText(_translate("Widget", "Select Image"))
        self.label.setText(_translate("Widget", "Explore Jovian System"))
        self.go.setText(_translate("Widget", "Lets Goo -->"))
    def open_home(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        Tfile="Temp/temp.png"
        x=0
        self.ui.setupUi(self.window,fname,Tfile,x)
        Widget.hide()
        self.window.show()
    def open_dialog(self):
            global fname
            fname= QtWidgets.QFileDialog.getOpenFileName(
                    None,
                    "Open File",
                    "${HOME}",
                    "PNG Files (*.png);;JPG Files (*.jpg);; JPEG Files (*.jpeg);;All Files (*)",
                )
            
            pixmap = QtGui.QPixmap(fname[0])
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
