"""Realice un programa que determine, en una sola instrucción de decisión, si un
punto de coordenadas (x, y) cae dentro del área sombreada, todos los círculos son
de radio igual a uno. """
print("Vamos a ver si el punto esta dentro del area sombreada.")
x, y = float(input("Inserte la componente x: ")), float(input("Inserte la componente y: "))
booleano_1 = (x <= -y + 2) and ((x - 1)**2 + (y - 1)**2 <= 1)
booleano_2 = (y >= x - 2) and ((x - 1)**2 + (y + 1)**2 <= 1)
booleano_3 = (y <= x + 2) and ((x + 1)**2 + (y - 1)**2 >= 1) and (y > 0) and (x < 0)
booleano_4 = (y >= x + 2) and ((x + 1)**2 + (y - 1)**2 <= 1)
booleano_5 = (y <= - x - 2) and ((x + 1)**2 + (y + 1)**2 <= 1)
booleano_total = booleano_1 or booleano_2 or booleano_3 or booleano_4 or booleano_5
if booleano_total:
    print("Esta dentro del area sombreada.")
else:
    print("No esta dentro del area sombreada.")
