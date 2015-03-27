import static java.lang.Math.pow;

public class Viga {

    public double h, d,bw,fck,fyk,fyd,fcd,eyd,Asmin,Asmax, Ecs,Ey;
    public double hf   = 0.0;
    public double bf   = 0.0;
    public double As   = 0.0;
    public double Asl  = 0.0;
    public int dominio = 1;
    public double Mk   = 0.0;
    public double Md   = 0.0;
    public double dl;


    public static void main(String[] args){
        System.out.println("h[cm], bw[cm], fck[MPa], CA[10MPa], Ey[GPa?], coe[cm], dl [cm], d[cm]");

        //Teste: Viga retangular simples: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 119: Exemplo 1
        Viga VigaSimples = new Viga();
        VigaSimples.Caracteristicas(30.0,12.0,20.0,50.0,210.0,2.5,2.6,29.0);
        VigaSimples.Dimensionar(12.2);
        System.out.println("Teste: Viga com armadura positiva: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 138: Exemplo 7");
        System.out.println("Dominio = "+VigaSimples.dominio);
        System.out.println("As = " +VigaSimples.As);
        System.out.println("Asl =" + VigaSimples.Asl);
        System.out.println("----------------------------");

        //Teste: Viga com armadura dupla e no dominio 5: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 142: Exemplo 8
        Viga VigaDominio5 = new Viga();
        VigaDominio5.Caracteristicas(30.0,12.0,20.0,50.0,210.0,2.5,2.6,29.0);
        VigaDominio5.Dimensionar(45.0);
        System.out.println("Teste: Viga com armadura positiva: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 138: Exemplo 7");
        System.out.println("Dominio = "+VigaDominio5.dominio);
        System.out.println("As = " +VigaDominio5.As);
        System.out.println("Asl =" + VigaDominio5.Asl);
        System.out.println("----------------------------");


        //Teste: Viga T: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 142: Exemplo 8
        Viga VigaT = new Viga();
        VigaT.Caracteristicas(175.0,18.0,26.0,50.0,210.0,2.5,2.6,175.0);
        VigaT.DimensionarT(10000.0/1.4, 20.0,170.0);
        System.out.println("Teste: Viga T: Livro Calculo e Detalhamento de Estrturas Usuais de Concreto Armado: Pagina 142: Exemplo 8");
        System.out.println("Dominio = "+VigaT.dominio);
        System.out.println("As = " +VigaT.As);
        System.out.println("Asl =" + VigaT.Asl);

    }

    public void Caracteristicas(double h,double bw,double fck,double CA,double Ey,double coe, double dl){
        this.Ey    = Ey*pow(10.0,9.0);
        this.h     = h/100.0;
        this.d     = (h-coe)/100.0;
        this.bw    = bw/100.0;
        this.fck   = fck;
        this.fyk   = CA*pow(10.0,7.0);
        this.fyd   = this.fyk/1.15;
        this.fcd   = fck/1.4*pow(10.0,6.0);
        this.Ecs   = 0.85*5600.0*(pow(fck*pow(10.0,-6.0),0.5))*pow(10.,6.);
        this.eyd   = this.fyd/this.Ey;
        this.Asmin = 0.0015*this.h*this.bw*pow(10.0,4.);
        this.Asmax = 0.04*this.h*this.bw*pow(10.0,4.0);
        this.dl    = dl/100.0;
    }

    public void Caracteristicas(double h,double bw,double fck,double CA,double Ey,double coe,double dl, double d){
        this.Ey    = Ey*pow(10.0,9.0);
        this.h     = h/100.0;
        this.d     = d/100.0;
        this.bw    = bw/100.0;
        this.fck   = fck;
        this.fyk   = CA*pow(10.0,7.0);
        this.fyd   = this.fyk/1.15;
        this.fcd   = fck/1.4*pow(10.0,6.0);
        this.Ecs   = 0.85*5600.0*(pow(fck*pow(10.0,-6.0),0.5))*pow(10.,6.);
        this.eyd   = this.fyd/this.Ey;
        this.Asmin = 0.0015*this.h*this.bw*pow(10.0,4.);
        this.Asmax = 0.04*this.h*this.bw*pow(10.0,4.0);
        this.dl    = dl/100.0;
    }

    public void Dimensionar(double Mk){

        double a,b,c,x1,x2,x,x34,M34,As34,M2,esl,dl,fsl;
        
        this.Md = (Mk*1.4)*1000.0;
        dl      = this.dl;

        a = -0.272*this.bw*this.fcd;
        b =  0.68*this.d*this.bw*this.fcd;
        c = -this.Md;
        x1 = (-b+pow(b*b-4*a*c,0.5))/(2*a);
        x2 = (-b-pow(b*b-4*a*c,0.5))/(2*a);
        if (x2>this.d || x2<0) {
            x = x1;
        }
        else{
            x = x2;
        }

        if (x<=0) {
            this.dominio=1;
        }
        else{
            if (x>0 && x<=0.259*this.d) {
               this.dominio=2; 
            }
            else{
                if (x>0.259*this.d && x<=(0.0035*this.d)/(this.eyd+0.0035)) {
                   this.dominio=3;
                }
                else{
                    if (x>(0.0035*this.d)/(this.eyd+0.0035) && x<=this.h) {
                       this.dominio = 4; 
                    }
                    else{
                        dominio = 5;
                    }
                }
            }
        }

        if (this.dominio==4 || this.dominio==5) {
            x34 = 0.0035*this.d/(this.eyd+0.0035);
            M34 = (0.85*this.fcd*this.bw*0.8*x34)*(this.d-0.4*x34);
            As34= M34/(this.fyd*(this.d-0.4*x34));
            M2  = this.Md-M34;
            esl = 0.35*(x34-dl)/x34;

            if (esl<this.eyd) {
                fsl = this.Ey*esl/1.15;
            }
            else{
                fsl = this.fyd;
            }

            this.Asl = M2/((this.d-dl)*fsl);
            this.As  = this.Asl + As34;

        }

        else{
            this.As = this.Md/(this.fyd*(this.d-0.4*x));
        }

        this.As     = this.As*pow(10.0,4.0);
        this.Asl    = this.Asl*pow(10.0,4.0);
    }

    public void DimensionarT(double Mk, double hf, double bf){
        double a,b,c,x1,x2,x,x34,M34,As34,M2,esl,dl,fsl,Mf,Af,Ma,Aa;
        Ma = 0.0;
        hf = hf/100.0;
        bf = bf/100.0;
        this.hf = hf;
        this.bf = bf;
        
        this.Md = (Mk*1.4)*1000.0;
        dl      = this.dl;

        a = -0.272*this.bf*this.fcd;
        b =  0.68*this.d*this.bf*this.fcd;
        c = -this.Md;
        x1 = (-b+pow(b*b-4*a*c,0.5))/(2*a);
        x2 = (-b-pow(b*b-4*a*c,0.5))/(2*a);
        if (x2>this.d || x2<0) {
            x = x1;
        }
        else{
            x = x2;
        }

        if (x*0.8>hf) {

            Mf = 0.85*this.fcd*hf*(bf-this.bw)*(this.d-hf/2.0); 
            Af = Mf/((this.d-hf/2.0)*this.fyd);  
            Ma = this.Md-Mf;
            a = -0.272*this.bw*this.fcd;
            b =  0.68*this.d*this.bw*this.fcd;
            c = -Ma;
            x1 = (-b+pow(b*b-4*a*c,0.5))/(2*a);
            x2 = (-b-pow(b*b-4*a*c,0.5))/(2*a);
            if (x2>this.d || x2<0) {
                x = x1;
            }
            else{
                x = x2;
            }

            if (x<=0) {
                this.dominio=1;
            }
            else{
                if (x>0 && x<=0.259*this.d) {
                   this.dominio=2; 
                }
                else{
                    if (x>0.259*this.d && x<=(0.0035*this.d)/(this.eyd+0.0035)) {
                       this.dominio=3;
                    }
                    else{
                        if (x>(0.0035*this.d)/(this.eyd+0.0035) && x<=this.h) {
                           this.dominio = 4; 
                        }
                        else{
                            dominio = 5;
                        }
                    }
                }
            }

            if (this.dominio==4 || dominio==5) {
                x34 = 0.0035*this.d/(this.eyd+0.0035);
                M34 = (0.85*this.fcd*this.bw*0.8*x34)*(this.d-0.4*x34);
                As34= M34/(this.fyd*(this.d-0.4*x34));
                M2  = this.Md-M34;
                esl = 0.35*(x34-dl)/x34;

                if (esl<this.eyd) {
                    fsl = this.Ey*esl/1.15;
                }
                else{
                    fsl = this.fyd;
                }

                this.Asl = M2/((this.d-dl)*fsl);
                Aa  = this.Asl + As34;

            }

            else{
                Aa = Ma/(this.fyd*(this.d-0.4*x));
            }

            this.As = Aa + Af;
        }

        else{
            if (x<=0) {
                this.dominio=1;
            }
            else{
                if (x>0 && x<=0.259*this.d) {
                   this.dominio=2; 
                }
                else{
                    if (x>0.259*this.d && x<=(0.0035*this.d)/(this.eyd+0.0035)) {
                       this.dominio=3;
                    }
                    else{
                        if (x>(0.0035*this.d)/(this.eyd+0.0035) && x<=this.h) {
                           this.dominio = 4; 
                        }
                        else{
                            dominio = 5;
                        }
                    }
                }
            }

            if (this.dominio==4) {
                x34 = 0.0035*this.d/(this.eyd+0.0035);
                M34 = (0.85*this.fcd*this.bw*0.8*x34)*(this.d-0.4*x34);
                As34= M34/(this.fyd*(this.d-0.4*x34));
                M2  = this.Md-M34;
                esl = 0.35*(x34-dl)/x34;

                if (esl<this.eyd) {
                    fsl = this.Ey*esl/1.15;
                }
                else{
                    fsl = this.fyd;
                }

                this.Asl = M2/((this.d-dl)*fsl);
                this.As  = this.Asl + As34;

            }

            else{
                this.As = this.Md/(this.fyd*(this.d-0.4*x));
            }
        }
        this.As     = this.As*pow(10.0,4.0);
        this.Asl    = this.Asl*pow(10.0,4.0);
        
    }

}
