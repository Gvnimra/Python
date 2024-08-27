#Interpolaçao de variaveis 

print("INTERPOLACAO DE VARIAVEIS")
print()
print("Old Style % ")
print()
nome = "Giovani de Moura André"
idade = 31 
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Giovani de Moura André", "idade": 28, "profissao": "programador", "linguagem": "Python"}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou estudando %s." %(nome, idade, profissao, linguagem))
print()
print("MÉTODO FORMAT")
print()
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou estudando {}." .format(nome, idade, profissao, linguagem))
print()
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou estudando {0}." .format(linguagem, profissao, idade, nome))
print()
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou estudando {linguagem}." .format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
print()
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou estudando {linguagem}." .format(**pessoa))
print()

print("F-String")
print()
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou estudando {linguagem}.")
print()
PI = 3.14159
print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")



