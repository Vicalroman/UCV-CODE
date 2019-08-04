"""Realice un programa que permita al usuario llevar adelante una de las siguientes
operaciones para números imaginarios: suma, resta, multiplicación o división. El
usuario debe poder seleccionar una de las operaciones, dar los valores y obtener
el resultado."""
#python soporta operaciones con numeros imaginarios.
print("Vamos a indicar el primer numero complejo.")
complejo_1 = complex(float(input("Ingrese la parte real: ")), float(input("Ingrese la parte imaginaria: ")))
print("\nVamos a indicar el segundo numero complejo.")
complejo_2 = complex(float(input("Ingrese la parte real: ")), float(input("Ingrese la parte imaginaria: ")))
n = 10
while n > 0:
    try:
        operacion = (input("\nIndique que operacion desea realizar: ")).lower()
        if (operacion == "suma") or (operacion == "resta") or (operacion == "multiplicacion") or (operacion == "division"):
            break
        else:
            raise TypeError("La operacion que usted ingreso no es valida.")
    except TypeError:
        n -= 1
        print("Intente nuevamente le quedan {} intentos.".format(n))
if operacion == "suma":
    resultado = complejo_1 + complejo_2
elif operacion == "resta":
    resultado = complejo_1 - complejo_2
elif operacion == "multiplicacion":
    resultado = complejo_1 * complejo_2
elif operacion == "division":
    resultado = complejo_1 / complejo_2
print("El resultado de la {} es {}".format(operacion, resultado))
