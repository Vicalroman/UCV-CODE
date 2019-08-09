"""Se dice que un número natura es factorion si al sumar los factoriales de los
dígitos que lo componen, dan el mismo número. Por ejemplo, para el número 145
tenemos: 1! + 4! + 5! = 145. Realice un programa que indique si un número
entero y positivo dado como dato por el usuario cumple con esta particular
característica. Nota: 1! = 1 y 2! = 2 no son sumas y por lo tanto no se deben
incluir. Asuma no disponer la función factorial, ni debe emplear funciones de
manejo de alfanuméricos."""
#Bueno ya que nos limitaron el uso de funciones suponemos que tenemos que hacerlo
#sin definir funciones
print("Vamos a determinar si un numero natural es un factorion.")
num = int(input("Ingrese un numero natural: "))
numero = num
numeros = []
count = 0
while num > 1:
    numeros.append(int(num % 10))
    num = num / 10
    count += 1
lista = []
for i in numeros:
    n = 1
    for j in range(1, i + 1):
        n = n * j
    lista.append(n)
if sum(lista) == numero and numero is not 2:
    print("El numero {} es un factorion.".format(numero))
else:
    print("El numero {} no es un factorion.".format(numero))
