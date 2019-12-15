import numpy as np
import Noise_reduction

def sobel_filters(img):
    #Definovanie matic sobelovej masky
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    #Vypocet konvolucii pixelov obrazu s maskou	
    Ix = Noise_reduction.convolution(img, Kx)
    Iy = Noise_reduction.convolution(img, Ky)
    #Vypocet gradientu jednotlivych suradnic
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    #Vypocet smeru gradientu
    theta = np.arctan2(Iy, Ix)
    return (G, theta)
