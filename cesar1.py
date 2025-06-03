# ...existing code...

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

# Interaction avec l'utilisateur
texte = input("Tape le texte à coder ou décoder : ")
try:
    decalage = int(input("Donne la clé (un nombre entier) : "))
except ValueError:
    print("Il faut entrer un nombre entier pour la clé.")
    exit()

# Menu pour choisir chiffrer ou déchiffrer
choix = input("Tu veux coder ou décoder ? (c/d) : ").lower()

if choix == 'c':
    texte_chiffre = chiffrer_cesar(texte, decalage)
    print("Résultat codé :", texte_chiffre)
elif choix == 'd':
    texte_dechiffre = dechiffrer_cesar(texte, decalage)
    print("Résultat décodé :", texte_dechiffre)
else:
    print("Je n'ai pas compris. Mets 'c' pour coder ou 'd' pour décoder.")
# ...existing code...
