import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255,255,255)
BLUE = (0,0,255)
pygame.init()
pygame.display.set_caption("3.py")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen,(0,0,0),[50,50,100,100],0)
    pygame.draw.rect(screen,BLUE,[(WINDOW_WIDTH//2)-25,(WINDOW_HEIGHT//2)-25,50,50],0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
