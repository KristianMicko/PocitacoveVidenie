import cv2
import numpy as np
import matplotlib.pyplot as plt

#nacitanie obrazka
img = cv2.imread('hrany.jpg')
#pouzitie cannyho detektora hran implementovane v kniznici OpenCV
edges = cv2.Canny(img,385,460)
#nastavenie obrazka na binarnu podobu
plt.imshow(edges,cmap=plt.cm.gray)

plt.show()