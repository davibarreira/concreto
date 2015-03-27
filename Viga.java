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


    public static void main(String[] args){
        System.out.println("h=22.9, bw=100, fck=25, CA=50, Ey=210*10**9, coe=2.5, Mk=14.6");
        Viga A = new Viga();
        A.Caracteristicas(22.9,100.0,25.0,50.0,210.0,2.5);
        A.Dimensionar(14.6);
        System.out.println(A.dominio);
        System.out.println(A.As);

    }

    public void Caracteristicas(double h,double bw,double fck,double CA,double Ey,double coe){
        this.Ey         = Ey*pow(10.0,9.);
        this.h     = h/100.0;
        this.d     = (h-coe)/100.0;
        this.bw    = bw/100.0;
        this.fck   = fck;
        this.fyk   = CA*pow(10.0,7.0);
        this.fyd   = this.fyk/1.15;
        this.fcd   = fck/1.4*pow(10.0,6.0);
        this.Ecs   = 0.85*5600.0*(pow(fck*pow(10.0,-6.0),0.5))*pow(10.,6.);
        this.eyd   = this.fyd/Ey;
        this.Asmin = 0.0015*this.h*this.bw*pow(10.0,4.);
        this.Asmax = 0.04*this.h*this.bw*pow(10.0,4.0);
    }

    public void Caracteristicas(double h,double bw,double fck,double CA,double Ey,double coe, double d){
        Ey         = Ey*pow(10.0,9.);
        this.h     = h/100.0;
        this.d     = d/100.0;
        this.bw    = bw/100.0;
        this.fck   = fck;
        this.fyk   = CA*pow(10.0,7.0);
        this.fyd   = this.fyk/1.15;
        this.fcd   = fck/1.4*pow(10.0,6.0);
        this.Ecs   = 0.85*5600.0*(pow(fck*pow(10.0,-6.0),0.5))*pow(10.,6.);
        this.eyd   = this.fyd/Ey;
        this.Asmin = 0.0015*this.h*this.bw*pow(10.0,4.);
        this.Asmax = 0.04*this.h*this.bw*pow(10.0,4.0);
    }

    public void Dimensionar(double Mk){

        double a,b,c,x1,x2,x,x34,M34,As34,M2,esl,dl,fsl;
        
        this.Md = (Mk*1.4)*1000.0;
        dl      = 0.05;

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

        this.As     = this.As*pow(10.0,4.0);
        this.Asl    = this.Asl*pow(10.0,4.0);
    }

    public void DimensionarT(double Mk, double bf, double hf){
        double a,b,c,x1,x2,x,x34,M34,As34,M2,esl,dl,fsl,Mf,Af,Ma,Aa;

        this.hf = hf/100.0;
        this.bf = bf/100.0;
        
        this.Md = (Mk*1.4)*1000.0;
        dl      = 0.05;

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

        this.As     = this.As*pow(10.0,4.0);
        this.Asl    = this.Asl*pow(10.0,4.0);

        }
        
    }

}
