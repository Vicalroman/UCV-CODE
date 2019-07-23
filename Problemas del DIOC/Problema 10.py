"""Diseñe un programa que indique si tres puntos dados por sus coordenadas(x, y)
forman triángulo y en caso de formarlo debe indicarse que tipo de triángulo
forma."""
x,y = int(input("Ingrese el primer punto: \nx: ")), int(input("y: "))
x2,y2 = int(input("Ingrese el segundo punto: \nx: ")), int(input("y: "))
x3,y3 = int(input("Ingrese el tercer punto: \nx: ")), int(input("y: "))
import math
def ladosDelTriangulo(a,b,a2,b2):
    l =((a2-a)**2 + (b2-b)**2)**0.5
    return l
def angulosDelTriangulo(a,b,c):
    angle = math.degrees(math.acos((a**2 + b**2 - c**2)//(2*a*b)))/2
    return angle
def tipoDeTriangulo():
    a = ladosDelTriangulo(x2,y2,x3,y3)
    b = ladosDelTriangulo(x,y,x2,y2)
    c = ladosDelTriangulo(x3,y3,x,y)
    #print(a,b,c)
    alpha = angulosDelTriangulo(a,b,c)
    beta = angulosDelTriangulo(a,c,b)
    gamma = angulosDelTriangulo(b,c,a)
    #print(alpha,beta,gamma)
    if alpha or gamma or beta == 90:
        print("Es un triagulo rectangulo.")
    if alpha == gamma == beta:
        print("Es un triangulo equilatero.")
    if alpha > 90 or gamma > 90 or beta > 90:
        print("Es un triangulo obtuso")
    if alpha < 90 and gamma < 90 and beta < 90:
        print("Es un triangulo acuso")
    if a == b or b == c or c == a:
        print("Es un triangulo isoceles.")
    if alpha != gamma != beta:
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
