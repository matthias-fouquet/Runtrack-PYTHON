def Ordre_croissant(L):
    nombre_element = 0
    for o in L:
        nombre_element += 1

    flag = True
    while flag:
        flag = False
        i = 0
        while i < nombre_element - 1:
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp
                flag = True
            i += 1

    return L

ma_liste = [42, 7, 11, 2, 39]
print("Avant tri :", ma_liste)
ma_liste = Ordre_croissant(ma_liste)
print("Après tri :", ma_liste)