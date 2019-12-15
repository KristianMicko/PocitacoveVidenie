import gradient_calculation
import hysteresis
import Noise_reduction
import nonmaxsuppression
import threshold
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#premena do sedotonu
def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray
#implementacia finalnej verzie celeho algoritmu Canny Edge Detector do jednej funkcie
def detect(img):
	#premena obrazku z farebneho odtiena do sedotonu
	img = rgb2gray(img)
	#vypocet gaussovej masky
	kernel = Noise_reduction.gaussian_kernel(3)
	#konvolucia obrazka podla masky
	img = Noise_reduction.convolution(img,kernel)
	#vypocet gradientu
	gradientMat, thetaMat= gradient_calculation.sobel_filters(img)
	#detekcia lok extremov
	img = nonmaxsuppression.non_max_suppression(gradientMat, thetaMat)
	#dvojite prahovanie
	img,weak,strong = threshold.threshold(img)
	#detekcia hysteresiou
	img = hysteresis.hysteresis(img,weak,strong)
	#vystupny obrazok
	return img
#importovanie obrazka do programu	
img = mpimg.imread('2.jpg')
img = np.asarray(img)



#vyuzitie nami vytvoreneho algoritmu
img = detect(img)
#nastavenie obrazka na binarnu podobu
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
