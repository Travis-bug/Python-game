import pygame
import os

class BackgroundSound:
    def __init__(self):
        pygame.mixer.init() # Initialize the mixer module
        self.music_files=  { 
            
            "Loading_screen": "assets/sounds/background_music.WAV", # 

            
            "Game_Play": "assets/sounds/game_music.WAV",
            "Game_Over": "assets/sounds/game_over_music.WAV",
            "game_pause": "assets/sounds/pause_music.WAV"
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

