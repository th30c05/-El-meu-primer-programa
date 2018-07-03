
def input_con_confirmacion():
    confirmacion = False
    while not confirmacion:
        dato_usuario = input("Como te llamas: ")
        seguro= input("Has dicho {}, ¿Estas seguro? [Si / No] ").format(nombre).upper()
        if seguro == "SI":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("¿com te llamas? ")
print("Has confirmado que te llamas {}".format(nombre))

numero = input_con_confirmacion("Dime un numero ")
print("Has confirmado que el numero es {}".format(nombre))