import random
from english_words import get_english_words_set

print("BIENVENUE bienvenue joyeux pendu 🎉")

def pseudo():
    choix = input("Voulez-vous un pseudo ? (y/n) 😁 ").lower()
    if choix == "y":
        name = input("Entrez votre pseudo : ")
        print("BIENVENU", name)
        return name
    else:
        print("Très bien, bonne chance anonyme 🎉")
        return "anonyme"

player = pseudo()

# Choisir un mot aléatoirement
words = list(get_english_words_set(['web2'], lower=True))
secret = random.choice(words)

# Affichage du mot masqué
word_display = ["_"] * len(secret)
attempts = 0
max_attempts = 12
guessed_letters = []

print(" ".join(word_display))

# Boucle principale
while attempts < max_attempts and "_" in word_display:
    user = input("Entre une lettre ou le mot 🔠: ").lower()

    # Vérifier si l'utilisateur propose le mot complet
    if len(user) > 1:
        if user == secret:
            print(f"🎉🎉🎉 Bravo {player} ! Tu as trouvé le mot : {secret}")
            break
        else:
            print("❌ Mauvais mot.")
            attempts += 1

    # Sinon, il propose une lettre
    elif len(user) == 1 and user.isalpha():
        if user in guessed_letters:
            print("⚠️ Tu as déjà esseyerr cette lettre.")
        else:
            guessed_letters.append(user)
            if user in secret:
                print(f"✅ Bien joué ! La lettre '{user}' est dans le mot.")
                for i, letter in enumerate(secret):
                    if letter == user:
                        word_display[i] = user
            else:
                print(f"❌ Désolé, la lettre '{user}' n'est pas dans le mot.")
                attempts += 1
    else:
        print("⚠️ Entre une seule lettre ou un mot valide.")

    print("Mot:", " ".join(word_display))
    print(f"Tentatives restantes: {max_attempts - attempts}")

# Fin du jeu
if "_" not in word_display:
    print(f"🎉 Félicitations {player} ! Tu as trouvé le mot '{secret}' en {attempts} tentatives.")
else:
    print(f"💀 Tu as perdu {player}... Le mot était : {secret}")
