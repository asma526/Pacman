import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("PACMAN")


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Ghost CLASS CODE  

class Ghost():
    x_location = 1
    y_location = 50

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ghost_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ghost_size = ghost_size 

    # GHOST METHODS 
    # Flash and Bounce: The actions the ghost can perform 
    def flashGhost(self, screen, ghost_color, screen_width, screen_height):

        ghost_color = ghost_color 

        if self.x_location >= screen_width - self.ghost_size or self.x_location < self.ghost_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ghost_size or self.y_location < self.ghost_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ghost_color, [self.x_location, self.y_location], self.ghost_size)

# -------- Main Program Loop -----------
ghost = Ghost(50,50,10,2,20)
ghost2 = Ghost(250,150,5,3,20)

x,y=100,100
moveX,moveY=0,0
clock = pygame.time.Clock()
gameloop = True
while gameloop:
    # --- Main event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameloop = False
    
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT):
 
                moveX = -5
 
            if (event.key==pygame.K_RIGHT):
 
                moveX = 5
 
            if (event.key==pygame.K_UP):
 
                moveY = -5
 
            if (event.key==pygame.K_DOWN):
 
                moveY = 5
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
 
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
 
                moveX=0
 
            if (event.key==pygame.K_UP):
 
                moveY=0
 
            if (event.key==pygame.K_DOWN):
 
                moveY=0
    if x == Ghost.x_location - 20 and y == Ghost.y_location - 20:
        pygame.draw.circle(screen,BLACK,(x,y),60)
        gameloop = False
        
    screen.fill(BLACK)

    ghost.flashGhost(screen,RED,SCREEN_WIDTH,SCREEN_HEIGHT)
    ghost2.flashGhost(screen,BLUE,SCREEN_WIDTH,SCREEN_HEIGHT)
    
    x+=moveX
    y+=moveY
    
    pygame.draw.circle(screen,YELLOW,(x,y),60)
    
        

    # --- Game logic should go here
  
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


