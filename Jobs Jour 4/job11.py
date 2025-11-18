def Time_to_text(nombre_entier):
    heure = 0
    while nombre_entier >= 60:
        nombre_entier = nombre_entier - 60
        heure += 1
    print(f"{heure} heures et {nombre_entier} minutes.")


Time_to_text(120)
Time_to_text(130)
Time_to_text(340)