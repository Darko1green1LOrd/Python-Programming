# zakladne nastavenie okna
import turtle
import tkinter as tk
from tkinter import *

def ifanythingclosed():
   exit()

maze = Tk()
maze.protocol("WM_DELETE_WINDOW", ifanythingclosed)
maze.title('Von z bludiska')
maze.geometry("1390x1080+10+10")

background_pic = PhotoImage(file = "map.png")
background_label = Label(maze, image=background_pic)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack(side=TOP, anchor=NW)

maze_gui = tk.Canvas(maze)


# vytvorenie korytnacky a jej zakladne nastavenie
k = turtle.RawTurtle(maze_gui)
k.shape("turtle")
k.color("yellow")
k.shapesize(1.5,1.5,3)
k.pensize(10)
k.speed(20)
k.setheading(270)

# definicia vlastnych definicii aby sme pouzivali slovenske nazvy
def dopredu(vzdialenost):
   k.forward(vzdialenost)

def vlavo(uhol):
   k.lt(uhol)

def vpravo(uhol):
   k.rt(uhol)

def opakuj(kolko_krat,uhol,vzdialenost):  #otacame sa v smere hodinovych ruciciek (doprava)
   for i in range(kolko_krat):
    k.rt(uhol)
    k.forward(vzdialenost)
maze_gui.mainloop()
