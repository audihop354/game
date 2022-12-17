from turtle import width
import pygame
from pygame.locals import *
import math
import random
import time

pygame.init()

#set color
green = (76,208,56)
gray = (100,100,100)
red = (200,0,0)
yellow = (255,232,0)
white = (255,255,255)

#set screen
WIDTH=1000
HEIGHT=600  
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)

#set caption and icon and image
pygame.display.set_caption("Game cua Khoi")
icon = pygame.image.load('img/car.png')
pygame.display.set_icon(icon)
arrow = pygame.image.load('img/arrow.png')


#Background
class BACKGROUND:
    def __init__(self,img, start,end) :
        self.img=img
        self.start=start
        self.end=end
        self.car=[]

bg=[] 
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg1.png'),(WIDTH,HEIGHT)),200,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg2.png'),(WIDTH,HEIGHT)),0,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg3.png'),(WIDTH,HEIGHT)),0,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg4.png'),(WIDTH,HEIGHT)),0,800))

#Car
class CAR:
    def __init__(self, img, car_y ,velocity,curRound):
        self.img = pygame.transform.scale(img,(WIDTH/12.5,HEIGHT/12))
        self.x = 0
        self.y = car_y
        self.velocity = velocity
        self.destination = 0
        self.curRound=curRound

        # self.ratio=ratio
    def run(self):
        self.x += self.velocity
    
car=[]
des = int(WIDTH/1.25)
car.append(CAR(pygame.image.load('img/0_red_formulaOne.png'), int(HEIGHT/1.65), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_yellow_formulaOne.png'), int(HEIGHT/1.47), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_blue_formulaOne.png'), int(HEIGHT/1.32), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_pink_formulaOne.png'), int(HEIGHT/1.19), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_white_formulaOne.png'), int(HEIGHT/1.1),random.uniform(2,3), 0))


#setting run
def draw(player_car,x,y):
    screen.blit(player_car,(x, y))
    
#game Loop
clock = pygame.time.Clock()
fps = 60

#Initalize
r=0
selected=0
pressed=0
for i in range (5):
    bg[r].car.append(i)
    car[i].x=bg[r].start
    car[i].curRound=r

running=True
while running:

    clock.tick(fps)     
    screen.blit(bg[car[selected].curRound].img,(0,0))
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print (event.key)
            pressed=1
            if event.key==pygame.K_F1:
                selected=0
            if event.key==pygame.K_F2:
                selected=1
            if event.key==pygame.K_F3:
                selected=2
            if event.key==pygame.K_F4:
                selected=3
            if event.key==pygame.K_F5:
                selected=4
        if event.type == pygame.KEYUP:
            pressed=0

    #draw 5 car
    for i in bg[car[selected].curRound].car:
        draw(car[i].img,car[i].x,car[i].y)

    if pressed ==1:
        for i in bg[car[selected].curRound].car:
            if i==selected :
                draw(arrow,car[i].x+10,car[i].y-45)
    #check if the car have finish the race
    for i in range (5):
        if car[i].x<=bg[car[i].curRound].end:
            car[i].run()
        elif car[i].curRound<3: 
            bg[car[i].curRound].car.remove(i)
            car[i].curRound+=1
            bg[car[i].curRound].car.append(i)
            car[i].x=bg[car[i].curRound].start-100

    
        #resize display
        # if event.type == VIDEORESIZE:
            
        #     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        #     background = pygame.transform.scale(background,(event.w,event.h))

    pygame.display.update()
pygame.quit()