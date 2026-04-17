import random
from english_words import get_english_words_set

HANGMAN_STAGES = [
    """
     ------
     |    |
          |
          |
          |
          |
    ========""",
    """
     ------
     |    |
     O    |
          |
          |
          |
    ========""",
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    ========""",
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    ========""",
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ========""",
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ========""",
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ========""",
]

MAX_ATTEMPTS = len(HANGMAN_STAGES) - 1  # 6 erreurs autorisées


def ask_pseudo():
    choix = input("Voulez-vous un pseudo ? (y/n) 😁 ").strip().lower()
    if choix == "y":
        name = input("Entrez votre pseudo : ").strip()
        if not name:
            name = "anonyme"
        print("BIENVENU", name)
        return name
    print("Très bien, bonne chance anonyme 🎉")
    return "anonyme"


def pick_secret_word(min_len=4, max_len=10):
    words = [
        w for w in get_english_words_set(["web2"], lower=True)
        if w.isalpha() and min_len <= len(w) <= max_len
    ]
    return random.choice(words)


def render_state(word_display, guessed_letters, attempts):
    print(HANGMAN_STAGES[attempts])
    print("Mot :", " ".join(word_display))
    if guessed_letters:
        print("Lettres essayées :", ", ".join(sorted(guessed_letters)))
    print(f"Tentatives restantes : {MAX_ATTEMPTS - attempts}")


def play_round(player):
    secret = pick_secret_word()
    word_display = ["_"] * len(secret)
    guessed_letters = set()
    attempts = 0

    render_state(word_display, guessed_letters, attempts)

    while attempts < MAX_ATTEMPTS and "_" in word_display:
        user = input("Entre une lettre ou le mot 🔠 : ").strip().lower()

        if not user:
            print("⚠️ Entre une seule lettre ou un mot valide.")
            continue

        if len(user) > 1:
            if not user.isalpha():
                print("⚠️ Entre un mot alphabétique valide.")
                continue
            if user == secret:
                word_display = list(secret)
                print(f"🎉🎉🎉 Bravo {player} ! Tu as trouvé le mot : {secret}")
                break
            print("❌ Mauvais mot.")
            attempts += 1

        elif user.isalpha():
            if user in guessed_letters:
                print("⚠️ Tu as déjà essayé cette lettre.")
                continue
            guessed_letters.add(user)
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
            continue

        render_state(word_display, guessed_letters, attempts)

    if "_" not in word_display:
        print(f"🎉 Félicitations {player} ! Le mot était '{secret}' ({attempts} erreur(s)).")
    else:
        print(HANGMAN_STAGES[MAX_ATTEMPTS])
        print(f"💀 Tu as perdu {player}... Le mot était : {secret}")


def main():
    print("BIENVENUE bienvenue joyeux pendu 🎉")
    player = ask_pseudo()
    while True:
        play_round(player)
        again = input("Rejouer ? (y/n) ").strip().lower()
        if again != "y":
            print(f"Merci d'avoir joué, {player} ! 👋")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPartie interrompue. À bientôt ! 👋")
