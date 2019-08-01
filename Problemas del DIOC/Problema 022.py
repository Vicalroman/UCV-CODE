"""Dados los conjuntos de puntos pertenecientes al círculo cuya ecuación es x2+y2=16,
a la elipse determinada por la ecuación x2/36+y2/16 =1 y a la recta cuya
ecuación es y =2x+1 diseñar un programa que para un punto definido por sus
coordenadas (x, y), leídos como datos, se indique la figura (o conjunto de ellas)
a las que pertenece."""
print("Vamos a identificar a que curvas pertenece el punto.")
x, y = float(input("Indique el valor de x: ")), float(input("Indique el valor de y: "))
if x**2 + y**2 == 16:
    print("Pertenece a la circurferencia.")
if (x**2) /(36) + (y**2)/(16) == 1:
    print("Pertenece a la elipse.")
if y == 2*x + 1:
    print("Pertence a la recta.")
else:
    print("No pertenece a ninguno.")
