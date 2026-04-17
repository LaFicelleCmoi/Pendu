import random
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

from english_words import get_english_words_set

# Palette Catppuccin Mocha
BG = "#1e1e2e"
SURFACE = "#313244"
SURFACE2 = "#45475a"
TEXT = "#cdd6f4"
SUBTEXT = "#a6adc8"
GREEN = "#a6e3a1"
RED = "#f38ba8"
YELLOW = "#f9e2af"
BLUE = "#89b4fa"
MAUVE = "#cba6f7"
PEACH = "#fab387"
OVERLAY = "#6c7086"

MAX_WRONG = 6
KEYBOARD_ROWS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]


def load_words(min_len=4, max_len=10):
    return [
        w for w in get_english_words_set(["web2"], lower=True)
        if w.isalpha() and min_len <= len(w) <= max_len
    ]


class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Le Pendu")
        self.root.configure(bg=BG)
        self.root.geometry("860x720")
        self.root.minsize(820, 700)

        self.words = load_words()
        self.player = "anonyme"
        self.secret = ""
        self.display = []
        self.guessed = set()
        self.wrong = 0
        self.game_over = False
        self.key_buttons = {}

        self._build_fonts()
        self._build_ui()
        self._show_welcome()

    def _build_fonts(self):
        self.title_font = tkfont.Font(family="Segoe UI", size=28, weight="bold")
        self.word_font = tkfont.Font(family="Consolas", size=36, weight="bold")
        self.label_font = tkfont.Font(family="Segoe UI", size=12)
        self.small_font = tkfont.Font(family="Segoe UI", size=10)
        self.key_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")
        self.btn_font = tkfont.Font(family="Segoe UI", size=11, weight="bold")

    # ---------- UI layout ----------
    def _build_ui(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=24, pady=(20, 8))
        tk.Label(
            header, text="🎪 Le Pendu", font=self.title_font,
            fg=MAUVE, bg=BG,
        ).pack(side="left")
        self.player_label = tk.Label(
            header, text="", font=self.label_font, fg=SUBTEXT, bg=BG,
        )
        self.player_label.pack(side="right")

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=24, pady=8)

        # Gauche : canvas pendu
        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="y", padx=(0, 20))
        self.canvas = tk.Canvas(
            left, width=280, height=340, bg=SURFACE,
            highlightthickness=0, bd=0,
        )
        self.canvas.pack()
        self.attempts_label = tk.Label(
            left, text="", font=self.label_font, fg=YELLOW, bg=BG,
        )
        self.attempts_label.pack(pady=(12, 0))

        # Droite : mot, message, clavier, actions
        right = tk.Frame(body, bg=BG)
        right.pack(side="left", fill="both", expand=True)

        self.word_label = tk.Label(
            right, text="", font=self.word_font, fg=TEXT, bg=BG,
        )
        self.word_label.pack(pady=(10, 6))

        self.message_label = tk.Label(
            right, text="", font=self.label_font, fg=SUBTEXT, bg=BG,
            wraplength=500, justify="center",
        )
        self.message_label.pack(pady=(0, 12))

        self.keyboard_frame = tk.Frame(right, bg=BG)
        self.keyboard_frame.pack(pady=(4, 8))
        self._build_keyboard()

        # Ligne : proposer un mot entier
        guess_frame = tk.Frame(right, bg=BG)
        guess_frame.pack(pady=(6, 4))
        tk.Label(
            guess_frame, text="Proposer le mot :",
            font=self.label_font, fg=SUBTEXT, bg=BG,
        ).pack(side="left", padx=(0, 8))
        self.guess_entry = tk.Entry(
            guess_frame, font=self.label_font, bg=SURFACE, fg=TEXT,
            insertbackground=TEXT, relief="flat", width=18,
        )
        self.guess_entry.pack(side="left", ipady=4)
        self.guess_entry.bind("<Return>", lambda _e: self._guess_word())
        self._make_button(
            guess_frame, "Valider", BLUE, self._guess_word,
        ).pack(side="left", padx=(8, 0))

        # Bouton nouvelle partie
        self._make_button(
            right, "🔁 Nouvelle partie", MAUVE, self._new_game,
        ).pack(pady=(16, 0))

        # Raccourcis clavier physiques
        self.root.bind("<Key>", self._on_key)

    def _build_keyboard(self):
        for row_idx, row in enumerate(KEYBOARD_ROWS):
            row_frame = tk.Frame(self.keyboard_frame, bg=BG)
            row_frame.pack(pady=3)
            for letter in row:
                btn = tk.Button(
                    row_frame, text=letter.upper(), width=3,
                    font=self.key_font, bg=SURFACE, fg=TEXT,
                    activebackground=SURFACE2, activeforeground=TEXT,
                    relief="flat", bd=0, cursor="hand2",
                    command=lambda l=letter.lower(): self._guess_letter(l),
                )
                btn.pack(side="left", padx=3, ipadx=4, ipady=6)
                self.key_buttons[letter.lower()] = btn

    def _make_button(self, parent, text, color, command):
        btn = tk.Button(
            parent, text=text, font=self.btn_font,
            bg=color, fg=BG, activebackground=color, activeforeground=BG,
            relief="flat", bd=0, cursor="hand2",
            padx=16, pady=6, command=command,
        )
        return btn

    # ---------- Flow ----------
    def _show_welcome(self):
        win = tk.Toplevel(self.root)
        win.title("Bienvenue")
        win.configure(bg=BG)
        win.geometry("380x220")
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        tk.Label(
            win, text="🎉 Bienvenue !", font=self.title_font,
            fg=MAUVE, bg=BG,
        ).pack(pady=(18, 6))
        tk.Label(
            win, text="Entre ton pseudo (laisse vide pour anonyme) :",
            font=self.label_font, fg=SUBTEXT, bg=BG,
        ).pack(pady=(0, 8))
        entry = tk.Entry(
            win, font=self.label_font, bg=SURFACE, fg=TEXT,
            insertbackground=TEXT, relief="flat", width=22, justify="center",
        )
        entry.pack(ipady=6)
        entry.focus_set()

        def submit(_e=None):
            name = entry.get().strip() or "anonyme"
            self.player = name
            self.player_label.config(text=f"👤 {name}")
            win.destroy()
            self._new_game()

        entry.bind("<Return>", submit)
        self._make_button(win, "C'est parti !", GREEN, submit).pack(pady=16)

        self.root.wait_window(win)

    def _new_game(self):
        self.secret = random.choice(self.words)
        self.display = ["_"] * len(self.secret)
        self.guessed = set()
        self.wrong = 0
        self.game_over = False
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        for btn in self.key_buttons.values():
            btn.config(state="normal", bg=SURFACE, fg=TEXT)
        self._set_message("Devine une lettre ou propose le mot !", SUBTEXT)
        self._redraw()

    def _guess_letter(self, letter):
        if self.game_over or letter in self.guessed or not letter.isalpha():
            return
        self.guessed.add(letter)
        btn = self.key_buttons.get(letter)
        if letter in self.secret:
            for i, c in enumerate(self.secret):
                if c == letter:
                    self.display[i] = letter
            if btn:
                btn.config(bg=GREEN, fg=BG, state="disabled", disabledforeground=BG)
            self._set_message(f"✅ '{letter.upper()}' est dans le mot.", GREEN)
        else:
            self.wrong += 1
            if btn:
                btn.config(bg=RED, fg=BG, state="disabled", disabledforeground=BG)
            self._set_message(f"❌ '{letter.upper()}' n'y est pas.", RED)
        self._redraw()
        self._check_end()

    def _guess_word(self):
        if self.game_over:
            return
        word = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END)
        if not word or not word.isalpha():
            self._set_message("⚠️ Entre un mot alphabétique.", YELLOW)
            return
        if word == self.secret:
            self.display = list(self.secret)
            self._redraw()
            self._win()
        else:
            self.wrong += 1
            self._set_message(f"❌ Ce n'est pas '{word}'.", RED)
            self._redraw()
            self._check_end()

    def _on_key(self, event):
        if self.game_over:
            return
        # Évite de capturer les touches quand l'utilisateur tape dans l'Entry
        if self.root.focus_get() is self.guess_entry:
            return
        key = event.keysym.lower()
        if len(key) == 1 and key.isalpha():
            self._guess_letter(key)

    def _check_end(self):
        if "_" not in self.display:
            self._win()
        elif self.wrong >= MAX_WRONG:
            self._lose()

    def _win(self):
        self.game_over = True
        self._set_message(
            f"🎉 Bravo {self.player} ! Le mot était '{self.secret}'.", GREEN,
        )
        self._disable_all_keys()

    def _lose(self):
        self.game_over = True
        self._set_message(
            f"💀 Perdu {self.player}. Le mot était '{self.secret}'.", RED,
        )
        self._disable_all_keys()

    def _disable_all_keys(self):
        for btn in self.key_buttons.values():
            btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def _set_message(self, text, color):
        self.message_label.config(text=text, fg=color)

    # ---------- Render ----------
    def _redraw(self):
        remaining = MAX_WRONG - self.wrong
        color = GREEN if remaining > 3 else YELLOW if remaining > 1 else RED
        self.attempts_label.config(
            text=f"❤️ Vies restantes : {remaining} / {MAX_WRONG}", fg=color,
        )
        # Mot masqué : espace visuel entre les lettres
        shown = "  ".join(c.upper() if c != "_" else "_" for c in self.display)
        self.word_label.config(text=shown)
        self._draw_hangman()

    def _draw_hangman(self):
        c = self.canvas
        c.delete("all")
        w = int(c["width"])
        h = int(c["height"])

        # Gibet (toujours visible)
        c.create_line(30, h - 20, w - 30, h - 20, fill=OVERLAY, width=6)
        c.create_line(80, h - 20, 80, 30, fill=OVERLAY, width=6)
        c.create_line(80, 30, 200, 30, fill=OVERLAY, width=6)
        c.create_line(200, 30, 200, 65, fill=OVERLAY, width=4)

        stage = self.wrong
        body_color = RED if stage >= MAX_WRONG else PEACH

        if stage >= 1:  # tête
            c.create_oval(175, 65, 225, 115, outline=body_color, width=4)
        if stage >= 2:  # torse
            c.create_line(200, 115, 200, 200, fill=body_color, width=4)
        if stage >= 3:  # bras gauche
            c.create_line(200, 135, 170, 175, fill=body_color, width=4)
        if stage >= 4:  # bras droit
            c.create_line(200, 135, 230, 175, fill=body_color, width=4)
        if stage >= 5:  # jambe gauche
            c.create_line(200, 200, 175, 245, fill=body_color, width=4)
        if stage >= 6:  # jambe droite + yeux X
            c.create_line(200, 200, 225, 245, fill=body_color, width=4)
            c.create_text(187, 85, text="✕", fill=RED, font=("Segoe UI", 12, "bold"))
            c.create_text(213, 85, text="✕", fill=RED, font=("Segoe UI", 12, "bold"))


def main():
    try:
        root = tk.Tk()
    except tk.TclError as e:
        print(f"Impossible d'ouvrir l'interface graphique : {e}")
        print("Lance plutôt la version console : python Pendu.py")
        return
    HangmanApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
