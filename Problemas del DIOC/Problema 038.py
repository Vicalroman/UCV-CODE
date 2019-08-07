"""Definamos N como número suficiente si cumple las siguientes características:
ser entero positivo, impar y al sumar todos sus divisores (salvo él mismo) da un
valor superior a N. Diseñe un programa que indique cuántos números suficientes
existen por debajo de un valor M dado como dato."""
print("Vamos a analizar cuantos numeros suficientes existen debajo un valor.")
M = int(input("Indique un valor entero positivo: "))
N = 0
n_suficientes = []
while N < M:
    divisores = [i for i in range(1, N) if N % i == 0]
    impar = N % 2 != 0
    suma = sum(divisores) > N
    if impar and suma:
        n_suficientes.append(N)
    N += 1
print("Debajo de M hay {} numeros suficientes.".format(len(n_suficientes)))
print(n_suficientes)
