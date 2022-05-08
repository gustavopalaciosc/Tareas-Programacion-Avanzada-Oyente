from parametros import DEUDA_TOTAL, PROBABILIDAD_EVENTO
from win_prob import win_prob
import random

class Casino():

    def __init__(self, juegos, bebestibles):
        
        self.jugador = None
        self.bebestibles= bebestibles
        self.juegos = juegos
        self.dinero_faltante = DEUDA_TOTAL
    
    @property
    def dinero_faltante(self):
        return self.__dinero_faltante
    
    @dinero_faltante.setter
    def dinero_faltante(self, valor):
        if 0 <= valor:
            self.__dinero_faltante = valor
        else:
            self.__dinero_faltante = 0
    
    def evento_especial(self):
        exe = win_prob(PROBABILIDAD_EVENTO)
        if exe:
            print("Se ha ejecutado el evento especial!")
            premio = random.choice(self.bebestibles)
            premio.consumir(self.jugador)
        else:
            pass

    def jugar(self):
        self.jugador.apostar(self)
    
        



