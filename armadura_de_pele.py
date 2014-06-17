import numpy as np

#input
h = .7
bw = .2
d = h-0.06
bitola = 0.006

#Armadura de pele

Ap = 0.1*h*bw
t  = min([d/3.,0.2,16*bitola])
print t
