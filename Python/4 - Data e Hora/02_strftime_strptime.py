import datetime

d = datetime.datetime.now()

#formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

#Convertendo string para datetime

date_string = "04/09/2024 22:25"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)
