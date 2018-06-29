apetece_helado_input = input("¿te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False

else:
    print("The he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tienes_dinero_input = input("¿tienes dinero para un helado? (Si / No): ").upper()
esta_el_senor_helados_input = input("Esta el señor de los helados? (Si / No): ").upper()
esta_tu_tia_input = input("esta con tu tia? (Si/No): ").upper()

apetece_helado = apetece_helado_input == "SI"
puedes_permitirtelo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puedes_permitirtelo and esta_el_senor_helados:
    print("pues comete un helado")
else:
    print("pues nada")