"""Diseñe un programa que indique si un número entero y positivo “M” leído como
dato, es perfecto o no. Sabiendo que un número es perfecto cuando la suma de
todos sus divisores, salvo él mismo, es igual al mismo número. Por ejemplo: 6 es
dividido de manera exacta por 1, 2 y 3 que al sumarlos da el valor origina: 6."""
print("Vamos a determinar si un numero es perfecto.")
n = 10
while n > 0:
    try:
        M = int(input("Indique un numero entero: "))
        break
    except ValueError:
        print("\nValor invalido intente nuevamente")
        n -= 1
divisores = [i for i in range(1, M) if M % i == 0]
suma = sum(divisores)
if suma == M:
    print("Es un numero perfecto.")
else:
    print("No es un numero perfecto.")
