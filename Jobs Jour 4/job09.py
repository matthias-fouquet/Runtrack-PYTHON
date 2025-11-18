def moyenne(a, b, c):
    return (a + b + c) / 3

def appreciation(m):
    if 15 <= m <= 20:
        return "Très bon élève"
    elif 11 <= m < 15:
        return "Bon élève"
    elif 8 <= m < 11:
        return "Élève moyen"
    elif 0 <= m < 8:
        return "Élève devant faire des efforts"
    # else:
    #     return "Moyenne hors barème"    ->  Tout cette partie n'est plus nécessaire car on empêche l'utilisateur de rentrer autre chose que des notes comprises entre 0 et 20.


def lire_note(invite):
    while True: #on creer une boucle infini pour que on demande à l'utilisateur d'entrer une valeur tant que elle n'est pas valide, et le "return n" permettra de sortir de la boucle "while".
        try:
            n = float(input(invite))
            if 0 <= n <= 20:
                return n
            print("⚠️ La note doit être entre 0 et 20.")
        except ValueError: #si quelques chose au mauvais format était rentré par l'utilisateur, donc une "ValueError", on va afficher le print et re proposer à l'utilisateur de rentrer qlq chose.
            print("⚠️ Entre un nombre (ex: 12 ou 14.5).")

n1 = lire_note("Note 1 (0-20) : ")
n2 = lire_note("Note 2 (0-20) : ")
n3 = lire_note("Note 3 (0-20) : ")

moyenne_etudiant = moyenne(n1, n2, n3)
print(f"Moyenne : {moyenne_etudiant:.2f}") #la partie ":.2f" permet d'avoir quoi qu'il arrive un résultat avec 2 chiffres aprés la virgule et au format "f" (float).
print(appreciation(moyenne_etudiant))