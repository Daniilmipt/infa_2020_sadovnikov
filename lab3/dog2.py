import pygame
import math as mt
from pygame.draw import *

black=(0,0,0) # чёрный
color_pover=(0,255,251) # цвет поверхности для всех surf
color_pool=(0,255,0) # цвет травы
color_zabor=(207,41,0) # цвет забора
color_sky=(86,109,255) # цвет неба
grey=(105,105,105) # серый (цвет круглой штуки в цепи
color_dog=(139,69,19) # цвет собак
color_zep=(47,79,79) # цвет цепи
color_conura=(141,0,26) # цвет конуры
white=(255,255,255) # белый

def vivod(surf1): # функция вывода поверхности на экран
    screen.blit(surf1,(0,0)) # беру левый верхний угол
    
    
def prozr(surf1): # делаю прозрачным всё кроме нужной фигуры
    surf1.fill((0,255,251)) #закрышиваю поверхность одним цветом
    surf1.set_colorkey(color_pover) #делаю прозрачным все "пиксели" этого цвета
    

def sky(i): # рисую небо 800-ширина i=120
    polygon(screen, color_sky,[(0,0),(800,0),(800,i),(0,i)]) # x-ширина i-высота неба
    

def zabor(i,h,n): # i=120-координата по y у верхнего края забора 800-ширина забора h=240-высота забора n=10-количество прямоугольников в заборе
    polygon(surf3,(207,41,0),[(0,i),(800,i),(800,h+i),(0,i+h)]) # закрашиваю весь забор
    line(surf3,black,(0,i+h),(800,i+h)) #нижняя линия забора
    line(surf3,black,(800,i),(800,i+h)) # правая сторона забора
    line(surf3,black,(0,i),(800,i)) # верхняя сторона забора
    line(surf3,black,(800,i+h),(0,i+h)) # нижняя сторона забора
    for i1 in range(n):  # 10-число вертикальных прямых
        line(surf3,black,(i1*800//n,i),(i1*800//n,i+h)) # сами линии забора
    surf4.blit(pygame.transform.scale(surf3,(800//2,800-200)),(800-300,i-170)) # правое отражение забора
    surf5.blit(pygame.transform.scale(surf3,(800//2,800-300)),(20,i-190)) # левое отражение забора


def poll(y,h): # пол или трава по y: y=120 h=240
    polygon(screen,color_pool,[(0,y+h),(800,y+h),(800,780),(0,780)]) # трава



def conura(i,j): # конура по х:i=480  по у:j=540 (i,j)-координата левого верхнего угла переднего вида конуры
    polygon(screen,color_conura,[(i,j),(i,j-100),(i+80,j-70),(i+80,j+35)]) # передний вид
    polygon(screen,color_conura,[(i+80,j-70),(i+95,j-95),(i+95,j-4),(i+80,j+35)]) # боковой вид
    polygon(screen,color_conura,[(i+95,j-95),(i+80,j-70),(i,j-100),(i+40,j-150),(i+70,j-160)]) # крыша
     # контур конуры
    polygon(screen,black,[(i+95,j-95),(i+80,j-70),(i,j-100),(i+40,j-150),(i+70,j-160),(i+95,j-95)],3)
    polygon(screen,black,[(i,j),(i,j-100),(i+80,j-70),(i+80,j+35)],3)
    polygon(screen,black,[(i+95,j-95),(i+95,j-4),(i+80,j+35),(i+80,j-70)],3) 
    line(screen,black,(i+40,j-150),(i+80,j-70),3)    
    circle(screen,black,(i+40,j-40),18) # проход в конуру(дырка)


def zep(i,j): # команды описывают кольца по порядку, первое это самое близкое к конуре кольцо i=497 j=508
              # (если мы хотим чтобы цепь выходила из дырки, то i=i+40 j=j-40, где i и j взяты из координат конуры)
    ellipse(screen,color_zep,[i,j,20,14],2) # первое кольцо
    ellipse(screen,color_zep,[i-6,j+5,18,23],2) # второе кольцо
    ellipse(screen,grey,[i-18,j+16,24,24]) # третье кольцо и т.д.
    ellipse(screen,color_zep,[i-18,j+16,24,24],2) # 4
    ellipse(screen,color_zep,[i-28,j+26,20,17],2) # 5
    ellipse(screen,color_zep,[i-43,j+27,24,13],2) # 6
    ellipse(screen,color_zep,[i-53,j+19,18,18],2) # 7
    ellipse(screen,color_zep,[i-56,j+9,12,20],2) # 8
    ellipse(screen,color_zep,[i-71,j+9,22,11],2) # 9
    ellipse(screen,color_zep,[i-77,j+10,14,14],2) # 10
    ellipse(screen,color_zep,[i-78,j+15,9,21],2) # 11


def dog(i,j): # координаты левой задней лапы: по х:i=270, по у:j=580
    ellipse(surf1,color_dog,[i,j,34,14]) # Левая задняя нога
    ellipse(surf1,color_dog,[i+60,j+50,34,14]) # правая задняя нога
    ellipse(surf1,color_dog,[i-60,j+66,34,14]) # правая передняя нога
    ellipse(surf1,color_dog,[i-120,j+40,34,14]) # левая передняя нога
    ellipse(surf1,color_dog,[i+84,j+5,15,50]) # правая задняя штука
    ellipse(surf1,color_dog,[i+24,j-45,15,50]) # левая задняя штука
    ellipse(surf1,color_dog,[i-50,j-29,40,100]) # правая передняя штука
    ellipse(surf1,color_dog,[i-110,j-55,40,100]) # левая передняя штука
    circle(surf1,color_dog,(i+70,j-10),30) # правый задний круг
    circle(surf1,color_dog,(i+18,j-60),30) # левый задний круг
    ellipse(surf1,color_dog,[i,j-80,90,60]) # туловище1
    ellipse(surf1,color_dog,[i-90,j-85,120,80]) # туловище2
    rect(surf1,color_dog,(i-90,j-120,85,85)) # лицо
    rect(surf1,black,(i-90,j-120,85,85),2) # лицо обводка
    circle(surf1,color_dog,(i-90,j-105),15) # левое ухо
    circle(surf1,black,(i-90,j-105),15,2) # контур левого уха
    circle(surf1,color_dog,(i-5,j-105),15) # правое ухо
    circle(surf1,black,(i-5,j-105),15,2) # контур правого уха
    ellipse(surf1,white,[i-73,j-88,23,12]) # левый глаз
    ellipse(surf1,black,[i-73,j-88,23,12],3) # контур левого глаза
    ellipse(surf1,white,[i-40,j-88,23,12]) # правый глаз
    ellipse(surf1,black,[i-40,j-88,23,12],3) # контур правого глаза
    circle(surf1,black,(i-62,j-82),6) # левый зрачок
    circle(surf1,black,(i-29,j-82),6) # правый зрачок
    arc(surf1,black,(i-65,j-60,39,24),mt.pi/100,mt.pi*99/100,3) # улыбка
    polygon(surf1,white,[(i-63,j-54),(i-59,j-58),(i-64,j-62)]) # левый зуб
    polygon(surf1,white,[(i-31,j-54),(i-36,j-58),(i-31,j-62)]) # правый зуб
    surf2.blit(pygame.transform.scale(pygame.transform.flip(surf1, True, False),(300,300)),(0,200)) # левая верхняя собака
    surf6.blit(pygame.transform.scale(surf1,(2200,2200)),(30,-760)) # правая нижняя собака
    surf7.blit(pygame.transform.scale(surf2,(300,300)),(600,200)) # правая верхняя маленькая собака


    
 # Начало основной прогаммы
pygame.init()
screen = pygame.display.set_mode((800, 780)) # определение размеров экрана


 # определение размеров поверхностей
surf1=pygame.Surface((800,780))
surf2=pygame.Surface((800,780))
surf3=pygame.Surface((800,780))
surf4=pygame.Surface((800,780))
surf5=pygame.Surface((800,780))
surf6=pygame.Surface((800,780))
surf7=pygame.Surface((800,780))


 # прозрачность поверхностей
prozr(surf1)
prozr(surf2)
prozr(surf3)
prozr(surf4)
prozr(surf5)
prozr(surf6)
prozr(surf7)


 # ввод значений isky=120, h=240, n=10, iconura=480, jconura=540, izep=497, jzep=508, idog=270, jdog=580
isky=int(input()) # координаты неба по оу
h=int(input()) # высота забора
n=int(input()) # количество палок забора
iconura=int(input()) # х координата конуры
jconura=int(input()) # у координата конуры
izep=int(input()) # х координата цепи
jzep=int(input()) # у координата цепи
idog=int(input()) # х координата левой задней лапы собаки
jdog=int(input()) # у координата левой задней лапы собаки


 # рисование
sky(isky) # небо
poll(isky,h) # пол
zabor(isky,h,n) # забор с его копиями
conura(iconura,jconura) # конура
zep(izep,jzep) # цепь, чтобы выходило из цетра конуры нужно взять izep=iconura+40, jzep=jconura-40
dog(idog,jdog) # собака с её копиями


 # вывод поверхностей на screen
vivod(surf5) # левое отражение забора
vivod(surf4) # правое отражение забора
vivod(surf3) # основной забор
vivod(surf1) # собака
vivod(surf2) # левая верхняя собака
vivod(surf6) # правая нижняя собака
vivod(surf7) # правая верхняя собака


clock = pygame.time.Clock()
finished = False
FPS=30
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()

pygame.quit()
