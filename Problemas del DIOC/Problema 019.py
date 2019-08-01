"""Diseñe un programa que, dada la longitud de tres segmentos de recta, indique
si los con ellos se puede formar un triángulo Acutángulo, Rectángulo o
Obtusángulo."""
import math
def tipoDeTriangulo():
    alpha = angulosDelTriangulo(longitud_1,longitud_2,longitud_3)
    beta = angulosDelTriangulo(longitud_1,longitud_3,longitud_2)
    gamma = angulosDelTriangulo(longitud_2,longitud_3,longitud_1)
    if alpha == 90 or gamma == 90 or beta == 90:
        print("Es un triagulo rectangulo.")
    elif alpha > 90 or gamma > 90 or beta > 90:
        print("Es un triangulo obtuso.")
    elif alpha < 90 and gamma < 90 and beta < 90:
        print("Es un triangulo acutangulo.")
def angulosDelTriangulo(a,b,c):
    angle = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    return round(angle)
print("Vamos a identificar triangulos segun la longitud de sus lados.")
longitud_1 = float(input("Ingresa la longitud del primer lado: "))
longitud_2 = float(input("Ingresa la longitud del segundo lado: "))
longitud_3 = float(input("Ingresa la longitud del tercer lado: "))
#Utilizando la desigualdad de triangulos.
if not (longitud_1 + longitud_2 > longitud_3 and longitud_2 + longitud_3 > longitud_1 and\
longitud_3 + longitud_1 > longitud_2):
    print("No es un triangulo.")
else:
    tipoDeTriangulo()
