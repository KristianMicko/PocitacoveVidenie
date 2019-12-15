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
![picture](images/grafy/Opencv.svg)
Conclusion
