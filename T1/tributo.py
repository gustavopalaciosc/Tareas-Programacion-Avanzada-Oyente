from parametros import COSTO_OBJETO, ENERGIA_ACCION_HEROICA, ENERGIA_ATACAR, ENERGIA_BOLITA, POPULARIDAD_ACCION_HEROICA
from objeto import Arma, Consumible, Especial
import random

class Tributo():

    def __init__(self, nombre, distrito, edad, vida, energia, agilidad, fuerza, ingenio, popularidad):

        self.nombre = nombre
        self.distrito = distrito
        self.edad = edad
        self.vida = vida 
        self.energia = energia 
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.ingenio = ingenio
        self.popularidad = popularidad
        self.esta_vivo = True
        self.mochila = []
        self.peso = 0
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor > 0:
            self.__vida = valor

        else: 
            self.__vida = 0 
            self.esta_vivo = False
    

    def atacar(self, enemigo, tributos):
        
        n = (60*self.fuerza + 40*(self.agilidad + self.ingenio) - 30*self.peso)/self.edad
        attack = min(90, max(5, n))

        if self.energia >= ENERGIA_ATACAR:

            enemigo.vida = enemigo.vida - attack      
            self.energia -= ENERGIA_ATACAR

            if enemigo.vida == 0:

                print("Has matado a {}".format(enemigo.nombre))
                tributos.remove(enemigo)
                print("Energia restante: {}".format(self.energia))
            
            else:

                print("\nLe has quitado {} de vida a {}.".format(attack, enemigo.nombre))
                print("Energía restante: {}".format(self.energia))
            
        
        else:
            print("\nNo tienes energia suficiente para atacar")
    
    

    def atacar_npc(self, enemigo, tributos):

        n = (60*self.fuerza + 40*(self.agilidad + self.ingenio) - 30*self.peso)/self.edad
        attack = min(90, max(5, n))

        if self.energia >= ENERGIA_ATACAR:

            enemigo.vida = enemigo.vida - attack      
            self.energia -= ENERGIA_ATACAR

            if enemigo.vida == 0:

                print("{} ha matado a {}".format(self.nombre, enemigo.nombre))
                tributos.remove(enemigo)
                
            
            else:

                print("\n{} le ha quitado {} de vida a {}.".format(self.nombre, attack, enemigo.nombre))
                
            
        
        else:
            pass
                
            

    def utilizar_objeto(self, arena):

        if len(self.mochila) == 0:

            print("¡No tienes objetos para usar!")
            
        else:
            a = 1
            print("\nLos objetos disponibles son: ")
            for i in self.mochila:
                print("[{}] {}: {}".format(a, i.nombre.title(), i.tipo))
                a += 1
            
            

            try:
                opcion = int(input("\nEliga el objeto que desea utilizar: "))

                if opcion == 0:
                    print("¡Opcion invlida!")
                    
                
                else:
                    self.mochila[opcion - 1].entrega_beneficio(self, arena)
                    del self.mochila[opcion - 1]
                    
            
            except (ValueError, IndexError):

                print("¡Opcion invalida!")

            


        



    def pedir_objeto(self):
        
        print("Has pedido un objeto a los patrocinadores")
        
        if self.popularidad >= COSTO_OBJETO:

            self.popularidad -= COSTO_OBJETO
            objetos = open("objetos.csv").readlines()
            eleccion = random.choice(objetos[1:]).split(",")

            if eleccion[1] == "arma":
                self.mochila.append(Arma(eleccion[0], eleccion[1], eleccion[2]))
                self.peso += int(eleccion[2])

            elif eleccion[1] == "consumible":
                self.mochila.append(Consumible(eleccion[0], eleccion[1], eleccion[2]))
                self.peso += int(eleccion[2])

            else:
                self.mochila.append(Especial(eleccion[0], eleccion[1], eleccion[2]))
                self.peso += int(eleccion[2])
            
            print("Los patrocinadores te han enviado el {} {}".format(eleccion[1], eleccion[0]))


            

        else:
            print("No tienes popularidad suficiente para pedir el objeto! Los patrocinadores dicen: 'VO TENI QUE SER DEL HUACHIPATO'")


    def accion_heroica(self):

        self.popularidad += POPULARIDAD_ACCION_HEROICA
        self.energia -= ENERGIA_ACCION_HEROICA
        
        print("Has realizado una ACCION HEROICA\n")
        print("Tu tributo {} ha ganado {} de popularidad. Te queda {} de energía.".format(self.nombre, POPULARIDAD_ACCION_HEROICA, self.energia))
            
                    
    def hacerce_bolita(self):

        self.energia += ENERGIA_BOLITA
        
        print("\n¡Te has hecho bolita!")
        print("Has recuperado {} de energia".format(ENERGIA_BOLITA))      


    def print_objetos_mochila(self):
        mis_objetos = ""

        for i in self.mochila:
            mis_objetos += "{}, ".format(i.nombre)

        return mis_objetos.rstrip(", ") 
        

    def estado_tributo(self):

        print("{}Estado tributo{}".format(" "*29, " "*29))
        print("-"*72)
        print("Nombre: {}".format(self.nombre))
        print("Distrito: {}".format(self.distrito))
        print("Edad: {}".format(self.edad))
        print("Vida: {}".format(self.vida))
        print("Energía: {}".format(self.energia))
        print("Agilidad: {}".format(self.agilidad))
        print("Fuerza: {}".format(self.fuerza))
        print("Ingenio: {}".format(self.ingenio))
        print("Popularidad: {}".format(self.popularidad))
        print("Objetos: {}".format(self.print_objetos_mochila()).lstrip())
        print("Peso: {}".format(self.peso))