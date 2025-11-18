def arrondir(x):
    entier = int(x)
    fraction = x - entier
    if fraction >= 0.5:
        return entier + 1
    else:
        return entier

def tri_croissant(L):
    n = 0
    for o in L:
        n += 1

    a_change = True
    while a_change:
        a_change = False
        i = 0
        while i < n - 1:
            if L[i] > L[i + 1]:
                tmp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = tmp
                a_change = True
            i += 1
    return L


L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Liste d'origine :", L)


L_arrondie = []
for x in L:
    L_arrondie.append(arrondir(x))

print("Après arrondi   :", L_arrondie)


L_triee = tri_croissant(L_arrondie)
print("Tri croissant   :", L_triee)