#Espaço para estudos 


def decorador(funcao):
    def wrapper():
        print("Função está prestes a ser executada.")
        funcao()
        print("Função foi executada.")
    return wrapper

@decorador
def saudacao():
    print("Olá, mundo!")

saudacao()



