from tkinter import Canvas
def moved(pos):
    global d
    x=((str(pos).split("x=",1)[1]).split(" ",1)[0]);y=((str(pos).split("y=",1)[1]).split(">",1)[0])
    d = (x,y)
    create_polygon()
maincan = Canvas(width=400,height=400,bg="white");maincan.grid()
a,b,c,d=(100,100),(200,100),(250,150),(150,300)
def create_polygon():
    maincan.delete("all")
    maincan.create_polygon(a,b,c,fill="",outline="blue",width=4)
    maincan.create_polygon(a,b,d,fill="",outline="red",width=4)
    maincan.create_polygon(a,c,d,fill="",outline="green",width=2)
create_polygon()
maincan.bind("<Button-1>",moved);maincan.mainloop()
