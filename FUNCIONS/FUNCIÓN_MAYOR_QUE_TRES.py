def mayor_de_tres(max_de_tres):
    resultado = max(primer_numero, segundo_numero, tercer_numero)
    return resultado

primer_numero = int(input("primer numero: "))
segundo_numero = int(input("segundo numero: "))
tercer_numero = int(input("tercer numero: "))


print("El mas grande es {}".format(mayor_de_tres(primer_numero, segundo_numero, tercer_numero)))

