contatos = {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}}

resultado = contatos.pop("giovani@gmail.com")  # {'nome': 'Giovani', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("giovani@gmail.com", {})  # {}
print(resultado)