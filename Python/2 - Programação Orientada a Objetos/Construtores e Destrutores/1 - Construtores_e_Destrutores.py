class Cachorro:
    def __init__(self, nome, cor, acordado = True): #Metodo Construtor
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self): #Metodo Destrutor
        print("Removendo a instância da classe.")

    def latir(self):
        print("AU AU")

def criar_cachorro():
    c = Cachorro("Toby", "Verde", False)
    print(c.nome)

c = Cachorro("Milu", "Cinza")
del c   

print("Teste1")
print("Teste2")
print("Teste3")


criar_cachorro()

