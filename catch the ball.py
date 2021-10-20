from tkinter import *
from random import randrange as rnd, choice


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

global score
score = 0
Label = Label(root, bg='white', fg='black', width=40)
Label['text'] = 'score: ' + str(score)
Label.pack()
colors = ['green', 'red', 'yellow', 'blue', 'black']
balls = []  # хранит данные о всех когда-либо существовавших шариках

def new_ball():
    '''
    создает новый шарик, параметры шарика добавляются в массив balls
    '''
    x, y = rnd(100, 700), rnd(100, 500)
    r = rnd(30, 50)
    vx, vy = rnd(-5, 5), rnd(-5, 5)
    dead=False
    balls.append([x, y, r, choice(colors), vx, vy, dead])

def click(event):
    '''
    опредение щелчка мыши по шарику
    '''
    global score
    for ball in balls:
        x, y = ball[0], ball[1]
        r = ball[2]
        color = ball[3]
        dead = ball[6]
        if dead == False and ((x - event.x)**2 + (y - event.y)**2 <= r**2):
            if color == 'black':
                score = 0
                Label['text'] = 'score: 0'
            else:
                score += 1
                Label['text'] = 'score: ' + str(score)
            ball[6] = True

def moving():
    '''
    рисует все шарики, меняя координаты
    '''
    global balls
    canv.delete(ALL)
    for ball in balls:
        if ball[6] == False:
            dx, dy = ball[4], ball[5]
            ball[0] += dx
            ball[1] += dy
            x, y = ball[0], ball[1]
            r = ball[2]
            if y - r <= 5 or y + r >= 575:
                ball[5] = -dy
            if x - r <= 5 or x + r >= 795:
                ball[4] = -dx
            color = ball[3]
            canv.create_oval(x-r, y-r, x+r, y+r, fill=color, width=0)

def main():
    if rnd(0, 15) == 1:
        new_ball()
    moving()
    root.after(50, main)

main()
canv.bind('<Button-1>', click)
root.mainloop()