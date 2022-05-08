from parametros import CARISMA_GANAR, CONFIANZA_PERDER, EGO_GANAR, FRUSTRACION_GANAR, FRUSTRACION_PERDER


class Juego():

    def __init__(self, nombre, esperanza, apuesta_min, apuesta_max):
        self.nombre = nombre
        self.esperanza = esperanza
        self.apuesta_max = apuesta_max
        self.apuesta_min = apuesta_min	
    
    def entrega_resultado(self, jugador, result, apuesta, casino):
        
        if result:
            print("EUREKA, HAS GANADO!")
            jugador.ego += EGO_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.frustracion -= FRUSTRACION_GANAR
            jugador.dinero += apuesta
            casino.dinero_faltante -= apuesta
        
        else:
            print("OOOPS, HAS PERDIDO!")
            jugador.frustracion += FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
            jugador.dinero -= apuesta
            casino.dinero_faltante += apuesta



    def prob_ganar(self, jugador, apuesta):
        pg = min(1, jugador.prob_ganar(apuesta, self) - (apuesta - (jugador.favorito(self) * 50 - (self.esperanza * 30)))  / 10000)
        return pg

    