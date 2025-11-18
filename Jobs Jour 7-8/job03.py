def draw_carpet(n: int) -> None:
    """Affiche un tapis de n+1 lignes et n+1 colonnes traversé par une diagonale."""
    
    # Ligne du haut
    print("+" + "-" * (n + 1) + "+")
    
    # Lignes du milieu
    for i in range(n + 1):
        ligne = "|"
        for j in range(n + 1):
            if j == n - i:  # position de la diagonale (du coin haut gauche au bas droit)
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print(ligne)
    
    # Ligne du bas
    print("+" + "-" * (n + 1) + "+")

taille = int(input("Taille du tapis ? "))
draw_carpet(taille)