import numpy as np


class Viga():
    def __init__(self,h,bw,fck=25,CA=50,d=False,Ey = 210*10**9):
        '''
        VIGA: Propriedades
        ==================
        INPUT:
            h         = altura da viga em centimetros
            d         = distancia entre topo da viga e centroide da armadura
            bw        = espessura em centimetros
            fck       = resistencia caracteristica do concreto (MPa)
            CA        = resistencia do aco (10MPa)
            Ey        = modulo de elasticidade do aco
            
        STORED:
            h         = altura da viga em metros
            bw        = largura da viga em metros
            fyk       = resistencia caracteristica do aco
            fyd       = resistencia de projeto do aco
            fcd       = resitencia de projeto do concreto
            Ecs       = modulo de elasticidade secante do concreto - formula empirica
            eyd       = deformacao de escoamento de projeto do aco - caso deforme mais que esse valor
                        o aco ira comecar a escoar.
            Asmax     = area maxima de aco para viga simples (cm2)
            Asmin     = area minima de aco para viga simples (cm2)
            
            Obs: Os valores de projeto sao encontrados atraves de fatores de minoracao e majoracao de carga.
                 Nesse programa adotacao os valores prescritos na NBR 6118:2014
                 Para concreto utiliza-se 1.4 e para o aco 1.15
            
        '''
        self.h      = h/100.0
        self.d      = (h-6.0)/100.0
        self.bw     = bw/100.0
        self.fyk    = CA*10.0**7
        self.fyd    = self.fyk/1.15
        self.fcd    = fck/1.4*10**6
        self.Ecs    = 0.85*5600*((fck*10**(-6))**0.5)*10**6
        self.eyd    = self.fyd/Ey
        self.Asmin=0.0015*self.h*self.bw*10**4
        self.Asmax=0.04*self.h*self.bw*10**4
        
    def Dimensionar(self,Mk,Md=False):
        '''
        DIMENSIONAR: Essa funcao faz o dimensionamento da armadura da viga simples.
        
        INPUT:
            Mk         = Momento Caracteristico maximo atuando na viga
            Md         = Momento de Projeto maximo atuando na viga
        
        STORED:
            As         = area de aco na viga (cm2)
            Asl        = area de aco superior (cm2)
            dominio    = dominio de deformacao
            Md         = momento de projeto
        '''
        
        self.Md       = (Mk*1.4)*1000
        dl       = 0.05
        self.Asl      = 0.0 #Valor de area de armadura superior. O default eh 0.
        
        #Resolvendo para 'x' - eq de 2o grau
        a = -0.272*self.bw*self.fcd
        b = 0.68*self.d*self.bw*self.fcd
        c = -self.Md
        x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        dominio=1
        if x2>self.d or x2<0: x = x1
        
        #Determinando o dominio
        
        if x<=0:dominio=1
        elif x>0 and x<=0.259*self.d: dominio=2
        elif x>0.259*self.d and x<=(0.0035*self.d)/(self.eyd+0.0035): dominio=3
        elif x>(0.0035*self.d)/(self.eyd+0.0035) and x<=self.h: dominio=4
        else: dominio=5
        
        
        #Estimando a area de armadura
        if dominio==4:
            x34 = 0.0035*self.d/(self.eyd+0.0035)
            M34 = (0.85*self.fcd*self.bw*0.8*x34)*(self.d-0.4*x34)
            As34= M34/(self.fyd*(self.d-0.4*x34))
            M2  = self.Md-M34
            esl = 0.35*(x34-dl)/x34 #epsilon` , a deformacao da armadura superior para retirar do dominio 4
            if esl<self.eyd: fsl = self.Ey*esl/1.15
            else: fsl = self.fyd
            self.Asl = M2/((self.d-dl)*fsl)
            self.As  = self.Asl + As34
            
        else:
            self.As = self.Md/(self.fyd*(self.d-0.4*x))
        
            
        self.As     = self.As*10**4
        self.Asl    = self.Asl*10**4
    
    def DimensionarT(self,Mk,bf,hf,Md=False):
        
        '''
        DIMENSIONAR: Essa funcao faz o dimensionamento da armadura da viga simples.
        
        INPUT:
            Mk         = Momento Caracteristico maximo atuando na viga
            Md         = Momento de Projeto maximo atuando na viga
        
        STORED:
            As         = area de aco na viga (cm2)
            Asl        = area de aco superior (cm2)
            dominio    = dominio de deformacao
            Md         = momento de projeto
        '''
        
        self.Md       = (Mk*1.4)*1000  #Momento de projeto
        dl            = 0.05                 #Distancia da armadura superior a face superior da viga
        self.Asl      = 0.0             #Valor de area de armadura superior. O default eh 0.
        hf            = hf/100.
        bf            = bf/100.
        
        #Resolvendo para 'x' considerando somente secao T
        a = -0.272*bf*self.fcd
        b = 0.68*self.d*bf*self.fcd
        c = -self.Md
        x1 = (-b+(b**2-4*a*c)**0.5)/(2.*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2.*a)
        if x2>self.d or x2<0: x = x1
        
        
        if x*0.8>hf:                            #If x>hf, entao a viga eh comprimida alem da sua secao T
            Mf = 0.85*self.fcd*hf*(bf-self.bw)*(self.d-hf/2.0) #Momento resistido pelas abas
            Af = Mf/((self.d-hf/2.0)*self.fyd)            #Area de ferro considerando momento nas abas
            Ma = self.Md-Mf                          #Momento resistido pela alma
            a = -0.272*self.bw*self.fcd
            b = 0.68*self.d*self.bw*self.fcd
            c = -Ma
            x1 = (-b+(b**2-4*a*c)**0.5)/(2.*a)
            x2 = (-b-(b**2-4*a*c)**0.5)/(2.*a)
            if x2>self.d or x2<0: x = x1
            if x<=0:dominio=1
            elif x>0 and x<=0.259*self.d: dominio=2
            elif x>0.259*self.d and x<=(0.0035*self.d)/(self.eyd+0.0035): dominio=3
            elif x>(0.0035*self.d)/(self.eyd+0.0035) and x<=self.h: dominio=4
            else: dominio=5
            if dominio==4:
                x34 = 0.0035*self.d/(self.eyd+0.0035)
                M34 = (0.85*self.fcd*self.bw*0.8*x34)*(self.d-0.4*x34)
                As34= M34/(self.fyd*(self.d-0.4*x34))
                M2  = self.Md-M34
                esl = 0.35*(x34-dl)/x34 #epsilon` , a deformacao da armadura superior para retirar do dominio 4
                if esl<self.eyd: fsl = self.Ey*esl/1.15
                else: fsl = self.fyd
                Asl = M2/((self.d-dl)*fsl)
                Aa  = Asl + As34
            
            else:
                Aa = Ma/(self.fyd*(self.d-0.4*x))
            self.As = Aa + Af
        
        else:
            
            if x<=0:dominio=1
            elif x>0 and x<=0.259*self.d: dominio=2
            elif x>0.259*self.d and x<=(0.0035*self.d)/(self.eyd+0.0035): dominio=3
            elif x>(0.0035*self.d)/(self.eyd+0.0035) and x<=self.h: dominio=4
            else: dominio=5
            
            
            #Estimando a area de armadura
            if dominio==4:
                x34 = 0.0035*self.d/(self.eyd+0.0035)
                M34 = (0.85*self.fcd*bf*0.8*x34)*(self.d-0.4*x34)
                As34= M34/(self.fyd*(self.d-0.4*x34))
                M2  = Md-M34
                esl = 0.35*(x34-dl)/x34 #epsilon` , a deformacao da armadura superior para retirar do dominio 4
                if esl<self.eyd: fsl = self.Ey*esl/1.15
                else: fsl = self.fyd
                self.Asl = M2/((self.d-dl)*fsl)
                self.As  = Asl + As34
                
            else:
                self.As = self.Md/(self.fyd*(self.d-0.4*x))
        self.As     = self.As*10**4     #para cm2
        self.Asl    = self.Asl*10**4    #para cm2
        self.dominio= dominio
                
        
a = Viga(175+6, 18, 26)
a.DimensionarT(10000.0/1.4, 170, 20)

