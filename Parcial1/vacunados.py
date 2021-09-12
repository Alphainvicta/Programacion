lista = [
    {"nombre": "gg1", "edad": 20, "curp": "183h9dwd1dja0s9dj", "vacunado": "si"},
    {"nombre": "gg2", "edad": 21, "curp": "283h9dwd1dja0s9dj", "vacunado": "no"},
    {"nombre": "gg3", "edad": 22, "curp": "383h9dwd1dja0s9dj", "vacunado": "si"},
    {"nombre": "gg4", "edad": 23, "curp": "483h9dwd1dja0s9dj", "vacunado": "si"},
    {"nombre": "gg5", "edad": 24, "curp": "583h9dwd1dja0s9dj", "vacunado": "si"},
]


def agregar():
    lista.append(
        {
            "nombre": input("Ingresa el nombre: "),
            "edad": input("Ingresa la edad: "),
            "curp": input("Ingresa el curp: "),
            "vacunado": input("Esta vacunado? s/n: "),
        }
    )


def revicion():
    si = 0
    no = 0
    for i in lista:
        cont = i.get("vacunado")
        if cont == "si":
            si += 1
        else:
            no += 1
    return si, no


def mostrarvacunados(si, no):
    psi = 100 * float(si / (no + si))
    pno = 100 * float(no / (no + si))
    print("Hay un total de ", si, " usuarios vacunados")
    print("")
    print("Hay un total de ", no, " usuarios no vacunados")
    print("")
    print("Porcentaje final:")
    print("")
    print(psi, "% vacunadas ", pno, "% no vacunadas")


def main():
    print("***************************************************************")
    print("*               Revision de usuarios vacunados                *")
    print("***************************************************************")
    print("")
    print("Selecciona la opcion a realizar")
    print("")
    print("agregar a la lista un usuario nuevo: 1")
    print("")
    print("revisar el porcentaje de usuarios vacunados: 2")
    print("")
    opcion = input()
    print("")
    if opcion == "1":
        agregar()
    else:
        si, no = revicion()
        mostrarvacunados(si, no)
    print("")


programa = "y"
while programa == "y":
    main()
    print("")
    programa = input("desea volver a iniciar? (y/n): ")
    print("")
    print("")
