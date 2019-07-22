"""En un reloj de agujas (que sólo tiene horario y minutero), elabore un\
programa que calcule y muestre el menor ángulo en grados que forman tales\
agujas dada una hora suministrada por el usuario. """
print("Ingrese la hora del reloj: ")
h,m = int(input("Horas: ")), int(input("Minutos: "))
if m < 60:
    am = m/5*30
if m == 60:
    am = 0
if m > 60 :
    print("Por favor ingrese una hora valida: ")
pm = (am*100)/(360*100)
ah = (h + pm)*30
if abs(ah - am) < 180:
    print(abs(ah - am))
if abs(ah - am) > 180:
    print(360 - abs(ah - am))
