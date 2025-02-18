from tkinter import *

Window = Tk()
Window.geometry("200x200+50+50") # heightxwidth+x+y

mainPanel = Canvas(Window, width = 200, height = 200) # main screen
mainPanel.pack()

entry_text = StringVar() # the text in  your entry
entry_widget = Entry(mainPanel, width = 20, textvariable = entry_text) # the entry
mainPanel.create_window(100, 100, window = entry_widget)

def character_limit(obj):
    if len(obj.get()) > 0:
        obj.set(obj.get()[-1])

entry_text.trace("w", lambda *args: character_limit(entry_text))
Window.mainloop()

#you can change this line of code: entry_text.set(entry_text.get()[-1])change the index in the square brackets to change the range

#For example:
#obj.set(obj.get()[:5]) first 5 characters limit
#obj.set(obj.get()[-5:]) last 5 characters limit
#obj.set(obj.get()[:1]) first character only
#obj.set(obj.get()[:-1]) last character only
