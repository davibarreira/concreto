import numpy as np
from matplotlib import pyplot as plt
from FEMsolver import *

'''3) Esforcos na Viga'''

'''Programa baseado no codigo em elementos finitos do 
   Professor Dorival Pedroso para estimar
   os esforcos nas vigas.'''

#Input - Informacoes fornecidas pelo usario
'''
 ____________
/\    /\    /\ 
|---->        
x
Eixo considerado sempre da esquerda para direita
'''

L = 5 #largura total da viga a ser dimensionado
apoios=[[0,'ap'],[2,'ap'],[5,'ap']] #lista das cotas horizontais dos apoios com o tipo ("ap"-apoiado, "en"-engastado)

V = [[0, -101,  0.0, 0.0],
     [1, -102,  4.0, 0.0],
     [2, -103,  8.0, 0.0]]
#id tag verts
C = [[0, -1, [0,1]]]
m = FEMmesh(V, C)
#2) create dictionary with all parameters
p = {-1:{'E':2.0e8, 'A':4.5e-2, 'I':3.375e-4,
         'qnqt':(-20.0,-20.0,0.)}}
# 3) allocate fem solver object
s = FEMsolver(m, 'EelasticBeam', p)
# 4) set boundary conditions
vb = {-101:{'ux':0.0,'uy':0.0,'wz':0.0},
      -102:{'ux':0.0,'uy':0.0,'wz':0.0}}
s.set_bcs(vb=vb)
# 5) solve equilibrium problem
s.solve_steady(True) # True ==> with reactions
# 6) print results
s.print_u(); s.print_e();s.print_r()


# 7) plot bending moments
s.beam_plot();
print s.esvs['M']

m.draw()
m.show()