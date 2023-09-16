import pygame
import os
import sys
import random
from time import sleep
import tkinter as tk
root = tk.Tk()


SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()



GRID_SIZE = 20
GRID_WIDTH =  SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE


UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

WHITE = (255,255,255)
RED = (250,0,0)
GRAY = (100,100,100)
ORANGE = (255,158,73)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
PURPLE = (245,153, 255)



class Snake():
    def __init__(self):
        self.create()
    def create(self):
        self.length = 17
        self.positions = [(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
    def control(self,xy):
        if (xy[0]*-1,xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0]+(x*GRID_SIZE)),(cur[1]+(y*GRID_SIZE))

        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0]<0 or new[0]>=SCREEN_WIDTH or new[1]<0 or new[1]<0 or new[1]>= SCREEN_HEIGHT:
            sleep(1)
            self.create()    
        else:
            self.positions.insert(0,new)
            if len(self.positions)>self.length:
                self.positions.pop()

    def eat(self, feed):
        self.length+=feed.eat_length
    def draw(self,screen):
        red, purple, blue = 50/ (self.length-1), 150,150/ (self.length -1)
        for i , p in enumerate(self.positions):
            color = (100 +red *i, purple, blue *i)
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, color, rect)

class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = RED
        self.eat_length = 3
        self.create()
    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0,GRID_HEIGHT-1)
        self.position = x*GRID_SIZE, y*GRID_SIZE
    def draw(self, screen):
        rect = pygame.Rect((self.position[0],self.position[1]),(GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,self.color,rect)

class Feed1():
    def __init__(self):
        self.position = (0,0)
        self.color = ORANGE
        self.eat_length = 5
        self.create()
    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0,GRID_HEIGHT-1)
        self.position = x*GRID_SIZE, y*GRID_SIZE
    def draw(self, screen):
        rect = pygame.Rect((self.position[0],self.position[1]),(GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,self.color,rect)

class Feed2():
    def __init__(self):
        self.position = (0,0)
        self.color = GREEN
        self.eat_length = 30
        self.create()
    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0,GRID_HEIGHT-1)
        self.position = x*GRID_SIZE, y*GRID_SIZE
    def draw(self, screen):
        rect = pygame.Rect((self.position[0],self.position[1]),(GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,self.color,rect)

class Feed3():
    def __init__(self):
        self.position = (0,0)
        self.color = PURPLE
        self.eat_length = 1
        self.create()
    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0,GRID_HEIGHT-1)
        self.position = x*GRID_SIZE, y*GRID_SIZE
    def draw(self, screen):
        rect = pygame.Rect((self.position[0],self.position[1]),(GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,self.color,rect)
        

class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.feed1 = Feed1()
        self.feed2 = Feed2()
        self.feed3 = Feed3()
        self.speed = 25
        self.length = 0
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
                elif event.key == pygame.K_1:
                    self.speed += 3
                elif event.key == pygame.K_2:
                    self.speed += 5
                elif event.key == pygame.K_3:
                    self.speed -= 8
                
        return False
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake,self.feed)
        self.check_eat(self.snake,self.feed1)
        self.check_eat(self.snake,self.feed2)
        self.check_eat(self.snake,self.feed3)
        
    def check_eat(self,snake,feed):
        if snake.positions[0] == feed.position:
            snake.eat(feed)
            feed.create()

        


    def draw_info(self,length,speed,screen):
        info = "Length:"+str(length)+ "  "+ "Speed:" + str(speed)+ "     "+ "K1 = speed+3"+ "   "+ "K2 = speed+5"+ "   "+ "K3 = speed-8"+ "       "+ "RED = length+3"+ "   "+ "ORANGE = length+5"+ "   "+ "GREEN = length+30"+ "   "+ "PURPLE = length+1"
        font = pygame.font.SysFont('FixedSys',50,False, False)
        text_obj = font.render(info,True,WHITE)
        text_rect = text_obj.get_rect()
        text_rect.x,text_rect.y = 10,10
        screen.blit(text_obj,text_rect)

    def display_frame(self,screen):
        screen.fill(BLACK)
        self.draw_info(self.snake.length,self.speed,screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        self.feed1.draw(screen)
        self.feed2.draw(screen)
        self.feed3.draw(screen)
        screen.blit(screen,(0,0))
        
                


def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(game.speed)
    pygame.quit()
if __name__ == '__main__':
    main()
