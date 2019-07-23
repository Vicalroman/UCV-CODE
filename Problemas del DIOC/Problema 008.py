"""Diseñe un programa que dado un punto en el plano por sus coordenadas (x,y),
determinar en qué cuadrante se encuentra indicándolo con un mensaje al
usuario."""
x, y = float(input("Ingrese las coordenadas del punto: \nx: ")), float(input("y: "))
bool1 = x > 0
bool2 = y > 0
if x == 0:
    if y == 0:
        print("El punto esta en el origen.")
    elif bool2:
        print("El punto esta sobre el eje de las ordenadas positivo.")
    else:
        print("El punto esta sobre el eje de las ordenadas negativo.")
elif y == 0:
    if bool1:
        print("El punto esta sobre el eje de las abscisas positivo.")
    else:
        print("El punto esta sobre el eje de las abscisas negativo.")
elif bool1 and bool2:
    print("El punto esta en el primer cuadrante.")
elif not bool1 and bool2:
    print("El punto esta en el segundo cuadrante.")
elif not bool1 and not bool2:
    print("El punto esta en el tercer cuadrante.")
else:
    print("El punto esta en el cuarto cuadrante.")
