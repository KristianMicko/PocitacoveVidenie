import cv2
import numpy as np
import matplotlib.pyplot as plt

#nacitanie obrazka
img = cv2.imread('Muz.jpg')
#pouzitie cannyho detektora hran implementovane v kniznici OpenCV
edges = cv2.Canny(img,297,345)
#nastavenie obrazka na binarnu podobu
plt.imshow(edges,cmap=plt.cm.gray)

plt.show()