""" chaîne = "abcdefghijklmnopqrstuvwxyz" * 10

indexe = 0

résultat = (chaîne[indexe])

while indexe <= len(chaîne):
    print(résultat)
    indexe = indexe +1
    résultat = résultat + (chaîne[indexe]) """



chaine = "abcdefghijklmnopqrstuvwxyz" * 10 #initialisation de la chaîne
indexe = 0 #indexe sert à choisir quelle lettre afficher dans la chaîne
resultat = "" #on initialise l'affichage
pas= 1
while indexe < len(chaine):
    resultat = resultat  + chaine[indexe:indexe + pas]
    print(resultat)
    indexe = indexe + pas# on ajoute une lettre à la suite
    pas= pas + 1 # on passe à la lettre suivante

""" chaine= "abcdefghijklmnopqrstuvwxyz"*9

i= 1 
while i <= len(chaine):
    print(chaine[:i])
    i+=2 """