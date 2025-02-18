import pyperclip
from rich.traceback import install
from rich.console import Console
from rich.console import Group
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
import signal
from os import system
from time import sleep
from re import sub

zero_var = "\u200D"
one_var = "\u2062"
originalclip = pyperclip.paste()
decoymsg = ""
hiddenmsg = ""
binary_bl = 8

install(show_locals=True)
console = Console()

class exitValue:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        self._notify_observers(old_value, new_value)

    def _notify_observers(self, old_value, new_value):
        for callback in self._callbacks:
            callback(old_value, new_value)

    def trigger_onchange(self, callback):
        self._callbacks.append(callback)

noexit_reason = exitValue()
noexit_reason.value = ""
noexit_bypass = 3
exit_requested = False
exitdel = False
def proper_exit():
    global exitdel,noexit_bypass
    console.print(f'\n[#e3e536]Exitting[/#e3e536][#dfac48],[/#dfac48] [#41e738]Hope the messagehider was useful.[/#41e738]', justify="center")
    pyperclip.copy(originalclip)
    exit()
def check_change(old_value, new_value):
    if len(old_value) >= 1 and len(new_value) <= 0:proper_exit()
def exitfunc(signum, frame):
    global noexit_reason,noexit_bypass,exit_requested,exitdel
    if noexit_reason.value == "":proper_exit()
    else:
        if not exit_requested:
            noexit_reason.trigger_onchange(check_change)
            exit_requested = True
        noexit_bypass -= 1
        if noexit_bypass <= 0:noexit_reason.value = ""
        console.print(f"\n[bold #e72a24]Exit blocked, will exit as soon as it gets unblocked[/bold #e72a24] \n[#41e738]Reason[/#41e738][#abf3a7]:[/#abf3a7] [#e3e536]{noexit_reason.value}[/#e3e536]\n[bold #e72a24]For Forced Exit press [bold #e3e536]Ctrl[/bold #e3e536][#FFFFFF]+[/#FFFFFF][bold #e3e536]C[/bold #e3e536] [bold #48dfdd]{noexit_bypass}[/bold #48dfdd] [#e72a24]More Time{'s' if noexit_bypass > 1 else ''}[/#e72a24]", justify="center")

signal.signal(signal.SIGINT, exitfunc) #Bind ctrlc to exitfunc

def encode_binary_string(s,byte_length="08",hide=True):
    return_string = ''.join(format(ord(x), f'{byte_length}b') for x in s)
    return return_string.replace("1",one_var).replace("0",zero_var) if hide else return_string
    #link to encrypt the messages withouth the tool https://gchq.github.io/CyberChef/#recipe=To_Binary('Space',8)Find_/_Replace(%7B'option':'Regex','string':'%20'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'0'%7D,'%E2%80%8D',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'1'%7D,'%E2%81%A2',true,false,true,false)&input=dGVzdA&oenc=65001

def decode_binary_string(s,byte_length=8):
    decoded_str = s.replace(one_var,"1").replace(zero_var,"0")
    return ''.join(chr(int(decoded_str[i*byte_length:i*byte_length+byte_length],2)) for i in range(len(decoded_str)//byte_length))
    #link to read the mesages withouth the tool https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%5B%5E%E2%80%8D%E2%81%A2%5D'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%80%8D'%7D,'0',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%E2%81%A2'%7D,'1',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%20'%7D,'',true,false,true,false)From_Binary('Space',8)&input=aGkg4oCN4oGi4oGi4oGi4oCN4oGi4oCN4oCN4oCN4oGi4oGi4oCN4oCN4oGi4oCN4oGi4oCN4oGi4oGi4oGi4oCN4oCN4oGi4oGi4oCN4oGi4oGi4oGi4oCN4oGi4oCN4oCNIGxhbGE

def printout():
    deck_group = Group(
        f"[bold #5ae9ff]Decoy Message[/bold #5ae9ff] [#ff6063]:[/#ff6063] [#ffffff]{decoymsg.replace(zero_var,'').replace(one_var,'')}[/#ffffff]",
        f"[bold #7eff61]Hidden Message[/bold #7eff61] [#ff6063]:[/#ff6063] [#ffffff]{hiddenmsg}[/#ffffff]",
        f"[bold #ff5500]Binary Byte Length[/bold #ff5500] [#ff6063]:[/#ff6063] [#ffffff]{binary_bl:02d}[/#ffffff]",
    )
    console.print(Panel(deck_group, border_style="bright_green", style="on #141414", box=box.DOUBLE_EDGE), justify="center")
    console.print(f"[#27ec20]Press[/#27ec20] [bold #f4f62c]Ctrl[/bold #f4f62c][#bdbe61]+[/#bdbe61][bold #f4f62c]C[/bold #f4f62c] [#27ec20]To exit[/#27ec20]", justify="center")

while True:
    system('cls||clear')
    printout()
    dk_input = console.input(f"\n[bold #dce62d]Message hider[/bold #dce62d] [#00ff2c]Please type in\n\n[#7ec7ff][#57e3ff]copy[/#57e3ff] to copy the message into your clipboard[/#7ec7ff]\n\n[#7ec7ff][bold #36ff13]create[/bold #36ff13] to create new hidden message[/#7ec7ff]\n[#7ec7ff][bold #d47dff]read[/bold #d47dff] to read hidden message from your copied message[/#7ec7ff]\n[#7ec7ff][bold #00aa7f]setbl[/bold #00aa7f] to change your Byte Length, use this if the hidden message looks like random text[/#7ec7ff]\n\n[#75d5f4]Input[/#75d5f4] [#21c2f6]:[/#21c2f6] ").strip()
    if dk_input == "copy":
        if decoymsg != "":pyperclip.copy(decoymsg)
        else:
            console.print(f"\n[bold #ff0000]Your Decoy Message is empty[/bold #ff0000]", justify="center")
            sleep(1)
    elif dk_input == "create":
        dm_inp = console.input(f"\n[#00ff2c]Please type in [#7ec7ff][#57e3ff]Decoy Message[/#57e3ff]\nYour decoy message has to contain atleast one space between 2 words/letters\nor has to be nothing[/#7ec7ff]\n\n[#75d5f4]Input[/#75d5f4] [#21c2f6]:[/#21c2f6] ").strip()
        if " " in dm_inp or dm_inp == "":
            hm_inp = encode_binary_string(console.input(f"\n[#00ff2c]Please type in [#57e3ff]Hidden Message[/#57e3ff]\n\n[#75d5f4]Input[/#75d5f4] [#21c2f6]:[/#21c2f6] ").strip(),f"{binary_bl:02d}")
            decoymsg = dm_inp.split(" ",1) if " " in dm_inp else hm_inp
            if type(decoymsg) == list:
                decoymsg.insert(1,hm_inp)
                decoymsg = f"{decoymsg[0]} {decoymsg[1]}{decoymsg[2]}"
            try:
                hiddenmsg = decode_binary_string(sub(f'[^{zero_var}{one_var}]','',decoymsg).replace(" ",""),binary_bl)
            except TypeError:
                console.print(f"\n[bold #ff0000]Something went wrong, your decoy or hidden message most likely were typed in wrongly[/bold #ff0000]", justify="center")
                sleep(1)
        else:
            console.print(f"\n[bold #ff0000]You didnt put in any spaces[/bold #ff0000]", justify="center")
            sleep(1)
    elif dk_input == "read":
        toread = pyperclip.paste()
        if any(each in toread for each in [zero_var,one_var]):
            decoymsg = toread
            hiddenmsg = decode_binary_string(sub(f'[^{zero_var}{one_var}]','',decoymsg).replace(" ",""),binary_bl)
        else:
            console.print(f"\n[bold #ff0000]Given Input doesnt contain hidden message[/bold #ff0000]", justify="center")
            sleep(1)
    elif dk_input == "setbl":
        try:
            binary_bl_inp = int(console.input(f"\n[#00ff2c]Please type in [#7ec7ff][#57e3ff]number[/#57e3ff] to change the Byte Length[/#7ec7ff]\n\n[#75d5f4]Input[/#75d5f4] [#21c2f6]:[/#21c2f6] ").strip())
            if binary_bl_inp < 7:binary_bl_inp = 7
            binary_bl = binary_bl_inp
        except ValueError:
            console.print(f"\n[bold #ff0000]Not a number[/bold #ff0000]", justify="center")
            sleep(1)
    else:
        console.print(f"\n[bold #ff0000]Invalid Selection[/bold #ff0000]", justify="center")
        sleep(1)
