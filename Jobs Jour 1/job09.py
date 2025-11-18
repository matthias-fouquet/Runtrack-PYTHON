# Définition du produit
nom = "Stylo"
prix = 2.5
quantite = 100

# Affichage des infos initiales
print("Produit :", nom)
print("Prix unitaire :", prix, "€")
print("Quantité en stock :", quantite)

# Demande à l'utilisateur combien il veut acheter
achat = int(input("Combien de produits voulez-vous acheter ? "))

# Mise à jour du stock
quantite -= achat

# Mise à jour du prix (inflation de 10 %)
prix *= 1.10

# Affichage des infos mises à jour
print("\n--- Après mise à jour ---")
print("Produit :", nom)
print("Nouveau prix unitaire :", round(prix, 2), "€")
print("Quantité restante :", quantite)