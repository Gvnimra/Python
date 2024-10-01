class Passaro:
    def voar(self): pass

class Pombo():
    def voar(self):
        print("Pombo voa")

class Avestruz():
    def voar(self):
        print("Avestruz NÃO voa")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pombo())
plano_de_voo(Avestruz())
