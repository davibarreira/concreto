import numpy

''' Input '''
lx = 4.00       #largura horizontal em metros
ly = 4.00       #comprimento vertical em metros
h  = 0.08       #altura da laje em metros
q  = 6.0*10**3 #carregamento caracteristico atuando na laje (peso, carga acidental, etc)
fck= 20*10**6   #fck em Pa
CA =50          #Tipo do aco
cobrimento=0.020#cobrimento em metros
tipox = 1       #numero de lados engastados na horizontal
tipoy = 0       #numero de lados engastados na vertical

''' Input - end '''

''' Calculos preliminares'''
fyk =CA*10**7
fyd =fyk/1.15 # 1.15 foi o fator de minoracao para o aco
fcd =fck/1.4
lamb=ly/lx    #lambda para Marcus
d   = h - cobrimento - 0.005

''' Calculando Esforcos'''
if tipox == 0:
    alphax=5.0
    mx=8.0
    nx=0.
elif tipox == 1:
    alphax=2.0
    mx=14.22
    nx=8.0
elif tipox == 2:
    alphax=1.0
    mx=24.0
    nx=12.0
    
if tipoy == 0:
    alphay=5.0
    my=8.0
    ny=0.
elif tipoy == 1:
    alphay=2.0
    my=14.22
    ny=8.0
elif tipoy == 2:
    alphay=1.0
    my=24.0
    ny=12.0

ky = 1.0/(1.0+(alphay/alphax)*lamb**4)
kx = 1.0-ky

Mx = (1.0-(20./3.)*kx/(mx*lamb**2))*q*kx*(lx**2)/mx #Momento caracteristico atuante no quinhao horizontal
My = (1.0-(20./3.)*ky*lamb**2/my)*q*ky*(ly**2)/my   #Momento caracteristico atuante no quinhao vertical
Mxd = 1.4*Mx
Myd = 1.4*My
if nx==0: Nx = 0.0
else : Nx  =q*kx*lx**2/nx
if ny==0: Ny = 0.0
else : Ny  =q*ky*ly**2/ny
Nxd = 1.4*Nx
Nyd = 1.4*Ny
print "''''''''''''''' Esforcos na Laje em N*m''''''''''''''''''''''"
print "Mx caracteristico e de projeto = ",round(Mx,2),' ', round(Mxd,2)
print "Nx caracteristico e de projeto = ",round(Nx,2),' ', round(Nxd,2)
print "My caracteristico e de projeto = ",round(My,2),' ', round(Myd,2)
print "Ny caracteristico e de projeto = ",round(Ny,2),' ', round(Nyd,2)
print

'''Reacoes nas Vigas'''

if tipox==1: 
    Pxe = q*kx*lx*5.0/8.0
    Px  = q*kx*lx*3.0/8.0
else:
    Px = q*kx*lx/2.0
    Pxe = 0.0

if tipoy==1: 
    Pye = q*ky*ly*5.0/8.0
    Py  = q*ky*ly*3.0/8.0
else:
    Py = q*ky*ly/2.0
    Pye = 0.0

print "'''''''''''''' Carregamentos nas Vigas ''''''''''''''''"
print 'Px e Pxe =', round(Px,2),' ', round(Pxe,2), 'N/m'
print 'Py e Pye =', round(Py,2),' ', round(Pye,2), 'N/m'
