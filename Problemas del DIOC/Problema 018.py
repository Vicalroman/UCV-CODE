"""Hacer un programa que, dada una hora en el espejo, devuelva la hora real. Por
ejemplo, las 8:05 vista en el espejo es las 3:55."""
#Vamos a considerar horarios de 12 horas
hora, minutos = int(input("Ingrese la hora: ")), int(input("Ingrese los minutos: "))
if hora > 12 or minutos > 59:
    print("Por favor ingrese una hora valida en formato de 12 horas.")
if hora == 12:
    hora = 11
elif hora == 11:
    hora = 12
else:
    hora = 11 - hora
minutos = 60 - minutos
if hora < 10:
    if minutos < 10:
        print("0{}:0{}".format(hora, minutos))
    else:
        print("0{}:{}".format(hora, minutos))
elif (hora > 9 and minutos > 9) and (hora <= 12 and minutos <= 59):
    print("{}:{}".format(hora, minutos))
