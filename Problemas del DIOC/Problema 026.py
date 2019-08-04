"""Desarrolle un programa que indique si un número entero positivo dado como dato
es lo que se conoce como número primo o no."""
print("Vamos a ver si un numero es primo.")
numero = int(input("Indique un numero entero positivo: "))
divisores = [i for i in range(1, numero + 1) if numero % i == 0]
if len(divisores) <= 2:
    print("Es primo.")
else:
    print("No es primo.")
