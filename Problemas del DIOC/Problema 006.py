"""Diseñar un programa que dadas las coordenadas cartesianas (x, y, z)\
de un punto en el espacio, calcule y muestre sus coordenadas cilíndricas\
y sus coordenadas esféricas."""
import math
print("Ingrese valores para las coordenadas cartesianas x,y,z: ")
x,y,z = int(input("x: ")),int(input("y: ")),int(input("z: "))
#Cilindricas
ro = (x**2 + y**2)**0.5
fi = 0
if x == 0:
    fi = 90
elif y == 0:
    fi = 0
elif x > 0 and y > 0:
    fi = math.degrees(math.atan(y/x))
elif x < 0 and y > 0:
    fi = 90 - math.degrees(math.atan(y/x))
elif x < 0 and y < 0:
    fi = 180 + math.degrees(math.atan(y/x))
elif x > 0 and y < 0:
    fi = 270 - math.degrees(math.atan(y/x))
print(ro,fi,z)
#Esfericas
if z == 0:
    tita = 90
elif ro == 0:
    tita = 0
elif z > 0 and ro > 0:
    tita = math.degrees(math.atan(ro/z))
elif z < 0 and ro > 0:
    tita = 180 + math.degrees(math.atan(ro/z))
r = (ro**2 + z**2)**0.5
print("(",r,tita,fi,")")
