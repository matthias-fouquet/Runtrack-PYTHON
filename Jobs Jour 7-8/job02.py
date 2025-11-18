# job02.py

def draw_triangle(height: int) -> None:
    """Affiche un triangle avec une hauteur donnée."""
    if height < 2:
        print("Hauteur minimale : 2")
        return

    # On parcourt chaque ligne du haut vers le bas
    for i in range(height - 1):
        # Espaces avant le début du triangle
        espaces = " " * (height - i - 1)
        # Intérieur du triangle
        interieur = " " * (i * 2)
        print(espaces + "/" + interieur + "\\")

    # Base du triangle
    print("/" + "_" * ((height - 1) * 2) + "\\")

draw_triangle(100)