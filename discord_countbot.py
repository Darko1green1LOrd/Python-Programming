from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import time
import sys
import math
import keyboard


mode_select_gui = Tk()

text1=Label(mode_select_gui, text="Discord CountBot", fg='green', font=("Helvetica", 20))
text1.place(x=50, y=30)


sel=Entry(mode_select_gui)
sel.place(x=60, y=80)

def confirmaction(event):
    global mode
    addition = int(1)
    mode=int((sel.get()))
    texttosend=str(mode)
    while 1:
        if keyboard.is_pressed('escape'): 
            exit()
        time.sleep(2)
        keyboard.write(texttosend)
        keyboard.send('enter')
        mode = mode+addition
        texttosend=str(mode)


confirm = Button(mode_select_gui, text='OK')
confirm.place(x=60, y=105, w=177)
confirm.bind('<Button-1>', confirmaction)


mode_select_gui.title('CountBot')
mode_select_gui.geometry("300x200+10+10")
mode_select_gui.mainloop()