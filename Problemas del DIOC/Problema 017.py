"""Realizar un programa que determine el mayor, el menor y el valor intermedio de
tres números enteros y positivos dados como datos. Considere que el usuario
puede suministrar los valores en cualquier orden. """
print("Vamos a analizar tres valores de mayor a menor.")
valor_1, valor_2, valor_3 = int(input("Ingrese tres valores.\nX: ")), int(input("Y: ")), int(input("Z: "))
lista = [valor_1, valor_2, valor_3]
lista_2 = [j for j in range(1, max(lista)+1) for i in lista if i == j]
print("El mayor es {} el valor intermedio es {} el valor menor es {}.".format(lista_2[2], lista_2[1], lista_2[0]))
