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
rect_x = int(WINDOW_WIDTH / 2)
rect_y = int(WINDOW_HEIGHT / 2)
rect_dx = 0
rect_dy = 0
rect_size = 40

running = True
while  running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect_dy +=4
                elif event.key == pygame.K_DOWN:
                    rect_dy-=4
                elif event.key == pygame.K_LEFT:
                    rect_dx-=4
                elif event.key == pygame.K_RIGHT:
                    rect_dx+=4
            elif event.type == pygame.KEYUP:
                 rect_dx,rect_dy = 0,0
    rect_x+=rect_dx
    rect_y+=rect_dy
    screen.fill(WHITE)
    if(rect_x)+20 >=WINDOW_WIDTH:
         rect_x  = rect_x-5
    if(rect_y)+20 <= WINDOW_HEIGHT:
         rext_y = rect_y-5
    if rect_x <= 0:
         pygame.draw.rect(screen,color,[rect_x,rect_y,20,20],0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
         

         
    