from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import random


mode_select_gui = Tk()

text1=Label(mode_select_gui, text="Select Mode", fg='green', font=("Helvetica", 16))
text1.place(x=60, y=50)

data=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17")
sel=Combobox(mode_select_gui, values=data)
sel.place(x=60, y=80)

def confirmaction(event):
    global mode
    mode=(sel.get())
    mode_select_gui.destroy()

confirm = Button(mode_select_gui, text='OK')
confirm.place(x=60, y=105, w=177)
confirm.bind('<Button-1>', confirmaction)


mode_select_gui.title('Mode Select')
mode_select_gui.geometry("300x200+10+10")
mode_select_gui.mainloop()

def ifanythingclosed():
    exit()

# Answer 1 :
# Answer 2 : Yes, its possible to make the triangle image or make the lines in different order
# Answer 3 : mode = 4
pgui = Tk()
pgui.protocol("WM_DELETE_WINDOW", ifanythingclosed)
paint_gui = tk.Canvas(pgui)
paint_gui.pack()
if mode == "1":
    paint_gui.create_line(10, 100, 200, 100, 10, 200)
    paint_gui.create_line(10, 100, 10, 200, fill="red")
elif mode == "2":
    paint_gui.create_line(110, 10, 10, 200, fill="blue")
    paint_gui.create_line(10, 200, 210, 200, fill="blue")
    paint_gui.create_line(210, 200, 110, 10, fill="blue")
elif mode == "3":
    paint_gui.create_line(10, 100, 200, 100, width=5, fill='red')
elif mode == "4":
    paint_gui.create_line(110, 10, 10, 200, fill='blue')
    paint_gui.create_line(10, 200, 210, 200, fill='blue')
    paint_gui.create_line(210, 200, 110, 10, fill='blue')
    paint_gui.create_line(210, 10, 110, 200, 310, 200, 210, 10, fill='red')
elif mode == "5":
    paint_gui.create_oval(80, 34, 180, 130, outline='#e33a1c',width=12)
    text2=Label(paint_gui, text="6 t", fg='green', font=("Arial", 35))
    text2.place(x=102, y=55)
elif mode == "6":
	def genline(event):
		rand_color=str((random.randrange(111111, 999999)))  
		paint_gui.create_line(0, 0, random.randrange(0, 250), random.randrange(0, 250), fill=("#"+rand_color), width=2)
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
	genline('event')
elif mode == "7":
    y = 0
    for i in range(1,6):
        y = y + 10
        paint_gui.create_line(10, y, 200, y)
elif mode == "8":
    num = 0
    for i in range(0,5):
        num = num + 1
        paint_gui.create_text(random.randrange(400),random.randrange(300), text=num)
elif mode == "9":
    for i in range(0,6):
        print(i*10)
        paint_gui.create_line(10, i*10, 200, i*10)
        paint_gui.update()
        paint_gui.after(1000)
elif mode == "10": #2
    value1mw=10
    print("value was set")
    for value2 in range(0,6):
        print(f"Middle Window Progression: {value2*20}%")

        paint_gui.create_line(value1mw, value2*10, 200, value2*10)
        value1mw=value1mw+10
        paint_gui.update()
        paint_gui.after(200)

    one = tk.Tk()
    one.geometry("380x265+868+231")
    one.protocol("WM_DELETE_WINDOW", ifanythingclosed)


    two = tk.Tk()
    two.geometry("380x265+98+231")
    two.protocol("WM_DELETE_WINDOW", ifanythingclosed)


    subgui = tk.Canvas(one)
    subgui.pack()
    for value3 in range(0,6):
        print(f"Right Window Progression: {value3*20}%")

        subgui.create_line(10, value3*10, 200, value3*20)
        subgui.update()
        subgui.after(200)


    subgui2 = tk.Canvas(two)
    subgui2.pack()
    for value1 in range(0,11):
        print(f"Left Window Progression: {value1*10}%")

        subgui2.create_line(10, value1*10, 200, value1*10)
        subgui2.update()
        subgui2.after(200)

    tk.mainloop()
elif mode == "11": #3
    value1mw=10
    print("value was set")
    for value2 in range(0,6):
        print(f"Middle Window Progression: {value2*20}%")

        paint_gui.create_line(value2*10, value1mw, value2*10, 200)
        value1mw=value1mw+30
        paint_gui.update()
        paint_gui.after(200)

    one = tk.Tk()
    one.geometry("380x265+868+231")
    one.protocol("WM_DELETE_WINDOW", ifanythingclosed)


    two = tk.Tk()
    two.geometry("380x265+98+231")
    two.protocol("WM_DELETE_WINDOW", ifanythingclosed)


    subgui = tk.Canvas(one)
    subgui.pack()
    value1rw=10
    value2rw=100
    for value3 in range(0,6):
        print(f"Right Window Progression: {value3*20}%")

        subgui.create_line(value3*10, value1rw, value3*10, value2rw)
        value1rw=value1rw+30
        value2rw=value2rw+30
        subgui.update()
        subgui.after(200)


    subgui2 = tk.Canvas(two)
    subgui2.pack()
    for value1 in range(0,11):
        print(f"Left Window Progression: {value1*10}%")

        subgui2.create_line(value1*10, 10, value1*10, 200)
        subgui2.update()
        subgui2.after(200)

    tk.mainloop()
elif mode == "12": #4
    x = 0
    for i in range(1,11):
        x = x + 20
        paint_gui.create_rectangle(x, 10, x+15, 20)
    value1 = 20
    value2 = 10
    value3 = 35
    value4 = 10
    for i in range(1,11):
        paint_gui.create_line(value1, value2, value3, value4,fill='red')
        paint_gui.create_line(value1, value2+10, value3, value4+10,fill='red')
        paint_gui.create_line(value1, value2, value3-15, value4+10,fill='red')
        paint_gui.create_line(value1+15, value2, value3, value4+10,fill='red')
        value1 = value1 + 20
        value2 = value2 + 0
        value3 = value3 + 20
        value4 = value4 + 0
        paint_gui.update()
        paint_gui.after(200)
elif mode == "13": #5
    firstvaule = 70
    secondvalue = 85
    for i in range(1,7):
        paint_gui.create_rectangle(10, firstvaule, 200, secondvalue, width=1.5)
        firstvaule = firstvaule + 30
        secondvalue = secondvalue + 30
elif mode == "14": #6
    exit()
elif mode == "15": #7
    anglevaule = 0
    for i in range(1,7):
        paint_gui.create_text(190, 90, text="ŤAHAŤ", fill="blue", anchor=tk.CENTER, angle=anglevaule, font=("Arial", 35))
        anglevaule = anglevaule + 120
elif mode == "16": #8
    n = 6
    angle = 360 / n
    for i in range(n):
        paint_gui.create_text(190, 120, text="  Python", fill="black", activefill="black", anchor=tk.W, angle=i*angle, font=("Arial", 20))
elif mode == "17": #9
    value1f = 100
    value2f = 10
    value3f = 100
    value4f = 100

    value1s = 100
    value2s = 10
    value3s = 10
    value4s = 10
    print("value was set")
    pgui.geometry("600x600+50+50")
    for value2 in range(0,8):
        print(f"Left Window Progression: {value2*15-5}%")

        paint_gui.create_line(value1f, value2f, value3f, value4f)
        paint_gui.create_line(value1s, value2s, value3s, value4s)
        value1f = value1f + 90
        value2f = value2f + 90
        value3f = value3f + 90
        value4f = value4f + 90

        value1s = value1s + 90
        value2s = value2s + 90
        value3s = value3s + 90
        value4s = value4s + 90
        paint_gui.update()
        paint_gui.after(200)


    one = tk.Tk()
    one.geometry("600x600+700+50")
    one.protocol("WM_DELETE_WINDOW", ifanythingclosed)


    subgui = tk.Canvas(one)
    subgui.pack()
    value1f = 10
    value2f = 10
    value3f = 10
    value4f = 100

    value1s = 100
    value2s = 10
    value3s = 10
    value4s = 10
    for value3 in range(0,2):
        print(f"Right Window Progression: {value3*15-5}%")

        #subgui.create_line(value1f, value2f, value3f, value4f)
        #subgui.create_line(value1s, value2s, value3s, value4s)
        subgui.create_line(100, 100, 100, 200)
        subgui.create_line(200, 100, 100, 100)
        subgui.create_line(100, 200, 100, 300,fill='red',width=5)
        value1f = value1f - 90
        value2f = value2f + 90
        value3f = value3f - 90
        value4f = value4f + 90

        value1s = value1s - 90
        value2s = value2s + 90
        value3s = value3s - 90
        value4s = value4s + 90
        subgui.update()
        subgui.after(200)


    tk.mainloop()
else:
    exit()

paint_gui.mainloop()
