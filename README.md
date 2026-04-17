# 🎉 Jeu du Pendu — Python

## 🧩 Description

Ce projet est une version console du **jeu du pendu** écrite en **Python 3**.
Le but est simple : deviner un mot anglais caché, lettre par lettre ou en proposant directement le mot entier, avant d'épuiser le nombre de tentatives disponibles.

Le jeu inclut une gestion de pseudo, un affichage dynamique du mot à deviner, un dessin ASCII du pendu qui évolue à chaque erreur, et l'historique des lettres déjà essayées.

---

## 🚀 Fonctionnalités

- 🎭 Choix d'un **pseudo** ou jeu en mode **anonyme**
- 🔠 Sélection **aléatoire d'un mot anglais** (4 à 10 lettres, alphabétique)
- 💬 Affichage progressif du mot masqué (`_ _ _ _`)
- 🪢 **Dessin ASCII du pendu** qui se construit à chaque erreur
- 🧠 Gestion et affichage des **lettres déjà essayées**
- ❌ Limite de **6 erreurs** (pendu classique)
- 🔁 Possibilité de proposer directement le **mot complet**
- ♻️ Option **rejouer** à la fin de chaque partie
- 🎉 Messages personnalisés selon le résultat du joueur

---

## 🧰 Prérequis

Avant d'exécuter le script, assure-toi d'avoir installé :

- Python **3.8 ou supérieur**
- Le module `english_words`

### Installation du module requis

```bash
pip install english-words
```

---

## ▶️ Lancer le jeu

```bash
python Pendu.py
```

---

## 🎮 Exemple de partie

```
BIENVENUE bienvenue joyeux pendu 🎉
Voulez-vous un pseudo ? (y/n) 😁 y
Entrez votre pseudo : Alex
BIENVENU Alex

     ------
     |    |
          |
          |
          |
          |
    ========
Mot : _ _ _ _ _
Tentatives restantes : 6
Entre une lettre ou le mot 🔠 :
```
