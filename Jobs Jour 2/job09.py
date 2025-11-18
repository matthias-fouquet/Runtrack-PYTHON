#essai 1

""" print("Chiffres & Nombres impairs compris entre 0 et 30 inclus :")

i=-1
while i < 29:
    i += 2
    print(i)

print("Chiffres & Nombres pairs compris entre 0 et 30 inclus :")

p=0
while p < 30:
    p += 2
    print(p) """

#essai 2


""" for i in range(1, 16):
    print(f"{(i * 2) - 1} est impair",end=" ")
    print(f"{i * 2} est pair") """

#essai 3

impairs = []
pairs = []

for i in range(1, 16):
    impairs.append((i * 2) - 1)
    pairs.append(i * 2)

print(f"liste des impairs : {impairs}")
print(f"liste des pairs : {pairs}")