def taille(mot):
    compteur = 0
    for o in mot:
        compteur += 1
    return compteur

def my_long_word(n, phrase):
    mots = []
    mot_courant = ""

    for c in phrase:
        if c != " " and c != "," and c != ".":
            mot_courant += c
        else:
            if mot_courant != "":
                mots.append(mot_courant)
                mot_courant = ""

    if mot_courant != "":
        mots.append(mot_courant)

    mots_valides = []
    for mot in mots:
        if taille(mot) > n:
            mots_valides.append(mot)

    resultat = ""
    premier = True
    for mot in mots_valides:
        if premier:
            resultat += mot
            premier = False
        else:
            resultat += " " + mot

    return resultat

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, phrase))