print("FUNÇÕES")

def exibir_mensagem():
    print("Olá Mundo! Testando Funções em Python")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Olá, seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome= "Giovani")
exibir_mensagem_3(nome = "Max Payne")

def calcular_numeros(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor
print(calcular_numeros([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print()

print("################### CADASTRAMENTO DE VEÍCULOS ###################")
print()

def salvar_veiculo(marca, modelo, ano, placa):
    #salva o veiculo no banco de dados...
    print(f"Veiculo inserido com sucesso no sistema!{marca}/{modelo}/{ano}/{placa}")

salvar_veiculo("Fiat", "Palio", 1999, "ABC-1234")
salvar_veiculo(marca = "Fiat", modelo ="Palio", ano = 1999, placa = "ABC-1234")
salvar_veiculo(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})