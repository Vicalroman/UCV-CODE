"""Diseñe un programa que, dado un recipiente cilíndrico, solicite los datos\
pertinentes para poder calcular su volumen y área, y mostrar tales resultados."""
import math #Se necesita el valor de pi, si no sé importa math se puede calcular el valor de pi
#Solicitamos los datos
r, h = float(input("Ingrese el radio del cilindro\nr: ")),\
float(input("Ingrese la altura del cilindro\nh: "))
#Imprimos los resultados
print("El volumen del cilindro es {}".format(math.pi*r*h))
print("El area del cilindro es {}".format(2*math.pi*r*(h+r)))
