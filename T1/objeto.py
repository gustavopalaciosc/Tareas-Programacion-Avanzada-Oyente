from abc import ABC, abstractclassmethod
from parametros import AUMENTAR_AGILIDAD, AUMENTAR_ENERGIA, AUMENTAR_INGENIO, PONDERADOR_AUMENTAR_ENERGIA, PONDERADOR_AUMENTAR_FUERZA

class Objeto(ABC):

    def __init__(self, nombre, tipo, peso):
        
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
    
    @abstractclassmethod
    def entrega_beneficio(self):
        pass


class Consumible(Objeto):

    def __init__(self, nombre, tipo, peso):
        super().__init__(nombre, tipo, peso)
    
    def entrega_beneficio(self, tributo, arena):

        tributo.energia += AUMENTAR_ENERGIA
        print("Has consumido una {}, la cual te ha dado {} de energia".format(self.nombre, AUMENTAR_ENERGIA))
        #return "Has consumido una {}, la cual te ha dado {} de energia".format(self.nombre, AUMENTAR_ENERGIA)
        

class Arma(Objeto):

    def __init__(self, nombre, tipo, peso):
        super().__init__(nombre, tipo, peso)
    
    def entrega_beneficio(self, tributo, arena):
        
        aumento_fuerza =  tributo.fuerza*(PONDERADOR_AUMENTAR_FUERZA * float(arena.riesgo) + 1)
        tributo.fuerza += aumento_fuerza

        print("Has utilizado tu {}, por lo que tu fuerza a aumentado en {}".format(self.nombre, aumento_fuerza))


class Especial(Objeto):

    def __init__(self, nombre, tipo, peso):
        super().__init__(nombre, tipo, peso)
    
    def entrega_beneficio(self, tributo, arena):

        tributo.energia += AUMENTAR_ENERGIA
        tributo.fuerza += tributo.fuerza*(PONDERADOR_AUMENTAR_FUERZA * arena.riesgo + 1)
        tributo.ingenio += AUMENTAR_INGENIO
        tributo.agilidad += AUMENTAR_AGILIDAD


















    
