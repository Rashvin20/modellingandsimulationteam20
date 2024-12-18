from pygame_info import windows_width, windows_height, window, nutri_quare_size
import pygame 
import math as m


class Terminal_Show:
    @classmethod
    def print_nutri_map(cls, nutri_map):
        for i in nutri_map:
            lister = []
            for j in i:
                lister += [round(j.nutrient_amount,2)] 
            print(lister)

class Pygame_Display:
    @classmethod
    def show_nutrients(cls, nutri_map):
        for nutri_row in nutri_map:
            for nutri in nutri_row:
                nutri.draw_self()

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

    @classmethod
    def tree_eat_nutrients(cls, tree_list, nutri_map, list_lifespan_trees):
        for tree in tree_list:
            tree.eat(nutri_map, tree_list, list_lifespan_trees)
        
    @classmethod
    def kill_trees_no_sun(cls, tree_list, list_lifespan_trees):
        for tree in tree_list:
            tree.die_if_under_canopy(tree_list, list_lifespan_trees)
