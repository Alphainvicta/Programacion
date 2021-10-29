y = "s"
Result = 0
while y == "s":
    yy = "s"
    Calificaciones = []
    while yy == "s":
        print("Introduce una de las calificaciones:")
        Numero = float(input())
        Calificaciones.append(Numero)
        print(Calificaciones)
        yy = input("¿Deseas añadir otra calificación? s/n: ")
    print("")
    Suma = sum(Calificaciones)
    Cal = Suma / len(Calificaciones)
    print(f"Tu Promedio es: {Cal}")
    y = input("¿Deseas Sacar Otro Promedio? s/n:  ")
