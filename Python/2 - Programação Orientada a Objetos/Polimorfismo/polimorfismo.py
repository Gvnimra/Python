class Passaro:
    def voar(self): pass

class Pombo():
    def voar(self):
        print("Pombo voa")

class Avestruz():
    def voar(self):
        print("Avestruz NÃO voa")

def plano_de_voo(objeto):
    objeto.voar()


class Aviao(Passaro): #exemplo ruim do uso de herança para "ganhar" o método voar
    def voar(self):
        print("Avião esta voando...")




pombo = Pombo()
avestruz = Avestruz()

plano_de_voo(pombo)
plano_de_voo(avestruz)
plano_de_voo(Aviao())

