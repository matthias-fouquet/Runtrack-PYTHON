import random

def Creation_liste():
    L = []
    for i in range(5):
        nombre = random.randint(1, 100)
        L.append(nombre)
    print("La liste est :", L )
    print("Deuxième élément :", L[1])
    return L

def Transformation_liste(L):
    L[3] = L[2] + L[4]
    print("Liste transformée :", L)
    return L


ma_liste = Creation_liste()
ma_liste = Transformation_liste(ma_liste)
print("Dernier élément :", ma_liste[-1])