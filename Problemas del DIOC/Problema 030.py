"""Un número capicúa es aquel que leído de izquierda a derecha es el mismo que
leído de derecha a izquierda, por ejemplo 124421. Desarrolle un programa que
determine si un número dado por el usuario es capicúa o no. Como condición se le
impone que no puede usar artificios basados en el manejo de cadenas
alfanuméricas."""
print("Vamos a determinar si un numero es capicua.")
numero = list(input("Ingrese un numero entero: "))
if numero == list(reversed(numero)):
    print("Es un numero capicua.")
else:
    print("No es un numero capicua.")
