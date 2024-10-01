class Aluno:
    escola = "Escola de programação"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objts):
    for objts in objts:
        print(objts)


aluno1 = Aluno("Giovani de Moura André", 1)
aluno2 = Aluno("Giovana de Moura André", 2)
mostrar_valores(aluno1, aluno2)



