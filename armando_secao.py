import numpy as np

''' Esse programa serve para escolher a armadura que sera usada
    na secao da viga, dada a area de aco ja previamente encontrada
'''


As_calc =5.3 #cm2 - Valor antes de escolher as bitolas
cobrimento =2.5#cm
bit_estribo=5#mm - bitola do estribo
bw = 20

largura_armavel = 20 - 2*(cobrimento+bit_estribo/10.)
print '---Largura disponivel =',largura_armavel
bitolas = np.array([5.5,6.3,8.0,10.0,12.5,16.0,20.0,22.5,25.0,32.0])#mm
areas   = (bitolas/10.0)**2*np.pi/4.0 #cm2 - area de cada bitola
for i in bitolas/10.:
    ah = max([2.,i])
    area = (i)**2*np.pi/4.0
    n_barras = np.ceil(As_calc/area)
    n_inf=np.floor((largura_armavel+ah)/(i+ah))
    print 'Bitola',i*10.,'','| Numero de Barras =',n_barras,'| Quantidade na Primeira camada',n_inf,'| Area Efetiva =',round(n_barras*area,2),'cm2'


