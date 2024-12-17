import random
import math as m
import pygame
from pygame_info import windows_width, windows_height, window, nutri_quare_size



class Tree:
    def __init__(self, x_pos = None, y_pos = None):
        self.age = 0
        #self.age_expectancy = age_expectancy
        self.growth_pts = 0 #earn points if grows
        self.reserves_pts = 0 #loose pts if no food, die if <0
        # self.x_pos = random.randint(0, windows_width)
        # self.y_pos = random.randint(0, windows_height)

        if x_pos == None:
            x_pos = random.randint(0, windows_width)
        if y_pos == None:
            y_pos = random.randint(0, windows_height)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.alive = True

        #print("xpos = ", x_pos, "y_pos", y_pos)
        
        #coeficients for equations
        self.fully_grown_age = 40 # 40 years to reach max height

    def draw_self(self):
        #draw tree in window
        pygame.draw.circle(window, (0, 125, 0), [self.x_pos, self.y_pos], 5, 0)

    def reproduce(self, tree_list):
        # change this to exp rand num depending on size and whatnot
        if random.random() > 0.9:
            self.add_new_tree(tree_list)
        #pass
    
    def add_new_tree(self, trees_list):
        coef = 0.1
        new_x = self.x_pos + (random.randint(0,1)*2-1)*random.expovariate(coef)
        new_y = self.y_pos + (random.randint(0,1)*2-1)*random.expovariate(coef)
        trees_list.append(Tree(new_x, new_y))

    def eat(self, map):
        hunger = self.hunger()

        #check if 

        if map[m.floor(self.Y)][m.floor(self.X)] > hunger:
            map[m.floor(self.Y)][m.floor(self.X)] -= hunger

    def hunger(self):
        """
        Returns how much ground nutrients the tree must eat
        """
        # #parameters
        # x_offset = 5
        # coef1 = self.fully_grown_age/10

        # #formula is modified sigmoid for a constrained growth
        # hunger = 1/(1+m.exp(-self.age * coef1 + x_offset))   

        coef = 1

        hunger = self.size() * coef

        return hunger
    
    def size(self):
        """
        How big the tree is, on a 0-1 scale, where 0 is smallest and 1 is biggest.
        Size is used to calculate other properties of the tree.
        """
        #parameters
        x_offset = 5
        coef1 = self.fully_grown_age/10

        #formula is modified sigmoid for a constrained growth
        return 1/(1+m.exp(-self.age * coef1 + x_offset))   

    def max_reserves(self):
        """
        Maximum amount of reserves (food to eat when there is no food) a tree can have 
        """
        max_reserves = self.size()

        pass

    def max_food_abs(self):
        """
        Maximum amount of food that tree can absorb at once
        """
        pass




            

class Nutrient:
    def __init__(self, init_nutri_amount, x_pos, y_pos):
        self.nutrient_amount = init_nutri_amount
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw_self(self):
        #draw nutri square in window
        red = int(170 * (1 - self.nutrient_amount) + 58)
        green = int(174* (1 - self.nutrient_amount) + 38)
        blue = int(126 * (1 - self.nutrient_amount))
        rect = pygame.Rect(self.x_pos,self.y_pos,nutri_quare_size,nutri_quare_size)
        pygame.draw.rect(window, (red,green,blue), rect)

    def replenish(self):
        """
        simulate soil growing back its nutrients, 
        (we assume it hapens independently of other events) 
        (no noise)
        """
        coef1 = 1.3
        coef2 = 0.3
    
        self.nutrient_amount = self.nutrient_amount * coef1 - self.nutrient_amount**2 * coef2

    

    
