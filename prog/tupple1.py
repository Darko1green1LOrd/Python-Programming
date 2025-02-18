from tkinter import Canvas
x,y,add,c=10,30,40,("Red","Green","Blue","Yellow","Pink","Purple")
maincan = Canvas(width=400,height=100,bg="white");maincan.grid()
for color in c:maincan.create_rectangle(x,y,x+add,y+30,fill=color);x=x+add
maincan.mainloop()
