import pygame
pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 14, 201, 30)
RED = ( 255, 0, 0)
size = (700, 500)
YELLOW = ( 255, 249, 82)
BLUE = ( 107, 204, 242)
BROWN = ( 97, 68, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Freedom")
carryOn = True
clock = pygame.time.Clock()

 
 

while carryOn:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
 
   
 
    
    screen.fill(BLUE)

	
    pygame.draw.rect(screen, GREEN, [0, 450, 1000, 70],200)
    pygame.draw.circle(screen, YELLOW, [20,20,], 100)
    pygame.draw.rect(screen, BROWN, [598, 275, 10, 90], 10)
    pygame.draw.circle(screen, GREEN, [600,250], 30)
	
    pygame.display.flip()
     
    
    clock.tick(60)
 
pygame.quit()