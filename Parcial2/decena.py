y = "s"
lista = []
des = 10
cont = 0
dess = 0

while y == "s":
    numero = int(input("agrega un numero: "))
    print("")
    if numero > 50 or numero < 1:
        print("Elige un numero entre 1 y 50")
        print("")
    else:
        lista.append(numero)
    y = input("quieres agregar otro numero? s/n: ")
    print("")

lista = sorted(lista)

for i in range(len(lista)):
    while lista[i] > des:
        des += 10
        dess += 10
    if dess <= lista[i] and lista[i] <= des:
        print(lista[i], end=" ")
        cont += 1
    if cont == 3:
        cont = 0
        des += 10
        dess += 10
