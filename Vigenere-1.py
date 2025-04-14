liste_lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def vigenere(liste_lettre , mot, key):
    key = key * (len(mot) // len(key)) + key[1-(len(mot) % len(key))]
    for i in range(len(mot)):
        for j in range(len(liste_lettre)):
            if mot[i] == liste_lettre[j]:
                for k in range(len(liste_lettre)):
                    if key[i] == liste_lettre[k]:
                        if j + k >= len(liste_lettre):
                            print(liste_lettre[j + k - len(liste_lettre)] , end = "")
                        else:
                            print(liste_lettre[j + k] , end = "")
    print("\n", key)
    print("")


def dechiffrementvigenere(liste_lettre , mot, key):
    key = key * (len(mot) // len(key)) + key[1-(len(mot) % len(key))]
    for i in range(len(mot)):
        for j in range(len(liste_lettre)):
            if mot[i] == liste_lettre[j]:
                for k in range(len(liste_lettre)):
                    if key[i] == liste_lettre[k]:
                        if j - k < 0:
                            print(liste_lettre[j - k + len(liste_lettre)] , end = "")
                        else:
                            print(liste_lettre[j - k] , end = "")
    print("\n", key)
    print("")


mot = input("Entrez le mot : ")
key = input("Entrez la clé : ")
vigenere(liste_lettre , mot, key)
dechiffrementvigenere(liste_lettre , mot, key)


