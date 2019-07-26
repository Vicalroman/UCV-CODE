"""Ork el planeta natal de Mork celebra un gran festejo planetario cada ocho años, de
manera similar cada 72 años se celebra el cumpleaños de Orson y para hacerlo en
grande se festeja también al año siguiente, pero cada 48 años la celebración que
pudiese haber ese año se suspende debido al penoso recuerdo que dejó la derrota
con su planeta enemigo en las Guerras Impúdicas. Realice un programa para saber
si un año dado como dato es o no festivo. Asuma que el conteo de los años
empezó en el año uno."""
año = int(input("Ingrese un año a comprobar: "))
bool_1 = año % 8 == 0
bool_2 = año % 72 == 0
bool_3 = ((año - 1) % 72) == 0
bool_4 = año % 48 == 0
if bool_4:
    print("Se suspenden las celebraciones por la derrota en las Guerras Impudicas.")
elif bool_3:
    print("Continua la celebracion del año pasado(El cumpleaños de Orson).")
elif bool_1 and bool_2:
    print("Se celebra el festejo planetario y el cumpleaños de Orson.")
elif bool_1:
    print("Se celebra el festejo planetario.")
elif bool_2:
    print("Se celebra el cumpleaños de Orson.")
else:
    print("No es festivo.")
