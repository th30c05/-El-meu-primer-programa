numero_tabla = int(input("De que numero quieres la tabla de multiplicar?: ")).__neg__()

for multiplo in range(-10, 1):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))