import numpy

#Input
bw =0.20
h  =0.55
fck=25*10**6
CA =50
cobrimento = 0.025
estribo    = 0.006
Mk = 214.37*1000#79.62*10**3
Ey = 210*10**9


#Estimado
Md = Mk*1.4
fcd = fck/1.4
fyk =CA*10**7
fyd =fyk/1.15
eyd = fyd/Ey
xd = (0.0035/(0.0035+eyd))
dmin = (Md/(bw*fcd*(0.68*xd-0.272*xd**2)))**0.5

#Output

print 'Altura minima = ',round(dmin*100,1)