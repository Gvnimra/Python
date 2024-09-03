contatos = {"giovani@gmail.com": {"nome": "Giovani", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["giovani@gmail.com"] = {"nome": "Gigi"}

print(contatos["giovani@gmail.com"])  # {"nome": "giovani", "telefone": "3333-2221"}

print(copia["giovani@gmail.com"])  # {"nome": "Gigi"}