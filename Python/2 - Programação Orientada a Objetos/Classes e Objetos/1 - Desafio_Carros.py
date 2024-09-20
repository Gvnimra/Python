class Carro:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 

    def buzinar(self):
        print("PIIIII!!!")

    def parar(self):
        print("Parando carro...")
        print("CArro Parado!")

    def correr(self):
        print("Vruuumm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
volkswagen = Carro("Prata", "Gol", 2024, 35000)
volkswagen.correr()
volkswagen.buzinar()
volkswagen.parar()
print(volkswagen.ano, volkswagen.cor, volkswagen.valor)

fiat = Carro("Vermelho", "Palio", 2023, 28500)
fiat.buzinar()
print(fiat.cor)


