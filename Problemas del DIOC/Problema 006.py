"""Diseñar un programa que dadas las coordenadas cartesianas (x, y, z)\
de un punto en el espacio, calcule y muestre sus coordenadas cilíndricas\
y sus coordenadas esféricas."""
import math
print("Ingrese valores para las coordenadas cartesianas x,y,z: ")
x, y, z = int(input("x: ")),int(input("y: ")),int(input("z: "))
#Cilindricas
angulo_ro = (x**2 + y**2)**0.5
angulo_fi = 0
if x == 0:
    angulo_fi = 90
elif y == 0:
    angulo_fi = 0
elif x > 0 and y > 0:
    angulo_fi = math.degrees(math.atan(y/x))
elif x < 0 and y > 0:
    angulo_fi = 90 - math.degrees(math.atan(y/x))
elif x < 0 and y < 0:
    angulo_fi = 180 + math.degrees(math.atan(y/x))
elif x > 0 and y < 0:
    angulo_fi = 270 - math.degrees(math.atan(y/x))
print("({}, {}, {})".format(angulo_ro,angulo_fi,z))
#Esfericas
if z == 0:
    angulo_tita = 90
elif angulo_ro == 0:
    angulo_tita = 0
elif z > 0 and angulo_ro > 0:
    angulo_tita = math.degrees(math.atan(angulo_ro/z))
elif z < 0 and angulo_ro > 0:
    angulo_tita = 180 + math.degrees(math.atan(angulo_ro/z))
radio = (angulo_ro**2 + z**2)**0.5
print("({}, {}, {})".format(radio,angulo_tita,angulo_fi))
