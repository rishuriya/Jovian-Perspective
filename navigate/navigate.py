
from PyQt6 import QtCore, QtGui, QtWidgets

class Edit:
    
    def img_saved(self,Form,pfile,fname,counter):
        from Home import Ui_Form
        self.window=QtWidgets.QWidget()
        print(pfile)
        self.ui=Ui_Form()
        self.ui.setupUi(self.window,pfile,fname,counter)
        Form.hide()
        self.window.show()
    
    def img_discarded(self,Form,pfile,fname,counter):
        from Home import Ui_Form
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        pfile=pfile
        print(pfile)
        self.ui.setupUi(self.window,pfile,fname,counter)
        Form.hide()
        self.window.show()