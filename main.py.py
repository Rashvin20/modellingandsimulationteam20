# import the pygame module 
import pygame 
import objects as libs
#from python_sim import windows_width, windows_height
from pygame_info import windows_width, windows_height, window, nutri_quare_size
import more_function


pygame.init() 
timer = pygame.time.Clock()
  
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 202) 
  
# Define the dimensions of 
# screen object(width,height) 
# window = pygame.display.set_mode((windows_width, windows_height)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Modelling Project') 
  
# Fill the background colour to the screen 
window.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 
  
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


# trees +=[libs.Tree()]
# pygame.display.update()

timestep = pygame.USEREVENT + 1
pygame.time.set_timer(timestep, 1000)

nutri_map = [[libs.Nutrient(init_nutri_amount=0.5,x_pos=i*nutri_quare_size, y_pos=j*nutri_quare_size)
               for i in range(windows_width//nutri_quare_size)] 
               for j in range(windows_height//nutri_quare_size)]


more_function.Terminal_Show.print_nutri_map(nutri_map)

def show_nutrients(nutri_map, window):
    flag1 = True
    for i in nutri_map:
        for j in i:
            if flag1:
                pygame.draw.rect(window, (0,0,255*j.nutrient_amount),
                                  pygame.Rect(j.x_pos,j.y_pos,nutri_quare_size,nutri_quare_size))
            flag1 = not flag1


# game loop 
while running: 

    # for loop through the event queue   
    for event in pygame.event.get(): 

        if event.type == timestep: 
            show_nutrients(nutri_map, window)

            print("tree population:",len(trees))
            # trees += [libs.Tree()]
            trees_t = trees.copy() #trees at this moment in time
            for tree in trees_t:
                tree.reproduce(trees)
            pygame.display.update()
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

