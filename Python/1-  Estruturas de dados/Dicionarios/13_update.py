contatos = {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}}

contatos.update({"giovani@gmail.com": {"nome": "Gigi"}})
print(contatos)  # {'giovani@gmail.com': {'nome': 'Gigi'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'giovani@gmail.com': {'nome': 'Gigi'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)