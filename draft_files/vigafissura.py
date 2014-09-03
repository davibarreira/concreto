import numpy as np

'''Dimensionamento da armadura para viga de secao retangular'''

'''INPUT'''
bw =0.2             #Em metros
h  =0.5             #Em metros
fck=25*10**6        #Em Pa
CA =50              #
cobrimento = 0.025  #Em metros
estribo    = 0.005  #Em metros
Mk = 94.9/1.4*1000    #Em Newtons.Metros
Ey = 210*10**9      #Em Pa - modulo do aco
d   =0.45 # 0.06 eh uma estimativa media da altura do centro de gravidade das armaduras
            # Para lajes d = h - cobrimento - 0.005
ae  = 8.82
dl  = 0.05           #Em metros - d' no caso da viga cair no dominio 4
As  = 15.75
''' INPUT - End '''

Xln = ae*As/bw*((1+2*bw*d)/(ae*As))**0.5
I2  = bw*Xln**3/12.0 + (bw*Xln)*(Xln/2.0)**2+ae*As*(d-Xln)
I2  = bw*Xln**3/3.0 + ae*As*(d-Xln)**2

