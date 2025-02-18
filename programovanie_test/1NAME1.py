from tkinter import *
import tkinter as tk
import random

def ifanythingclosed():
    exit()

pgui = Tk()
pgui.protocol("WM_DELETE_WINDOW", ifanythingclosed)
paint_gui = tk.Canvas(pgui)
paint_gui.pack()
def create_square(x, y, r, canvasName):
    rand_color = str((random.randrange(111111, 999999)))
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return paint_gui.create_rectangle(x0, y0, x1, y1, fill=("#" + rand_color))
def circle(event):
    create_square(random.randrange(20, 300), random.randrange(0, 200), random.randrange(0, 20), paint_gui)


for x in range(0, 20):
    circle('event')

firstvaule = 145
secondvalue = 180
posy1 = 85
posy2 = 160
paint_gui.create_rectangle(firstvaule, posy1, secondvalue, posy2, width=1.5, fill="#002153", outline="#002153")
firstvaule = firstvaule + 36
secondvalue = secondvalue + 36
paint_gui.create_rectangle(firstvaule, posy1, secondvalue, posy2, width=1.5, fill="#ffffff", outline="#ffffff")
firstvaule = firstvaule + 36
secondvalue = secondvalue + 36
paint_gui.create_rectangle(firstvaule, posy1, secondvalue, posy2, width=1.5, fill="#cf0921", outline="#cf0921")



tk.mainloop()