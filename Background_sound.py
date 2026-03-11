import pygame
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class BackgroundSound:
    def __init__(self):
        pygame.mixer.init() # Initialize the mixer module

        self.music_files=  { 
            
            "Loading_screen": resource_path("assets/sounds/background_music.WAV"), # 
            "Game_Play": resource_path("assets/sounds/game_music.WAV"),
            "Game_Over": resource_path("assets/sounds/game_over_music.WAV"),
            "game_pause": resource_path("assets/sounds/pause_music.WAV")
        }

        self.present_state = None # Initialize with no state

    def change_state(self, new_state):
    
        if new_state == self.present_state: 
            return  # No change in state, do nothing
        
        self.present_state = new_state # Update the current state

        track = self.music_files.get(self.present_state, "assets/sounds/background_music.WAV")

        if track and os.path.exists(track):

         pygame.mixer.music.load(track)
         pygame.mixer.music.play(-1)  # Loop indefinitely

