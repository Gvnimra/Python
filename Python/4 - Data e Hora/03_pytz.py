import datetime
import pytz

#criando datetime com timezone

d= datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)
