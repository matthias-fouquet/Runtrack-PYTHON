L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme = 0

for i in L:
    if i % 2 == 0:
        print("Nombre paire",i)
        somme += i

print("Le total de toutes les valeurs paires contenues dans la liste L s’élève à", somme)