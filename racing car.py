import pygame
import os
import random
from time import sleep
import sys
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)
RED = (200,0,0)

CAR_COUNT = 3
LANE_COUNT = 5
SPEED = 10
FPS = 60

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

class Car():
    def __init__(self, x = 0,y = 0,dx = 0,dy = 0):
        self.x  = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
        car_images_path = assets_path('assets')
        image_file_list = os.listdir(car_images_path)
        self.image_path_list = [os.path.join(car_images_path,file)for file in image_file_list if file.endswith(".png")]
        
        crash_image_path = assets_path('assets/crash.png')
        crash_sound_path = assets_path('assets/crash.wav')
        collision_sound_path = assets_path('assets/collision.wav')
        engine_sound_path = assets_path('assets/engine.wav')
        self.crash_image = pygame.image.load(crash_image_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
        self.collision_sound = pygame.mixer.Sound(collision_sound_path)
        self.engine_sound = pygame.mixer.Sound(engine_sound_path)
        
    def load_image(self):
        choice_car_path= random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car_path)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        
    def load(self):
        self.load_image()
        self.x = (SCREEN_WIDTH//2)
        self.y = SCREEN_HEIGHT - self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()
        
    def load_random(self):
        self.load_image()
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.dx = 0
        self.dy = random.randint(4,9)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def out_of_screen(self):
        if self.x + self.width > SCREEN_WIDTH or self.x <0:
            self.x -= self.dx
        if self.y + self.height > SCREEN_HEIGHT or self.y <0:
            self.y -=self.dy
            
    def check_crash(self, car):
        if (self.x + self.width >car.x) and (self.x <car.x + car.width) and (self.y <car.y + car.height) and (self.y + self.height> car.y):
            return True
        
        else:
            return False
        
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
        
    def draw_crash(self,screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x +(self.width //2) - (width //2)
        draw_y = self.y + (self.height//2) - (height//2)
        screen.blit(self.crash_image, (draw_x, draw_y))
        pygame.display.update()
        
class Lane():
    def __init__(self):
        self.color = WHITE
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (SCREEN_WIDTH - (self.width * LANE_COUNT)) / (LANE_COUNT - 1)
        self.count = 10
        self.x = 0
        self.y = -self.height
        
    def move(self,speed,screen):
        self.y += speed
        if self.y >0:
            self.y = -self.height
        self.draw(screen)
        
    def draw(self, screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.width, self.height))
            next_lane += self.height + self.gap
            
class Game():
    def __init(self):
        
        menu_image_path = assets_path('assets/menu_car.png')
        self.image_intro = pygame.image.load(menu_image_path)
        pygame.mixer.music.load(assets_path('asseets/race.wav'))
        font_path = assets_path('assets/NanumGothicCoding-Bold.ttf')
        self.font_40 = pygame.font.Font(font_path , 40)
        self.font_30 = pygame.font.Font(font_path, 30)
        
        
        self.lanes = []
        for i in range(LANE_COUNT):
            lane = Lane()
            lane.x = i * int(lane.space + lane.width)
            self.lanes.append(lane)
        self.cars = []
        for i in range(CAR_COUNT):
            car = Car()
            self.cars.append(car)
        self.player = Car()
        
        self.score = 0
        
        self.menu_on = True
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
        if self.menu_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                    self.score = 0
                    self.menu_on = False
                    
                    self.player.load()
                    for car in self.cars:
                        car.load_random()
                    sleep(4)
                    
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.dy -= -5
                elif event.key == pygame.K_DOWN:
                    self.player.dy += 5
                elif event.key == pygame.K_LEFT:
                    self.player.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx +=5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.dy = 0
                    
        return False
    def run_logic(self,screen):
        for car in self.cars:
            if car.y > SCREEN_HEIGHT:
                self.score +=10
                car.load_random()
                
            if self.player.check_crash(car):
                self.menu_on = True
                pygame.mixer.music.stop()
                self.player.crash_sound.play()
                self.player.draw_crash(screen)
                car.draw_crash(screen)
                sleep(1)
                pygame.mouse.set_visible(True)
            for com in self.cars:
                if car ==com:
                    pass
                elif car.check_crash(com):
                    self.score +=10
                    car.collision_sound.play()
                    car.draw_crash(screen)
                    car.load_random()
                    com.draw_crash(screen)
                    com.load_random()
                    
    def draw_text(self, screen, text,font,x,y, main_color):
        text_obj = font.render(text,True,main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x,y
        screen.blit(text_obj, text_rect)
    def display_menu(self, screen):
        screen.fill(GRAY)
        screen.blit(self.image_intro, [40,150])
        draw_x = (SCREEN_WIDTH//2)
        draw_y = (SCREEN_HEIGHT//2)
        self.draw_text(screen, "레이싱 게임!!", self.font_40, draw_x , draw_y +50, BLACK)
        self.draw_text(screen, "Score" + str(self.score), self.font_40, draw_x, draw_y +150 , WHITE)
        self.draw_text(screen, "스페이스바를 누르세여", self.font_30, draw_x, draw_y +200, RED)
        
    def display_frame(self, screen):
        screen.fill(GRAY)
        
        for lane in self.lanes:
            lane.move(SPEED, screen)
        self.player.draw(screen)
        self.player.move()
        self.player.out_of_screen()
        
        for car in self.cars:
            car.draw(screen)
            car.move()
            
        self.draw_text(screen, "Score: " + str(self.score), self.font_30,80,20,BLACK)
        
    def assets_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('레이싱 게임!!')
    clock = pygame.time.Clock()
    game = Game()

    running  = True
     
    while running:
        running = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)
        

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

main()

    
        
                    
        
            
        
    
        
        
        
        
        

    