"""Diseñe un programa que indique si tres puntos dados por sus coordenadas(x, y)
forman triángulo y en caso de formarlo debe indicarse que tipo de triángulo
forma."""
x,y = float(input("Ingrese el primer punto: \nx: ")), float(input("y: "))
x2,y2 = float(input("Ingrese el segundo punto: \nx: ")), float(input("y: "))
x3,y3 = float(input("Ingrese el tercer punto: \nx: ")), float(input("y: "))
import math
def ladosDelTriangulo(a,b,a2,b2):
    l =((a2-a)**2 + (b2-b)**2)**0.5
    return round(l,2)
def angulosDelTriangulo(a,b,c):
    angle = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    return round(angle)
def tipoDeTriangulo():
    a = ladosDelTriangulo(x2,y2,x3,y3)
    b = ladosDelTriangulo(x,y,x2,y2)
    c = ladosDelTriangulo(x3,y3,x,y)
    print(a,b,c)
    alpha = angulosDelTriangulo(a,b,c)
    beta = angulosDelTriangulo(a,c,b)
    gamma = angulosDelTriangulo(b,c,a)
    print(alpha,beta,gamma)
    if alpha == gamma and beta == alpha and beta == gamma:
        print("Es un triangulo equilatero.")
    elif alpha == 90 or gamma == 90 or beta == 90:
        print("Es un triagulo rectangulo.")
    elif alpha > 90 or gamma > 90 or beta > 90:
        print("Es un triangulo obtuso")
    elif alpha < 90 and gamma < 90 and beta < 90:
        print("Es un triangulo acutangulo")
    if (a == b or b == c or c == a) and not (a == b and b== c and c == a):
        print("Es un triangulo isoceles.")
    elif alpha != gamma and alpha != beta and beta != gamma:
        print("Es un triangulo escaleno")
m = 0
if x == x2 and x == x3:
    print("No forman un triangulo")
else:
    if (x2 - x) != 0:
        m = (y2-y)/(x2-x)
        if y3-y == m*(x3-x):
            print("No forman un triangulo.")
        else:
            tipoDeTriangulo()
    elif (x3 - x) != 0:
        m = (y3-y)/(x3-x)
        if y2-y == m*(x2-x):
            print("No forman un triangulo.")
        else:
            tipoDeTriangulo()
