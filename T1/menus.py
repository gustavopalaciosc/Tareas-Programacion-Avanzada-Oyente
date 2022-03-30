from eleccion import Eleccion
from parametros import ENERGIA_ACCION_HEROICA
from tributo import Tributo
from menu_printer import printer_menu_inicio, printer_menu_principal, printer_simulacion_hora
from arenas import Arena


class Menus():
    
    def __init__(self):
        print("¡Bienvenidos a los juegos anuales DCCAPITOL!\n")
        self.mitributo_nombre = None 
        self.mitributo = None
        self.otros_tributos = []
        self.started = False
        self.arena = None
        self.ambientes = None
        
  

    def Menu_inicio(self):

        printer_menu_inicio()

        opcion = str(input("Eliga una opcion: "))

        if opcion == "1":
            
            if not self.started:
                self.elegir_tributo()

            else:
                self.Menu_principal()

        elif opcion == "2":
            print("Te esperamos para otros juegos! :D")
        
        else:
            print("Opción invalida.\n")
            self.Menu_inicio()


    def elegir_tributo(self):

        self.mitributo_nombre = Eleccion().elegir_tributo()

        file = open("tributos.csv")
        a = file.readlines()

        for i in range(1, len(a)):
    
            b = a[i].split(",")

            if b[0] != self.mitributo_nombre:

                self.otros_tributos.append(Tributo(b[0], b[1], int(b[2]), int(b[3]), int(b[4]), int(b[5]), int(b[6]), int(b[7]), int(b[8])))
            
            else:
                self.mitributo = Tributo(b[0], b[1], int(b[2]), int(b[3]), int(b[4]), int(b[5]), int(b[6]), int(b[7]), int(b[8]))
            
        print("\nComo tributo has elegido a {} del distrito {}".format(self.mitributo.nombre, Eleccion().get_info(self.mitributo_nombre, 1)))

        self.started = True

        self.elegir_arena()
    


    def elegir_arena(self):

        arenas = open("arenas.csv").readlines()
        print("Las arenas disponibles para jugar son: \n")

        for i in range(1, len(arenas)):
            print("[{}] {}".format(i, arenas[i].split(",")[0]))
        
        while True:

            try:
                opcion = int(input("\nEliga una opcion: "))
                

                if opcion > 0:

                    miarena = arenas[opcion].split(",")
                    self.arena = Arena(miarena[0], miarena[2], miarena[1], self.mitributo, self.otros_tributos)
                    print("Has elegido jugar en la arena {}\n".format(self.arena.nombre))
                    break

                else:
                    
                    print("Opcion invalida, VO TENI QUE SER DEL HUACHIPATO WEON")

        
            except IndexError:
                print("Opcion invalida, VO TENI QUE SER DEL HUACHIPATO WEON")
            

        self.Menu_principal()



    def Menu_principal(self):

        printer_menu_principal()
        opcion = str(input("Eliga una opcion: "))

        if opcion == "1":
            
            self.simulacion_hora()

        elif opcion == "2":

            self.arena.jugador.estado_tributo()
            self.Menu_principal()

        elif opcion == "3":
            
            self.arena.jugador.utilizar_objeto(self.arena)
            self.Menu_principal()

        elif opcion == "4":   
            
            print("{}Estado DCCapitolio{}".format(" "*15, " "*15))
            print("-"*49)
            print("Dificultad: {}".format(self.arena.dificultad))
            
            print("Tributos vivos: ")
            print("   {}: {}".format(self.arena.jugador.nombre, self.arena.jugador.vida))
            for i in self.arena.tributos:
                print("   {}: {}".format(i.nombre, i.vida))
            print("Proximo ambiente: {}".format(self.arena.ambientes[self.arena.ambiente_actual].nombre))

            self.Menu_principal()
            

                


        elif opcion == "5":
            self.Menu_inicio()

        elif opcion == "6":
            print("\n¡Hasta pronto! May Huachipato be ever in your favor")

        else:
            print("\nOpción invalida, vo teni que ser del huachipato weon\n")
            self.Menu_principal() 



    def simulacion_hora(self):
        
        printer_simulacion_hora()

        opcion = input("Eliga una opción:\n")


        if opcion == "1":
            
            if self.arena.jugador.energia >= ENERGIA_ACCION_HEROICA:

                self.arena.jugador.accion_heroica()

                ##Simulacion de hora##
                
                self.arena.ejecutar_evento()
                self.arena.encuentros()

                print("\nLa opcion elegida fue hacer una accion heroica\n")
                print("\nLos tributos con vida son: ")
                for i in self.arena.tributos:
                    print(i.nombre)

                if not self.arena.jugador.esta_vivo:
                    print("Has muerto durante la simulacion de hora, PRESS F FOR RESPECT")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()

                elif len(self.arena.tributos) == 0:
                    print("Felicitaciones! Has ganado los Juegos del hambre!")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()
                
                print(self.arena.jugador.nombre)
                
                self.Menu_principal()


            
            else:
                 print("No tienes la energía suficiente para hacer una accion heroica. Te diría que si, pero te faltan créditos.")
                 self.simulacion_hora()


        elif opcion == "2":
            
            print("Los tributos que siguen con vida son los siguientes: \n")

            for i in range(0, len(self.arena.tributos)):

                print("[{}] {}: {}".format(i + 1, self.arena.tributos[i].nombre, self.arena.tributos[i].vida))

                """

                if self.otros_tributos[i].esta_vivo:

                    print("[{}] {}: {}".format(i + 1, self.otros_tributos[i].nombre, self.otros_tributos[i].vida))
                    """

            while True:

                try: 
                    opcion = int(input("\nElige al tributo que deseas atacar: "))

                    if opcion > 0:

                        print("Has elegido atacar a {}".format(self.arena.tributos[opcion - 1].nombre))
                        
                        self.arena.jugador.atacar(self.arena.tributos[opcion - 1], self.arena.tributos)

                        ##Simulacion de hora##
                        
                        self.arena.ejecutar_evento()
                        self.arena.encuentros()

                        print("\nLa simulacion de hora elegida fue atacar a un tributo\n")
                        print("\nLos tributos con vida son: ")
                        for i in self.arena.tributos:
                            print(i.nombre)

                        if not self.arena.jugador.esta_vivo:
                            print("Has muerto durante la simulacion de hora, PRESS F FOR RESPECT")
                            self.started = False
                            self.otros_tributos = []
                            self.Menu_inicio()
                        
                        elif len(self.arena.tributos) == 0:
                            print("Felicitaciones! Has ganado los Juegos del hambre!")
                            self.started = False
                            self.otros_tributos = []
                            self.Menu_inicio()
                        
                        print(self.arena.jugador.nombre)


                        self.Menu_principal()


                    else:
                        print("Opcion invalida! Vo teni que ser del huachipato")


                except (ValueError, IndexError):

                    print("Opcion invalida! Vo teni que ser del huachipato")
            
            


        elif opcion == "3":
            
            self.arena.jugador.pedir_objeto()

            ##Simulacion de hora##
            self.arena.ejecutar_evento()
            self.arena.encuentros()

            print("\nLa opcion elegida fue pedir un objeto a patrocinadores\n")
            print("\nLos tributos con vida son: ")
            for i in self.arena.tributos:
                print(i.nombre)

            if not self.arena.jugador.esta_vivo:
                    print("Has muerto durante la simulacion de hora, PRESS F FOR RESPECT")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()
            
            elif len(self.arena.tributos) == 0:
                    print("Felicitaciones! Has ganado los Juegos del hambre!")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()
            
            print(self.arena.jugador.nombre)


            self.Menu_principal()
            

        elif opcion == "4":
            
            self.arena.jugador.hacerce_bolita()

            ##Simulacion de hora##
            self.arena.ejecutar_evento()
            self.arena.encuentros()

            print("\nLa opcion elegida fue hacerse bolita\n")
            print("\nLos tributos con vida son: ")
            for i in self.arena.tributos:
                print(i.nombre)

            if not self.arena.jugador.esta_vivo:
                    print("Has muerto durante la simulacion de hora, PRESS F FOR RESPECT")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()
            
            elif len(self.arena.tributos) == 0:
                    print("Felicitaciones! Has ganado los Juegos del hambre!")
                    self.started = False
                    self.otros_tributos = []
                    self.Menu_inicio()
            
            print(self.arena.jugador.nombre)

            self.Menu_principal()
            
        elif opcion == "5":

            self.Menu_principal()

        else:
            print("¡Debes elegir un numero entre el 1 y el 5! VO TENI QUE SER DEL HUACHIPATO WEON")
            self.simulacion_hora()
        




    