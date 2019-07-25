"""Diseñe un programa que, dado un recipiente cilíndrico, solicite los datos\
pertinentes para poder calcular su volumen y área, y mostrar tales resultados."""
import math #Se necesita el valor de pi, si no sé importa math se puede calcular el valor de pi
#Solicitamos los datos
radio, altura = float(input("Ingrese el radio del cilindro.\nRadio: ")),\
float(input("Ingrese la altura del cilindro.\nAltura: "))
#Imprimos los resultados
print("El volumen del cilindro es {}".format(math.pi*radio*altura))
print("El area del cilindro es {}".format(2*math.pi*radio*(altura+radio)))
