"""Un número natural se define como Automórfico cuando su cuadrado tiene como
últimas cifras las mismas que ese número. Los primeros números automórficos
son 5, 6, 25, 76, 376, 625... En efecto: 5**2=25, 6**2=36, 25**2= 625, 76**2= 5776."""
#Aunque el problema no lo indique nosotros por efectos del problema haremos un
#programa que identifique numeros naturales Automorficos.
print("Vamos a identificar numeros Automorficos.")
numero = int(input("Indique un numero natural: "))
cuadrado = numero**2
numero, cuadrado, automorfico = list(str(numero)), list(str(cuadrado)), False
for i in range(-1, -len(numero) - 1, -1):
    if numero[i] == cuadrado[i]:
        automorfico = True
    else:
        automorfico = False
        break
if automorfico:
    print("El numero natural se define como Automorfico.")
else:
    print("El numero natural no es Automorfico.")
