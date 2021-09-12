def defmatriz(col1, fil1, col2, fil2):
    print("")
    print("introduce los numeros de la primera matriz")
    print("")

    mat1 = []
    for i in range(fil1):
        x = []
        for j in range(col1):
            x.append(int(input()))
        mat1.append(x)
    print("")
    print("introduce los numeros de la segunda matriz")
    print("")

    mat2 = []
    for i in range(fil2):
        y = []
        for j in range(col2):
            y.append(int(input()))
        mat2.append(y)

    return mat1, mat2


def mul(x, y, mat1, mat2, z):
    matf = []
    r = 0
    for i in range(x):
        w = []
        for j in range(y):
            for l in range(z):
                r += mat1[i][l] * mat2[l][j]
            w.append(r)
            r = 0
        matf.append(w)
    return matf


def printmatrizz(mat, fil, col):
    for i in range(fil):
        for j in range(col):
            print(mat[i][j], end=" ")
        print()


def main():
    print("***************************************************************")
    print("*       Calculadora para multiplicacion de dos matrices       *")
    print("***************************************************************")
    print("")
    print("introduce los siguentes datos...")
    print("")
    print("matriz 1")
    print("")
    fil1 = int(input("introduce el rango de filas: "))
    print("")
    col1 = int(input("introduce el rango de columnas: "))
    print("")
    print("***************************************************************")
    print("matriz 2")
    print("")
    fil2 = int(input("introduce el rango de filas: "))
    print("")
    col2 = int(input("introduce el rango de columnas: "))
    print("")

    if col1 == fil2:
        mat1, mat2 = defmatriz(col1, fil1, col2, fil2)
        print("")
        print("estas son las matrices dadas:")
        print("")
        print("matriz 1: ")
        printmatrizz(mat1, fil1, col1)
        print("")
        print("matriz 2: ")
        printmatrizz(mat2, fil2, col2)
        print("")
        print("esta es la matriz resultante:")
        z = col1
        matf = mul(fil1, col2, mat1, mat2, z)
        printmatrizz(matf, fil1, col2)
        print("")
        print("")

    else:
        print(
            "el numero de filas de la primera matriz debe ser el mismo que el numero de columnas de la segunda matriz o contrario"
        )


programa = "y"
while programa == "y":
    main()
    print("")
    programa = input("desea volver a iniciar? (y/n): ")
    print("")
    print("")
