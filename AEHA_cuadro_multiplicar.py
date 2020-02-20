# AEHA_cuadro_multiplicar.py

class Tabla():
    def mult(self):
        print("________________________________________")
        print("     Muestra la tabla de multiplicar,")
        print("       acorde al multiplo ingresado")
        print("     Alan Herrera 1218100481 GDS0152")
        print("________________________________________")

        nums =[1,2,3,4,5,6,7,8,9,10] 
        mult = int(input("Ingrese hasta que multiplo mostrar: "))
        r=(mult+1)
        for i in range(1, r):
            #print (i, 2*i, 3*i, 4*1, 5*i, 6*i, 7*i, 8*i, 9*i, 10*i)
            for j in nums:
                print (i*j,end=' | ')
            print ("")

tb = Tabla()
tb.mult()
