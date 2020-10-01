def circleosnov(x,y,r): #Основной круг, лицо
    circle(screen,(0,255,0),(x,y),r)

def circleLEFT(x,y,r):#Левый глаз
    circle(screen,(255,255,0),(x-30,y-30),r//4)

def circleRIGHT(x,y,r):#Правый глаз
    circle(screen,(255,255,0),(x+30,y-30),r//6)

def circleLEFTOKO(x,y,r):#Левое око
    circle(screen,(0,0,0),(x-30,y-30),r//8)

def circleRIGHTOKO(x,y,r):#Правое око
    circle(screen,(0,0,0),(x+30,y-30),r//12)

def rot(x,y,r):#Рот
    polygon(screen,(0,0,0),[(x-r//3,y+r//5),(x+r//3,y+r//5),(x+r//3,y+r//5+r//7),(x-r//3,y+r//5+r//7)])

def brovLEFT(x,y,r):#Левая бровь
    line(screen, (0,128,0), (x-30+round(mn.sqrt(2)*r//4)-40,y-70), (x-30+round(mn.sqrt(2)*r//4),y-30), 3)


def brovRIGHT(x,y,r):#Правая бровь
    line(screen, (0,128,0), (x+30-r//3+round(40//(mn.sqrt(3)/3)),y-70), (x+30-r//3,y-30), 5)

import pygame
import math as mn
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
#Рисуем лицо,рот, левый глаз, правый глаз, левое око, правое око,левую бровь, правую бровь
x=int(input())
y=int(input())
r=int(input())
circleosnov(x,y,r)
rot(x,y,r)
circleLEFT(x,y,r)
circleRIGHT(x,y,r)
circleLEFTOKO(x,y,r)
circleRIGHTOKO(x,y,r)
brovLEFT(x,y,r)
brovRIGHT(x,y,r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

