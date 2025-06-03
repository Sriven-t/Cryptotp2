# Cryptotp2
# Sriven TAMILALAGAN CSM4
# TP2 crypto efrei
# Voici le code du César du TP2


def chiffrer_cesar(texte, decalage):
    resultat = ""
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
        else:
            resultat += char
    return resultat

def dechiffrer_cesar(texte, decalage):
    return chiffrer_cesar(texte, -decalage)


texte = input("Tape le texte à coder ou décoder : ")
try:
    decalage = int(input("Donne la clé (un nombre entier) : "))
except ValueError:
    print("Il faut entrer un nombre entier pour la clé.")
    exit()

choix = input("Tu veux coder ou décoder ? (c/d) : ").lower()

if choix == 'c':
    texte_chiffre = chiffrer_cesar(texte, decalage)
    print("Résultat codé :", texte_chiffre)
elif choix == 'd':
    texte_dechiffre = dechiffrer_cesar(texte, decalage)
    print("Résultat décodé :", texte_dechiffre)
else:
    print("Je n'ai pas compris. Mets 'c' pour coder ou 'd' pour décoder.")

# TP2 crypto efrei _____________________________________________________________________________________________________________________________________________
# Voici le code du Vigenere du TP2

def chiffrer_vigenere(texte, cle):
    resultat = ""
    cle = cle.lower()
    i = 0
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[i % len(cle)]) - ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
            i += 1
        else:
            resultat += char
    return resultat

def dechiffrer_vigenere(texte, cle):
    resultat = ""
    cle = cle.lower()
    i = 0
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[i % len(cle)]) - ord('a')
            resultat += chr((ord(char) - base - decalage) % 26 + base)
            i += 1
        else:
            resultat += char
    return resultat


choix = input("Tu veux chiffrer ou déchiffrer ? (c/d) : ").lower()

if choix == 'c':
    texte = input("Quel texte veux-tu chiffrer ? ")
    cle = input("Quelle clé Vigenère veux-tu utiliser ? ")
    print("Texte chiffré :", chiffrer_vigenere(texte, cle))
elif choix == 'd':
    texte = input("Quel texte veux-tu déchiffrer ? ")
    cle = input("Quelle clé Vigenère a été utilisée ? ")
    print("Texte déchiffré :", dechiffrer_vigenere(texte, cle))
else:
    print("Choix non reconnu. Tape 'c' pour chiffrer ou 'd' pour déchiffrer.")

