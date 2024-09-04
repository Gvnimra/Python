contato = {"nome": "Giovani", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Giovani"
print(contato)  # {'nome': 'Giovani', 'telefone': '3333-2221'}

contato.setdefault("idade", 31)  # 31
print(contato)  # {'nome': 'Giovani', 'telefone': '3333-2221', 'idade': 31}