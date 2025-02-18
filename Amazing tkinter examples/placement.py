import tkinter as tk

root = tk.Tk()
geow = 600 # Width
geoh = 300 # Height

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x = (root.winfo_screenwidth()/2) - (geow/2)
y = (root.winfo_screenheight()/2) - (geoh/2)
root.geometry(f"{geow}x{geoh}+{int(x)}+{(int(y))}")
root.mainloop()
