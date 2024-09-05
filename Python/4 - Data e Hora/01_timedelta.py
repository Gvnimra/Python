from datetime import datetime, timedelta

tipo_carro = input("""
  (TESTE!!!)                   
  Lava-Rápido!                  
                                    
  Por favor, informe o porte do veículo:
  [P] - Pequeno Porte
  [M] - Médio porte
  [G] - Grande porte
                   
  informe aqui => """) # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P" or tipo_carro == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M" or tipo_carro == "m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "G" or tipo_carro == "g":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    print("ERRO: Tipo de veículo não localizado!")


    