"""Diseñar un programa que al introducir parte de la fecha de nacimiento (día y mes)
muestre el nombre del signo del zodíaco correspondiente. Asuma las fechas
estándar ofrecidas para cada signo."""
print("Vamos a decirle su signo zodiacal.")
dia, mes = int(input("Dia de nacimiento: ")), str.lower(input("Mes de nacimiento: "))
meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
"agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
if len(mes) > 2:
    mes = meses[mes]
elif len(mes) <= 2:
    mes = int(mes)
if (mes == 3 and dia >= 21 and dia <=  31) or (mes == 4 and dia >= 1 and dia <= 20):
    print("Su signo zodiacal es Aries.")
elif (mes == 4 and dia >= 21 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 20):
    print("Su signo zodiacal es Tauro.")
elif (mes == 5 and dia >= 21 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 24):
    print("Su signo zodiacal es Geminis.")
elif (mes == 6 and dia >= 25 and dia <= 30) or (mes == 7 and dia >= 1 and dia <= 22):
    print("Su signo zodiacal es Cancer.")
elif (mes == 7 and dia >= 23 and dia <= 31) or (mes == 8 and dia >= 1 and dia <= 23):
    print("Su signo zodiacal es Leo.")
elif (mes == 8 and dia >= 24 and dia <= 31) or (mes == 9 and dia >= 1 and dia <= 23):
    print("Su signo zodiacal es Virgo.")
elif (mes == 9 and dia >= 24 and dia <= 30) or (mes == 10 and dia >= 1 and dia <= 22):
    print("Su signo zodiacal es Libra.")
elif (mes == 10 and dia >= 23 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 22):
    print("Su signo zodiacal es Escorpio.")
elif (mes == 11 and dia >= 23 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 21):
    print("Su signo zodiacal es Sagitario.")
elif (mes == 12 and dia >= 22 and dia <= 31) or (mes == 1 and dia >= 1 and dia <= 19):
    print("Su signo zodiacal es Capricornio.")
elif (mes == 1 and dia >= 20 and dia <= 31) or (mes == 2 and dia >= 1 and dia <= 18):
    print("Su signo zodiacal es Acuario.")
elif (mes == 2 and dia >= 19 and dia <= 29) or (mes == 3 and dia >= 1 and dia <= 20):
    print("Su signo zodiacal es Piscis.")
else:
    print("Por favor introduzca una fecha valida.")
