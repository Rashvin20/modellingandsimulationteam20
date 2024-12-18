# import the pygame module 
import pygame 
import objects as libs
#from python_sim import windows_width, windows_height
from pygame_info import windows_width, windows_height, window, nutri_quare_size
import more_function


timer = pygame.time.Clock()
    
# Variable to keep our game loop running 
running = True

def square_forest(width, height, trees):
    x_mid = width//2
    y_mid = height//2
    side = 3
    space = x_mid//5
    for x in range(side):  
        for y in range(side):
            trees += [libs.Tree(x_mid - space + space//side*(side//2)*x,y_mid - space + space//side*(side//2)*y)]
    
    

trees = []
square_forest(windows_width, windows_height, trees)
pygame.display.update()


timestep = pygame.USEREVENT + 1
pygame.time.set_timer(timestep, 1000) 

nutri_map = [[libs.Nutrient(init_nutri_amount=0.5,x_pos=i*nutri_quare_size, y_pos=j*nutri_quare_size)
               for i in range(windows_width//nutri_quare_size)] 
               for j in range(windows_height//nutri_quare_size)]


more_function.Terminal_Show.print_nutri_map(nutri_map)

iter = 0

# game loop 
while running: 

    # for loop through the event queue   
    for event in pygame.event.get(): 

        if event.type == timestep: 
            #make nutrients grow
            more_function.Simulation.nutriments_growth(nutri_map)
            more_function.Pygame_Display.show_nutrients(nutri_map)

            #make trees eat nutrients
            more_function.Simulation.tree_eat_nutrients(trees, nutri_map)
            more_function.Pygame_Display.show_nutrients(nutri_map)

            #tree reproduction
            more_function.Simulation.tree_reproduction(trees)
            more_function.Pygame_Display.show_trees(trees)
            

            #kill trees with no sunlight
            more_function.Simulation.kill_trees_no_sun(trees)
            more_function.Pygame_Display.show_trees(trees)

            #terminal view
            more_function.Terminal_Show.print_nutri_map(nutri_map)
            print("iteration:", iter)
            print("tree population:",len(trees))
            iter += 1
            
            #update window
            pygame.display.update()
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

