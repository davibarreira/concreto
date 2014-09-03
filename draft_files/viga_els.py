import numpy as np
#Analise da viga para estado limite de servico

'''Dimensionamento da armadura para viga de secao retangular'''

'''INPUT'''
bw =25              #Em cm
h  =80              #Em cm
fck=25              #Em MPa
CA =50              #
Ms = 300            #Em kN.m - Momento solicitante sem majoracao
Ey = 210*10**3      #Em MPa
d   =75.5           #Em cm
ae  = 8.82
As  = 15.75         #Em cm2
bitola  = 20 #mm bitola em analise
ni      = 2.25 #O que eh isso?
pcri    =0.032 #pcri = Asi/Acri o que eh isso?

fctm    = 0.3*fck**(2./3.)
''' INPUT - End '''

Mr  = 1.5*fctm*(bw/100.0)*((h/100.0)**3/12.0)/((h/100.)*0.5)

