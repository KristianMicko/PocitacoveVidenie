import numpy as np
def gaussian_kernel(size, sigma=1):
    #vypocet velkosti masky
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    #vypocet hodnot matice masky podla gaussovej distribucie
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

def convolution(img, kernel):
    #vypocet velkosti obrazka
    hi, wi= img.shape
    #vypocet velkosti masky
    hk, wk = kernel.shape
    #vytvorenie matice z nul podla velkosti matice povodneho obrazka
    image_padded = np.zeros(shape=(hi + hk - 0, wi + wk - 0))
    #"ponorenie" obrazka "mora" nul
    image_padded[hk//2:-hk//2, wk//2:-wk//2] = img
    #roznasobovanie pixelov obrazka a masky podla predpisu konvolucie
    out = np.zeros(shape=img.shape)
    for row in range(hi):
        for col in range(wi):
            for i in range(hk):
                for j in range(wk):
                    out[row, col] += image_padded[row + i, col + j]*kernel[i, j]
    return out