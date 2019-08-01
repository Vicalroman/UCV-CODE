"""Dados los datos que permitan formar la ecuación de segundo grado
Ax2 + Bx +C = 0, genere un programa que calcule las raíces de dicha ecuación;
contemple la posibilidad de mostrar resultados imaginarios. """
print("Vamos a calcular las raices de una ecuacion de segundo grado.")
print("Por favor introduzca los coeficientes que acompañan las variables respectivamente.")
A = int(input("Introduzca el coeficiente de la x al cuadrado: "))
B = int(input("Introduzca el coeficiente de la x: "))
C = int(input("Introduzca el termino independiente: "))
if B**2 - 4*A*C >= 0:
    resolvente_1 = (-B + (B**2 - 4*A*C)**0.5)/(2*A)
    resolvente_2 = (-B - (B**2 - 4*A*C)**0.5)/(2*A)
    print("Las raices son {} y {}.".format(resolvente_1, resolvente_2))
else:
    resolvente_1_real = (-B)/(2*A)
    resolvente_complejo = ((abs(B**2 - 4*A*C))**0.5)/(2*A)
    resolvente_2_real = (-B)/(2*A)
    print("Las raices son {} + {} i y {} - {} i".format(resolvente_1_real, resolvente_complejo, resolvente_2_real, resolvente_complejo))
