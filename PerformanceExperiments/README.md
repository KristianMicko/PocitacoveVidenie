Experiment 1.

Hypothesis H0:
stredna hodnota vlastnej implementacie a implementacie v openCV su rovnake

Hypothesis H1:
stredna hodnota vlastnej implementacie a implementacie v openCV su odlisne

Experiment description
Na overenie tejto hypotezy bol spravený párový t-test

Process of validation (can be matlab function and its description) - calculation
t.test(x$V1,y$V1, paired = TRUE, conf.level = 0.95)$p.value
Tento prikaz bol vykonany v Rstudio

Results
p hodnota= 2.2*10^-16
Graph to support my evidence + description
![picture](https://github.com/KristianMicko/PocitacoveVidenie/blob/master/images/grafy/Opencv.svg)
![picture](https://github.com/KristianMicko/PocitacoveVidenie/blob/master/images/grafy/Vlastne.svg)

Conclusion
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