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

pombo = Pombo()
avestruz = Avestruz()

plano_de_voo(pombo)
plano_de_voo(avestruz)
