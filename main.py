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


root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()