#-*-coding:utf-8-*-
import sys
import pygame
import os
import random
from pygame.locals import *
 
background=0,0,0
 
 
size=width,height=320,500
screen=pygame.display.set_mode(size)
pygame.display.set_caption('fly')
 
 
 
def load_image(name,colorkey=None):
    fullname=os.path.join ('data',name)
    try:
 
        image=pygame.image.load(fullname)
    except pygame.error,message:
        print 'cannot load image:',name
        raise SystemExit,message
    image=image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey=image.get_at(0,0)
        image.set_colorkey(colorkey,RLEACCEL)
    return image,image.get_rect()
 
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect=load_image('bullet.png')
        self.rect.midtop=player.rect.midtop
        self.speed=5
    def update(self):
        self.rect.top-=self.speed
         
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect=load_image('player.png')
        self.rect.midtop=(width/2,height-30)
        self.move={K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0,K_SPACE:0}
        self.allbullets=pygame.sprite.Group()
         
    def update(self):
        
        for event in pygame.event.get():
             
            if event.type==KEYDOWN:
                if event.key in self.move:
                    self.move[event.key]=3
            elif event.type==KEYUP:
                if event.key in self.move:
                    self.move[event.key]=0
        x=self.rect.midtop[0]   
        y=self.rect.midtop[1]
        if self.rect.left>0:
            x -= self.move[K_LEFT]
        if self.rect.right<width:
            x += self.move[K_RIGHT]
        if self.rect.top>0:
            y -= self.move[K_UP]
        if self.rect.bottom<height:
            y += self.move[K_DOWN]
        self.rect.midtop=(x,y)
 
    def shoot(self):
        bullet=Bullet()
        self.allbullets.add(bullet)
        for bullet in self.allbullets:
            if bullet.rect.top<0:
                self.allbullets.remove(bullet)
    
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect=load_image('enemy.png')
        self.rect.midtop=(random.randint(0,width),0)
        self.speed=1
         
         
    def update(self):
        self.rect.top+=self.speed
                        
pygame.init()
 
shoot_frequency=0
enemy_frequency=0
 
player=Player()
allenemys=pygame.sprite.Group()
allsprites=pygame.sprite.Group(player)
 
clock=pygame.time.Clock()
 
while True:
    clock.tick(60)
    screen.fill(background)
 
    if enemy_frequency%500==0:
        enemy=Enemy()
        allenemys.add(enemy)
        for enemy in allenemys:
            if enemy.rect.top>height:
                allenemys.remove(enemy)
    enemy_frequency+=1
    if enemy_frequency>500:
        enemy_frequency=0
     
    for event in pygame.event.get():
        if event.type==QUIT:
                pygame.quit()
                sys.exit()
        if event.type==KEYDOWN:
            if event.key in player.move:
                player.move[event.key]=1
        if event.type==KEYUP:
            if event.key in player.move:
                player.move[event.key]=0
    if player.move[K_SPACE]==1:
        if shoot_frequency%15==0:
            player.shoot()
    shoot_frequency+=1
    if shoot_frequency>15:
        shoot_ferquency=0
 
    for enemy in allenemys:
        for bullet in player.allbullets:
            if pygame.sprite.collide_rect(bullet,enemy):
                allenemys.remove(enemy)
                player.allbullets.remove(bullet)
 
    allenemys.update()
    player.update()
    player.allbullets.update()
    player.allbullets.draw(screen)
    allsprites.draw(screen)
    allenemys.draw(screen)   
 
    
    pygame.display.flip()
