import pygame
import re

from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

FPS = 60

'''Счётчик для шаров(BALL_RATE) и квадратов(SQUARE_RATE) по времени'''
BALL_RATE = FPS*120
SQUARE_RATE = FPS*320

'''Параметры экрана: ширина(X_LENGTH), высота(Y_WIDTH)'''
X_LENGTH = 600
Y_WIDTH = 600

FONT_SIZE = 32 # Размер шрифта надписи на экране

'''определяю цвета'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE ,YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''
    Ожидается, что шары будут двигаться по прямым
    Случайно определяю параметры шара и возвращаю их в качестве кортежа:
    x, y - координата центра
    dx, dy - смещение вдоль осей центра
    r - радиус
    color - случайный цвет из набора COLORS
    '''
    x = randint(100, X_LENGTH - 100)
    y = randint(100, Y_WIDTH - 100)
    dx = randint(-5, 5)
    dy = randint(-5, 5)
    r = randint(20, 40)
    color = COLORS[randint(0, 5)]
    return (x, y, dx, dy, r, color)


def move_ball(tuple):
    '''
    Рисую шары, перемещаю их и возвращаю их новое положение и смещение через (вспомогательный)кортеж new_tuple:
    цвет и радиус остаются неизменными
    На вход ожидает тот самый кортеж tuple из старых параметров
    Создаём кортеж(new_tuple_ball) из кортежей координат центра, смещений, радиуса и цвета: x, y, dx, dy, r, color
    '''   
    x, y, dx, dy, r, color = tuple
    circle(screen, color, (x, y), r)
    if (x - r <= 0) or (x + r >= X_LENGTH):
        dx = -dx
    if (y - r <= 0) or (y + r >= Y_WIDTH):
        dy = -dy
    new_tuple_ball = x + dx, y + dy, dx, dy, r, color # фиксирую новые параметры шарика
    return new_tuple_ball


def check_ball(new_tuple_ball, event):
    '''
    Проверяю попал ли кликом мышки по шару, возвращая параметры True or False
    на вход функция ожидает параметры шарика через new_tuple_ball и клик мышки
    '''
    event.x, event.y = event.pos
    x, y, dx, dy, r, color = new_tuple_ball
    if (x - event.x)**2 + (y - event.y)**2 <= r**2:
        check = True
    else:
        check = False
    return check


def new_square():
    '''
    Ожидается, что квадраты будут двигаться по параболам
    Создаю случайные параметры квадрата:
    x, y - координаты центра
    dx, dy - смещение вдоль осей центра
    ay - вертикальное ускорение(положительное)
    r - длина стороны квадрата
    color - случайный цвет из набора COLORS
    '''
    x = randint(100, X_LENGTH - 100)
    y = randint(100, Y_WIDTH - 100)
    dx = randint(-5, 5)
    dy = randint(-5, 5)
    ay = randint(1,8)/10
    r = randint(50, 70)
    color = COLORS[randint(0, 5)]
    return (x, y, dx, dy, ay, r, color)

def move_square(tuple):
    '''
    Рисую квадраты, перемещаю их и возвращаю их новое положение и смещение через кортеж new_tuple
    на вход ожидается кортеж из старых параметров
    '''   
    x, y, dx, dy, ay, r, color = tuple
    rect(screen, color, (x, y, r, r))
    dy = dy + ay
    if (x <= 0) or (x + r >= X_LENGTH):
        dx = -dx
    if (y <= 0) or (y + r >= Y_WIDTH):
        dy = -dy
    new_tuple_square = x + dx, y + dy, dx, dy, ay, r, color # новый кортеж
    return new_tuple_square


def check_square(new_tuple_square, event):
    '''
    Проверяю попал ли кликом мышки по квадрату, возвращая параметры True or False
    на вход функция ожидает параметры шарика через new_tuple_square и клик мышки
    '''
    event.x, event.y = event.pos
    x, y, dx, dy, ay, r, color = new_tuple_square
    if (0 < (event.x - x) < r) and (0 < (event.y - y) < r):
        check = True
    else:
        check = False
    return check


def sort(stroka):
'''
Функция ожидает массив из строк, береёт каждую строку, находит её численную часть и сортирует "пузырьком"
'''
    for i in range(len(stroka) - 1):
        si = stroka[i]
        s2 = (re.sub(r'\D', '', si)) # выделяет численную часть строки
        s2_1=int(s2)
                 
        for j in range (len(stroka) - i):
            sj = stroka[j]
            s1=(re.sub(r'\D', '', sj))
            s1_1=int(s1)
            if (s2_1 > s1_1) :
                stroka[i],stroka[j] = stroka[j],stroka[i] 
        

'''
ввожу имя игрока
открываю файл и заполняю две колоны таблицы 'Игрок' и 'Счёт' 
'''

name=input()

screen = pygame.display.set_mode((X_LENGTH, Y_WIDTH))
pygame.display.update()

finished = False

'''создаю массив функций шаров с их параметрами, тоесть создаю массив из кортежей параметров каждого шара(balls_list) и квадрата(squares_list)'''
balls_list = [] 
squares_list = []
score_list=[]
massiv=[]
k=0

score = 0 # счёт(количество очков)
time_counter = 0 # счётчик времени

while not finished:
    pygame.time.Clock().tick(FPS)
    time_counter += FPS # увеличиваю каждый раз счётчик времени
    screen.fill(BLACK)

    '''
    Если счётчик времени кратен счётчику шара(квадрата), то добавляем новый шар(квадрат) через функцию
    Тоесть каждый промежуток времени BALL_RATE(SQUARE_RATE) будет появляться шар(квадрат)
    '''
    if time_counter % BALL_RATE == 0:
        balls_list.append(new_ball())
    if time_counter % SQUARE_RATE == 0:
        squares_list.append(new_square())
        
    '''
    Двигаем каждый из шаров и квадратов:
    идём по массиву кортежей, выбираем каждый кортеж соответсвующего шара и с ним уже работаем
    '''
    for i in range(len(balls_list)):
        balls_list[i] = move_ball(balls_list[i])
    for i in range(len(squares_list)):
        squares_list[i] = move_square(squares_list[i])
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            for i in range(len(balls_list)):
                '''
                Проверяем попал ли наш клик в шарик, если да, то:
                увеличиваем счётчик на 1 и удаляем наш шарик из списка шариков
                Тот же механизм и с квадратами, только счётчик увеличивается на 5, так как квадраты более ценные чем шарики
                '''
                if check_ball(balls_list[i], event):
                    score += 1
                    balls_list.pop(i)
                    break
            for i in range(len(squares_list)):
                if check_square(squares_list[i], event):
                    score += 5
                    squares_list.pop(i)
                    break
                
    '''Добавляю количество очков за мишени на главную панель'''
    screen.blit(pygame.font.Font(None, FONT_SIZE).render(str(score), 1, WHITE), 
        (X_LENGTH/2 - FONT_SIZE/2, 0)) # FONT_SIZE это размер шрифта
    
    '''Добавляю надпись о начале игры на главную панель'''
    if time_counter < 100*FPS: # if нужен, чтобы надпись держалась некоторое время
        screen.blit(pygame.font.Font(None, FONT_SIZE).render('Catch the ball (and the square)!', 1, WHITE),
            (X_LENGTH/2 - FONT_SIZE*5, FONT_SIZE)) # FONT_SIZE это размер шрифта
    
    pygame.display.update()
    




'''Заполняю файл именами игроков и их результатом(количеством очков) '''
balls = open('bools_prob.txt', 'a')
s=name+"    " + str(score) # name - имя игрока, которые мы вводим
balls.write(s+'\n')
balls.close()

'''Читаю запоненный файл и записываю строки файла в массив stroka'''
balls = open('bools_prob.txt','r')
stroka=balls.readlines()
balls.close

'''Сортирую таблицу по убыванию'''
sort(stroka,k) 

'''Вывожу в конечный файл итоговую таблицу '''
balls = open('bools.txt','w')
for i in range(len(stroka)):
    balls.write(stroka[i]+'\n')
balls.close()


pygame.quit()
pygame.font.quit()
