from os import read


class Eleccion():

    def __init__(self):
        pass


    def mostrar_tributos(self):

        file = open("tributos.csv")
        a = file.readline().split(",")
        b = file.readlines()
        a[-1] = a[-1].strip()
        
        for i in range(12):
            print("Tributo {}".format(i + 1))

            for n in range(9):
                print("{caract}: {dato}".format(caract = a[n].title(), dato = b[i].split(",")[n]))

    
    def elegir_tributo(self):

        print("Los tributos para su selección son los siguientes:\n")
        self.mostrar_tributos()
        
        while True:

            try:

                mi_tributo = int(input("\nEliga uno utilizando el número respectivo del tributo a seleccionar: "))

                if mi_tributo <= 12 and mi_tributo > 0:

                    file = open("tributos.csv")
                    a = file.readlines()
                    return a[mi_tributo].split(",")[0]

                else:
                    print("\nDEBES INGRESAR UN NUMERO ENTRE 1 Y 12! VO TENI QUE SER DEL HUACHIPATO WEON")
            
            except (ValueError):
                print("\nDEBES INGRESAR UN NUMERO ENTRE 1 Y 12! VO TENI QUE SER DEL HUACHIPATO WEON")
                pass
    

    def get_info(self, nombre, index):
        
        tributos = open("tributos.csv")
        
        for i in tributos.readlines():

            if nombre == i.split(",")[0]:
                return i.split(",")[index].rstrip()




        
"""
n = Eleccion()
print(n.get_info("Christian-Klempau",1))      """


    
        
          

            


        