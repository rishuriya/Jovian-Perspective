import cv2 
import numpy as np

# to Combine the R, G and B filters (Enter the file names as arguments)
def combineRGB(r,g,b):
  red = cv2.imread(r)
  blue = cv2.imread(g)
  green = cv2.imread(b)
  out = cv2.merge((r,g,b))
  return out

# to get different variations of R, G and B
def RGBvariation(r,g,b,rvar=1,gvar=1,bvar=1):
  r = r*rvar
  
  r = r.astype('uint8')
  g = g*gvar
  
  g = g.astype('uint8')
  b = b*bvar
  
  b = b.astype('uint8')
  out = cv2.merge((r,g,b))
  return out

# To increse the brighness
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# To change the gamma
def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

# To denoise the image
def denoise(img,p3,p4):
  denoise = cv2.fastNlMeansDenoisingColored(img,None,p3,p4,7,21)
  return denoise

# detecting edges using canny edges (the the values of x and y less edges will be visible)
def edgeCanny(img,x,y):
  edge = cv2.Canny(img,x,y)
  return edge

# detecting edges using XSobel (kernel size is a N x N matrix which is used to convolve and detect edges)
def edgeYSobel(img,kernelSize=5):
  y_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=kernelSize)
  return y_sobel

def edgeXSobel(img,kernelSize=5):
  x_sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=kernelSize)
  return x_sobel