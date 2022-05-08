from abc import ABC, abstractmethod
import sys
from jugador import Jugador 
from parametros import DEUDA_TOTAL

class Menu(ABC):

    def __init__(self, nombre, opciones):
        
        self.nombre = nombre
        self.opciones = opciones

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def run(self):
        """ Imprime el menu y toma el input del usuario """
        while True:
            self.display_menu()
            entrada = input("\nEliga una opcion: ")
            opcion = self.opciones.get(entrada)

            if opcion:
                break
            else:
                print("Opcion invalida")
        
        return opcion()
    
    @abstractmethod
    def salir(self):
        print("¡Hasta pronto!")
        sys.exit()

    
class Menu_inicio(Menu):

    def __init__(self, casino):
        self.casino = casino

        super().__init__("inicio", {"1": self.iniciar_partida, "x": self.salir})
    
    def display_menu(self):
        print(""" 
*** Menu de Inicio ***
----------------------
[1] Iniciar partida
[X] Salir
""")  
    
    def run(self):
        return super().run()    
            
    def iniciar_partida(self):
        self.casino.dinero_faltante = DEUDA_TOTAL
        return ["opciones"]

    def salir(self):
        return super().salir()


class Menu_principal(Menu):

    def __init__(self, casino):
        self.casino = casino

        super().__init__("principal", {"1": self.opciones_juego, "2": self.comprar_bebestible, "3": self.habilidades_jugador, "0": self.volver, "x": self.salir})
   
    def display_menu(self):
        print(""" 
   *** Menu Principal ***
---------------------------
[1] Opciones de juegos
[2] Comprar bebestibles
[3] Habilidades jugador
[0] Volver
[X] Salir
""")
    
    def run(self):
        return super().run()
        
    def opciones_juego(self):
        return ["juegos"]

    def comprar_bebestible(self):
        return ["Bebestibles"]

    def habilidades_jugador(self):
        return ["Estado Jugador"]

    def volver(self):
        return ["inicio"]

    def salir(self):
        return super().salir()


class Opciones_jugador(Menu):
    def __init__(self, casino):
        self.casino = casino
        super().__init__("Opciones de jugador", {"1": self.elegir, "0": self.volver, "x": self.salir})
          
    def display_menu(self):
        mifile = open("jugadores.csv").readlines()
        print("""
     *** Opciones de Jugador ***
-------------------------------------""")
        for i in range(1, len(mifile)):
            info = mifile[i].split(",")
            print(f"[{i}] {info[0]}: {info[1]}")
        print("[0] Volver")
        print("[X] Salir")
    
    def run(self):
        """ Imprime el menu y toma el input del usuario """
        while True:
            self.display_menu()
            entrada = input("\nEliga una opcion: ")
            try:
                if 1 <= int(entrada) <= 27:
                    elec = int(entrada)
                    entrada = "1"
            except:
                pass
            opcion = self.opciones.get(entrada)

            if opcion:
                break
            else:
                print("Opcion invalida")
        
        if entrada == "x" or entrada == "0":
            return opcion()      
        else:          
            return opcion(elec)
        
    def elegir(self, entrada):
        mifile = open("jugadores.csv").readlines()
        player = mifile[entrada].split(",")
        print(f"Has elegido a {player[0]}, jugador que es {player[1]}")
        self.casino.jugador = Jugador(player[0], player[1], int(player[2]), int(player[3]), int(player[4]), int(player[5]), int(player[6]), int(player[7]), int(player[8]), player[9].rstrip())
        self.casino.dinero_faltante -= self.casino.jugador.dinero
        return ["Principal"]
    
    def volver(self):
        return ["inicio"]
    
    def salir(self):
        return super().salir()


class Opciones_juego(Menu):
    def __init__(self, casino):
        self.casino = casino
        super().__init__("Opciones de juegos", {"0": self.volver, "x": self.salir, "1": self.cara_sello, "2": self.ruleta, "3": self.poker, "4": self.black_jack, "5": self.maquinas})
    
    def display_menu(self):
        print("""
   *** Opciones de Juegos ***
--------------------------------
   [1] Cara o Sello
   [2] Ruleta de la suerte
   [3] Poker 
   [4] Black Jack
   [5] Maquinas
   [0] Volver
   [X] Salir       
        """)
    
    def run(self):
        return super().run()

    def volver(self):
        return ["Principal"]
    
    def salir(self):
        return super().salir()
    
    def cara_sello(self):
        print("Has elegido jugar cara o sello\n")
        self.casino.jugador.apostar(self.casino.juegos["cara o sello"], self.casino)
        self.casino.evento_especial()
        return self.estado_juego()
        
    def ruleta(self):
        print("Has elegido jugar a la ruleta\n")
        self.casino.jugador.apostar(self.casino.juegos["ruleta"], self.casino)
        self.casino.evento_especial()
        return self.estado_juego()

    def poker(self):
        print("Has elegido jugar unos poker\n")
        self.casino.jugador.apostar(self.casino.juegos["poker"], self.casino)
        self.casino.evento_especial()
        return self.estado_juego()

    def black_jack(self):
        print("Has elegido jugar black jack\n")
        self.casino.jugador.apostar(self.casino.juegos["blackjack"], self.casino)
        self.casino.evento_especial()
        return self.estado_juego()

    def maquinas(self):
        print("Has elegido jugar en las maquinas tragamonedas\n")
        self.casino.jugador.apostar(self.casino.juegos["maquinas"], self.casino)
        self.casino.evento_especial()
        return self.estado_juego()
    
    def estado_juego(self):
        if self.casino.jugador.dinero == 0:
            print("Te has quedado sin dinero. Juego terminado.")
            return ["inicio"]
        elif self.casino.dinero_faltante == 0:
            print("Has recolactado todo el dinero que necesitabas. HAS GANADO")
            return ["inicio"]
        else:
            return "Juego terminado"


class Compra_bebestible(Menu):
    def __init__(self, casino):
        self.casino = casino
        super().__init__("Bebestibles", {"1": self.elegir, "0": self.volver, "x": self.salir})
    
    def volver(self):
        return ["Principal"]
    
    def salir(self):
        return super().salir()
    
    def elegir(self, eleccion):
        self.casino.bebestibles[eleccion].consumir(self.casino.jugador)
    
    def run(self):
        """ Imprime el menu y toma el input del usuario """
        while True:
            self.display_menu()
            entrada = input("\nEliga una opcion: ")
            try:
                if 1 <= int(entrada) <= 13:
                    eleccion = int(entrada)
                    entrada = "1"
            except:
                pass
            opcion = self.opciones.get(entrada)

            if opcion:
                break
            else:
                print("Opcion invalida")
        
        if entrada == "x" or entrada == "0":
            return opcion()
        else:
            return opcion(eleccion)
   
    def display_menu(self):
        print(""" 
         *** Bebestibles ***
-------------------------------------
  N° |  Nombre   | Tipo     | Precio
""")
        for i in range(0, len(self.casino.bebestibles)):
    
            print(f" [{i}] | {self.casino.bebestibles[i].nombre} | {self.casino.bebestibles[i].tipo}    | {self.casino.bebestibles[i].precio}")
        print("\n [0] Volver")
        print(" [X] Salir")
    

class Estado_jugador(Menu):
    def __init__(self, casino):
        self.casino = casino
        super().__init__("Estado Jugador", {"0": self.volver, "x": self.salir})

    def volver(self):
        return ["Principal"]
    
    def salir(self):
        return super().salir()
    
    def display_menu(self):
        print(f"""
         *** Ver estado del Jugador ***
--------------------------------------------
    Nombre: {self.casino.jugador.nombre}
    Personalidad: {self.casino.jugador.personalidad}
    Energia: {self.casino.jugador.energia}
    Suerte: {self.casino.jugador.suerte}
    Dinero: {self.casino.jugador.dinero}
    Frustracion: {self.casino.jugador.frustracion}
    Ego: {self.casino.jugador.ego}
    Carisma: {self.casino.jugador.carisma}
    Confianza: {self.casino.jugador.confianza}
    Juego favorito: {self.casino.jugador.juego_favorito}
    Dinero faltante: {self.casino.dinero_faltante}
    [0] Volver
    [X] Salir
""")
    
    def run(self):
        return super().run()


class MenusDic(dict):
    
    def __init__(self):
        self.key = "inicio"
    
    def cambio(self):
        menu = self[self.key]
        while True:
            datos_menu = menu.run()
            if type(datos_menu) == list:
                cambiar_menu = datos_menu[0]
            else: 
                cambiar_menu = False
            
            if cambiar_menu:
                self.key = cambiar_menu
                break
    







    
    
   
    
