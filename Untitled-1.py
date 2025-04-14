liste_lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def foot(liste_lettre , decal , mot):
    for i in range(len(mot)):
        for j in range(len(liste_lettre)):
            if mot[i] == liste_lettre[j]:
                if j + decal >= len(liste_lettre):
                    print(liste_lettre[j + decal - len(liste_lettre)] , end = "")
                else:
                    print(liste_lettre[j + decal] , end = "")
    print("")

decal = int(input("Entrez le décalage : "))
mot = input("Entrez le mot : ")
foot(liste_lettre , decal , mot)
