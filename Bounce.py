"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]

screen = pygame.display.set_mode((400, 300), 0, 32)


pygame.display.set_caption("Bouncing Ball Game")

listcolors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]
color = random.choice(listcolors)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.



# WRITE YOUR CODE HERE
x_pos = 0
y_pos = 0
x = (x_pos, y_pos)



screen.fill(GREEN)
ball = pygame.draw.circle(screen, color, (x_pos, y_pos), 20, 0)
pygame.display.flip()
x_pos = random.randint(0,400)
y_pos = random.randint(0,300)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


