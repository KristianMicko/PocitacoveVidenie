# Experiment

**Hypothesis H0**
stredna a priemerna hodnota vlastnej implementacie a implementacie v openCV su rovnake

**Hypothesis H1**
stredna a priemerna hodnota vlastnej implementacie a implementacie v openCV su odlisne

# Postup riešenia
Na overenie tejto hypotézy bol spravený párový t-test

t.test(x$V1,y$V1, paired = TRUE, conf.level = 0.95)$p.value
Tento príkaz bol vykonaný v Rstudio

# Výsledok
p hodnota= 2.2*10^-16

**Grafy meraní**
![picture](https://github.com/KristianMicko/PocitacoveVidenie/blob/master/images/grafy/Opencv.svg)
![picture](https://github.com/KristianMicko/PocitacoveVidenie/blob/master/images/grafy/Vlastne.svg)

# Vyhodnotenie
Implementácia Cannyho hranového detektora v openCV knižnica je rýchlejšia oproti našej mnohokrát. 
Dôvodom je implementácia knižnice v jazyku C++, ktorý je kompilovaný priamo do strojového kódu a tým pádom je vykonanie kódu omnoho rýchlejšie. 
Náš kód bol implementovaný celý v jazyku python, ktorý je interpretovaným jazykom, to znamená, 
že celý kód sa najprv preloží do jazyka C alebo iného jazyka, v ktorom bol interpreter naprogramovaný 
a až tak potom kompilátor preloží ten kód do strojového kód-u. 
Python využíva aj garbage collector, ktorý sa stará o správu pamäte. 
Tieto faktory spôsobujú značne spomalenie výpočtu nami implementovaných funkcii v našom algoritme. 
Na druhej strane Python je jazykom vysokej úrovne s rozsiahlou podporou knižníc, 
čo znamená, že má veľkú podporu s zaobchádzaním rôznych dátových typov, 
čo zjednodušuje prácu s pomerne rôznymi typmi dát a ich predspracovanie. 
