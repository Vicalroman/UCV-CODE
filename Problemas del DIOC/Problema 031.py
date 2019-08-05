"""Un número entero positivo se le llama primo capicúa cuando siendo primo
también es primo cuando se invierten sus dígitos. Así tenemos que 17, 31, 37 y
113 son ejemplos de primos capicúas pues 71, 13, 73, 311 son también primos.
Diseñe un programa para indicar si un número N dado como dato es primo
capicúa."""
print("Vamos a determinar si un numero es primo capicua.")
N = input("Introduzca un numero: ")
if len([i for i in range(1,int(N) + 1) if int(N) % i == 0]) <= 2:
    primo =True
else:
    primo = False
if primo:
    primo_capicua = 0
    capicua = [int(i) for i in list(reversed(list(N)))]
    for i in range(len(capicua)):
        primo_capicua = primo_capicua + capicua[i]*(10**i)
    if len([i for i in range(1, primo_capicua) if primo_capicua % i == 0]) == 2:
        print("Es primo capicua.")
    else:
        print("No es primo capicua.")
else:
    print("No es primo capicua.")
