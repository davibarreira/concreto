import numpy as np
#Analise da viga para estado limite de servico

'''Dimensionamento da armadura para viga de secao retangular'''

'''INPUT'''
bw =25              #Em cm
h  =80              #Em cm
fck=25              #Em MPa
CA =50              #
Ecs=0.85*5600*fck**0.5

Ms = 300            #Em kN.m - Momento solicitante sem majoracao
Ey = 210*10**3      #Em MPa
d   =75.5           #Em cm
ae  = 8.82
As  = 15.75         #Em cm2
alpha   = 5./48.    #Valor tabelado dependendo do tipo de apoio da viga

l       =8.0    #Em m, comprimento da viga

''' INPUT - End '''

fctm    = 0.3*fck**(2./3.)


Xln = ae*As/bw*(((1+2*bw*d)/(ae*As))**0.5-1)

Ic = (bw*h**3/12.0)/10**8
I2  = (bw*Xln**3/3.0 + ae*As*(d-Xln)**2)/10**8

Mr  = 1.5*fctm*(bw/100.0)*(((h/100.0)**3)/12.0)/((h/100.)*0.5)*1000  #em kN.m - Momento Resistido pelo concreto tracionado

EIeq = Ecs*((Mr/Ms)**3*Ic + (1-(Mr/Ms)**3)*I2)*10**3 #Em kN.m2
print EIeq
fi  = alpha*Ms*l**2/EIeq*100    #Em cm - Flecha imediata
print fi
