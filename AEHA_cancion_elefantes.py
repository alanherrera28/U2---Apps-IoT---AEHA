# AEHA_cancion_elefantes.py

class Elefantes():
    def cancion(self):
        print("_______________________________")
        print("    Cancion de los elefantes")
        print("Alan Herrera 1218100481 GDS0152")
        print("_______________________________")
        
        
        el = 0
        for i in range(1, 101):
            el = el + i
            print(f"{i} elefantes se columpiaban sobre la tela de una araña,")
            print("como veian que resistia, fueron a llamar a otro elefante")
            print()

elf = Elefantes()
elf.cancion()
