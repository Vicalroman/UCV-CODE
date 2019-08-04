"""En un tablero de ajedrez se coloca en la primera casilla un grano de arroz, en la
segunda se coloca el doble de granos que en la anterior y así sucesivamente hasta
la 64ava casilla. Diseñe un programa para presentar un listado en donde se indique
el número de la casilla, el número de granos colocados en esa casilla y la suma de
los granos acumulados hasta esa casilla."""
numero_de_casilla = int(input("Indique por favor el numero de la casilla: "))
if numero_de_casilla > 0 and numero_de_casilla < 65:
     granos = 2**(numero_de_casilla - 1)
     granos_acumulados = sum([2**(i - 1) for i in range(1, numero_de_casilla + 1)])
print("El numero de la casilla indicado es {}.".format(numero_de_casilla),\
"\nEl numero de granos colocados en la casilla es {}.".format(granos),\
 "\nLa cantidad de granos acumulados hasta la casilla es {}.".format(granos_acumulados))
