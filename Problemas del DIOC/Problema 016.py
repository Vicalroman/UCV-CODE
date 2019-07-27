"""Las siguientes unidades de distancia son de origen hispanoamericano y se muestra
también su equivalencia con el metro: Almud (0,27 m), Cana (1,541 m), Dedo
(0,0174 m), Estadal (3,391 m), Jarocha (4,19 m), Palmo (0,212 m), Mecate
(20,062 m). Realice un programa donde dada una medida suministrada en
metros, se indique su equivalente en la medida seleccionada por el usuario. """
print("Vamos a pasar de metros a unidades de distancias de origen hispanoamericano")
metros = float(input("Ingrese una distancia en metros: "))
unidades = {"almud": 0.27, "cana": 1.541, "dedo": 0.0174, "estadal": 3.391, "jarocha": 4.19,\
"palmo": 0.212, "mecate": 20.062}
print("Las posibles unidades son: Almud, Cana, Dedo, Estadal, Jarocha, Palmo, Mecate")
indicacion = input("¿A que unidad desea convertir?\n")
resultado = unidades[str.lower(indicacion)] * metros
print("Serian {} {}.".format(resultado, indicacion))
