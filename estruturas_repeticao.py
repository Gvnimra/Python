#Estruturas de repetição

#Primeiro Exemplo: Receba um número do teclado e exiba os 2 numeros seguintes

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#FOR, FOR ELSE

texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa o final do laço")

#Exemplo utilizando a função Built-in range

for numero in range(0, 11):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")

#WHILE, While Else

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o extrato... ")
else: 
    print("Obrigado por usar nosso sistema bancário, até logo")

#BREAK

while true:
    num = int(input("Informe um número: "))

    if num == 10:
        break
    print(num)

for num2 in range(100):

    if num2 == 12:
        break
    print(num2, end=" ")
