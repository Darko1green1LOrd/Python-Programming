import tkinter as tk
from tkinter import messagebox
from sys import exit
from keyboard import block_key,unblock_key,press_and_release,on_release,wait
from time import sleep
from pyperclip import copy,paste
from atexit import register
from platform import system

def run():
    global togglevalue
    originalclip = paste()
    def exitfunc():copy(originalclip)
    register(exitfunc)
    
    togglevalue = True

    maingui = tk.Tk()
    maingui.title("Discord Reaction Messaging")
    maingui.geometry("1100x200+0+0")
    maingui.resizable(False, False)
    maingui.config(bg="#1a1a1a")
    maingui.attributes('-topmost', True)
    #maingui.overrideredirect(True)
    maingui.wait_visibility(maingui)
    maingui.wm_attributes("-alpha", 0.7)


    textframe = tk.Frame(maingui)
    textframe.pack(padx=20, pady=20, side="left")
    textframe.config(bg="#1a1a1a")

    alphabet = tk.Text(textframe, height=1, width=46, wrap="none", bg="#1a1a1a", highlightbackground = "#1a1a1a", highlightcolor= "#1a1a1a")
    alphabet.grid(column=0,row=0)

    numbers = tk.Text(textframe, height=1, width=46, wrap="none", bg="#1a1a1a", highlightbackground = "#1a1a1a", highlightcolor= "#1a1a1a")
    numbers.grid(column=0,row=1)

    others = tk.Text(textframe, height=1, width=46, wrap="none", bg="#1a1a1a", highlightbackground = "#1a1a1a", highlightcolor= "#1a1a1a")
    others.grid(column=0,row=2)

    for each in [alphabet,numbers,others]:
        each.config(state="disabled",font=("", 25))
        each.tag_configure("g", foreground="limegreen")
        each.tag_configure("r", foreground="red")
        each.tag_configure("o", foreground="orange")



    buttons = tk.Frame(maingui)
    buttons.pack(padx=20, pady=20, side="right")
    buttons.config(bg="#1a1a1a")

    def info():messagebox.showinfo("Discord Reaction Messaging Info", 
"""
This program turns your keyboard input into discord reactions 

Click add reaction on right my message(right next to edit)
then just type

Red background = cooldown

The program will show you which letter you can type and how many times:
Green  : You can type it minimally twice
Orange : You have only one of this letter left
Red    : You ran out of this letter

When you want to react on new message with new set of characters just click
Restart

You can toggle reaction messaging by clicking on Enabled / Disabled
""")

    def run_toggle():
        global togglevalue
        togglevalue = not togglevalue
        if togglevalue:toggle.config(bg="#6be016",activebackground='#88e645', text ='Enabled')
        else:toggle.config(bg="#e6911c",activebackground='#e3ae64', text ='Disabled')

    def update():
        for full,short in zip([alphabet,numbers,others],["l","n","o"]):
            full.config(state="normal")
            full.delete("1.0","end")
            for key,value in items[short].items():
                full.insert("end", value[0],"r" if len(value) <= 1 else "o" if len(value) == 2 else "g")
            full.config(state="disabled")

    def run_restart():
        global items
        letters_d = {
            "a" : ["A",":regional_indicator_a:",
                       ":a:"],
            "b" : ["B",":regional_indicator_b:",
                       ":b:"],
            "c" : ["C",":regional_indicator_c:"],
            "d" : ["D",":regional_indicator_d:"],
            "e" : ["E",":regional_indicator_e:"],
            "f" : ["F",":regional_indicator_f:"],
            "g" : ["G",":regional_indicator_g:"],
            "h" : ["H",":regional_indicator_h:"],
            "i" : ["I",":regional_indicator_i:"],
            "j" : ["J",":regional_indicator_j:"],
            "k" : ["K",":regional_indicator_k:"],
            "l" : ["L",":regional_indicator_l:"],
            "m" : ["M",":regional_indicator_m:",
                       ":m:"],
            "n" : ["N",":regional_indicator_n:"],
            "o" : ["O",":regional_indicator_o:",
                       ":o2:",
                       ":o:"],
            "p" : ["P",":regional_indicator_p:",
                       ":parking:"],
            "q" : ["Q",":regional_indicator_q:"],
            "r" : ["R",":regional_indicator_r:"],
            "s" : ["S",":regional_indicator_s:"],
            "t" : ["T",":regional_indicator_t:"],
            "u" : ["U",":regional_indicator_u:"],
            "v" : ["V",":regional_indicator_v:"],
            "w" : ["W",":regional_indicator_w:"],
            "x" : ["X",":regional_indicator_x:",
                       ":x:"],
            "y" : ["Y",":regional_indicator_y:"],
            "z" : ["Z",":regional_indicator_z:"]
        }
        numbers_d = {
            "0" : ["0",":zero:"],
            "1" : ["1",":one:"],
            "2" : ["2",":two:"],
            "3" : ["3",":three:"],
            "4" : ["4",":four:"],
            "5" : ["5",":five:"],
            "6" : ["6",":six:"],
            "7" : ["7",":seven:"],
            "8" : ["8",":eight:"],
            "9" : ["9",":nine:"]
        }
        other_d = {
            "right" : ["➡",":arrow_right:"],
            "left" : ["⬅",":arrow_left:"],
            "down" : ["⬇",":arrow_down:"],
            "up" : ["⬆",":arrow_up:"],
            "?" : ["?",":grey_question:",
                              ":question:"],
            "space" : ["Space",":blue_square:",
                               ":red_square:",
                               ":green_square:",
                               ":black_large_square:",
                               ":yellow_square:",
                               ":purple_square:",
                               ":brown_square:",
                               ":white_large_square:",
                               ":orange_square:",
                               ":white_square_button:",
                               ":black_square_button:",
                               ":black_small_square:",
                               ":white_small_square:",
                               ":black_medium_small_square:",
                               ":white_medium_small_square:",
                               ":black_medium_square:",
                               ":white_medium_square:"]
        }

        items = {
            "l" : letters_d,
            "n" : numbers_d,
            "o" : other_d
        }
        
        update()

    restart = tk.Button(buttons, text ='Restart', command = run_restart,width=8,bg="#24c1c7",fg="black",activebackground='#3ae9f0',activeforeground="#1c1c1c",bd=0).grid(row=0)
    close = tk.Button(buttons, text ='Exit', command = exit,width=8,bg="#cf200c",fg="black",activebackground='#e04d3d',activeforeground="#1c1c1c",bd=0).grid(row=1,pady=5)
    toggle = tk.Button(buttons, text ='Enabled', command = run_toggle,width=8,bg="#6be016",fg="black",activebackground='#88e645',activeforeground="#1c1c1c",bd=0)
    toggle.grid(row=2)
    infob = tk.Button(buttons, text ='Info', command = info,width=8,bg="#ddeb1a",fg="black",activebackground='#eefa46',activeforeground="#1c1c1c",bd=0).grid(row=3,pady=5)

    run_restart()
    keys = [item for sublist in [list(items[each].keys()) for each in ["l","n","o"]] for item in sublist]

    def cooldownfunc():
        for key in keys:
            block_key(key)
            maingui.config(bg="#cf2d27")
        sleep(1)
        for key in keys:
            unblock_key(key)
            maingui.config(bg="#1a1a1a")

    def do_reaction(var_type,text):
        copy(items[var_type][text][1])
        press_and_release('backspace, shift+insert, shift+enter, alt+esc' if system() == "Linux" else 'backspace, shift+insert, shift+enter, ctrl+a, del')
        cooldownfunc()
        del(items[var_type][text][1])
        update()

    def keypressed(event):
        if togglevalue:
            if event.name in items["l"] and len(items["l"][event.name]) >= 2:do_reaction("l",event.name)
            elif event.name in items["n"] and len(items["n"][event.name]) >= 2:do_reaction("n",event.name)
            elif event.name in items["o"] and len(items["o"][event.name]) >= 2:do_reaction("o",event.name)

    on_release(keypressed)
    maingui.mainloop()

if __name__ == "__main__":run()
else:raise Exception("Please dont include this file in your .py file")
