import tkinter as tk
from tkinter import messagebox
import time
import random
import os
import pygame

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Vitesse de Typage")
        self.center_window(600, 400)
        # Initialize Pygame mixer for audio
        pygame.mixer.init()

        # Load music and sound effects
        self.music_file = "background_music.mp3"
        self.sfx_file = "keyboard_stroke.mp3"
        self.load_audio()

        # List of French sentences
        self.sentences = [
            "Le vif renard brun saute par-dessus le chien paresseux.",
            "Emballez ma boîte avec cinq douzaines de bouteilles de liqueur.",
            "Comment les grenouilles sauteurs razorback peuvent-elles niveler six gymnastes piqués ?",
            "Sphinx de quartz noir, juge mon vœu.",
            "Les cinq sorciers boxeurs sautent rapidement."
        ]

        self.difficulty_levels = {
            "Facile": 0,
            "Moyenne": 1,
            "Difficile": 2
        }

        self.current_sentence = ""
        self.start_time = 0
        self.highest_speed = self.load_highest_speed()

        self.create_main_menu()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        def load_audio(self):
            # Load background music
            self.music = pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play(-1)  # Play music in a loop

            # Load sound effect
            self.sfx = pygame.mixer.Sound(self.sfx_file)

        def create_main_menu(self):
            self.menu_frame = tk.Frame(self.root)
            self.menu_frame.pack(fill=tk.BOTH, expand=True)

            self.title_label = tk.Label(self.menu_frame, text="Test de Vitesse de Typage", font=("Arial", 24))
            self.title_label.pack(pady=20)

            # Difficulty Selection
            self.difficulty_var = tk.StringVar(value="Facile")
            self.difficulty_label = tk.Label(self.menu_frame, text="Sélectionnez la difficulté :")
            self.difficulty_label.pack(pady=5)

            for level in self.difficulty_levels:
                tk.Radiobutton(self.menu_frame, text=level, variable=self.difficulty_var, value=level).pack(anchor=tk.W)

            # Music and SFX Options
            self.music_var = tk.BooleanVar(value=True)
            self.sfx_var = tk.BooleanVar(value=True)

            tk.Checkbutton(self.menu_frame, text="Musique", variable=self.music_var, command=self.toggle_music).pack(
                anchor=tk.W)
            tk.Checkbutton(self.menu_frame, text="Effets Sonores", variable=self.sfx_var, command=self.toggle_sfx).pack(
                anchor=tk.W)

            # Buttons
            self.play_button = tk.Button(self.menu_frame, text="Jouer", command=self.show_loading_screen)
            self.play_button.pack(pady=10)

            self.quit_button = tk.Button(self.menu_frame, text="Quitter", command=self.root.quit)
            self.quit_button.pack(pady=10)

            self.highest_speed_label = tk.Label(self.menu_frame,
                                                text=f"Vitesse Typique la Plus Élevée: {self.highest_speed:.2f} MPM",
                                                font=("Arial", 16))
            self.highest_speed_label.pack(pady=20)

        def toggle_music(self):
            if self.music_var.get():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()

        def toggle_sfx(self):
            # Toggle SFX not needed as sound is played directly
            pass

        def show_loading_screen(self):
            self.menu_frame.pack_forget()
            self.create_loading_screen()
            self.root.after(5000, self.start_test)

        def create_loading_screen(self):
            self.loading_frame = tk.Frame(self.root)
            self.loading_frame.pack(fill=tk.BOTH, expand=True)

            self.loading_label = tk.Label(self.loading_frame, text="Chargement...", font=("Arial", 24))
            self.loading_label.pack(pady=20)

            # Load images and show loading animation
            self.images = [tk.PhotoImage(file=f"loading_{i}.png") for i in range(1, 4)]
            self.image_label = tk.Label(self.loading_frame, image=self.images[0])
            self.image_label.pack(pady=20)

            self.image_index = 0
            self.animate_loading()


root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()