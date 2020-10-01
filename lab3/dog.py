def rot_center(image, angle):
    center = image.get_ellipse().center
    rotated_image = transform.rotate(image, angle)
    new_ellipse = rotated_image.get_ellipse(center = center)

    return rotated_image, new_ellipse




def sky():
    polygon(screen,(86,109,255),[(0,0),(800,0),(800,120),(0,120)])

def zabor():
    polygon(screen,(207,41,0),[(0,120),(800,120),(800,360),(0,360)])
    for i in range(10):#10-число вертикальных прямых
        line(screen,(0,0,0),(i*80,120),(i*80,360))
    line(screen,(0,0,0),(0,360),(800,360))


def poll():
    polygon(screen,(0,255,0),[(0,360),(800,360),(800,780),(0,780)])#трава



def conura():
    polygon(screen,(141,0,26),[(480,540),(480,440),(560,470),(560,575)])#передний вид
    polygon(screen,(141,0,26),[(560,470),(575,445),(575,536),(560,575)])#боковой вид
    polygon(screen,(141,0,26),[(575,445),(560,470),(480,440),(520,390),(550,380)])#крыша
    #контур конуры
    polygon(screen,(0,0,0),[(575,445),(560,470),(480,440),(520,390),(550,380),(575,445)],3)
    polygon(screen,(0,0,0),[(480,540),(480,440),(560,470),(560,575)],3)
    polygon(screen,(0,0,0),[(575,445),(575,536),(560,575),(560,470)],3) 
    line(screen,(0,0,0),(520,390),(560,470),3)
    
    circle(screen,(0,0,0),(520,500),18)#проход в конуру

def zep():#команды описывают кольца по порядку, первое это самое близкое к конуре кольцо
    ellipse(screen,(47,79,79),[497,508,20,14],2)
    ellipse(screen,(47,79,79),[491,513,18,23],2)
    ellipse(screen,(105,105,105),[479,524,24,24])
    ellipse(screen,(47,79,79),[479,524,24,24],2)
    ellipse(screen,(47,79,79),[469,534,20,17],2)
    ellipse(screen,(47,79,79),[454,535,24,13],2)
    ellipse(screen,(47,79,79),[444,527,18,18],2)
    ellipse(screen,(47,79,79),[441,517,12,20],2)
    ellipse(screen,(47,79,79),[426,517,22,11],2)
    ellipse(screen,(47,79,79),[420,518,14,14],2)
    ellipse(screen,(47,79,79),[419,523,9,21],2)

def dog():
    ellipse(surf1,(139,69,19),[270,580,34,14])#Левая задняя нога
    ellipse(surf1,(139,69,19),[330,630,34,14])#правая задняя нога
    ellipse(surf1,(139,69,19),[210,646,34,14])#правая передняя нога
    ellipse(surf1,(139,69,19),[150,620,34,14])#левая передняя нога
    ellipse(surf1,(139,69,19),[354,585,15,50])#правая задняя штука
    ellipse(surf1,(139,69,19),[294,535,15,50])#левая задняя штука
    ellipse(surf1,(139,69,19),[220,551,40,100])#правая передняя штука
    ellipse(surf1,(139,69,19),[160,525,40,100])#левая передняя штука
    circle(surf1,(139,69,19),(340,570),30)#правый задний круг
    circle(surf1,(139,69,19),(288,520),30)#левый задний круг
    ellipse(surf1,(139,69,19),[270,500,90,60])#туловище1
    ellipse(surf1,(139,69,19),[180,495,120,80])#туловище2
    rect(surf1,(139,69,19),(180,460,85,85))#лицо
    rect(surf1,(0,0,0),(180,460,85,85),2)#лицо обводка
    circle(surf1,(139,69,19),(180,475),15)#левое ухо
    circle(surf1,(0,0,0),(180,475),15,2)#контур левого уха
    circle(surf1,(139,69,19),(265,475),15)#правое ухо
    circle(surf1,(0,0,0),(265,475),15,2)#контур правого уха
    ellipse(surf1,(255,255,255),[197,492,23,12])#левый глаз
    ellipse(surf1,(0,0,0),[197,492,23,12],3)#контур левого глаза
    ellipse(surf1,(255,255,255),[230,492,23,12])#правый глаз
    ellipse(surf1,(0,0,0),[230,492,23,12],3)#контур правого глаза
    circle(surf1,(0,0,0),(208,498),6)#левый зрачок
    circle(surf1,(0,0,0),(241,498),6)#правый зрачок
    arc(surf1,(0,0,0),(205,520,39,24),mt.pi/100,mt.pi*99/100,3)#улыбка
    polygon(surf1,(255,255,255),[(207,526),(211,522),(206,518)])#левый зуб
    polygon(surf1,(255,255,255),[(239,526),(234,522),(239,518)])#правый зуб
    
    



import pygame
import math as mt
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((800, 780))
surf1 = pygame.Surface((800,780))
surf2=pygame.Surface((800,780))
surf3=pygame.Surface((800,780))
surf4=pygame.Surface((800,780))
surf5=pygame.Surface((800,780))
surf6=pygame.Surface((800,780))

surf1.fill((255,255,255))
surf1.set_colorkey((255,255,255))


FPS = 30
zabor()
sky()
poll()
conura()
zep()
dog()

clock = pygame.time.Clock()
finished = False
screen.blit(surf1,(0,0))
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()

pygame.quit()
