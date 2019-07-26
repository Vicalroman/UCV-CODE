"""Una forma de determinar si un año es bisiesto es que el mismo sea divisible de
manera exacta por cuatro, pero si el mismo es fin de siglo (año secular) en este
caso debe ser divisible de forma exacta por cuatrocientos. Realice un programa
que basado en el criterio anterior determine si un año dado como dato es o no
bisiesto, generando un mensaje adecuado. """
print("Determinaremos si un año es bisiesto.") #print es una funcion que imprime un mensaje en pantalla
año = int(input("Ingrese un año para calcular si es bisiesto: ")) #declaramos la variable que representa a los años
if año % 4 == 0 and año % 400 == 0: #condiciones junto con los calculos
    print("El año es bisiesto y secular.")
elif año % 4 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
