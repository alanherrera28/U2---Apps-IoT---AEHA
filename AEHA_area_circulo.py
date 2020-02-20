# AEHA_area_circulo.py

import math

class Area():
    def circulo(self):
        print("_______________________________")
        print("  Calcular Área de un Circulo")
        print("Alan Herrera 1218100481 GDS0152")
        print("_______________________________")

        r = float (input("Ingresa el radio del circulo:" ))

        area = (math.pi * (r * r))
        print(str(area))

ar = Area()
ar.circulo()
