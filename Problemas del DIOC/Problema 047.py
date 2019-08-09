"""Se dice que un número entero y positivo es cubifinito cuando al elevar todos sus
dígitos al cubo y sumarlos el resultado es 1, o da otro número cubinfinito. Por
ejemplo, el número 1234 realizamos lo siguiente 1**3+2**3+3**3+4**3 = 100
que es cubifinito. Como contraejemplo el número 513 no cumple con lo indicado.
Elabore un programa que indique si un número dado por el usuario cumple con esta
definición."""
print("Vamos a determinar si un numero es cubifinito.")
num = int(input("Ingrese un numero entero positivo: "))
numero = list(str(num))
lista = [int(i) for i in numero]
suma = sum([i**3 for i in lista])
suma_l = list(str(suma))
lista_2 = [int(i) for i in suma_l]
suma_2 = sum([i**3 for i in lista_2])
if suma_2 == 1:
    print("El numero {} es cubifinito.".format(num))
else:
    print("El numero {} no es cubifinito.".format(num))
