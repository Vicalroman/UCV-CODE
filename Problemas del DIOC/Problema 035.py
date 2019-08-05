"""Desarrolle un programa que dados dos números naturales N y M suministrados
por el usuario, calcule el mínimo común múltiplo (mcm) de los mismos. """
print("Vamos a calcular el minimo con un multiplo entre dos numeros naturales.")
N, M = int(input("Indique dos numeros naturales: \nN: ")), int(input("M: "))
factor = 2
factores_primos_1 = []
while N > 1:
    if N % factor == 0:
        N = N / factor
        factores_primos_1.append(factor)
    else:
        factor += 1
factor = 2
factores_primos_2 = []
while M > 1:
    if M % factor == 0:
        M = M / factor
        factores_primos_2.append(factor)
    else:
        factor += 1
min_com_mul = []
for i in factores_primos_1:
    for j in factores_primos_2:
        if i not in min_com_mul:
            min_com_mul.append(i)
        elif j not in min_com_mul:
            min_com_mul.append(j)
print("El minimo con un multiplo es: {}".format(min_com_mul))
