"""Una pareja prima es un par de números primos separados por dos unidades
(como ejemplo tome 11 y 13, así como el 29 y el 31). Realice un programa para
contabilizar cuantas parejas primas se encuentran entre 2 y un valor N dado como
dato por el usuario."""
print("Vamos a contabilizar cuantas parejas primas hay dentro de un intervalo.")
N = int(input("Ingrese un valor donde terminara el intervalo: "))
#definire una funcion que identifique numeros primos
def esPrimo(n):
    div = [i for i in range(1, n + 1) if n % i == 0]
    if len(div) <= 2:
        return n
#lista de numeros primos hasta el rango acordado
prim = [esPrimo(i) for i in range(2, N + 1) if esPrimo(i) != None]
#Buscaremos parejas que cumplan la condicion
parejas = []
for i in range(len(prim) - 1):
    if prim[i + 1] - prim[i] == 2:
        parejas.append(prim[i])
        parejas.append(prim[i + 1])
    else:
        None
#Por el metodo hecho tendremos que quitar los numeros repetidos
j = None
for i in parejas:
    if j == i:
        parejas.remove(i)
    j = i
#imprimimos el resutlado
print("Desde 2 hasta {} hay un total de {} pares de numeros primos.".format(N, len(parejas)//2))
