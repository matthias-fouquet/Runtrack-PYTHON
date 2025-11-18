import random

def Echange_element_liste():
    L = []
    for i in range(5):
        nombre = random.randint(1, 10)
        L.append(nombre)
    print("La liste est :", L )
    
    a = L[0]
    b = L[-1]
    L[-1] = a
    L[0] = b
    print(L)

Echange_element_liste()