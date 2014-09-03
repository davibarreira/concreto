import numpy as np

'''Dimensionamento da armadura para viga de secao retangular'''

'''INPUT'''
bw =25              #Em cm
h  =80              #Em cm
fck=25              #Em MPa
CA =50              #
Md = 300            #Em kN.m
Ey = 210*10**3      #Em MPa
d   =75.5           #Em cm
ae  = 8.82
As  = 15.75         #Em cm2
bitola  = 20 #mm bitola em analise
ni      = 2.25 #O que eh isso?
pcri    =0.032 #pcri = Asi/Acri o que eh isso?

fctm    = 0.3*fck**(2./3.)
''' INPUT - End '''

Xln = ae*As/bw*(((1+2*bw*d)/(ae*As))**0.5-1)
I2  = bw*Xln**3/12.0 + (bw*Xln)*(Xln/2.0)**2+ae*As*(d-Xln)
I2  = bw*Xln**3/3.0 + ae*As*(d-Xln)**2

print Xln
Fs  = ae*Md*100*(d-Xln)/I2             #Em kN/cm2
print Fs
Fs  = 281.9
wk  = np.array([bitola*Fs*3*Fs/(12.5*ni*Ey*fctm),bitola*Fs*(4./pcri+45)/(12.5*ni*Ey)])
print wk
