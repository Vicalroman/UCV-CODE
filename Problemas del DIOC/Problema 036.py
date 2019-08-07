"""En la filosofía de ¿Por qué hacerlo fácil? ¡Si se puede hacer difícil! Debe saber que
la parte entera de la raíz cuadrada de un número, puede calcularse como la
cantidad de sumas de números impares sucesivos que hay que hacer para
totalizar el número sin sobrepasarse del mismo. Como ejemplo tome el número 36
y obtiene 1+3+5+7+9+11 cuya suma es 36 observe que se han tomado 6 valores
y esta cantidad es la raíz cuadrada de 36 (se le invita a hacer la prueba con otros
valores). Realice un programa en que basado en el criterio anterior calcule la parte
entera de la raíz cuadrada de un número entero positivo N, leído como dato."""
print("Vamos a buscar la parte entera de la raiz de un numero.")
numero = int(input("Indique un numero: "))
n, lista = 0, []
while sum(lista) < numero :
    if sum(lista) + (2 * n + 1) > numero:
        break
    elif sum(lista) < numero:
        lista.append(2 * n + 1)
        n += 1
print("La parte entera de la raiz del numero es {}.".format(len(lista)))
