import random
import math as m
import pygame
from pygame_info import windows_width, windows_height, window, nutri_quare_size



class Tree:
    def __init__(self, x_pos = None, y_pos = None):
        self.age = 0
        self.growth = 0.01 #percentage of growth, at birth we assume it has 1% of its adult size
        self.reserves = 0 #loose pts if no food, die if <0
        self.size = 0.1 #no idea what unit that would be
        self.max_size = 15 #15m

        if x_pos == None:
            x_pos = random.randint(0, windows_width)
        if y_pos == None:
            y_pos = random.randint(0, windows_height)
        self.x_pos = x_pos
        self.y_pos = y_pos

        if 0 >= x_pos or x_pos >= windows_width or 0 >= y_pos or y_pos >= windows_height:
            del self # remove trees ouside map
        
        #coeficients for equations
        #self.fully_grown_age = 40 # 40 years to reach max height

    def draw_self(self):
        #draw tree in window
        pygame.draw.circle(window, (0, 125, 0), [self.x_pos, self.y_pos], m.ceil(8*self.growth), 0)

    def reproduce(self, tree_list):
        coef = 1
        # change this to exp rand num depending on size and whatnot
        # if random.random() > 0.9:
        #     self.add_new_tree(tree_list)
        
        for child in range(m.floor(random.expovariate(1/self.growth * coef))):
            self.add_new_tree(tree_list)

    
    
    def add_new_tree(self, trees_list):
        coef = 0.1
        new_x = self.x_pos + (random.randint(0,1)*2-1)*random.expovariate(coef)
        new_y = self.y_pos + (random.randint(0,1)*2-1)*random.expovariate(coef)
        trees_list.append(Tree(new_x, new_y))

    def eat(self, map, tree_list):
        """
        Function for trees "eating" ground nutrients.
        First the tree eats to assure its own survival, if successful in doing
        that, it then tries to eat surplus to grow bigger.
        If the tree cannot eat enough to grow, its growth is stunted, and if 
        the tree cannot eat enough to survive, it dies. 
        """
        coef_ntt = 1/750 #nutrient to tree coefficient (1 nutri square can feed 750pt of hunger, when 1 adult tree eats 150pt) 
        coef_min_nutri = 0.001
        coef_eff_nutri = 0.4 # 0-1, at what nutrient concentration do trees start having trouble eating

        #check available nutrients
        available_nutrients = map[int(self.y_pos//nutri_quare_size)][int(self.x_pos//nutri_quare_size)].nutrient_amount #in %
            
        #reserve and survival hunger
        survival_hunger = self.survival_hunger() #food tree must eat to stay alive
        res_hunger = (self.max_reserves() - self.reserves) #how much tree wants to eat to fill its reserves
        total_hunger = survival_hunger + res_hunger
        nutrients_absorbed = total_hunger * min([1, available_nutrients/coef_eff_nutri]) #if less than 20% nutrients, tree has trouble absorbing nutrients
        food_for_tree = nutrients_absorbed - survival_hunger #food for survival dissapears, rest is for tree reserves
        self.reserves += food_for_tree
        #remove nutrients from ground
        map[int(self.y_pos//nutri_quare_size)][int(self.x_pos//nutri_quare_size)].nutrient_amount = \
            max([coef_min_nutri, available_nutrients - coef_ntt * nutrients_absorbed]) #never make it less than minimum amount
        

        #growth hunger
        if self.reserves > self.max_reserves() * 0.9: #if tree has filled 90% of its reserves
            available_nutrients = map[int(self.y_pos//nutri_quare_size)][int(self.x_pos//nutri_quare_size)].nutrient_amount #update available nutrients
            desired_growth = self.growth * 1.2 - self.growth**2 * 0.2 #takes about 40 years to reach full size
            self.growth = desired_growth * min([1, available_nutrients/coef_eff_nutri]) #if less than 20% nutrients, tree has trouble absorbing nutrients
            
        #check if tree dies of hunger
        if self.reserves < 0:
            self.kill(tree_list)


    def survival_hunger(self):
        """
        Returns how much ground nutrients the tree must eat to stay alive
        """
        coef = 5

        return m.exp(self.growth * coef)

    
    # def size(self):
    #     """
    #     How big the tree is, on a 0-1 scale, where 0 is smallest and 1 is biggest.
    #     Size is used to calculate other properties of the tree.
    #     """
    #     #parameters
    #     x_offset = 5
    #     coef1 = self.fully_grown_age/10

    #     #formula is modified sigmoid for a constrained growth
    #     return 1/(1+m.exp(-self.age * coef1 + x_offset))   

    def max_reserves(self):
        """
        Maximum amount of reserves (food to eat when there is no food) a tree can have 
        """
        coef = 5.8

        return m.exp(self.growth * coef)
    
    def kill(self, tree_list):
        """
        kill the current tree
        """
        tree_list.remove(self)

        del self






            

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

    

    
