"""Dado un número entero y positivo, genere un programa que invierta los dígitos
del mismo; esto es: dado el número 1234 se debe obtener el número 4321. Como
condiciones se debe tomar en cuenta que no se debe pedir el número de dígitos al
usuario y tampoco se debe emplear ninguna función o procedimiento para trabajar
con valores alfanuméricos. """
print("Vamos a invertir numeros de mas de una cifra.\n")
numero = list(list(input("Indique un numero de mas de 1 cifra: ")))
enteros = [int(i) for i in numero]
resultado = 0
for i in range( len(enteros)):
    resultado = resultado + enteros[i]*(10**i)
print(resultado)
