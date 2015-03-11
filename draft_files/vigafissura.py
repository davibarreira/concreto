import numpy as np

'''Dimensionamento da armadura para viga de secao retangular'''

'''INPUT'''
bw = 25                                    # Em cm
h  = 80                                    # Em cm
fck= 25                                    # Em MPa
CA = 50                                    #
Md = 300                                   # Em kN.m
Ey = 210*10**3                             # Em MPa
d  = 75.5                                  # Em cm
ae = Ey/(0.85*5600*(fck)**0.5)             # 8.82                   # Relacao entre os modulos de elasticidade (Es/Ec)

bitola  = 20                               # mm bitola em analise
As      = 15.75                            # Em cm2
ni      = 2.25                             # Depende do tipo de aco
pcri    = 0.032                            # pcri = Asi/Acri

fctm    = 0.3*fck**(2./3.)
''' INPUT - End '''

Xln = ae*As/bw*((1+2*bw*d/(ae*As))**0.5-1)
I2  = bw*Xln**3/3.0 + ae*As*(d-Xln)**2

print'I2 = ',I2,'cm4'
print 'xln=', Xln

Fs  = ae*Md*1000*(d-Xln)/I2                # Em kN/mPa

print 'Fs = ',Fs,'kN/cm2'

wk  = np.array([bitola*Fs*3*Fs/(12.5*ni*Ey*fctm),bitola*Fs*(4./pcri+45)/(12.5*ni*Ey)])
print wk


