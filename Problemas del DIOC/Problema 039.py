"""Un número narcisista es aquel número entero y positivo, que es igual a la suma
de cada uno de sus dígitos elevados a la "n" potencia (donde "n" es el número de
cifras del número). La metáfora de su nombre alude a lo mucho que parecen
"quererse a sí mismos" estas cifras. Por ejemplo, el 153 es un número narcisista
puesto que 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153. Los primeros números narcisistas
son: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474 y 54748.
Realice un programa que indique si un número entero y positivo leído como dato
es un número narcisista."""
print("Vamos a analizar si un numero entero positivo es narcisista.")
numero = int(input("Ingrese un numero entero positivo: "))
#Transformamos el numero dado en un objeto iterable
numero_2 = list(str(numero))
#Como la lista esta compuesta por strings lo llevamos a enteros
lista = [int(i) for i in numero_2]
#elevamos a la cantidad de cifras que tiene el numero a cada elemento de la lista
lista_2 = [i**len(numero_2) for i in lista]
#Ahora realizamos la condicion y la salida
if sum(lista_2) == numero:
    print("El numero {} es narcisista.".format(numero))
else:
    print("El numero no es narcisista.")
#El problema se puede hacer mas resumido intente hacerlo lo mas optimo posible
