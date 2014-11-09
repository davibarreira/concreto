import numpy as np

''' Dimensionamento de Pilares Retangulares de acordo com a NBR6118-2013

    Dimensao minima do pilar = 19 cm
    
    |---bw---|
     ________  __       Ma__   
    |        |  |         \ |
    |        |  |h         \|
    |        |  |           |\
    |________| _|_          |_\ Mb
    
    y
    |__x
    
    '''

Nk  = 1072        #kN
Nd  = 1.4*Nk         
fck = 20.            #Mpa
fcd = fck*1000./1.4

CA  = 50.
fyd =CA*10**7/1.15
bw  = 25.           #cm
h   = 70.          #cm
l   = 4.70           #comprimento o pilar (m)
coefapoio = 1.    #coeficiente para comprimento equivalente. 0.5 para biengastado, 0.7 para engaste apoio, 1.0 para biapoiada, 2.0 para balanco
le  = coefapoio*l
Ac  = bw*h/(10**4)

Mdx = 15.3
Mdy = 0 
Max = 15.3          #maior momento absoluto
Mbx = -15.3         #momento no outro extremo
May = 0
Mby = 0


e1x  = Mdx/Nd
e1y  = Mdy/Nd

'''Corrigindo as unidades'''
bw = bw/100.    #m
h  = h/100.     #m



'''Analise na direcao x'''
#Esbeltez
esbx = 3.46*le/bw
if Max ==0: ab = 1.0
else: ab = np.max([0.6 + 0.4*Mbx/Max,0.4])

esb1x=(25.+12.5*e1x/bw)/ab
if   esb1x <= 35. : esb1x=35.
elif esb1x >= 90. : ebs1x=90.

if esbx>esb1x and esbx<=90:
    print 'Pilar medianamente esbelto'
    vx = Nd/(Ac*fcd)
    e2x = np.min([(le**2)/10.*0.005/(bw*(vx+0.5)),(le**2)/10.*0.005/bw])
    
elif esbx<esb1x:
    print 'Pilar curto. Nao tem excentricidade de segunda ordem local'
    e2x = 0.0
else:
    print 'Pilar esbelto. Nao sei ainda como fazer'
    

thetamin =1./300. 
thetamax =1./200.
theta = 1./(100*(le)**0.5)
if theta < thetamin: theta = thetamin
elif theta >thetamax: theta=thetamax

ea_ex = theta*l
ea_cx  = theta*l/2.
e1minx = 0.015 + 0.03*bw

if np.abs(coefapoio-2.0)<0.0001:
    ex = np.max([ea_ex+e1x+e2x,
                 ea_cx+e2x/2.0,
                 e1minx+e2x])

else :
    ex = np.max([ea_ex+e1x,
                 ea_cx+e2x,
                 e1minx+e2x])

Mxd = Nd*ex

vx = Nd/(Ac*fcd)
ux = Nd*ex/(Ac*bw*fcd)

Asmin = np.max([0.15*Nd/fyd,0.004*Ac])


print '----------',u"\u03BBx",'=',esbx
print '----------',u"\u03BB1",'=',esb1x

print '---------- e2x = ',e2x
print '---------- e1x =' ,e1x
print '---------- e1minx = ' ,e1minx
print '---------- ex = ',ex
print '---------- vx = ',vx
print '---------- ux = ',ux
print '---------- Nd = ',Nd
print '---------- Mxd = ',Mxd