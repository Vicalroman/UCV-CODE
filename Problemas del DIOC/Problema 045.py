"""Se dice que un número entero y positivo de N dígitos es n-pandigital si dicho
número contiene todos los dígitos de 1 a N sólo una vez. Por ejemplo, los números
15423 y 12435 son 5-pandigitales. Realice un programa que dado un valor leído
como dato indique si el mismo es n-pandigital. Como limitante, no puede
emplear funciones para manejos de alfanuméricos."""
print("Vamos a determinar si un numero es n-pandigital.")
num = int(input("Ingrese un numero: "))
numero = num
count = 0
lista = []
while num > 1:
    lista.append(int(num % 10))
    num = num / 10
    count += 1
n_pan = True
for i in lista:
    for j in lista:
        if i == j:
            n_pan = False
if n_pan:
    print("El numero {} es {}-pandigital.".format(numero, count))
else:
    print("El numero {} no es n-pandigital.".format(numero))
