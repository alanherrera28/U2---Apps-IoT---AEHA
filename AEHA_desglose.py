# AEHA_desglose.py

class Desglose():
    def iva(self):
        print("________________________________________")
        print("            Desglosar el IVA")
        print("     Alan Herrera 1218100481 GDS0152")
        print("________________________________________")
        print("")
        print("              IVA         16%")
        print("________________________________________")

        total = 0.0
        iva = 0.0
        
        monto = float (input("Ingresa el monto al cual aplicar el IVA:" ))

        iva = (monto * 0.16)

        total = monto + iva

        print("________________________________________")
        print(f"       Monto sin IVA:      {monto}")
        print(f"            IVA:           {iva}")
        print(f"       Monto mas IVA:      {total}")
        print("________________________________________")

des = Desglose()
des.iva()
