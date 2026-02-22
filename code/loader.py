import os
import sys
import pygame

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev & PyInstaller """
    if getattr(sys, 'frozen', False):  # Running as an .exe
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath("..")  # Go one level up to main project folder
    return os.path.join(base_path, relative_path)

def load_image(path):
    """ Load an image using the correct path """
    return pygame.image.load(resource_path(path))

def load_sound(path):
    """ Load a sound using the correct path """
    return pygame.mixer.Sound(resource_path(path))

def load_music(path):
    """ Load music using the correct path """
    pygame.mixer.music.load(resource_path(path))

def load_font(path, size):
    """ Load a font using the correct path """
    return pygame.font.Font(resource_path(path), size)