import numpy as np
# Lista de diametro comerciais para armadura de concreto
bitolas = [5.5,6.3,8.0,10.0,12.5,16.0,20.0,22.5,25.0,32.0]#mm

'''Dimensionando para o Cisalhamento - Modelo I'''

'''INPUT'''
Vsk= 122.6/1.4*10**3#cisalhamento maximo caracteristico
Mk = 112.6*10**3#Momento maximo caracteristico
fck = 25*10**6  #Em MPa
bw  = .2       #Em metros
d   = 0.45      #Depende da altura da viga e do chute quanto a altura da armadura
bitola_estribo = 5 #mm  #Valores de bitola do estribo ficam entre 5 a 8mm, sendo mais comum 5 ou 6.3.
CA  = 50
cobrimento = 0.025


                
''' !!Observacao!! - Se o cortante maximo for no apoio,
    pode-se reduzir seu valor (checar pagina 284 do livro)'''


'''Verificar a biela comprimida'''

Vsd  = Vsk * 1.4
Vrd2 = 0.27*(1-(fck/10.0**6)/250.)*fck*bw*d/1.4
print ' -------Conferindo a biela comprimida ----------'
print 'Resistencia da biela = ', Vrd2,'N'
if Vsd>Vrd2:
    print 'Cisalhamento maior do que resistencia a compressao da biela. Deve-se alterar a dimensao ou material da viga'
else: print 'Vrd2>Vsd - Viga esta ok nesse parametro'
print '------------------------------------------------'
print 

print '''-----------Espacamento dos estribos-------------'''
fyk =CA*10**7
fyd =fyk/1.15
Asw  = 2*(bitola_estribo/1000.)**2*np.pi/4.0

Vrdmin= 0.137*(fck/10.0**6)**(2./3.)*bw*d*10**6
sm = Asw*fyk/(0.2*0.3*bw*(fck/10.0**6)**(2./3.)*10**6) #Espacamento do cisalhamento minimo
print 'Vrmin =',round(Vrdmin,2),'N'

if Vrdmin>Vsd:
    print 'Vrmin > Vsd : Usar tudo minimo!(Cheque se passa do permitido)'
    s = sm
else:
    Vc= 0.6*0.15*(fck/(10**6))**(2./3.)*bw*d*(10**6)
    Vsw = Vsd - Vc
    s   = Asw*0.9*d*fyd/Vsw #Espacamento para Cortante maior que o minimo

if Vrd2*0.67>=Vsd: #Espacamento maximo permitido
    smax = min([0.6*d,.30])
else:
    smax = min([0.3*d,.20])

if s>smax:
    s=smax


print 'Espacamento para Armadura Minima',round(sm*100,2),'cm'
print 'Espacamento Maximo Permitido',round(smax*100,2),'cm'
print '***************'
print 'Espacamento para o Cortante Maximo',round(s*100,2),'cm'
print 'Comprimento unitario do estribo de gancho a 90graus =',((bw-2*cobrimento)*2+d*2+0.14)*100,'cm'
print 'Lembrar que os estribos nao entram nas vigas!!!'
print 'Subtrair as paredes quando for estimar a quantidade de estribos'
