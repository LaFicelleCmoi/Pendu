# 🎪 Jeu du Pendu — Python

## 🧩 Description

Version graphique du **jeu du pendu** écrite en **Python 3** avec **Tkinter**.
Le but : deviner un mot caché (🇫🇷 français ou 🇬🇧 anglais, switchable en un clic) lettre par lettre, ou proposer directement le mot, avant d'épuiser les 6 vies.

Interface soignée (thème sombre Catppuccin), pendu dessiné sur un canvas, clavier QWERTY cliquable et raccourcis clavier physiques.

---

## 🚀 Fonctionnalités

- 🎭 Choix d'un **pseudo** (ou mode anonyme) via une fenêtre d'accueil
- 🌍 **Toggle 🇫🇷 / 🇬🇧** pour basculer la langue des mots (relance une partie)
- 🎯 **Trois niveaux de difficulté** (Facile 4-6 / Normal 5-8 / Difficile 7-10 lettres)
- 💡 **Bouton indice** qui révèle une lettre au prix d'une vie (désactivé si ça tuerait le joueur)
- 📊 **Stats persistées** (victoires, défaites, % de réussite, série en cours et record), sauvegardées dans `~/.pendu_stats.json`
- 🔠 Sélection **aléatoire d'un mot** (alphabétique, accents retirés)
- 🪢 **Pendu dessiné** qui se construit à chaque erreur
- ⌨️ **Clavier QWERTY cliquable** + raccourcis clavier physiques, **Ctrl+N** pour nouvelle partie
- 🟢🔴 Touches colorées (vert = trouvée, rouge = absente, bleu = indice) et désactivées après usage
- 📝 Champ pour proposer le **mot complet**
- ❤️ Compteur de **vies** coloré (vert → jaune → rouge)
- 🔁 Bouton **Nouvelle partie** pour relancer sans fermer la fenêtre

---

## 🧰 Prérequis

- Python **3.8 ou supérieur**
- `tkinter` (inclus avec Python sur la plupart des systèmes ; sur Debian/Ubuntu : `sudo apt install python3-tk`)
- Le module `english_words`

---

## 📦 Installation

Sur les distributions récentes (Ubuntu 24+, Debian 12+), `pip` refuse l'installation globale (PEP 668). Utilise un environnement virtuel :

```bash
cd Pendu
python3 -m venv .venv
source .venv/bin/activate        # sous Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Lancer le jeu

```bash
python Pendu.py
```
