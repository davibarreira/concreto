'''Dimensionamento de Vigas de Acordo com a NBR6118/2014'''
import numpy as np
from matplotlib import pyplot as plt
from FEMsolver import *




class viga():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def bark(self):
        print self.x,'barks'
        print self.y*2,'+',self.x

mydog = viga('rex',2)
mydog.bark()








# 
# V = [[0, -101,  0.0, 0.0],
#      [1, -101,  6.0, 0.0]]
# #id tag verts
# C = [[0, -1, [0,1]]]
# m = FEMmesh(V, C)
# #2) create dictionary with all parameters
# p = {-1:{'E':2.0e8, 'A':4.5e-2, 'I':3.375e-4,
#          'qnqt':(-20.0,-20.0,0.)}}
# # 3) allocate fem solver object
# s = FEMsolver(m, 'EelasticBeam', p)
# # 4) set boundary conditions
# vb = {-101:{'ux':0.0,'uy':0.0}}
# s.set_bcs(vb=vb)
# # 5) solve equilibrium problem
# s.solve_steady(True) # True ==> with reactions
# # 6) print results
# s.print_u(); s.print_e()
# # 7) plot bending moments
# s.beam_plot();
# print s.esvs['M']
# m.show()
