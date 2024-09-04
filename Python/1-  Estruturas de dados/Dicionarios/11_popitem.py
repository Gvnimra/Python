contatos = {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('giovani@gmail.com', {'nome': 'Giovani', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError