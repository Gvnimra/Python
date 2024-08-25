#Manipulando Strings 

print("CONHECENDO MÉTODOS ÚTEIS DA CLASSE STRING!")

print()

curso = "pYtHoN"

print("Aprendendo manipulação de Strings: Maíuscula, minúscula e título")
print()
print(curso)
print(curso.upper())
print(curso.lower())
print(curso.title())
print()
print("Eliminando espaços em branco")
print()
curso_2 = "     Python  "
print()
print(curso_2)
print(curso_2.strip())
print(curso_2.lstrip())
print(curso_2.rstrip())
print()
print("Junções e centralização")
curso_3 = "Python"
print(curso_3.center(10, "#"))
print(".".join(curso_3))

