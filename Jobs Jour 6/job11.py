def augmenter_liste():
    L = [7, 11, 42, 39, 2]
    print("Liste avant modification :", L)

    for i in range(len(L)):
        L[i] = L[i] + 1

    print("Liste après modification :", L)
    return L

augmenter_liste()