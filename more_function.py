from pygame_info import windows_width, windows_height, window, nutri_quare_size
import pygame 


class Terminal_Show:
    @classmethod
    def print_nutri_map(cls, nutri_map):
        for i in nutri_map:
            lister = []
            for j in i:
                lister += [j.nutrient_amount] 
            print(lister)

class Pygame_Display:
    pass
