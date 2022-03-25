from parametros import VELOCIDAD_VIENTOS_PLAYA, HUMEDAD_PLAYA, NUBOSIDAD_MONTAÑA, PRECIPITACIONES_MONTAÑA, PRECIPITACIONES_BOSQUE, VELOCIDAD_VIENTOS_BOSQUE 
import random

class Ambiente():

    def __init__(self, nombre, *args):
        
        self.nombre = nombre
        self.eventos = {}
        self.evento_ejecutado = None

        for i in args:
            self.eventos[i.split(";")[0]] = int(i.split(";")[1])
    
    def calcular_daño(self):

        evento = random.choice(list(self.eventos.keys()))
        self.evento_ejecutado = evento
        
        if self.nombre == "playa":
            
            daño = max(5, (0.4*HUMEDAD_PLAYA + 0.2*VELOCIDAD_VIENTOS_PLAYA + int(self.eventos[evento]))/5)
            return daño

        elif self.nombre == "bosque":
            
            daño = max(5, (0.2*VELOCIDAD_VIENTOS_BOSQUE + 0.1*PRECIPITACIONES_BOSQUE + int(self.eventos[evento]))/5 )
            return daño

        else:
            
            daño = max(5, (0.1*PRECIPITACIONES_MONTAÑA + 0.3*NUBOSIDAD_MONTAÑA + int(self.eventos[evento]))/5 )
            return daño

