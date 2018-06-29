frase_del_usuario = input("Introduce una frase:")

puntos = [":", "." ]
comas = [",", ";"]
espacios = [" "]

n_espacios = 0
n_puntos = 0
n_comas = 0

for signo in frase_del_usuario:
    if signo in puntos:
        n_puntos += 1
    if signo in comas:
        n_comas += 1
    if signo in espacios:
        n_espacios += 1



print("los puntos son {}".format(n_puntos))
print("las comas son {}".format(n_comas))
print("los espacios son {}".format(n_espacios))