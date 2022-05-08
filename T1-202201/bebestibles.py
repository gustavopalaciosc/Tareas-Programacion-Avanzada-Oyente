from abc import ABC, abstractmethod 
from parametros import MAX_ENERGIA_BEBESTIBLE, MIN_ENERGIA_BEBESTIBLE
import random

class Bebestible(ABC):

    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre 
        self.tipo = tipo
        self.precio = precio
    
    @abstractmethod
    def consumir(self, jugador):
        beneficio = random.choice(range(MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE + 1))
        jugador.energia += beneficio
        print(f"El jugador {jugador.nombre} aumento su energia en {beneficio}")


class Jugo(Bebestible):
    
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)
    
    def consumir(self, jugador):

        super().consumir(jugador)
    
        largo = len(self.nombre)

        if largo <= 4:
            jugador.ego += 4
            print(f"El jugador {jugador.nombre} aumento su ego en 4")
        elif 7 >= largo >= 5:
            jugador.suerte += 7
            print(f"El jugador {jugador.nombre} aumento su suerte en 7")
        else:
            jugador.frustracion -= 10
            jugador.ego += 11
            print(f"El jugador {jugador.nombre} aumento su ego en 11 y disminuyo su frustracion en 10")
        
    
class Gaseosa(Bebestible):
    
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)
    
    def consumir(self, jugador):
        super().consumir(jugador)

        if jugador.personalidad == "Tacano" or jugador.personalidad == "Ludopata":
            jugador.frustracion -= 5
            print(f"El jugador {jugador.nombre} disminuyo su frustracion en 5")
        elif jugador.personalidad == "Bebedor" or jugador.personalidad == "Casual":
            jugador.frustracion += 5
            print(f"El jugador {jugador.nombre} aumento su frustracion en 5")
        
        jugador.ego += 6
        print(f"El jugador {jugador.nombre} ha aumentado su ego en 6")


class Brebaje_magico(Bebestible):
    
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)
    
    def consumir(self, jugador):
        super().consumir(jugador)

        largo = len(self.nombre)

        if largo <= 4:
            jugador.ego += 4
            print(f"El jugador {jugador.nombre} aumento su ego en 4")
        elif 7 >= largo >= 5:
            jugador.suerte += 7
            print(f"El jugador {jugador.nombre} aumento su suerte en 7")
        else:
            jugador.frustracion -= 10
            jugador.ego += 11
            print(f"El jugador {jugador.nombre} aumento su ego en 11 y disminuyo su frustracion en 10")
        
        if jugador.personalidad == "Tacano" or jugador.personalidad == "Ludopata":
            jugador.frustracion -= 5
            print(f"El jugador {jugador.nombre} disminuyo su frustracion en 5")
        elif jugador.personalidad == "Bebedor" or jugador.personalidad == "Casual":
            jugador.frustracion += 5
            print(f"El jugador {jugador.nombre} aumento su frustracion en 5")
        
        jugador.ego += 6
        print(f"El jugador {jugador.nombre} ha aumentado su ego en 6")

        jugador.carisma += 5
        print(f"El jugador {jugador.nombre} ha aumentado su carisma en 5")


        

        
