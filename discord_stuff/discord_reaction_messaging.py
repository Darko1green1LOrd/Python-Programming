#sudo python3.8 discord_reaction_messaging.py 
import keyboard
import pyperclip
import time
originalclip = pyperclip.paste()
altchar = False

arrows = ['left' , 'right', 'up', 'down']
numbers = ['zero' , 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
keys = ['left' , 'right', 'up', 'down', 'space', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("\nWelcome to Darko s Discord reaction messaging\nThis program turns your keyboard input into discord reactions \nso you react with letters , numbers , arrows and space\n\nToggle Mode : press capslock\nEsc : stop the program\n\n2 modes are here so you can react with same letter more than once\nMode 1 aviable keys :\nSpacebar , Direction Arrows , Numpad Numbers, Full alphabed withouth stuff like á é ž\n\nMode 2 Avaiable keys :\no Spacebar\n\nClick add reaction on right my message(right next to edit)\nthen just type")

def cooldownfunc():
    for key in keys:
        keyboard.block_key(key)
    time.sleep(1.5)
    for key in keys:
        keyboard.unblock_key(key)


def do_reaction(text):
    pyperclip.copy(f'{text}')
    keyboard.press_and_release('backspace, ctrl+v, shift+enter, ctrl+a, del') #Ctrl or Alt+esc instead of ctrl+a, del works but use only on linux 

def react_letter(letter):
    do_reaction(f'regional_indicator_{letter}')


def react_number(number):
    do_reaction(f'{numbers[int(number)]}')


def react_arrows(arrow):
    do_reaction(f'arrow_{arrow}')


def alternate_char(char):
    if char == "o":
        do_reaction('o2')
    elif char == "space":
        do_reaction('red_square')
    else:
        pass



while True:
    event = keyboard.read_event()

    if event.event_type == "up":
        char = event.name

        if char == "caps lock":
            altchar = not altchar
            print(f"\nAlternative Mode: {'On' if altchar else 'Off'}")
        if altchar:
            alternate_char(char)
            continue

        if "a" <= char <= "z" and len(char) == 1 and altchar == 0:
            react_letter(char)
        elif "0" <= char <= "9" and len(char) == 1:
            react_number(char)
        elif char == "space" and altchar == 0:
            do_reaction('blue_square')
        elif char in arrows:
            react_arrows(char)
        
        if char == "esc":
            pyperclip.copy(originalclip)
            break
        cooldownfunc()
