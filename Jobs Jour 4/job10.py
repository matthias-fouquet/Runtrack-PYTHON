def pair_ou_impair():
    try:
        nombre = int(input("\nVeuillez entrer un nombre entier et positif : "))
        if nombre > 0:
            if nombre % 2 == 0:
                print(f"\n{nombre} est pair.\n")
            else:
                print(f"\n{nombre} est impair.\n")
        else:
            print("\nLe nombre doit être positif.\n")
    except ValueError:
        print("\n⚠️ La valeur entrée ne respecte pas le format attendu (entier & positif).\n")

pair_ou_impair()