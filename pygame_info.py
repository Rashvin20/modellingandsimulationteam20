import pygame

windows_width = 1100
windows_height = 800

nutri_quare_size = 50

window = pygame.display.set_mode((windows_width, windows_height)) 



pygame.init() 
background_colour = (234, 212, 202) 
pygame.display.set_caption('Modelling Project') 
window.fill(background_colour) 
pygame.display.flip() 

