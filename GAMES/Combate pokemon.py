pokemon_elegido = input("Contra Que Pokemon Quieres Combatir? (Squirtle / Charmander / Bulbasur): ").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 80
    daño = 8
    nombre_pokemon = "SQUIRTLE"

if pokemon_elegido == "CHARMANDER":
    vida_enemigo = 90
    daño = 10
    nombre_pokemon = "CHARMANDER"

if pokemon_elegido == "BULBASUR":
    vida_enemigo = 100
    daño = 9
    nombre_pokemon = "BULBASUR"

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que Ataque Vamos A Usar? (Chispazo / Bola Voltio): ").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 17
        print("Daño Causado -7")

    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
        print("Daño Causado -12, Ahora {} Tiene {} De Vida".format(nombre_pokemon, vida_enemigo))

    if pokemon_elegido == "{}".format(nombre_pokemon):
        vida_pikachu -= daño
        print("{} Te Ha Quitado {} De Vida, Ahora Pikachu Tiene {} de vida".format(nombre_pokemon, daño, vida_pikachu))

    print("......................................................................")

if vida_pikachu > 0:
    print("El ganador es pikachu")

elif vida_enemigo > 0:
    print("El ganador es {}" .format(pokemon_elegido))