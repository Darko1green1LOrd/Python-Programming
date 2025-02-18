from tkinter import *

root=Tk()

second_window = None

def second_window_X():
    global second_window
    second_window=Toplevel(root)
    label=Label(second_window, text='window')
    label.pack()

button=Button(root, text='second window', command=second_window_X,width=100)
button.pack()

def move_me(event):
    try:
        if second_window != None:
            x = root.winfo_x()
            y = root.winfo_y()
            second_window.geometry(f"+{x}+{y}")
    except NameError:
        pass
root.bind("<Configure>", move_me)

root.mainloop()
