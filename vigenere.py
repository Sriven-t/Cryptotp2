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

# ...existing code...
# ...existing code...

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
# ...existing code...
