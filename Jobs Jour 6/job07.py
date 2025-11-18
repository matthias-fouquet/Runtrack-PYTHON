L = [8,24,48,2,16]

multiple_de_3 = 0

for e in L:
    if e % 3 == 0:
        multiple_de_3 += 1

print("il y a", multiple_de_3, "multiple.s de 3 dans la liste L.")