from typing import Counter
from PyQt6 import QtCore, QtGui, QtWidgets

import os
from navigate.dialog_discard import Ui_Dialog
from navigate.urls import Url

class Ui_Form(object):
    def setupUi(self, Form,File,Tfile,x):
        global wid
        wid=Form
        global counter
        counter=x
        print(counter)
        Form.setObjectName("Form")
        Form.resize(1200, 796)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1401, 801))
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
"}\n"
"#header{\n"
"text-color:#000;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.original = QtWidgets.QLabel(self.frame)
        self.original.setGeometry(QtCore.QRect(210, 140, 451, 501))
        self.original.setText("")
        self.original.setObjectName("original")

        global fname
        if len(File)==2:
            fname=File[0]
        else:
            fname=File
        print(fname)
        pixmap = QtGui.QPixmap(fname)
        self.original.setPixmap(pixmap)
        self.original.setScaledContents(True)

        self.change = QtWidgets.QLabel(self.frame)
        self.change.setGeometry(QtCore.QRect(710, 140, 451, 501))
        self.change.setText("")
        self.change.setObjectName("change")
        global tname
        tname=Tfile
        global isExist
        isExist = os.path.exists(tname)
        if isExist==True:
            pixmap_change = QtGui.QPixmap(tname)
            print(pixmap_change)
            self.change.setPixmap(pixmap_change)
            self.change.setScaledContents(True)

        self.ui = QtWidgets.QFrame(self.frame)
        self.ui.setGeometry(QtCore.QRect(-10, -10, 201, 801))
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
        self.auto_2.clicked.connect(self.open_autoenhance)
        self.sharpness = QtWidgets.QPushButton(self.ui)
        self.sharpness.setGeometry(QtCore.QRect(40, 210, 121, 61))
        self.sharpness.setObjectName("sharpness")
        self.sharpness.clicked.connect(self.open_Sharpness)
        self.edge = QtWidgets.QPushButton(self.ui)
        self.edge.setGeometry(QtCore.QRect(40, 290, 121, 61))
        self.edge.setObjectName("edge")
        self.edge.clicked.connect(self.open_Edge)
        self.brightness = QtWidgets.QPushButton(self.ui)
        self.brightness.setGeometry(QtCore.QRect(40, 370, 121, 61))
        self.brightness.setObjectName("brightness")
        self.brightness.clicked.connect(self.open_Brightness)
        self.colour = QtWidgets.QPushButton(self.ui)
        self.colour.setGeometry(QtCore.QRect(40, 450, 121, 61))
        self.colour.setObjectName("colour")
        self.colour.clicked.connect(self.open_Colour)
        self.noise = QtWidgets.QPushButton(self.ui)
        self.noise.setGeometry(QtCore.QRect(40, 530, 121, 61))
        self.noise.setObjectName("noise")
        self.noise.clicked.connect(self.open_Noise)
        self.gamma = QtWidgets.QPushButton(self.ui)
        self.gamma.setGeometry(QtCore.QRect(40, 610, 121, 61))
        self.gamma.setObjectName("noise")
        self.gamma.clicked.connect(self.open_Gamma)
        self.logo = QtWidgets.QLabel(self.ui)
        self.logo = QtWidgets.QLabel(self.ui)
        self.logo.setGeometry(QtCore.QRect(50, 20, 100, 100))
        self.logo.setText("")
        self.logo.setObjectName("logo")

        pixmap_logo = QtGui.QPixmap("Resource/space-app.png")
        self.logo.setPixmap(pixmap_logo)
        self.logo.setScaledContents(False)

        self.header = QtWidgets.QFrame(self.frame)
        self.header.setGeometry(QtCore.QRect(199, 10, 991, 61))
        self.header.setStyleSheet("QLabel{\n"
"color:#000;\n"
"    font: 30pt \"Ubuntu Condensed Bold\";\n"
"}")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.share = QtWidgets.QPushButton(self.header)
        self.share.setGeometry(QtCore.QRect(590, 10, 121, 41))
        icon = QtGui.QIcon.fromTheme("emblem-shared")
        self.share.setIcon(icon)
        self.share.setObjectName("share")
        self.share.clicked.connect(self.shar)
        self.discard = QtWidgets.QPushButton(self.header)
        self.discard.setGeometry(QtCore.QRect(720, 10, 121, 41))
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.discard.setIcon(icon)
        self.discard.setObjectName("discard")
        self.discard.clicked.connect(self.closeit)
        self.save = QtWidgets.QPushButton(self.header)
        self.save.setGeometry(QtCore.QRect(850, 10, 121, 41))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saveit)
        self.label = QtWidgets.QLabel(self.header)
        self.label.setGeometry(QtCore.QRect(6, 6, 541, 51))
        self.label.setObjectName("label")
        self.footer = QtWidgets.QFrame(self.frame)
        self.footer.setGeometry(QtCore.QRect(199, 670, 1001, 80))
        self.footer.setStyleSheet("QLabel{\n"
"color:#000\n"
"}")
        self.footer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.footer.setObjectName("footer")
        self.label_2 = QtWidgets.QLabel(self.footer)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.footer)
        self.label_3.setGeometry(QtCore.QRect(600, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.ui.raise_()
        self.original.raise_()
        self.change.raise_()
        self.header.raise_()
        self.footer.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open_autoenhance(self):
        Url.autoenhance(self,wid,fname,counter)

    def open_Sharpness(self):
        Url.sharpness(self,wid,fname,counter)
        
    def open_Brightness(self):
        Url.brightness(self,wid,fname,counter)
        
    def open_Edge(self):
        Url.edge(self,wid,fname,counter)
        
    def open_Colour(self):
        Url.colour(self,wid,fname,counter)

    def open_Noise(self):
        Url.noise(self,wid,fname,counter)

    def open_Gamma(self):
        Url.gamma(self,wid,fname,counter)

    def open_equaliser(self):
        Url.equaliser(self,wid,fname,counter)

    def shar(self):
        print("Hello")
        # code for share
        
    def closeit(self):
        if isExist == True:
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog,wid)
            Dialog.show()
            Dialog.exec()
        else:
            QtCore.QCoreApplication.instance().quit()

    def saveit(self):
        if isExist==True:
            Url.saveit(self,wid,tname)
        else:
            QtCore.QCoreApplication.instance().quit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.auto_2.setText(_translate("Form", "Auto Enhance"))
        self.sharpness.setText(_translate("Form", "Sharpness"))
        self.noise.setText(_translate("Form", "Noise"))
        self.gamma.setText(_translate("Form", "Gamma cor."))
        self.edge.setText(_translate("Form", "Edge"))
        self.brightness.setText(_translate("Form", "Brightness"))
        self.colour.setText(_translate("Form", "Colour"))
        self.discard.setText(_translate("Form", "Discard"))
        self.save.setText(_translate("Form", "Save"))
        self.share.setText(_translate("Form", "Share"))
        self.label.setText(_translate("Form", "Perspective"))
        self.label_2.setText(_translate("Form", "Original Image"))
        if isExist==True:
            self.label_3.setText(_translate("Form", "Processed Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
