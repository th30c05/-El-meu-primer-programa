frase_del_usuario = input("Introduce una frase: ")

majusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

n_majusculas = 0

for letra in frase_del_usuario:
    if letra in majusculas:
        n_majusculas += 1

print("Las majusculas son {}".format(n_majusculas))