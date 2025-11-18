def draw_rectangle(width: int, height: int) -> None:
    if width < 2 or height < 2:
        print("Dimensions minimales: width >= 2 et height >= 2")
        return

    # Lignes du haut et du bas : |----...----|
    top_bottom = "|" + "-" * (width - 2) + "|"
    # Lignes du milieu : |    ...    |
    middle = "|" + " " * (width - 2) + "|"

    # Haut du rectangle
    print(top_bottom)
    # Milieu (height - 2 lignes)
    for o in range(height - 2):
        print(middle)
    # Bas du rectangle
    print(top_bottom)

draw_rectangle(10, 3)