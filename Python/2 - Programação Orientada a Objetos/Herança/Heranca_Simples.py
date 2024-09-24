class Veiculo: 
    def __init__(self, cor, placa, numero_rodas, chassi, modelo, marca, ano, nome_proprietario):

        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.chassi = chassi
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.nome_proprietario = nome_proprietario
    
    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join
        ([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):

    def __init__(self, carregado, cor, placa, numero_rodas, chassi, modelo, marca, ano, nome_proprietario):
        super().__init__(cor, placa, numero_rodas, chassi, modelo, marca, ano, nome_proprietario)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2, "ABC1234ABC", "Fazer150", "Yamaha", 2022, "Jaspion da Silva")

carro = Carro("Azul", "CBA4321", 4, "987654ABCD123", "Marea", "Fiat", 2003, "Giovani de Moura André")

caminhao = Caminhão(False, "preto", "ZXC4567", 6, "QWER4567896EWQ", "Constellation 6x2", "Volkswagen", 2024, "Bino")

print("-" * 150)
print("VEICULOS CADASTRADOS".center(150))
print("-" * 150)
print(moto)
print("-" * 150)
print(carro)
print("-" * 150)
print(caminhao)
print("-" * 150)

