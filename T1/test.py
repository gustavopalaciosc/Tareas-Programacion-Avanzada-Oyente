class test:

    def __init__(self, nombre, *args):

        self.nombre = nombre
        self.areas = []

        for i in args:
            self.areas.append(i)

a = test("Gustavo", "Programacion", "Economia")
print(a.nombre)
print(a.areas)

        