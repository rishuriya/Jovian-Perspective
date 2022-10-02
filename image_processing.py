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
def RGBvariation(img,rvar=1,gvar=1,bvar=1):
  b,g,r = cv2.split(img)
  r = r*rvar
  
  r = r.astype('uint8')
  g = g*gvar
  
  g = g.astype('uint8')
  b = b*bvar
  
  b = b.astype('uint8')
  out = cv2.merge((b,g,r))
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

def automatic_brightness_and_contrast(image, clip_hist_percent=1):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)
    
    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))
    
    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0
    
    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    
    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    
    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha
    
    '''
    # Calculate new histogram with desired range and show histogram 
    new_hist = cv2.calcHist([gray],[0],None,[256],[minimum_gray,maximum_gray])
    plt.plot(hist)
    plt.plot(new_hist)
    plt.xlim([0,256])
    plt.show()
    '''

    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return auto_result

def gauss_diff(image, kernel_size=5):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    img=np.asarray(image)
    gaussian=np.asarray(gauss)

#subtract blurred image from original, then add to original
    img_unsharp=img+(img-gaussian)
    # diff = cv2.absdiff(gray, gauss)
    return img_unsharp

def equalize_this(image_file, with_plot=False, gray_scale=False):
    image_src = read_this(image_file=image_file, gray_scale=gray_scale)
    if not gray_scale:
        r_image, g_image, b_image = cv2.split(image_src)

        r_image_eq = cv2.equalizeHist(r_image)
        g_image_eq = cv2.equalizeHist(g_image)
        b_image_eq = cv2.equalizeHist(b_image)

        image_eq = cv2.merge((r_image_eq, g_image_eq, b_image_eq))
        cmap_val = None
    else:
        image_eq = cv2.equalizeHist(image_src)
        cmap_val = 'gray'

    # if with_plot:
    #     fig = plt.figure(figsize=(10, 20))

    #     ax1 = fig.add_subplot(2, 2, 1)
    #     ax1.axis("off")
    #     ax1.title.set_text('Original')
    #     ax2 = fig.add_subplot(2, 2, 2)
    #     ax2.axis("off")
    #     ax2.title.set_text("Equalized")

    #     ax1.imshow(image_src, cmap=cmap_val)
    #     ax2.imshow(image_eq, cmap=cmap_val)
    #     return True
    return image_eq