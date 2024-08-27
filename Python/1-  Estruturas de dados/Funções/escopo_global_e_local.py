salario = 2000

def salario_bonus(bonus, lista):
    global salario
    salario += bonus
    return salario


lista = [1]
salario_bonus(500, lista)
print(salario_bonus)
print(lista)

