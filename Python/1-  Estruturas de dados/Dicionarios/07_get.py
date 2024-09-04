contatos = {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "giovani@gmail.com", {}
)  # {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}
print(resultado)