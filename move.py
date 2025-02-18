import tkinter
from random import *
screen = tkinter.Canvas(bg="white", width=600, height=250)
screen.pack()

width=600

x_obj1=100
screen.create_rectangle(100,150,200,200,fill="blue",tags="obj1")
screen.create_oval(115,200,140,225,fill="yellow",tags="obj1")
screen.create_oval(160,200,185,225,fill="yellow",tags="obj1")
screen.move("x_obj1",-200,0)

x_obj2=200
screen.create_oval(200,100,230,130,fill="",width="5",outline="black",tags="obj2")
screen.create_oval(250,100,280,130,fill="",width="5",outline="black",tags="obj2")
screen.create_line(215,115,230,70,width=5,tags="obj2")
screen.create_line(225,90,240,115,265,115,265,115,270,85,width=5,tags="obj2")

def move():
    global x_obj1, x_obj2
    x_obj2=x_obj2-5
    screen.move("obj2",-5,0)
    if x_obj2<0:
        x_obj2=x_obj2+width
        screen.move("obj2",width,0)
    x_obj1=x_obj1+5
    screen.move("obj1",5,0)
    if x_obj1>width:
        x_obj1=x_obj1-width
        screen.move("obj1",-width,0)
    print(x_obj1)
    screen.after(100,move)

move()

screen.mainloop()