"""Diseñe un programa que dados dos puntos en el plano por sus coordenadas (x1, y1) y (x2, y2)\
calcule y muestre la longitud del segmento que determinan estos puntos, y que se calculen y\
muestren las coordenadas del punto medio de ese segmento"""
#Se pueden definir los puntos (x1,y1) y (x2,y2), pero para este problema solicitaremos los datos al usuario.
x1, y1 = float(input("Ingrese las coordenadas del primer punto \nX: ")),float(input("Y: "))
#\n realiza un cambio de linea, hacia la linea siguiente.
x2, y2 = float(input("Ingrese las coordenadas del segundo punto \nX: ")),float(input("Y: "))
#Se procede a calcular la longitud del segmento utilizando la famosa formula de la distancia
l = ((x2-x1)**2 + (y2-y1)**2)**0.5 #La potencia de la raiz puede ser "0.5" o "(1/2)" (encerrado entre parentesis obligatoriamente)
print("La longitud del segmento es {}".format(l))#Imprimimos el resultado obtenido aunque el problema no lo pida.
#Las llaves "{}" y el .format() se utilizan para agregar valores variables a una cadena de texto.
#Se puede reducir el codigo imprimiendo de una vez el valor de la longitud sin necesidad de asignar una variable "l" como se muestra en la siguiente linea.
#print("La longitud del segmento es {}".format(((x2-x1)**2 + (y2-y1)**2)**0.5)
