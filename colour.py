from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image
import os
import cv2
from navigate.navigate import Edit
import image_processing
class Ui_colour(object):
    
    def setupUi(self,Form,File,x):
        global val
        val=x
        global wid
        wid = Form
        global pfile
        pfile=File
        global name
        name="Temp/colour.png"
        Form.setObjectName("Form")
        Form.resize(889, 612)
        Form.setObjectName("Form")
        Form.resize(889, 612)
        Form.setStyleSheet("*{border:none;\n"
"background-color:#fff;\n"
"color:#000;}\n"
"#ui{\n"
"background-color:rgb(97, 53, 131)\n"
"}\n"
"QPushButton{\n"
"background-color:#071e26;\n"
"color:#fff}")
        global fname
        fname="Temp/temp.png"
        global isExist
        isExist = os.path.exists(fname)
        if isExist==False:
            img = Image.open(File)
            img = img.save(fname)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(738, 4, 121, 41))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.img_save)
        self.discard = QtWidgets.QPushButton(self.frame)
        self.discard.setGeometry(QtCore.QRect(598, 4, 121, 41))
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.discard.setIcon(icon)
        self.discard.setObjectName("discard")
        self.discard.clicked.connect(self.img_discard)
        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setGeometry(QtCore.QRect(6, 6, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 20, 451, 491))
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap(fname)
        print(pixmap)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.ui = QtWidgets.QFrame(self.frame_2)
        self.ui.setGeometry(QtCore.QRect(590, 0, 281, 541))
        self.ui.setStyleSheet("QLabel{\n"
"background-color:rgb(97, 53, 131)}")
        self.ui.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ui.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui.setObjectName("ui")
        self.reset = QtWidgets.QPushButton(self.ui)
        self.reset.setGeometry(QtCore.QRect(80, 310, 131, 41))
        icon = QtGui.QIcon.fromTheme("system-reboot")
        self.reset.setIcon(icon)
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.img_reset)
        self.compare = QtWidgets.QPushButton(self.ui)
        self.compare.setGeometry(QtCore.QRect(78, 384, 131, 41))
        icon = QtGui.QIcon.fromTheme("document-open")
        self.compare.setIcon(icon)
        self.compare.setObjectName("compare")
        self.r_slider = QtWidgets.QSlider(self.ui)
        self.r_slider.setGeometry(QtCore.QRect(50, 50, 16, 211))
        self.r_slider.setSingleStep(5)
        self.r_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.r_slider.setObjectName("r_slider")
        self.r_slider.valueChanged.connect(self.update_image)
        self.textEdit = QtWidgets.QTextEdit(self.ui)
        self.textEdit.setGeometry(QtCore.QRect(40, 270, 41, 31))
        self.textEdit.setStyleSheet("*{\n"
"background-color:rgb(97, 53, 131);\n"
"border-width:10px\n"
"}")
        self.textEdit.setText("0")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.update_r)
        self.textEdit_2 = QtWidgets.QTextEdit(self.ui)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 270, 41, 31))
        self.textEdit_2.setStyleSheet("*{\n"
"background-color:rgb(97, 53, 131);\n"
"border-width:10px\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText("0")
        self.textEdit_2.textChanged.connect(self.update_g)
        self.g_slider = QtWidgets.QSlider(self.ui)
        self.g_slider.setGeometry(QtCore.QRect(130, 50, 16, 211))
        self.g_slider.setSingleStep(5)
        self.g_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.g_slider.setObjectName("g_slider")
        self.g_slider.valueChanged.connect(self.update_image)
        self.textEdit_3 = QtWidgets.QTextEdit(self.ui)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 270, 41, 31))
        self.textEdit_3.setStyleSheet("*{\n"
"background-color:rgb(97, 53, 131);\n"
"border-width:10px\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText("0")
        self.textEdit_3.textChanged.connect(self.update_b)
        self.b_slider = QtWidgets.QSlider(self.ui)
        self.b_slider.setGeometry(QtCore.QRect(210, 50, 16, 211))
        self.b_slider.setSingleStep(5)
        self.b_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.b_slider.setObjectName("b_slider")
        self.b_slider.valueChanged.connect(self.update_image)
        self.r = QtWidgets.QLabel(self.ui)
        self.r.setGeometry(QtCore.QRect(40, 20, 41, 31))
        self.r.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r.setObjectName("r")
        self.g = QtWidgets.QLabel(self.ui)
        self.g.setGeometry(QtCore.QRect(120, 20, 41, 31))
        self.g.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.g.setObjectName("g")
        self.b = QtWidgets.QLabel(self.ui)
        self.b.setGeometry(QtCore.QRect(200, 20, 41, 31))
        self.b.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.b.setObjectName("b")
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def img_reset(self):
        print("reset")
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
        self.verticalSlider.setValue(0)
    def update_r(self):
        change_val_r=self.textEdit.toPlainText()
        change_val_r=int(change_val_r)
        self.r_slider.setValue(change_val_r)

    def update_g(self):
        change_val_g=self.textEdit_2.toPlainText()
        change_val_g=int(change_val_g)
        self.g_slider.setValue(change_val_g)

    def update_b(self):
        change_val_b=self.textEdit_3.toPlainText()
        change_val_b=int(change_val_b)
        self.b_slider.setValue(change_val_b)
    def update_image(self):
        r_value  = self.r_slider.value()
        g_value  = self.g_slider.value()
        b_value  = self.b_slider.value()
        print(r_value,g_value,b_value)
        isThere = os.path.exists(name)
        i = cv2.imread(fname)
        if isThere==False:
            img = Image.open(fname)
            img = img.save(name)
        out = image_processing.RGBvariation(i,r_value,g_value,b_value)
        cv2.imwrite(name,out)
        pixmap = QtGui.QPixmap(name)
        self.textEdit_2.setText(str(g_value))
        self.textEdit_3.setText(str(b_value))
        self.textEdit.setText(str(r_value))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
    def img_save(self):
        img = Image.open(name)
        img = img.save(fname)
        global val
        val=val+1
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
        Edit.img_saved(self,wid,pfile,fname,val)
    def img_discard(self):
        print(val)
        if val==0:
            os.remove(fname)
            print(pfile)
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
        Edit.img_discarded(self,wid,pfile,fname,val)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save.setText(_translate("Form", "Save"))
        self.discard.setText(_translate("Form", "Discard"))
        self.heading.setText(_translate("Form", "Colour"))
        self.reset.setText(_translate("Form", "Reset"))
        self.compare.setText(_translate("Form", "Compare"))
        self.r.setText(_translate("Form", "R"))
        self.g.setText(_translate("Form", "G"))
        self.b.setText(_translate("Form", "B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_colour()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
