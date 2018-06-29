numero_tabla = int(input("De que numero quieres la tabla de multiplicar?: "))

for multiplo in (2, 4, 6, 8, 10):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))