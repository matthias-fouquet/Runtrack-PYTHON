def supprimer_doublons(L):
    resultat = []

    for element in L:
        deja_present = False

        for e in resultat:
            if e == element:
                deja_present = True

        if not deja_present:
            resultat.append(element)

    return resultat


L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("Liste originale :", L)
L_sans_doublons = supprimer_doublons(L)
print("Liste sans doublons :", L_sans_doublons)