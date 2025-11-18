for nombre in range(2, 1001):
    est_premier = True
    i = 2

    # on teste seulement jusqu'à la racine carrée du nombre
    while i * i <= nombre and est_premier:
        if nombre % i == 0:
            est_premier = False
        i += 1

    if est_premier:
        print(nombre, end="-")