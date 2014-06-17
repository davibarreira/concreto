'''Dimensionamento Longitudinal da Viga'''
import numpy as np

'''INPUT'''
Vsk=75.1/1.4*10**3#cisalhamento maximo caracteristico em N
#Mk = 112.6/1.4*10**3#Momento maximo caracteristico em N*m
fck = 25*10**6  #Em MPa
bw  = .20       #Em metros
d   = 0.45      #Depende da altura da viga e do chute quanto a altura da armadura
CA  = 50
As  =  6.6#cm2 - Area de armadura de flexao
bitola_flexao =  12.5#mm
aderencia = 0   #Boa = 0 , Ruim = 1

momento_no_apoio_extremo = 0 #Condicional do momento no apoio extremo. 0 = Momento Nulo. 1= Momento nao nulo
                             #Na grande maioria das vezes isso eh sempre zero.

barra_apoioext = 3           #Decidir quantas barras levar ate o apoio extremo - testar valores
gancho         = 1           #0=Sem gancho , 1 = com gancho

''' INPUT - End '''
#Msd  = Mk*1.4
Vsd  = Vsk * 1.4
Vc= 0.6*0.15*(fck/(10**6))**(2./3.)*bw*d*(10**6)
fyk =CA*10**7
fyd =fyk/1.15

print Vc
print '''---------Calculando a decalagem----------'''

al = d*(Vsd/(2.0*(Vsd-Vc)))
almin = 0.5*d
almax = d
print 'Decalagem calculada,minima e maxima = al =',round(al,3),' ',round(almin,3),' ',round(almax,3)
if al<almin: al=almin
elif al>almax: al=almax
print 'Decalagem adotada =',al,'m'
print

print '----------Calculando a ancoragem-----------'
if aderencia == 0:fbd = 2.25*1.0*1.0*0.15*(fck/(10**6))**(2./3.)*(10**6)
if aderencia == 1:fbd = 2.25*0.7*1.0*0.15*(fck/(10**6))**(2./3.)*(10**6)

lb = bitola_flexao*fyd/(4*fbd)

print 'Comprimento da Ancoragem =',round(lb/1000.,3),'m'
print 'Para os momentos negativos sobre apoio intermediario'
print 'basta somar decalagem e ancoragem com o comprimento'
print 'obtido pelo grafico.'


print '-----------Calculando ancoragem necessaria -----------'
print 'Forca a ancorar'

Rsd = (al/d)*Vsd    #Desprezando efeito de forcas normais a viga
Ascal = Rsd/fyd*10**4#obter em cm2
print 'Rsd =',Rsd,'N',' ','Ascal =',Ascal,'cm2'
print ''

print 'Armadura imposta'
if momento_no_apoio_extremo==0:
    Asapoio = As/3.0
elif momento_no_apoio_extremo==1:
    Asapoio = As/4.0
print 'Asapoio =',round(Asapoio,2),'cm2'
Asef = barra_apoioext*(bitola_flexao/10.)**2*np.pi/4.0
print 'Asef    =',round(Asef,2),'cm2'

if gancho==0:lbn_calc = 1.0*lb*Ascal/(Asef*10.)     #cm
elif gancho==1:lbn_calc = 0.7*lb*Ascal/(Asef*10.)   #cm

lbn_min = max([0.3*lb/10.,10*bitola_flexao/10.,10.])
print 'Ancoragem necessaria para apoio EXTREMO'
print 'lb_necessario_calculado =',round(lbn_calc,4),'cm'
print 'lb_necessario_minimo =',round(lbn_min,2),'cm'
if lbn_calc<lbn_min: lbn=lbn_min
else: lbn = lbn_calc
print '**************'
print 'lb_necessario =',round(lbn,2),'cm'
print ''
lbn_intermediario=10*bitola_flexao/10. #cm
print 'Ancoragem necessaria para apoio INTERMEDIARIO =',round(lbn_intermediario,2),'cm'
print 'Somente caso tenha apoio intermediario'

