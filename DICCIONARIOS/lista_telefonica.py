
salida = False
agenda = dict()

while not salida:
    accion = input("Que quieres hacer? [Añadir numero[A] / Consultar numero[C] / Salir [S]: ").upper()

    if accion == "A":
        print("vamos a añadir un numero de telefono: ")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero

    elif accion == "C":
        print("Vamos a consultar un numero: ")
        print("----------------------------------------------")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])


    elif accion == "S":
        salida = True