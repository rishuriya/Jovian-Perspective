from cProfile import label
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import date
import os
import numpy as np
import cv2
from Home import Ui_Form
import urllib.request,json
class Ui_landing(object):
    def setupUi(self, Form):
        today=date.today()
        imagename="Resource/{}.png".format(today)
        if os.path.exists("Resource/{}.png".format(today))==False:
                url='https://api.nasa.gov/planetary/apod?api_key=UX6jrk1RJsuJLm8g7zl4FNJdkOnEBB6kNifpJe5B'
                filename="Resource/apod.json"
                today=date.today()
                
#fullpath='{}{}'.format(filepath,filename)
                urllib.request.urlretrieve(url,filename)
                f=open('{}'.format(filename))
                data=json.load(f)
#print(data)
                img_url=data["url"]
        
                urllib.request.urlretrieve('{}'.format(img_url),imagename)
                f.close()
        try:        
                os.mkdir("Temp")
        except:
                i=0
        if os.path.exists("Temp/temp.png")==True:
            os.remove("Temp/temp.png")
        Form.setObjectName("Form")
        Form.resize(1200, 768)
        Form.setStyleSheet("*{\n"
"background-color:Transparent;\n"
"border:None;\n"
"color:#000\n"
"}\n"
"QPushButton{\n"
"color:#000;\n"
"background-color:rgb(36, 31, 49)\n"
"}")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1200, 768))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.banner = QtWidgets.QFrame(self.frame_6)
        self.banner.setGeometry(QtCore.QRect(0, 0, 300, 750))
        self.banner.setMinimumSize(QtCore.QSize(300, 0))
        self.banner.setMaximumSize(QtCore.QSize(300, 16777215))
        self.banner.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.banner.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.banner.setObjectName("banner")
        self.banner_label = QtWidgets.QLabel(self.banner)
        self.banner_label.setGeometry(QtCore.QRect(0, 0, 291, 768))
        self.banner_label.setText("")
        self.banner_label.setObjectName("banner_label")
        pixmap_banner = QtGui.QPixmap("Resource/banner.png")
        self.banner_label.setPixmap(pixmap_banner)
        self.frame = QtWidgets.QFrame(self.frame_6)
        self.frame.setGeometry(QtCore.QRect(310, 0, 161, 768))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.banner_label_2 = QtWidgets.QLabel(self.frame)
        self.banner_label_2.setGeometry(QtCore.QRect(0, 10, 151, 768))
        self.banner_label_2.setText("")
        self.banner_label_2.setObjectName("banner_label_2")
        pixmap_banner_2 = QtGui.QPixmap("Resource/heading.png")
        self.banner_label_2.setPixmap(pixmap_banner_2)
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setGeometry(QtCore.QRect(320, 0, 885, 750))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(140, 0, 501, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 521, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(159, 79, 931, 931))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(70, 0, 251, 21))
        self.label_7.setObjectName("label_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(460, 290, 261, 71))
        self.frame_4.setStyleSheet("*{\n"
"background-color:rgb(97, 53, 131)\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(36, 31, 49);\n"
"color:#fff\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.quit = QtWidgets.QPushButton(self.frame_4)
        self.quit.setGeometry(QtCore.QRect(10, 10, 111, 51))
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.quit.setIcon(icon)
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.closeit)
        self.select = QtWidgets.QPushButton(self.frame_4)
        self.select.setGeometry(QtCore.QRect(130, 10, 121, 51))
        icon = QtGui.QIcon.fromTheme("document-new")
        self.select.setIcon(icon)
        self.select.setObjectName("select")
        self.select.clicked.connect(self.open_dialog)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 768))
        self.label.setText("")
        self.label.setObjectName("label")
        image = cv2.imread(imagename)
        overlay = image.copy()
  
# Rectangle parameters
        x, y, w, h = 0, 0, 1200, 768  
# A filled rectangle
        cv2.rectangle(overlay, (x, y), (x+w, y+h), (256,256,256), -1)  
  
        alpha = 0.6  # Transparency factor.
  
# Following line overlays transparent rectangle
# over the image
        image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
        #cv2.imshow("some", image_new)
        cv2.imwrite("Resource/bg.png", image_new)
        pixmap_label_1 = QtGui.QPixmap("Resource/bg.png")
        self.label.setPixmap(pixmap_label_1)
        self.label.setScaledContents(True)
        self.label.lower()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def closeit(self):
        QtCore.QCoreApplication.instance().quit()

    def open_dialog(self):
            global fname
            fname= QtWidgets.QFileDialog.getOpenFileName(
                    None,
                    "Open File",
                    "${HOME}",
                    "All Files (*);;JPG Files (*.jpg);; JPEG Files (*.jpeg);;PNG Files (*.png)",
                )
            self.window=QtWidgets.QWidget()
            if len(fname)==2:
                self.ui=Ui_Form()
                Tfile="Temp/temp.png"
                x=0
                self.ui.setupUi(self.window,fname,Tfile,x)
                Form.hide()
                self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Perspective"))
        self.label_6.setText(_translate("Form", "Team Perspective"))
        self.label_7.setText(_translate("Form", "Junocam Images"))
        self.quit.setText(_translate("Form", "Quit"))
        self.select.setText(_translate("Form", "Start project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_landing()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
