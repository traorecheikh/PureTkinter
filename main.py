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


root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()