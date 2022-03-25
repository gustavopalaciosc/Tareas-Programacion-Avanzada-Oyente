import random
from parametros import PROBABILIDAD_EVENTO
from ambiente import Ambiente
from tributo import Tributo

class Arena():

    def __init__(self, nombre, riesgo, dificultad, jugador, tributos):
        
        self.nombre = nombre
        self.riesgo = float(riesgo)
        self.dificultad = dificultad
        self.jugador = jugador
        self.tributos = tributos
        self.ambientes = []
        self.ambiente_actual = 0

        file = open("ambientes.csv").readlines()
        for i in range(1, len(file)):
            a = file[i].split(",")
            self.ambientes.append(Ambiente(a[0], a[1], a[2], a[3]))
        
        


    
    def rotar_ambiente(self):

        if self.ambiente_actual == 0:
            
            self.ambiente_actual += 1

        elif self.ambiente_actual < 2:
            
            self.ambiente_actual += 1
        
        else:
            self.ambiente_actual = 0
            
            




    def ejecutar_evento(self):
        

        if PROBABILIDAD_EVENTO >= round(random.random(),1):

            daño = self.ambientes[self.ambiente_actual].calcular_daño()
            print(f"Se ha ejecutado el evento {self.ambientes[self.ambiente_actual].evento_ejecutado}\n")
            print(f"El daño efectuado a los tributos por el ambiente es: {daño}\n")

            for i in self.tributos:
                i.vida -= int(daño)

                if not i.esta_vivo:
                    print(f"El ambiente hostil a matado a {i.nombre}")
                    self.tributos.remove(i)
        
        
            self.jugador.vida -= int(daño)
        
        else:
            pass

        

        self.rotar_ambiente()
        
        

    def encuentros(self):

        ne = (self.riesgo * len(self.tributos))//2

        tpp = self.tributos + [self.jugador]

        for i in range(0, int(ne)):
            player1 = random.choice(self.tributos)
            player2 = random.choice(tpp)

            while player1 == player2:
                player2 = random.choice(self.tributos)
            
    

            
            
            player1.atacar_npc(player2, self.tributos)

            


        
        

        
            


            