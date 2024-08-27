#Estruturas Condicionais 

#If, Elif, Else

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
conta_normal = True
conta_universitaria = False
cheque_especial = 150

if saldo >= saque:
    print("realizando saque!")
    
else:
    print("Saldo insuficiente!")

#Outro exemplo

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("informe a quantia para sacar: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    SystemExit("Opção inválida")

#If Aninhado 

if conta_normal: 
    if saldo >= saque: 
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saldo realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu o seu to´p de conta, entre em contato com o seu Gerente!")

#If Ternario 

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")



