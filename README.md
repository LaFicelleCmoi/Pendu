# 🎪 Jeu du Pendu — Python

## 🧩 Description

Deux versions du **jeu du pendu** en **Python 3** :

- 🖥️ **Console** ([Pendu.py](Pendu.py)) — dessin ASCII, pseudo, replay.
- 🎨 **Interface graphique** ([pendu_gui.py](pendu_gui.py)) — tkinter, thème sombre Catppuccin, canvas animé, clavier cliquable et raccourcis clavier.

Le but : deviner un mot anglais caché lettre par lettre, ou proposer directement le mot, avant d'épuiser les 6 vies.

---

## 🚀 Fonctionnalités

- 🎭 Choix d'un **pseudo** (ou mode anonyme)
- 🔠 Sélection **aléatoire d'un mot anglais** (4 à 10 lettres, alphabétique)
- 💬 Affichage progressif du mot masqué
- 🪢 **Pendu animé** (ASCII en console, dessin canvas en GUI)
- 🧠 Suivi des lettres déjà essayées (boutons colorés en GUI)
- ❤️ **6 vies** (compte à rebours visuel en GUI)
- ⌨️ **Raccourcis clavier** physiques dans l'interface graphique
- 🔁 Rejouer à la fin de la partie
- 🎉 Feedback visuel coloré (vert/jaune/rouge)

---

## 🧰 Prérequis

- Python **3.8 ou supérieur**
- Le module `english_words`
- Pour la GUI : `tkinter` (inclus avec Python sur la plupart des systèmes ; sur Debian/Ubuntu : `sudo apt install python3-tk`)

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

**Interface graphique (recommandé) :**

```bash
python pendu_gui.py
```

**Version console :**

```bash
python Pendu.py
```

---

## 🎮 Aperçu GUI

- Canvas avec le gibet et le pendu qui se construit à chaque erreur.
- Clavier QWERTY cliquable : les touches passent en **vert** si trouvées, **rouge** sinon et sont désactivées.
- Champ de saisie pour proposer le mot complet (`Entrée` pour valider).
- Compteur de vies coloré (vert → jaune → rouge).
- Bouton **Nouvelle partie** pour relancer.
