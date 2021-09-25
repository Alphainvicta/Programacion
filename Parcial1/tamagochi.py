maquina = [
    [
        "",
        "Neutral",
        "Feliz",
        "Triste",
        "Enojado",
        "Dormido",
        "Llorando",
        "Nervioso",
        "Sorprendido",
        "Sospechoso",
        "Muerto",
    ],
    [
        "Jugar",
        "Feliz",
        "Dormido",
        "Enojado",
        "Llorando",
        "Sorprendido",
        "Neutral",
        "Sorprendido",
        "Feliz",
        "Sorprendido",
        "Muerto",
    ],
    [
        "cantar",
        "Feliz",
        "Dormido",
        "Llorando",
        "Triste",
        "Dormido",
        "Dormido",
        "Neutral",
        "Feliz",
        "Neutral",
        "Muerto",
    ],
    [
        "Regalo",
        "Sorprendido",
        "Feliz",
        "Sorprendido",
        "Sospechoso",
        "Sorprendido",
        "Nervioso",
        "Sospechoso",
        "Nervioso",
        "Sospechoso",
        "Muerto",
    ],
    [
        "Gritar",
        "Triste",
        "Sorprendido",
        "Llorando",
        "Muerto",
        "Sorprendido",
        "Muerto",
        "Muerto",
        "Enojado",
        "Sorprendido",
        "Muerto",
    ],
    [
        "Dormir",
        "Dormido",
        "Dormido",
        "Enojado",
        "Muerto",
        "Dormido",
        "Muerto",
        "Neutral",
        "Nervioso",
        "Nervioso",
        "Muerto",
    ],
    [
        "Ignorar",
        "Sorprendido",
        "Nervioso",
        "Llorando",
        "Muerto",
        "Dormido",
        "Muerto",
        "Triste",
        "Nervioso",
        "Triste",
        "Muerto",
    ],
    [
        "Acariciar",
        "Sorprendido",
        "Feliz",
        "Feliz",
        "Sorprendido",
        "Neutral",
        "Triste",
        "Sorprendido",
        "Feliz",
        "Sorprendido",
        "Muerto",
    ],
    [
        "Aventar",
        "Enojado",
        "Sorprendido",
        "Llorando",
        "Enojado",
        "Muerto",
        "Muerto",
        "Muerto",
        "Enojado",
        "Enojado",
        "Muerto",
    ],
    [
        "Observar",
        "Nervioso",
        "Sorprendido",
        "Enojado",
        "Sospechoso",
        "Nervioso",
        "Nervioso",
        "Muerto",
        "Nervioso",
        "Nervioso",
        "Muerto",
    ],
    [
        "Hablar",
        "Feliz",
        "Feliz",
        "Neutral",
        "Llorando",
        "Neutral",
        "Triste",
        "Sospechoso",
        "Sospechoso",
        "Nervioso",
        "Muerto",
    ],
]


def tamagochi(estadoa):
    print("Selecciona la opcion a realizar")
    print("")
    print("Jugar: 0")
    print("Cantar: 1")
    print("Regalo: 2")
    print("Gritar: 3")
    print("Dormir: 4")
    print("Ignorar: 5")
    print("Acariciar: 6")
    print("Aventar: 7")
    print("Observar: 8")
    print("Hablar: 9")
    print("")
    accion = int(input()) + 1
    print("")
    for i in range(1, 10):
        if estadoa == maquina[0][i]:
            estadoa = maquina[accion][i]
            break

    print("estado actual del tamagochi: ", estadoa)
    return estadoa


def main():
    print("****************************************************************")
    print("*                          Tamagochi                           *")
    print("****************************************************************")
    print("")
    estado = "Neutral"
    while estado != "Muerto":
        estado = tamagochi(estado)
    print("")
    print("El tamagochi murio...")


programa = "y"
while programa == "y":
    main()
    print("")
    programa = input("desea volver a iniciar? (y/n): ")
    print("")
    print("")
