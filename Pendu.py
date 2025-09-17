import random
from english_words import get_english_words_set

print("BIENVENUE bienvenue joyeux pendu")

def pseudo():
        pseudo = input("Voulez-vous un pseudo y n 😁 ").lower()
        if pseudo == "y":
                pseudo = input("Entrez votre pseudo : ")
                print("BIENVENU", pseudo)
        else:
                print("Très bien, bonne chance anonyme 🎉 ")
pseudo()


#Choisir un mot
words = list(get_english_words_set(['web2'], lower = True))

#Mot choisi aléatoirement
secret = random.choice(list(words))
word_display = print('_' * len(secret))
attempts = 0
max_attempts = 12
guessed_letters = []
Rep= ""*caracter

#Demande de lettre
user = input("Entre une lettre ou le mot 🔠: ").lower()


