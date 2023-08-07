import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255,255,255)

pygame.init()
pygame.display.set_caption("1.py")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()




