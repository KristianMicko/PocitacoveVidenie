import numpy as np
#Vyhladavanie lok. extremov 
def non_max_suppression(img, D):
    #zistenie rozmerov obrazka
    M, N = img.shape
    #vytvorenie matice z nul podla rozmerov obrazka
    Z = np.zeros((M,N), dtype=np.int32)
    #zistenie uhla gradientov
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    #vyhladavanie lok. extremov podla orientacie gradientu    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    #navrat obrazka s tensenou hranou
    return Z