"""Dados dos puntos en el plano por sus coordenadas (x1, y1) y (x2, y2),\
diseñe un programa para calcular la ordenada correspondiente a una abscisa x\
cualquiera (también suministrada como dato) empleando interpolacion lineal."""
#Le asignamos a las variables las componentes de los puntos P1 y P2.
#Utilizamos float() para transformar el valor introducido por el usuario en un
#tipo format (Lo recibido en un input es tipo string)
x1, y1 = float(input("Ingrese las coordenadas del primer punto: \nX: ")),\
float(input("Y: "))
x2, y2 = float(input("Ingrese las coordenadas del segundo punto: \nX: ")),\
float(input("Y: "))
x = float(input("Ingrese el valor de la abscisa x: "))
#Imprimimos en pantalla el resultado de la interpolacion lineal directamente.
print((((x-x1)/(x2-x1))*(y2-y1))+y1)
