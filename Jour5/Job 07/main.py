mot = input("Entrer un mot de passe :")
if not mot.isalpha():
    print("Le mot doit contenir uniquement des lettres de l'alphabet.")
    exit()
liste_caracteres = list(mot)
liste_caracteres_triee = sorted(liste_caracteres)
indice_premiere_difference = None
for i in range(len(liste_caracteres)):
    if liste_caracteres[i] != liste_caracteres_triee[i]:
        indice_premiere_difference = i
        break
if indice_premiere_difference is None:
    print("Le mot est déjà dans l'ordre alphabétique.")
    exit()
indice_caractere_suivant = None
for i in range(indice_premiere_difference, len(liste_caracteres)):
    if liste_caracteres_triee[i] > liste_caracteres[indice_premiere_difference]:
        indice_caractere_suivant = i
        break
liste_caracteres[indice_premiere_difference], liste_caracteres[indice_caractere_suivant] = liste_caracteres[indice_caractere_suivant], liste_caracteres[indice_premiere_difference]
nouveau_mot = ''.join(liste_caracteres)
print("Le nouveau mot est :", nouveau_mot)
