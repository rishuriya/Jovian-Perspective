# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import numpy as np

from glob import glob

import cv2
import matplotlib.pylab as plt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel
from PyQt6.QtGui import QPixmap,QImage
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
    def greet(self):
        plt.style.use('ggplot')

        #reading Image
        img_files = glob(fname[0])

        img_cv2=cv2.imread(img_files[0])
        img_mpl = plt.imread(img_files[0])

        img_mpl.shape, img_cv2.shape

        #pd.Series(img_mpl.flatten()).plot(kind='hist',bins=50,title='Distribution of Pixel Values')
        #plt.show()

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_title("original image")
        ax.imshow(img_mpl)
        ax.axis('off')
        plt.show()
        #print(len(img_mpl[0][0]))
        # Display RGB Channels of our image
        try:
           print(len(img_mpl[0][0]))
           fig, axs = plt.subplots(1, 3, figsize=(15, 5))
           axs[0].imshow(img_mpl[:,:,0], cmap='Reds')
           axs[1].imshow(img_mpl[:,:,1], cmap='Greens')
           axs[2].imshow(img_mpl[:,:,2], cmap='Blues')
           axs[0].axis('off')
           axs[1].axis('off')
           axs[2].axis('off')
           axs[0].set_title('Red channel')
           axs[1].set_title('Green channel')
           axs[2].set_title('Blue channel')
           plt.show()
        except:
                fig, axs = plt.subplots(1, 3, figsize=(15, 5))
                axs[0].imshow(img_mpl[:,:], cmap='Reds')
                axs[1].imshow(img_mpl[:,:], cmap='Greens')
                axs[2].imshow(img_mpl[:,:], cmap='Blues')
                axs[0].axis('off')
                axs[1].axis('off')
                axs[2].axis('off')
                axs[0].set_title('Red channel')
                axs[1].set_title('Green channel')
                axs[2].set_title('Blue channel')
                plt.show()

        img = plt.imread(img_files[0])

        img_gray = cv2.cvtColor(img_cv2, cv2.COLOR_RGB2GRAY)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(img_gray, cmap='Greys')
        ax.axis('off')
        ax.set_title('Grey Image')
        plt.show()

        #edge_detection
        fig, axs = plt.subplots(figsize=(8, 8))
        edges = cv2.Canny(img_cv2,1,100)
        axs.imshow(edges,cmap = 'gray')
        axs.axis('off')
        plt.show()

        # Different Size
        img_resize = cv2.resize(img, (100, 200))
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(img_resize)
        ax.set_title('Lowered_pixel')
        ax.axis('off')
        plt.show()

        img_resize = cv2.resize(img, (5000, 5000), interpolation = cv2.INTER_CUBIC)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(img_resize)
        ax.set_title('Size_change')
        ax.axis('off')
        plt.show()

        # Sharpen Image
        kernel_sharpening = np.array([[-1,-1,-1],
                                      [-1,9,-1],
                                      [-1,-1,-1]])

        sharpened = cv2.filter2D(img, -1, kernel_sharpening)

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(sharpened)
        ax.axis('off')
        ax.set_title('Sharpened Image')
        plt.show()

        # Blurring the image
        kernel_3x3 = np.ones((3, 3), np.float32) / 9
        blurred = cv2.filter2D(img, -1, kernel_3x3)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(blurred)
        ax.axis('off')
        ax.set_title('Blurred Image')
        plt.show()


        plt.imsave('mpl_.png', blurred)
        cv2.imwrite('cv2_.png', blurred)
    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        self.button1 = self.findChild(QPushButton,"greet")
        self.button1.clicked.connect(self.open_dialog)
        self.button2 = self.findChild(QPushButton,"go")
        self.button2.clicked.connect(self.greet)
        ui_file.close()
    def open_dialog(self):
               global fname
               fname= QFileDialog.getOpenFileName(
                    self,
                    "Open File",
                    "${HOME}",
                    "PNG Files (*.png);;JPG Files (*.jpg);; JPEG Files (*.jpeg);;All Files (*)",
                )
               image=QImage("mpl_.png")
               label=self.findChild(QLabel,"Image")
               print(image)
               pixmap = QPixmap("mpl_.png")
               label.setPixmap(pixmap)
               label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
