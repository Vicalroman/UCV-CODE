"""Se dice que un número natural es oblongo: si cumple con ser el producto de dos
naturales consecutivos. Por ejemplo, los números 30, 42 y 56 lo son. Diseñe un
programa que indique si un número dado por el usuario cumple con la condición
señalada."""
print("Vamos a determinar si un numero natural es oblongo.")
#Vamos a reducir los nombres de las variables ya evidentes
num = int(input("Ingrese un numero natural: "))
#Busquemos los divisores del numero
div = [i for i in range(1, num + 1) if num % i == 0]
#luego planteamos una posible condicion para numero oblongo.
oblongo = False
for i in range(len(div)):
    if i == (len(div) - 1):
        oblongo = None
    else:
        if div[i] * (div[i] + 1) == num or div[i] * (div[i] - 1) == num:
            oblongo = True
            break
if oblongo:
    print("El numero {} es oblongo.".format(num))
else:
    print("El numero {} no es oblongo.".format(num))
