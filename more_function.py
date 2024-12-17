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
    @classmethod
    def show_nutrients(cls, nutri_map):
        for nutri_row in nutri_map:
            for nutri in nutri_row:
                nutri.draw_self()

    # @classmethod
    # def show_nutrients(cls, nutri_map, window):
    #     for i in nutri_map:
    #         for j in i:
    #             pygame.draw.rect(window, (0,0,255*j.nutrient_amount),
    #                             pygame.Rect(j.x_pos,j.y_pos,nutri_quare_size,nutri_quare_size))

    @classmethod
    def show_trees(cls, tree_list):
        for tree in tree_list:
            tree.draw_self()
        
class Simulation:
    @classmethod
    def tree_reproduction(cls, trees):
        trees_t = trees.copy() #trees at this moment in time
        for tree in trees_t:
            tree.reproduce(trees)

    @classmethod
    def nutriments_growth(cls, nutri_map):
        for nutri_row in nutri_map:
            for nutri in nutri_row:
                nutri.replenish()
