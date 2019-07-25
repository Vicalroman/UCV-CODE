"""Diseñe un programa que dadas las coordenadas (x,y) de un punto en el plano, determine y muestre sus coordenadas polares (R, θ )."""
import math #Importamos math para la aplicacion de atan(), degrees()
print("Vamos a calcular las coordenadas polares.")
x , y = float(input("Escriba un valor para X: ")) , float(input("Escriba un valor para Y: ")) #Asignamos las variables x,y , la funcion input se encarga de recibir valores introducidos por el usuario
radio = (x**2 + y**2)**(1 / 2) #Calculo de r
print("El radio es igual a " + str(float(radio))) #La funcion print imprime en pantalla lo indicado en su argumento.
#Theta hay que condicionarlo para que arroje el resultado en el cuadrante solicitado
if x == 0: #Si x es igual a cero el arctg tiende a infinito y esto da como resultado 90°
    print("Theta es igual a 90°")
else:
    theta = math.atan(y/x)
    theta1 = math.degrees(theta)
    if x > 0 and y >=0:
        print("Theta es igual a " + str(theta1) + "°")
    elif x < 0 and y == 0:
        print("Theta es igual a " + str(theta1) + "°")
    elif x < 0 and y > 0:
        print("Theta es igual a " + str(90 - theta1) + "°")
    elif x < 0 and y < 0:
        print("Theta es igual a " + str(180 + theta1) + "°")
    elif x > 0 and y == 0:
        print("Theta es igual a 0° " + str(270 - theta1) + "°")
    else:
        print ("Theta es igual a " + str(270 - theta1) + "°")
