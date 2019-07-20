"""Diseñe un programa que dada una cantidad de segundos, entera y positiva,\
indique a cuanto equivale en años, meses, días, horas y segundos.\
Asuma años de 360 días y simplifique a que todos los meses poseen 30 días.\
Por ejemplo: 31.803.310 segundos equivalen a 1 año, 3 días, 2 horas, 15 minutos\
y 10 segundos."""
#Por lo largo que puede ser el codigo se van a definir unas funciones
def years(s):
    year = 31104000 #Cantidad de segundos en un año definido
    if s / year < 1: #Condicion para casos en lo que no alcance para 1 año
        return 0, s #return es lo que indica los datos que va a arrojar la funcion una vez sea llamada
    else: #Caso en que si alcance para mas de un año
        return s//year, s % year #Retorna la cantidad de años y los segundos restantes
def months(s):
    month = 2592000
    if s / month < 1:
        return 0, s
    else:
        return s // month, s % month
def days(s):
    day = 86400
    if s / day < 1:
        return 0, s
    else:
        return s // day, s % day
def hours(s):
    hour = 3600
    if s / hour < 1:
        return 0, s
    else:
        return s // hour , s % hour
def minutes(s):
    minute = 60
    if s / minute < 1:
        return 0, s
    else:
        return s // minute, s % minute
s = int(input("Ingrese la cantidad de segundos: "))
y, seg = years(s)#La funcion retorna dos valores en forma de tupla, pero se le asigna un elemento de la tupla a una variable respectivamente
m, seg = months(seg)
d, seg = days(seg)
h, seg = hours(seg)
min, seg = minutes(seg)
print("\nLa cantidad de {} segundos equivalen a {} año(s), {} mes(es), {} dia(s), {} hora(s), {} minuto(s) \
y {} segundo(s)".format(s, y, m, d, h, min, seg))
