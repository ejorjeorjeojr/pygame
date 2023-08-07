import pygame
import random
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
pygame.init()
pygame.display.set_caption("3.py")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
color = BLACK

running = True

while not running:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                running  = False
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                    color = random.choice([BLUE,RED,GREEN])
    screen.fill(WHITE)
    rect = pygame.Rect(400,300,100,100)
    pygame.draw.rect(screen,color,rect,0)
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()