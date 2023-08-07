import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255,255,255)

pygame.init()
pygame.display.set_caption("2.py")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
    screen.fill(WHITE)
    pygame.draw.rect(screen,(0,0,0),[50,50,100,100],0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()