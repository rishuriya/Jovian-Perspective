from PyQt6 import QtCore, QtGui, QtWidgets
from glob import glob
import os
from Home import Ui_Form
class Ui_landing(object):
    def setupUi(self, Form):
        img_files = glob('ImageSet/*.png')
        Form.setObjectName("Form")
        Form.resize(1920, 1024)
        if os.path.exists("Temp/temp.png")==True:
            os.remove("Temp/temp.png")
        Form.setStyleSheet("*{\n"
"background-color:#000;\n"
"color:#fff\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.banner = QtWidgets.QFrame(Form)
        self.banner.setMinimumSize(QtCore.QSize(300, 0))
        self.banner.setMaximumSize(QtCore.QSize(300, 16777215))
        self.banner.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.banner.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.banner.setObjectName("banner")
        self.banner_label = QtWidgets.QLabel(self.banner)
        self.banner_label.setGeometry(QtCore.QRect(0, 0, 291, 1001))
        self.banner_label.setText("")
        self.banner_label.setObjectName("banner_label")
        pixmap_banner = QtGui.QPixmap("Resource/banner.png")
        self.banner_label.setPixmap(pixmap_banner)
        self.horizontalLayout.addWidget(self.banner, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 161, 1006))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.banner_label_2 = QtWidgets.QLabel(self.frame)
        self.banner_label_2.setGeometry(QtCore.QRect(0, 10, 151, 1001))
        self.banner_label_2.setText("")
        self.banner_label_2.setObjectName("banner_label_2")
        pixmap_banner_2 = QtGui.QPixmap("Resource/heading.png")
        self.banner_label_2.setPixmap(pixmap_banner_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(159, 0, 901, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 6, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(1090, -10, 501, 1031))
        self.frame_4.setStyleSheet("*{\n"
"background-color:#000\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(36, 31, 49);\n"
"color:#fff\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(90, 720, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(36)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5.setGeometry(QtCore.QRect(20, 240, 461, 471))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.quit = QtWidgets.QPushButton(self.frame_4)
        self.quit.setGeometry(QtCore.QRect(60, 30, 111, 51))
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.quit.setIcon(icon)
        self.quit.setObjectName("quit")
        self.select = QtWidgets.QPushButton(self.frame_4)
        self.select.setGeometry(QtCore.QRect(200, 30, 121, 51))
        icon = QtGui.QIcon.fromTheme("edit-find")
        self.select.setIcon(icon)
        self.select.setObjectName("select")
        self.select.clicked.connect(self.open_dialog)
        self.start = QtWidgets.QPushButton(self.frame_4)
        self.start.setGeometry(QtCore.QRect(350, 30, 111, 51))
        icon = QtGui.QIcon.fromTheme("go-next")
        self.start.setIcon(icon)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.open_home)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(159, 79, 931, 931))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(40, 40, 421, 431))
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap_label_1 = QtGui.QPixmap(img_files[1])
        self.label.setPixmap(pixmap_label_1)
        self.label.setScaledContents(True)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 251, 21))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(500, 40, 421, 431))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        pixmap_label_1 = QtGui.QPixmap(img_files[3])
        self.label_2.setPixmap(pixmap_label_1)
        self.label_2.setScaledContents(True)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(500, 480, 421, 431))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        pixmap_label_1 = QtGui.QPixmap(img_files[9])
        self.label_4.setPixmap(pixmap_label_1)
        self.label_4.setScaledContents(True)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(40, 480, 421, 431))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        pixmap_label_1 = QtGui.QPixmap(img_files[8])
        self.label_3.setPixmap(pixmap_label_1)
        self.label_3.setScaledContents(True)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open_home(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        Tfile="Temp/temp.png"
        x=0
        self.ui.setupUi(self.window,fname,Tfile,x)
        Form.hide()
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
            self.label_5.setPixmap(pixmap)
            self.label_5.setScaledContents(True)
            self.label_5.setStyleSheet("border: 1px solid black;")
            _translate = QtCore.QCoreApplication.translate
            self.label_8.setText(_translate("Form", "Selected Image"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Team Perespective"))
        self.quit.setText(_translate("Form", "Quit"))
        self.select.setText(_translate("Form", "Select Image"))
        self.start.setText(_translate("Form", "Lets Go"))
        self.label_7.setText(_translate("Form", "Junocam Images"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_landing()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
