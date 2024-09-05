import datetime
import pytz

#criando datetime com timezone

d= datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
d2 = datetime.datetime.now(pytz.timezone("Europe/Oslo"))

print(d)
print(d2)

#criando datetime com timezone

d3 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(d3)

#convertendo para outro time zone
d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)
