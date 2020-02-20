# AEHA_formato_usa.py

class Calificaciones():
    def letras(self):
        print("________________________________________________")
        print(" Letra de acuerdo a la calificacion de 0 a 100")
        print("     Alan Herrera 1218100481 GDS0152")
        print("________________________________________________")

        c = float(input("Ingrese calificación: "))

        if(c>=93 and c<=100):
            print(str(c)+" equivale a ~ A ~")
        else:
            if(c>=90 and c<93):
                print(str(c)+" equivale a ~ A- ~")
            else:
                if(c>=87 and c<90):
                    print(str(c)+" equivale a ~ B+ ~")
                else:
                    if(c>=83 and c<87):
                        print(str(c)+" equivale a ~ B ~")
                    else:
                        if(c>=80 and c<83):
                            print(str(c)+" equivale a ~ B- ~")
                        else:
                            if(c>=77 and c<80):
                                print(str(c)+" equivale a ~ C+ ~")
                            else:
                                if(c>=73 and c<77):
                                    print(str(c)+" equivale a ~ C ~")
                                else:
                                    if(c>=70 and c<73):
                                        print(str(c)+" equivale a ~ C- ~")
                                    else:
                                        if(c>=67 and c<70):
                                            print(str(c)+" equivale a ~ D+ ~")
                                        else:
                                            if(c>=60 and c<67):
                                                print(str(c)+" equivale a ~ D ~")
                                            else:
                                                if(c>=0 and c<60):
                                                    print(str(c)+" equivale a ~ F ~")

cal = Calificaciones()
cal.letras()
        
