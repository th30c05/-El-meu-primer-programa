
salida = False
agenda = dict()

while not salida:
    accion = input("Que quieres hacer? [Añadir cumpleaños[A] / Consultar cumpleaños[C] / Salir [S]: ").upper()

    if accion == "A":
        print("vamos a añadir un amigo: ")
        nombre = input("Nombre: ")
        cumpleaños = input("Cumpleaños: ")
        agenda[nombre] = cumpleaños

    elif accion == "C":
        print("Vamos a consultar un cumpleaños: ")
        print("----------------------------------------------")
        nombre = input("De quien quieres saber el cumpleaños: ")
        print(agenda[nombre])


    elif accion == "S":
        salida = True