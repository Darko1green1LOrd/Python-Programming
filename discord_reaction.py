import keyboard
keyboard.on_press_key("esc", lambda _:dostuff())
def dostuff():
    keyboard.write("+:litlantern")
    keyboard.press_and_release("enter")
    keyboard.write("+:unlitlantern")
    keyboard.press_and_release("enter")
while True:
	if keyboard.is_pressed('down'):
		break


#this is for a discord server
# to make look like dyno bot from card suggestions is adding 

#sudo python3.8 discord_reaction.py
