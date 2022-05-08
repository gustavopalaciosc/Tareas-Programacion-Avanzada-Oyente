class a():
    def __init__(self, vida):
       self.vida = vida
       
class b():
    def __init__(self, mia):
        self.mia = mia

    def subir_vida(self):
        self.mia.vida += 12

class c():
    def __init__(self, mia):
        self.mia = mia

    def mult_vida(self):
        self.mia.vida = self.mia.vida * 2


yo = a(100)
b = b(yo)
c = c(yo)
b.subir_vida()
c.mult_vida()

print(yo.vida)
        



