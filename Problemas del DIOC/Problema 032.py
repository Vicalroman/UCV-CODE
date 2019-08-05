"""Se dice que dos números M y N, enteros y positivos, profesan Amistad
Matemática entre sí, cuando al sumar los divisores de M (salvo él mismo) se
obtiene N y al sumar todos los divisores de N (salvo él mismo) se obtiene M. Por
ejemplo:
 los divisores de 220 son: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 que al
sumarlos da 284, y
 los divisores de 284 son: 1, 2, 4, 71, 142 que al sumarlos da 220
Generar un programa que dados dos números indique si los mismos profesan
mutua amistad matemática."""
print("Vamos a determinar si dos numeros profesan una profunda amistad matematica.")
N, M = int(input("Ingrese un numero entero positivo: ")), int(input("Ingrese otro numero entero positivo: "))
divisores_N = [i for i in range(1, N) if N % i == 0]
divisores_M = [i for i in range(1, M) if M % i == 0]
if sum(divisores_N) == M and sum(divisores_M) == N:
    print("Estos numeros tienen una profunda amistad matematica.")
else:
    print("Estos numeros no son panas.")
