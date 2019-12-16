# Experiment

**Popis**

V tomto experimente sme porovnávali kvalitu výstupných obrázkov, ktoré prešli cez Canny-ho edge detektor našej vlastnej implementácie, s OpenCV detektorom. Očakávanie bolo, že naša implementácia bude pomalšia a/alebo menej kvalitné vyobrazenie hrán pre všetky vstupné obrázky.



**Priebeh vyhodnotenia**

Vyhodnocovanie prebiehalo vizuálnym porovnaním oboch výsledkov pre každý obrázok na vstupe. Hodnotili sme úspešnosť a kvalitu zobrazených hrán a aj samotný čas, ako dlho algoritmom trvalo celkové vykreslenie.


## Výsledky detekcie hrán

### Pôvodný obrázok

![picture](dama.jpg)


### Vlastná implementácia

![picture](DamaVlastna.jpg)


### Implementácia v OpenCV

![picture](DamaOpenCV.jpg)


### Pôvodný obrázok

![picture](hrany.jpg)


### Vlastná implementácia

![picture](ZabaVlastna.jpg)


### Implementácia v OpenCV

![picture](ZabaOpenCV.jpg)


### Pôvodný obrázok

![picture](lena.jpg)


### Vlastná implementácia

![picture](lenaVlastna.jpg)


### Implementácia v OpenCV

![picture](LenaOpencv.jpg)


### Pôvodný obrázok

![picture](Muz.jpg)


### Vlastná implementácia

![picture](Muz.png)


### Implementácia v OpenCV

![picture](MuzVOpenCV.png)


## Vyhodnotenie
Na základe vizuálneho testu možeme zhodnotiť, že vykreslenie jednoduchých obrázkov prebehlo v obidvoch prípadoch pomerne rovnako, čo sa kvality týka, ale naša implementácia trvala podstatne dlhšie ako vstavaný algoritmus. Pri zložitejších obrázkoch, ktoré obsahujú veľa hrán alebo v prípade fotiek je rozdiel dosť veľký, či už v prípade kvality alebo časovej náročnosti.
