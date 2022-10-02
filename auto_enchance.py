from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image
import os
import cv2
from navigate.navigate import Edit
import image_processing
class Ui_autoenhance(object):

    def setupUi(self, Form,File,x):
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
        image = cv2.imread(File)
        cv2.imwrite(name,image)
        cv2.imwrite(fname,image)
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
        self.ui = QtWidgets.QFrame(self.frame_2)
        self.ui.setGeometry(QtCore.QRect(590, 0, 281, 541))
        self.ui.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        
        pixmap = QtGui.QPixmap(fname)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
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
        self.enhance_2 = QtWidgets.QPushButton(self.ui)
        self.enhance_2.setGeometry(QtCore.QRect(80, 240, 131, 41))
        icon = QtGui.QIcon.fromTheme("zoom-fit-best")
        self.enhance_2.setIcon(icon)
        self.enhance_2.setObjectName("enhance_2")
        self.enhance_2.clicked.connect(self.img_enhance_2)
        self.enhance_1 = QtWidgets.QPushButton(self.ui)
        self.enhance_1.setGeometry(QtCore.QRect(80, 170, 131, 41))
        icon = QtGui.QIcon.fromTheme("weather-clear")
        self.enhance_1.setIcon(icon)
        self.enhance_1.setObjectName("enhance_1")
        self.enhance_1.clicked.connect(self.img_enhance_1)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def img_reset(self):
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
    
    def img_enhance_1(self):
        i = cv2.imread(name)
        out = image_processing.automatic_brightness_and_contrast(i)
        cv2.imwrite(fname,out)
        pixmap = QtGui.QPixmap(fname)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def img_enhance_2(self):
        out = image_processing.equalize_this(fname)
        cv2.imwrite(name,out)
        pixmap = QtGui.QPixmap(name)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def img_save(self):
        # img = Image.open(name)
        # img = img.save(fname)
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
        self.heading.setText(_translate("Form", "Auto Enhance"))
        self.reset.setText(_translate("Form", "Reset"))
        self.compare.setText(_translate("Form", "Compare"))
        self.enhance_2.setText(_translate("Form", "enhance_2"))
        self.enhance_1.setText(_translate("Form", "enhance_1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_autoenhance()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
