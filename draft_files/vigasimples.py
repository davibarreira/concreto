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
d   =0.44 # 0.06 eh uma estimativa media da altura do centro de gravidade das armaduras
            # Para lajes d = h - cobrimento - 0.005

dl = 0.05           #Em metros - d' no caso da viga cair no dominio 4 
''' INPUT - End '''


#Calculos iniciais - primeiras variaveis a serem calculadas partindo do input

fyk =CA*10**7
fyd =fyk/1.15 # 1.15 foi o fator de minoracao para o aco
fcd =fck/1.4 # 1.4 foi o fator de minoracao para o concreto
Md  =Mk*1.4
Ecs = 0.85*5600*((fck*10**(-6))**0.5)*10**6
eyd = fyd/Ey
Asmin=0.0015*h*bw
Asmax=0.04*h*bw

#Resolvendo para 'x' - eq de 2o grau
a = -0.272*bw*fcd
b = 0.68*d*bw*fcd
c = -Md
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
if x2>d or x2<0: x = x1



#Determine o dominio

if x<=0:dominio=1
elif x>0 and x<=0.259*d: dominio=2
elif x>0.259*d and x<=(0.0035*d)/(eyd+0.0035): dominio=3
elif x>(0.0035*d)/(eyd+0.0035) and x<=h: dominio=4
else: dominio=5


#Estimando a area de armadura
if dominio==4:
    x34 = 0.0035*d/(eyd+0.0035)
    M34 = (0.85*fcd*bw*0.8*x34)*(d-0.4*x34)
    As34= M34/(fyd*(d-0.4*x34))
    M2  = Md-M34
    esl = 0.35*(x34-dl)/x34 #epsilon` , a deformacao da armadura superior para retirar do dominio 4
    if esl<eyd: fsl = Ey*esl/1.15
    else: fsl = fyd
    Asl = M2/((d-dl)*fsl)
    As  = Asl + As34
    
else:
    As = Md/(fyd*(d-0.4*x))


#Output
print 'Dominio de Deformacao: ',dominio
print 'Area de Aco =',round(As*10**4,2),'cm2'
if dominio==4: print 'Area de Aco Superior',round(Asl*10**4,2),'cm2'
print 'Area minima de Aco =',round(Asmin*10**4,2),'cm2  - 0,15% da Area de Concreto'
print 'Area maxima de Aco =',round(Asmax*10**4,2),'cm2  - 4,00% da Area de Concreto'

