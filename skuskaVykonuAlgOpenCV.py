import matplotlib.image as mpimg
import time
import cv2
import numpy as np

img = mpimg.imread('hrany.jpg')
img = np.asarray(img)

start_time = time.time()

for i in range(1000):
        
    #implementacia kniznice openCV pre python: trvala okolo 2.1438 sek.
    edges = cv2.Canny(img,385,460)

print("--- %s seconds ---" % (time.time() - start_time))