"""Diseñe un programa que dadas las coordenadas (x,y) de un punto en el plano, determine y muestre sus coordenadas polares (R, θ )."""
import math #Importamos math para la aplicacion de atan(), degrees()
x , y = float(input("Escriba un valor para X: ")) , float(input("Escriba un valor para Y: ")) #Asignamos las variables x,y , la funcion input se encarga de recibir valores introducidos por el usuario
r = (x**2 + y**2)**(1/2) #Calculo de r
print("r es igual a " + str(float(r))) #La funcion print imprime en pantalla lo indicado en su argumento.
#Theta hay que condicionarlo para que arroje el resultado en el cuadrante solicitado
if x == 0:
    print("Theta es igual a 90°")
else:
    t= math.atan(y/x)
    t1 = math.degrees(t)
    if x > 0 and y >=0 :
        print("Theta es igual a " + str(t1)+"°")
    elif x < 0 and y == 0 :
        print("Theta es igual a " + str(t1)+"°")
    elif x < 0 and y > 0 :
        print("Theta es igual a " + str(90 - t1)+"°")
    elif x < 0 and y < 0 :
        print("Theta es igual a " + str(180 + t1) +"°")
    elif x > 0 and y == 0 :
        print("Theta es igual a 0° " + str(270 - t1)+"°")
    else:
        print ("Theta es igual a " + str(270 - t1)+"°")
