# My First Pygame, Alex Scott, 12/01/21 2:23pm

import pygame, sys
from pygame import pixelarray
from pygame.locals import *
# Start Pygame
pygame.init()
      
# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
PURPLERAIN = (128, 110, 225) 

# Setup font. 
basicFont = pygame.font.SysFont(None, 48)

# Setup text. 
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color. 
windowSurface.fill(PURPLERAIN)

# Draw a polygon onto the screen
pygame.draw.polygon(windowSurface, BLACK, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw lines on the screen. 
pygame.draw.line(windowSurface, WHITE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (75, 60), (60, 75), 2)
pygame.draw.line(windowSurface, RED, (0,60), (120, 0), 1)

# Draw a circle.
pygame.draw.circle(windowSurface, PURPLERAIN, (128, 110), 10, 225)

# Draw an ellipse.
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw the text rectangle. 
pygame.draw.rect(windowSurface, WHITE, (textRect.left - 20, textRect.top - 20, textRect.width - 20, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLUE
del pixArray 

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Update Pygame Display
pygame.display.update()

# Run game loop.
while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()