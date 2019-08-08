"""Se dice que un número natural es Odioso cuando su equivalente en notación
binaria presenta una cantidad impar del número 1. Realice un programa que dado
un número entero suministrado por usuario indique si cumple con la definición
ofrecida."""
print("Vamos a determinar si un numero es odioso.")
numero = int(input("Ingrese un numero natural: "))
#Lo llevamos a binario
binario = bin(numero)
#Se genera un numero binario 0bxxx...
#En este caso lo hare iterable
lista = list(str(binario[2:]))#Utilizamos la herramienta de list slices para
#tomar la porcion de la lista que nos interesa.
#Transformare cada elemento a entero
print(lista)
lista_2 = [int(i) for i in lista]
#Realizamos la condicion
if sum(lista_2) % 2 != 0:
    print("El numero {} es odioso.".format(numero))
else:
    print("El numero {} no es odioso.".format(numero))
#Tambien hay una funcion para transformar a Octal(oct()) y Hexadecimal(hex())
