from tkinter import *
import tkinter as tk
import random

def ifanythingclosed():
    exit()

pgui = Tk()
pgui.protocol("WM_DELETE_WINDOW", ifanythingclosed)
paint_gui = tk.Canvas(pgui)
paint_gui.pack()
def create_circle(x, y, r, canvasName):
    rand_color = str((random.randrange(111111, 999999)))
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return paint_gui.create_oval(x0, y0, x1, y1, fill=("#" + rand_color))
def circle(event):
    create_circle(random.randrange(20, 300), random.randrange(0, 200), 20, paint_gui)


for x in range(0, 15):
    circle('event')

firstvaule = 85
secondvalue = 110
posx1 = 145
posx2 = 240
paint_gui.create_rectangle(posx1, firstvaule, posx2, secondvalue, width=1.5, fill="#d81e05", outline="#d81e05")
firstvaule = firstvaule + 25
secondvalue = secondvalue + 25
paint_gui.create_rectangle(posx1, firstvaule, posx2, secondvalue, width=1.5, fill="#ffffff", outline="#ffffff")
firstvaule = firstvaule + 25
secondvalue = secondvalue + 25
paint_gui.create_rectangle(posx1, firstvaule, posx2, secondvalue, width=1.5, fill="#d81e05", outline="#d81e05")



tk.mainloop()