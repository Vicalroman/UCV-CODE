"""Se dice que un número natural es Poderoso cuando al menos uno de sus
divisores (excepto el 1) es primo y que este divisor elevado al cuadrado, también
divida de forma exacta al número. Por ejemplo: el número 36 tiene los siguientes
divisores 2, 3, 4, 6, 9 y 12 donde 2**2 es 4, que divide de forma exacta a 36 (igual
pasa con 3). Realice un programa que dado un número entero suministrado por
usuario indique si cumple con la definición ofrecida. """
print("Vamos a determinar si un numero es poderoso.")
num = int(input("Ingrese un numero natural: "))
#definire una funcion que identifique los divisores de un numero
def divisores(n):
    div = [i for i in range(1,n) if num % i == 0]
    return div
#retorna una lista con los divisores de un numero
#definire una funcion que identifique los numeros primos
def esPrimo(n):
    lista = divisores(n)
    if len(lista) <= 2:
        return n
#lista de numeros primos divisores del numero natural
primos = [esPrimo(i) for i in divisores(num) if esPrimo(i) != None]
#Hacemos un condicional la funcion any indica que si al menos una vez se cumple
#la condicion en el iterable, arroja True. Otra funcion util es all, seria el caso
#para cuando se cumplen todas las condiciones dentro del iterable.
if any([num % i == 0 for i in primos]):
    print("El numero {} es un numero poderoso.".format(num))
else:
    print("El numero {} no es un numero poderoso.".format(num))
