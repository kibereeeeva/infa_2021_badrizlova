import pygame
from pygame.draw import *

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((600, 400))
    background(screen)
    umbrella(screen, 30, 230, 1)
    umbrella(screen, 180, 275, 0.6)
    cloud(screen, 110, 35, 1)
    cloud(screen, 230, 10, 2)
    cloud(screen, 50, 100, 1.5)
    boat(screen, 320, 110, 1)
    boat(screen, 170, 150, 0.5)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

def background(dest):
    '''
    рисует задний фон
    :param dest: поверхность ,на которой будет нарисован фон
    :return:
    '''
    rect(dest, 'lightblue', (0, 0, 600, 180))
    rect(dest, 'blue', (0, 180, 600, 100))
    rect(dest, 'yellow', (0, 280, 600, 120))
    circle(dest, 'yellow', (540, 60), 40)
    beach(dest)

def beach(dest):
    '''
    рисует волны на берегу
    :param dest: поверхость ,на которой будет нарисованы волны
    :return:
    '''
    for i in range(1,10):
        ellipse(dest, 'yellow', (50*(2*i-2), 272, 50, 20))
        ellipse(dest, 'blue', (50*(2*i-1), 268, 50, 20))

def umbrella(dest, x, y, scale):
    '''
    рисует зонт
    :param dest: поверность, на которой будет нарисован зонтик
    :param x, y: координаты зонтика
    :param scale: масштаб
    :return:
    '''
    rect(dest, 'orange', (x+65*scale, y+0*scale, 5*scale, 150*scale))
    polygon(dest, 'red', [(x+0*scale, y+30*scale), (x+65*scale, y+0*scale), (x+70*scale, y+0*scale), (x+135*scale, y+30*scale), (x+0*scale, y+30*scale)])
    line(dest, 'darkred', (x+65*scale, y+0*scale), (x+15*scale, y+30*scale), 1)
    line(dest, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 15 * scale, y + 30 * scale), 1)
    line(dest, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 35 * scale, y + 30 * scale), 1)
    line(dest, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 55 * scale, y + 30 * scale), 1)
    line(dest, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 80 * scale, y + 30 * scale), 1)
    line(dest, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 100 * scale, y + 30 * scale), 1)
    line(dest, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 120 * scale, y + 30 * scale), 1)

def cloud(dest, x, y, scale):
    '''
    рисует облако
    :param dest: поверность, на которой будет нарисовано облако
    :param x, y: координаты облака
    :param scale: масштаб
    :return:
    '''
    circle(dest, 'white', (x + 25 * scale, y + 15 * scale), 15 * scale)
    circle(dest, 'grey', (x + 25 * scale, y + 15 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 45 * scale, y + 15 * scale), 15 * scale)
    circle(dest, 'grey', (x + 45 * scale, y + 15 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 15 * scale, y + 25 * scale), 15 * scale)
    circle(dest, 'grey', (x + 15 * scale, y + 25 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 33 * scale, y + 27 * scale), 15 * scale)
    circle(dest, 'grey', (x + 33 * scale, y + 27 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 54 * scale, y + 27 * scale), 15 * scale)
    circle(dest, 'grey', (x + 54 * scale, y + 27 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 65 * scale, y + 15 * scale), 15 * scale)
    circle(dest, 'grey', (x + 65 * scale, y + 15 * scale), 15 * scale, 1)
    circle(dest, 'white', (x + 70 * scale, y + 27 * scale), 15 * scale)
    circle(dest, 'grey', (x + 70 * scale, y + 27 * scale), 15 * scale, 1)

def boat(dest, x, y, scale):
    '''
    рисует лодку
    :param dest: поверность, на которой будет нарисован лодка
    :param x, y: координаты лодки
    :param scale: масштаб
    :return:
    '''
    brown=(186, 80, 5)
    grey='darkgrey'
    rect(dest, 'black', (x+84*scale, y+0*scale, 5*scale, 101*scale))
    polygon(dest, (222, 213, 153), [(x+90*scale, y+0*scale), (x+145*scale, y+50*scale), (x+90*scale, y+95*scale), (x+107*scale, y+50*scale), (x+90*scale, y+0*scale)])
    line(dest, grey, (x + 90 * scale, y + 0 * scale), (x + 145 * scale, y + 50 * scale), 1)
    line(dest, grey, (x + 90 * scale, y + 0 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(dest, grey, (x + 145 * scale, y + 50 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(dest, grey, (x + 90 * scale, y + 95 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(dest, grey, (x + 90 * scale, y + 95 * scale), (x + 145 * scale, y + 50 * scale), 1)
    circle(dest, brown, (x+30*scale, y+95*scale), 30*scale, draw_bottom_left=True)
    rect(dest, brown, (x + 30 * scale, y + 95 * scale, 145 * scale, 30 * scale))
    polygon(dest, brown, [(x+175*scale, y+95*scale), (x+240*scale, y+95*scale), (x+175*scale, y+124*scale), (x+175*scale, y+95*scale)])
    circle(dest, 'black', (x+190*scale, y+106*scale), 6*scale)
    circle(dest, 'white', (x+190*scale, y+106*scale), 4*scale)

main()