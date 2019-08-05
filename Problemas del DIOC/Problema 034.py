"""Realice un programa que calcule y muestre el Máximo Común Divisor de dos
números naturales dados como datos."""
print("Vamos a calcular el maximo comun divisor de dos numeros naturales.")
numero_1, numero_2 = int(input("Indique un numero natural: ")), int(input("Indique un segundo numero natural: "))
#descomponemos en factores primos
factor = 2
factores_primos_1 = []
while numero_1 > 1:
    if numero_1 % factor == 0:
        numero_1 = numero_1 / factor
        factores_primos_1.append(factor)
    else:
        factor += 1
factor = 2
factores_primos_2 = []
while numero_2 > 1:
    if numero_2 % factor == 0:
        numero_2 = numero_2 / factor
        factores_primos_2.append(factor)
    else:
        factor += 1
max_com_div = []
for i in factores_primos_1:
    for j in factores_primos_2:
        if i == j:
            max_com_div.append(i)
            factores_primos_1.remove(i)
            break
if max_com_div is not []:
    print("El maximo con un divisor es: {}".format(max_com_div))
else:
    print("No tiene maximo con un divisor.")
