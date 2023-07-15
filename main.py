import os
import pygame
import random
import math
from os.path import isfile,join
from os import listdir

pygame.init()

pygame.display.set_caption('Platformer')

WIDTH, HEIGHT = 800,600
FPS=60
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))


#Flips the images for opposite direction movement

def flip(sprites):
    return [pygame.transform.flip(sprite,True,False) for sprite in sprites]


def load_sprites(dir1,dir2,width,height,direcion=False):
    path =  join('assets',dir1,dir2)
    images = [file for file in listdir(path) if isfile(join(path,file))] # Load images in list from the directory inside assets/dir1/dir2
    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path,image)).convert_alpha()
        sprites = []
        for i in range(sprite_sheet.get_width()//width):
            


    


def get_background(name):
    image = pygame.image.load(join('assets','Background',name))
    x, y, width, height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width+1):
        for j in range(HEIGHT // height+1):
            pos = (i*width, j*height)
            tiles.append(pos)
    
    return tiles, image

def draw(window,background,bg_image,player):
    for tile in background:
        window.blit(bg_image,tile)
    player.draw(window)
    pygame.display.update()
    
 
def handle_movement(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0 #* To move only when the key is pressed
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)
        
       
class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)
    GRAVITY = 1
    
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count  = 0
        
    def move(self,dx,dy):
        self.rect.x +=dx
        self.rect.y +=dy
        
    def move_left(self,vel):
        self.x_vel = -vel
        if self.direction !='left':
            self.direction = 'left'
            self.animation_count = 0
        
    def move_right(self,vel):
        self.x_vel = vel
        if self.direction !='right':
            self.direction = 'right'
            self.animation_count = 0
    
    def loop(self,fps):
        self.y_vel += min(1,(self.fall_count/fps)*self.GRAVITY)
        self.move(self.x_vel,self.y_vel)
        self.fall_count+=1
        
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,self.rect)
        

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background('Blue.png')
    player = Player(100,100,50,50)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_movement(player)
        draw(window,background,bg_image,player)
    pygame.quit()
    quit()    

if __name__ == '__main__':
    main(window)