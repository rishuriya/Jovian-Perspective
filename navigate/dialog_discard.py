from PyQt6 import QtCore, QtGui, QtWidgets
import os

from navigate.urls import Url

class Ui_Dialog(object):
    def setupUi(self, Dialog,Form):
        Dialog.setObjectName("Dialog")
        global wid
        wid=Form
        Dialog.resize(401, 163)
        Dialog.setStyleSheet("*{\n"
"background-color:#fff\n"
"}QPushButton{\n"
"background-color:rgb(97, 53, 131)\n"
"}\n"
"QLabel{\n"
"color:rgb(97, 53, 131)\n"
"}"
"QFrame{\n"
"border:none\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 90, 331, 45))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.discard = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.discard.setIcon(icon)
        self.discard.setObjectName("discard")
        self.horizontalLayout.addWidget(self.discard)
        self.discard.clicked.connect(self.closeit)
        self.cancel = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.cancel.setIcon(icon)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.cancel.clicked.connect(self.cancelit)
        self.save = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saveit)
        self.horizontalLayout.addWidget(self.save)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def closeit(self):
        isExist = os.path.exists("Temp/temp.png")
        if isExist==True:
            os.remove("Temp/temp.png")
        QtCore.QCoreApplication.instance().quit()

    def cancelit(self):
        Dialog.hide()

    def saveit(self):
        Url.saveit(self,wid,"Temp/temp.png")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Save Changes in Images"))
        self.label_2.setText(_translate("Dialog", "Your changes will be lost."))
        self.discard.setText(_translate("Dialog", "Discard"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.save.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
