import tkinter
from random import *
canvas = tkinter.Canvas(width=800, height=800, bg='white')
canvas.pack()


def timer1():
    canvas.delete('all')
    global sx, sy, typ, velkost
    sx=randrange(600)
    sy=randint(20, 600)
    typ = randint(0,1)
    if typ ==1:
        farba= 'green'
        canvas.create_rectangle(sx-velkost, sy-velkost, sx+velkost, sy+velkost, fill=farba)
    else:
        farba ='red'
        canvas.create_rectangle(sx-50, sy-50, sx+50, sy+50, fill=farba)
    canvas.create_text(100,10,text="Pocet ziskanych bodov:")
    canvas.create_text(200,10,text=pocet_bodov)
    if -10 < pocet_bodov < 10:
        canvas.after(800, timer1)
    if pocet_bodov >= 10:
        canvas.create_text(400,400,font='Arial 60 bold', text = 'VYBORNE')
    if pocet_bodov <= -10:
        canvas.create_text(400, 400,font='Arial 60 bold', text='Pomale reakcie')
    if pocet_bodov == 1:
        velkost=40
    if pocet_bodov == 2:
        velkost=30
    if pocet_bodov == 3:
        velkost=20
    if pocet_bodov == 4:
        velkost=10
    if pocet_bodov == 5:
        velkost=5
    if pocet_bodov >= 6:
        velkost=2,5


def klik(suradnice):
    global pocet_bodov
    x=suradnice.x
    y=suradnice.y
    if typ ==0:
        zmena = -2
    else:
        zmena = 1
    if sx-velkost <x<sx+velkost and sy-velkost <y<sy+velkost:
        pocet_bodov=pocet_bodov+zmena
    else:
        pocet_bodov=pocet_bodov-1


pocet_bodov=0
typ = 0
sx=0
sy=0
velkost=50
timer1()

canvas.bind('<Button-1>', klik)


canvas.mainloop()