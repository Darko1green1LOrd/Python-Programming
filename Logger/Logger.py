from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
from pytz import timezone
from sys import argv
import os

print(
'''
  _____             _
 |  __ \           | |
 | |  | | __ _ _ __| | _____
 | |  | |/ _` | '__| |/ / _ |
 | |__| | (_| | |  |   < (_) |
 |_____/ \__,_|_|  |_|\_\___/
 | |
 | |     ___   __ _  __ _  ___ _ __
 | |    / _ \ / _` |/ _` |/ _ \ '__|
 | |___| (_) | (_| | (_| |  __/ |
 |______\___/ \__, |\__, |\___|_|
               __/ | __/ |
              |___/ |___/

This script was made because i wanted to try out pynput s listeners , using all types of them and also to try out arguments when running
a python script in terminal,Its not intended for use withouth having permission to do so.
''') #This website was used to generate that ascii art text https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

Mpl,Mpr,Mrl,Mrr,Ms,Mm,Kkp,Kkr=(False,)*8
Include,logsprint=[],[]

def start():
    def start_log():
        ml = MouseListener(on_click=on_click,on_scroll=on_scroll, on_move=on_move)
        kl = KeyboardListener(on_press=on_press, on_release=on_release)

        ml.start()
        kl.start()
        ml.join()
        kl.join()

    def log(text):
        now = datetime.now(timezone('Europe/Bratislava')).strftime("%b %d %Y %H:%M:%S")
        with open('Logger_main.log', 'a+') as logfile:
                logfile.seek(0)
                logfile.write(f"{now}  {text}\n")

    def keych(keyin):
        keystr = str(keyin)
        if keystr.startswith("Key."):
            key = keystr.replace('Key.','').replace('_',' ').capitalize()
        else:
            key = keystr.replace("'",'')
        return key

    def on_click(x, y, ptype, state):
        mtype = (str(ptype).split('.',1)[1].capitalize())
        mstate = ("Pressed" if state else "Released")
        if mtype == "Left":
            if Mpl == True and state == True:
                log(f"{mtype} Mouse {mstate} at ({x},{y})")
            if Mrl == True and state == False:
                log(f"{mtype} Mouse {mstate} at ({x},{y})")
        else:
            if Mpr == True and state == True:
                log(f"{mtype} Mouse {mstate} at ({x},{y})")
            if Mrr == True and state == False:
                log(f"{mtype} Mouse {mstate} at ({x},{y})")

    def on_scroll(x, y, dx, dy):
        if Ms == True:
            log(f"Mouse scrolled At ({x},{y}) ({dx},{dy})")

    def on_move(x, y):
        if Mm == True:
            log(f"Mouse moved to ({x}, {y})")


    def on_press(key):
        if Kkp == True:
            log(f"Key {keych(key)} pressed")

    def on_release(key):
        if Kkr == True:
            log(f"Key {keych(key)} released")

    start_log()

def displogs():
    def addline():
        logsprint.append(f"({now-linetime} Ago){each.split('  ', 1)[0]} {funcs}")
    now = datetime.strptime(datetime.now(timezone('Europe/Bratislava')).strftime("%b %d %Y %H:%M:%S"), "%b %d %Y %H:%M:%S")
    with open('Logger_main.log', 'r') as logfile:
        logs = [line.strip() for line in logfile]
        for each in logs:
            linetime = datetime.strptime((each.split("  ", 1)[0]), "%b %d %Y %H:%M:%S")
            funcs = each.split('  ', 1)[1]
            if funcs.startswith(("Left","Right")):
                LR = funcs.split("Mouse ",1)[1]
                if funcs.startswith("Left"):
                    if Mpl == True and LR.startswith("Pressed"):
                        addline()
                    if Mrl == True and LR.startswith("Released"):
                        addline()
                if funcs.startswith("Right"):
                    if Mpr == True and LR.startswith("Pressed"):
                        addline()
                    if Mrr == True and LR.startswith("Released"):
                        addline()
            if funcs.startswith("Mouse scrolled"):
                if Ms:
                    addline()
            if funcs.startswith("Mouse moved"):
                if Mm:
                    addline()
            if funcs.startswith("Key") and funcs.endswith("pressed"):
                if Kkp:
                    addline()
            if funcs.startswith("Key") and funcs.endswith("released"):
                if Kkr:
                    addline()
    if logsprint == []:
        print("No logs based on your specifications, you can try using -all to display all logs")
    for line in logsprint:
        print(line)

def varsettings(action):
    global Mpl,Mpr,Mrl,Mrr,Ms,Mm,Kkp,Kkr
    del argv[0:2]
    Vars = argv
    for each in Vars:
        if each.startswith("I:"):
            for ivars in each.split("I:",1)[1].split(","):
                if ivars.startswith(("Mpl","Mpr","Mrl","Mrr","Ms","Mm","Kkp","Kkr")):
                    if ivars not in Include:
                        Include.append(ivars)
                else:
                    print(f"{ivars} is not accepted argument for I:, please use --help")
                    exit()
        elif each.startswith("-all"):
            Mpl,Mpr,Mrl,Mrr,Ms,Mm,Kkp,Kkr=(True,)*8
        else:
            print(f"{each} is not accepted argument for --{action}, please use --help")
            exit()
    for ichars in Include:
        exec(f"{ichars} = True",globals())
    if True not in (Mpl,Mpr,Mrl,Mrr,Ms,Mm,Kkp,Kkr):
        if action == "start":check = True
        else: check = False
        print(f"Please specify at least 1 thing to {'Log' if check else 'Display'}, please use --help")
        exit()

try:
    argv[1]
except IndexError:
    print("No arguments given, please use --help")
    exit()

if argv[1] == "--start":
    varsettings("start")
    start()

elif argv[1] == "--displogs":
    logfile_exists = os.path.exists("Logger_main.log")
    if logfile_exists == True:pass
    else:
        print("Nothing logged yet, please use --help")
        exit()
    varsettings("displogs")
    displogs()

elif argv[1] == "--help":
    print(
'''

EVERY COMMAND IS SEPARATED BY SPACE


--help
    Gives List of command and their usage



--start
    Starts the logger
    Requires specifying what you want to be logged

    Examples:
        Mouse presses are gonna be logged - python3 Logger.py --start I:Mpr,Mpl



--displogs
    Reads the file with logs and displays it with how much time has passed since each line has been logged
    Requires specifying what you want to displayed

    Examples:
        Only Key presses are gonna be displayed - python3 Logger.py --displogs I:Kkp
        Everything will be displayed - python3 Logger.py --displogs -all



By using I: you can specify which actions you want to be logged/displayed
Sperate specifications with,
Order of specification does not matter

By using -all you will specify all actions


List of specifications to log:
    both --start and --getlogs share these

    Mpl = Mouse press left
    Mpr = Mouse press right
    Mrl = Mouse release left
    Mrr = Mouse release right
    Ms = Mouse scroll
    Mm = Mouse movement
    Kkp = Keyboard key press
    Kkr = Keyboard key release
''')
else:
    print("Unknown Command, please use --help")
    exit()
