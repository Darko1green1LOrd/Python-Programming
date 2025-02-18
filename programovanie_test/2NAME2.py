import tkinter
from random import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def ifanythingclosed():
    exit()
main = tk.Tk()
main.protocol("WM_DELETE_WINDOW", ifanythingclosed)
area = tk.Canvas(main)
area = tkinter.Canvas()
area.pack()


def output_fails(fails):
	area.create_text(100, 10, text="Pokusy:")
	area.create_text(130, 10, text=fails)
def display_percentage(x,y):
	area.create_text(x, y, text="$", font="arial 20", fill="green")
def display_fence():
	x = 30
	for i in range(0,20):
		area.create_rectangle(0, x, 500, x+22, fill="yellow")
		x = x + 30
def click(coordinates):
	global fails,percentage_x,percentage_y
	x = coordinates.x
	y = coordinates.y
	area.delete("all")
	display_percentage(percentage_x,percentage_y)
	display_fence()
	if percentage_x-10<x<percentage_x+10:
		output = messagebox.askyesno('Výborne, získal si percento', 'Chceš skusit znova? teraz bude inde')
		if output:
			fails = 0
			area.delete("all")
			percentage_x = randrange(500)
			percentage_y = randint(40, 280)
			display_percentage(percentage_x,percentage_y)
			display_fence()
		else:
			exit()
	if x<percentage_x-10:
		area.create_text(200,10, text="Chod viac vpravo")
		fails=fails+1
		output_fails(fails)
	if percentage_x+10<x:
		area.create_text(200,10, text="Chod viac vľavo")
		fails=fails+1
		output_fails(fails)
	if fails == 5:
		output = messagebox.askyesno('To je škoda , nepodarilo sa :C', 'Chceš skusit znova?')
		if output:
			fails = 0
			area.delete("all")
			percentage_x = randrange(500)
			percentage_y = randint(40, 280)
			display_percentage(percentage_x,percentage_y)
			display_fence()
		else:
			exit()

fails = 0
percentage_x = randrange(500)
percentage_y = randint(40, 280)
display_percentage(percentage_x,percentage_y)
area.update()
area.after(100)
display_fence()

area.bind("<Button-1>", click)

sgui = Tk()
sgui.protocol("WM_DELETE_WINDOW", ifanythingclosed)
second_gui = tk.Canvas(sgui)
second_gui.pack()
sgui.title('Restart ???')
sgui.geometry("200x50+10+10")

def restart(event):
	fails = 0
	area.delete("all")
	percentage_x = randrange(500)
	percentage_y = randint(40, 280)
	display_percentage(percentage_x,percentage_y)
	display_fence()

confirm = Button(second_gui, text='Restart')
confirm.place(x=10, y=10, w=177)
confirm.bind('<Button-1>', restart)


area.mainloop()
paint_gui.mainloop()
