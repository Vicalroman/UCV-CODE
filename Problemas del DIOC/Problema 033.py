"""Existe lo que se llama la Amistad Cuadrática entre dos números cuando se
cumple lo que se narra en el siguiente ejemplo para los números 13 y 16:
El número 16 elevado al cuadrado da 256 y sumando sus dígitos 2+5+6-->13
El número 13 elevado al cuadrado da 169 y sumando sus dígitos 1+6+9--> 16
Cuando lo anterior sucede se dice que los números profesan amistad cuadrática.
Realizar un programa que indique si dos números dados como datos profesan
amistad cuadrática."""
print("Vamos a determinar si dos numeros profesan una amistad cuadratica.")
numero_1, numero_2 = int(input("Ingrese un numero entero positivo: ")),\
int(input("Ingrese un segundo numero entero positivo: "))
cuadrado_1 = sum([int(i) for i in list(str(numero_1**2))])
cuadrado_2 = sum([int(i) for i in list(str(numero_2**2))])
if cuadrado_1 == numero_2 and cuadrado_2 == numero_1:
    print("Estos numeros profesan una amistad cuadratica.")
else:
    print("Estos numeros no son panas.")
