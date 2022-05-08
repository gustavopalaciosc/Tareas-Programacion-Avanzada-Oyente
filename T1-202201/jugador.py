from win_prob import win_prob
from parametros import PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO, MULTIPLICADOR_BONIFICACION_BEBEDOR, BONIFICACION_SUERTE_CASUAL


class Jugador():

    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):

        self.nombre = nombre
        self.energia = energia
        self.suerte = suerte
        self.dinero = dinero
        self.frustracion = frustracion
        self.ego = ego
        self.personalidad = personalidad
        self.carisma = carisma
        self.confianza = confianza
        self.juego_favorito = juego_favorito
        self.juegos_jugados = []

    @property
    def frustracion(self):
        return self.__frustracion
    
    @frustracion.setter
    def frustracion(self, valor):
        if 0 <= valor:
            self.__frustracion = valor
        else:
            self.__frustracion = 0
    
    @property
    def dinero(self):
        return self.__dinero
    
    @dinero.setter
    def dinero(self, valor):
        if 0 <= valor:
            self.__dinero = valor
        else:
            self.__dinero = 0
    
    @property
    def confianza(self):
        return self.__confianza
    
    @confianza.setter
    def confianza(self, valor):
        if 0 <= valor:
            self.__confianza = valor
        else:
            self.__confianza = 0
    
    
    def comprar_bebestible(self, bebestible):

        if self.dinero > bebestible.precio:
            self.dinero -= bebestible.precio
            bebestible.consumir(self)
        else:
            print("No tienes dinero suficiente para comprar el bebestible")

        if self.personalidad == "Bebedor":
            self.cliente_recurrente(bebestible)



    """ Metodo principal para accion de jugar """
    def apostar(self, juego, casino):  

        if self.personalidad == "Casual":
            self.suerte_principiante()


        ge = round((self.ego + self.frustracion) * 0.15)
        self.energia -= ge

        
        if self.dinero >= juego.apuesta_min:
            
            while True:

                try:
                    print(f"Tu apuesta debe estar entre {juego.apuesta_min} y {juego.apuesta_max}")
                    apuesta = int(input("Ingrese cuanto dinero quiere apostar: "))

                    if apuesta < juego.apuesta_min or apuesta > juego.apuesta_max:
                        print(f"Tu apuesta debe estar entre {juego.apuesta_min} y {juego.apuesta_max}")
                    elif apuesta > self.dinero:
                        print("No tienes esa cantidad de dinero para apostar!")
                    
                    if apuesta >= juego.apuesta_min and apuesta <= juego.apuesta_max and apuesta <= self.dinero:
                        a = juego.prob_ganar(self, apuesta)
                        gano = win_prob(a)
                        juego.entrega_resultado(self, gano, apuesta, casino)


                    if self.personalidad == "Ludopata":
                        self.ludopatia(gano)
                    
                    elif self.personalidad == "Tacano":
                        self.tacano_extremo(apuesta, gano)
                    
                    self.juegos_jugados.append(juego)
                    break

                
                except (ValueError, UnboundLocalError):
                    print("Ingrese una apuesta valida!")


                
                       

        else:
            print("No tienes el dinero suficiente para poder apostar en este juego! Vo teni que ser del huachipato")
                           
    
   
    def prob_ganar(self, apuesta, juego):
    
        pg = min(1, max(0, (self.suerte * 15 - apuesta * 0.4 + self.confianza * 3 * self.favorito(juego) + self.carisma * 2)/1000 ))

        return pg
    
    
    def favorito(self, juego):
        if juego.nombre == self.juego_favorito:
            return 1
        else:
            return 0
    
    def ludopatia(self, gano):
        self.ego += 2
        self.suerte += 3
        if gano:
            self.frustracion += 5


    def tacano_extremo(self, apuesta, gano):
        if apuesta < PORCENTAJE_APUESTA_TACANO:
            if gano:
                self.dinero += BONIFICACION_TACANO

    def cliente_recurrente(self, bebestible):
        for i in range(1, MULTIPLICADOR_BONIFICACION_BEBEDOR):
                bebestible.consumir(self)

    def suerte_principiante(self):
        self.suerte += BONIFICACION_SUERTE_CASUAL 
    








