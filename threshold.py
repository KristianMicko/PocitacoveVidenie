import numpy as np
def threshold(img,lowThresholdRatio=0.05, highThresholdRatio=0.09):
    #nastavenie dolnych a hornych prahov
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    #zistenie velkosti obrazka a vytvorenie matice z nul podla rozmerov vstupneho obrazka
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    #nastavenie formatu "slabych" a "silnych" pixelov
    weak = np.int32(25)
    strong = np.int32(255)
    #priradenie suradnic silnych pixelov a pixelov, ktore su mimo hran
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    #priradenie suradnic slabych pixelov
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    #vytvorenie matice analyzovaneho obrazka
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    #navrat suradnic z slabymi, silnymi pixelami a ciastocne selektovaneho prahovanim binarneho obrazka
    return (res, weak, strong)