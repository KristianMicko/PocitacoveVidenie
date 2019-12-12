import gradient_calculation
import hysteresis
import Noise_reduction
import nonmaxsuppression
import threshold
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def detect(img):
	img = rgb2gray(img)
	kernel = Noise_reduction.gaussian_kernel(3)
	img = Noise_reduction.convolution(img,kernel)
	gradientMat, thetaMat= gradient_calculation.sobel_filters(img)
	img = nonmaxsuppression.non_max_suppression(gradientMat, thetaMat)
	img,weak,strong = threshold.threshold(img)
	img = hysteresis.hysteresis(img,weak,strong)
	return img

img = mpimg.imread('hrany.jpg')
img = np.asarray(img)

start_time = time.time()

for i in range(1000):
    #vlastna implementacia: trvala okolo 8176.323413610458 sek.
    img = detect(img)
    


print("--- %s seconds ---" % (time.time() - start_time))

