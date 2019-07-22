"""Dados tres puntos en el plano por sus coordenadas (x, y), realice un programa
que indique si los mismos se encuentran sobre una misma recta (si son Puntos
Colineales)."""
x,y = int(input("Ingrese el primer punto: \nx: ")), int(input("y: "))
x2,y2 = int(input("Ingrese el segundo punto: \nx: ")), int(input("y: "))
x3,y3 = int(input("Ingrese el tercer punto: \nx: ")), int(input("y: "))
if y3-y == ((y2 - y)/(x2 - x))*(x3-x):
    print("Son colineales.")
else:
    print("No son colineales.")
