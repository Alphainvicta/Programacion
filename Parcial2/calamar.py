import random

cj = 10
cm = 10
y = "s"
v = ["p", "i"]


def apostar(apj, apm, cj, cm):
    print("Elige las canicas que quieres apostar...")
    print("")
    ap = True
    while ap:
        apj = int(input())
        if apj > 0 and apj <= cj:
            break
        else:
            print("")
            print("el numero debe ser mayor a cero y menor a tu numero de canicas")
            print("")
    apm = random.choice(range(1, cm))
    return apj, apm


def elegir(elj, elm):
    elj = input("Elige par o impar. p/i: ")
    elm = random.choice(v)
    return elj, elm


def ronda(cj, cm, apj, apm, elj, elm):
    if apm % 2 == 0 and elj == "p":
        cj += apm
        cm -= apm
    if apm % 2 == 1 and elj == "i":
        cj += apm
        cm -= apm

    if apj % 2 == 0 and elm == "p":
        cm += apj
        cj -= apj
    if apj % 2 == 1 and elm == "i":
        cm += apj
        cj -= apj

    return cj, cm


def resr(cj, cm, apj, apm, elj, elm):
    print("El jugador aposto: ", apj, " y eligio: ", elj)
    print("")
    print("La maquina aposto: ", apm, " y eligio: ", elm)
    print("")
    print("Dejando al jugador con... ", cj, " restantes")
    print("")
    print("Dejando a la maquina con... ", cm, " restantes")


def main(cj, cm):
    print("Comienza el juego!")
    print("")
    apj, apm = 0, 0
    elj, elm = "", ""
    while cj > 0 and cm > 0:
        apj, apm = apostar(apj, apm, cj, cm)
        print("")
        elj, elm = elegir(elj, elm)
        print("")
        cj, cm = ronda(cj, cm, apj, apm, elj, elm)
        resr(cj, cm, apj, apm, elj, elm)
        print("")
    print("Se acabo!")
    print("")
    if cj == 0:
        ganador = "la maquina"
    if cm == 0:
        ganador = "el jugador"
    print("El ganador es: ", ganador)


while y == "s":
    main(cj, cm)
    print("")
    y = input("volver a jugar? s/n: ")
    print("")
