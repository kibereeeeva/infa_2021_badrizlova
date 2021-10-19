import pygame
from pygame.draw import *

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((600, 400))
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    
    for i in range(0, 500):
        animation(i, screen)
        pygame.display.update()
        clock.tick(FPS)

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

def animation(i, screen):
    '''
    рисует картинку в зависимости от момента времени i
    :param i: момент времени
    :param screen: поверхность, на которой эта картинка отображается
    :return: 
    '''
    background(screen, i)
    umbrella(screen, 30, 230, 1)
    umbrella(screen, 180, 275, 0.6)
    cloud(screen, 110+i, 35, 1)
    cloud(screen, 230+2*i, 10, 2)
    cloud(screen, 50+1.5*i, 100, 1.5)
    boat(screen, 320+2.5*i, 110, 1)
    boat(screen, 170+1.25*i, 150, 0.5)

def background(screen, i):
    '''
    рисует задний фон
    :param screen: поверхность ,на которой будет нарисован фон
    :return:
    '''
    sky_red, sky_green, sky_blue = min(250, 125+i), max(0, 255-i), max(0, 255-i)
    rect(screen, (sky_red, sky_green, sky_blue), (0, 0, 600, 180))
    circle(screen, 'yellow', (540, 60+i), 40)
    rect(screen, 'blue', (0, 180, 600, 100))
    rect(screen, 'yellow', (0, 280, 600, 120))
    beach(screen)

def beach(screen):
    '''
    рисует волны на берегу
    :param screen: поверхость ,на которой будет нарисованы волны
    :return:
    '''
    for i in range(1,10):
        ellipse(screen, 'yellow', (50*(2*i-2), 272, 50, 20))
        ellipse(screen, 'blue', (50*(2*i-1), 268, 50, 20))

def umbrella(screen, x, y, scale):
    '''
    рисует зонт
    :param screen: поверность, на которой будет нарисован зонтик
    :param x, y: координаты зонтика
    :param scale: масштаб
    :return:
    '''
    rect(screen, 'orange', (x+65*scale, y+0*scale, 5*scale, 150*scale))
    polygon(screen, 'red', [(x+0*scale, y+30*scale), (x+65*scale, y+0*scale), (x+70*scale, y+0*scale), (x+135*scale, y+30*scale), (x+0*scale, y+30*scale)])
    line(screen, 'darkred', (x+65*scale, y+0*scale), (x+15*scale, y+30*scale), 1)
    line(screen, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 15 * scale, y + 30 * scale), 1)
    line(screen, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 35 * scale, y + 30 * scale), 1)
    line(screen, 'darkred', (x + 65 * scale, y + 0 * scale), (x + 55 * scale, y + 30 * scale), 1)
    line(screen, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 80 * scale, y + 30 * scale), 1)
    line(screen, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 100 * scale, y + 30 * scale), 1)
    line(screen, 'darkred', (x + 70 * scale, y + 0 * scale), (x + 120 * scale, y + 30 * scale), 1)

def cloud(screen, x, y, scale):
    '''
    рисует облако
    :param screen: поверность, на которой будет нарисовано облако
    :param x, y: координаты облака
    :param scale: масштаб
    :return:
    '''
    circle(screen, 'white', (x + 25 * scale, y + 15 * scale), 15 * scale)
    circle(screen, 'grey', (x + 25 * scale, y + 15 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 45 * scale, y + 15 * scale), 15 * scale)
    circle(screen, 'grey', (x + 45 * scale, y + 15 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 15 * scale, y + 25 * scale), 15 * scale)
    circle(screen, 'grey', (x + 15 * scale, y + 25 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 33 * scale, y + 27 * scale), 15 * scale)
    circle(screen, 'grey', (x + 33 * scale, y + 27 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 54 * scale, y + 27 * scale), 15 * scale)
    circle(screen, 'grey', (x + 54 * scale, y + 27 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 65 * scale, y + 15 * scale), 15 * scale)
    circle(screen, 'grey', (x + 65 * scale, y + 15 * scale), 15 * scale, 1)
    circle(screen, 'white', (x + 70 * scale, y + 27 * scale), 15 * scale)
    circle(screen, 'grey', (x + 70 * scale, y + 27 * scale), 15 * scale, 1)

def boat(screen, x, y, scale):
    '''
    рисует лодку
    :param screen: поверность, на которой будет нарисован лодка
    :param x, y: координаты лодки
    :param scale: масштаб
    :return:
    '''
    brown=(186, 80, 5)
    grey='darkgrey'
    rect(screen, 'black', (x+84*scale, y+0*scale, 5*scale, 101*scale))
    polygon(screen, (222, 213, 153), [(x+90*scale, y+0*scale), (x+145*scale, y+50*scale), (x+90*scale, y+95*scale), (x+107*scale, y+50*scale), (x+90*scale, y+0*scale)])
    line(screen, grey, (x + 90 * scale, y + 0 * scale), (x + 145 * scale, y + 50 * scale), 1)
    line(screen, grey, (x + 90 * scale, y + 0 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(screen, grey, (x + 145 * scale, y + 50 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(screen, grey, (x + 90 * scale, y + 95 * scale), (x + 107 * scale, y + 50 * scale), 1)
    line(screen, grey, (x + 90 * scale, y + 95 * scale), (x + 145 * scale, y + 50 * scale), 1)
    circle(screen, brown, (x+30*scale, y+95*scale), 30*scale, draw_bottom_left=True)
    rect(screen, brown, (x + 30 * scale, y + 95 * scale, 146 * scale, 30 * scale))
    polygon(screen, brown, [(x+175*scale, y+95*scale), (x+240*scale, y+95*scale), (x+175*scale, y+124*scale), (x+175*scale, y+95*scale)])
    circle(screen, 'black', (x+190*scale, y+106*scale), 6*scale)
    circle(screen, 'white', (x+190*scale, y+106*scale), 4*scale)

main()