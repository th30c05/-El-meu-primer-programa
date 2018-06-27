pokemon_elegido = input("contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasur): ").upper()

vida_pikachu = 100
    print("Vida Pikachu {}" .format(vida_pikachu))
vida_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 80

if pokemon_elegido == "CHARMANDER":
    vida_enemigo = 90

if pokemon_elegido == "BULBASUR":
    vida_enemigo = 100


while vida_pikachu > 0 or vida_enemigo > 0:
    ataque_elegido = input("¿que ataque vamos a usar? (chispazo / Bola voltio): ").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
    if pokemon_elegido == "CHARMANDER":
        print("Vida CHARMANDER {}" .format(vida_enemigo))
    if pokemon_elegido == "SQUIRTLE":
        print("Vida SQUIRTLE {}" .format(vida_enemigo))
    if pokemon_elegido == "BULBASUR":
        print("Vida BULBASUR {}" .format(vida_enemigo))
    if pokemon_elegido == "SQUIRTLE":
        print("Squirtle te hace un ataque 8 de daño")
        vida_pikachu -= 8
    if pokemon_elegido == "CHARMANDER":
        print("Charmander te hace un ataque 10 de daño")
        vida_pikachu -= 10
    if pokemon_elegido == "BULBASUR":
        print("Bulbasur te hace un ataque 9 de daño")
        vida_pikachu -= 7
    print("Vida pikachu {}".format(vida_pikachu))

print("El combate ha termindo")