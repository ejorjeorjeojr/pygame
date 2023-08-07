import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
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
    rect2 = pygame.Rect(0,0,50,50)
    rect2.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
    pygame.draw.rect(screen,BLUE,rect2,0)
    rect3 = pygame.Rect(200,200,20,20)
    pygame.draw.rect(screen,RED, rect3,0)
    print(rect3.center)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
