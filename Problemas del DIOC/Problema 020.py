"""Realice un programa que dados cuatro valores A, B, C, D los presente, en
pantalla, ordenados de menor a mayor. Considere que el usuario puede
suministrar los valores en cualquier orden."""
print("Vamos a ordenar cuatro valores en orden.")
A, B, C, D = float(input("Inserte el primer valor: ")), float(input("Inserte el segundo valor: ")),\
float(input("Inserte el tercer valor: ")), float(input("Inserte el cuarto valor: "))
lista = [A, B, C, D]
lista_creciente = [j for j in range(int(max(lista)) + 1) for i in lista if i == j]
print(lista_creciente)
