"""Se dice que tres números naturales A, B y C forman terna pitagórica cuando se
cumple la relación A**2 + B**2 = C**2. Por ejemplo 3, 4 y 5 forman una terna pitagórica
ya que 3**2 + 4**2 = 5**2. Diseñe un programa que cuente cuántas ternas pitagóricas se
forman tales que tanto el Valor de A y de B sean menores que un número N dado
como dato."""
print("Vamos a calcular cuantas ternas pitagoricas se forman dentro de un intervalo.")
N = int(input("Indique el final del intervalo: "))
ternas = ["{}**2 + {}**2 ={}**2".format(i, j, int((i**2 + j**2)**0.5)) \
for i in range(1, N + 1) for j in range(1, N + 1) \
if (i**2 + j**2)**0.5 == int((i**2 + j**2)**0.5)]
print("En el intervalo hay {} ternas pitagoricas.".format(len(ternas)//2))
