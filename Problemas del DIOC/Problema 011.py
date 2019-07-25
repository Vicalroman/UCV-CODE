"""Dadas tres longitudes suministradas por el usuario, diseñe un programa que
indique si las mismas pueden formar triángulo y de ser así también calcule y
muestre el área del triángulo."""
#Indicamos al usuario que se va a realizar.
print("Vamos a calcular si es un triangulo mediante la longitud de sus lados.")
#Asignamos las variables
longitud_1,longitud_2,longitud_3 = float(input("Ingrese la longitud del primer lado: "))\
, float(input("Segundo lado: ")), float(input("Tercer lado: "))
#Utilizando el teorema de la desigualdad de triangulos
#"not" indica que si no se cumple el booleano realiza la operacion
if not (longitud_1 + longitud_2 > longitud_3 and longitud_2 + longitud_3 > longitud_1 and\
longitud_3 + longitud_1 > longitud_2):
    print("No es un triangulo.")
#En cualquier otro caso usamos la formula de Herón.
#Calculamos semiperimetro
else:
    se_pe = (longitud_1 + longitud_2 + longitud_3)/2
    area = (se_pe*(se_pe-longitud_1)*(se_pe-longitud_2)*(se_pe-longitud_3))**0.5
    print("El area del triangulo es {}".format(area))
