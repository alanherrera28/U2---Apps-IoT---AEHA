# AEHA_conversion.py

class ConvertirGrados():
    def convertir(self):
        print("________________________________________________")
        print("  Convertir Celsius a Fahrenheit y viceversa")
        print("     Alan Herrera 1218100481 GDS0152")
        print("________________________________________________")
        n=int(input("Seleccione Conversion\n1. -- ºC a ºF -- \n2. -- ºF a ºC -- \n" ))

        if(n==1):
            c = float(input("Ingrese grados Celsius: "))
            f = c*(9/5)+32
            print(str(c)+"ºC equivale a "+str(f)+"ºF")
        else:
            f = float(input("Ingrese grados Fahrenheit: "))
            c =(f-32)*(5/9)
            print(str(f)+"ºF equivale a "+str(c)+"ºC")

conv = ConvertirGrados()
conv.convertir()
