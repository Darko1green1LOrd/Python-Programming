# zakladne nastavenie okna
import turtle
import tkinter as tk

def setupturtle():
    k.penup()
    k.clear()
    k.home()
    k.setheading(270)
    k.shape("turtle")
    k.color("yellow")
    k.shapesize(1.5,1.5,3)
    k.pensize(10)
    k.speed(20)
    k.pendown()
def press():
    setupturtle()
    turtle_input = text.get(1.0, "end-1c")
    for line in turtle_input.splitlines():
        eval(line)

okno_width = 1033
okno_height = 1073
screen = turtle.Screen()
screen.title("Von z bludiska")
screen.setup(okno_width,okno_height)
screen.bgcolor("gray")
screen.bgpic('map.png')
#screen.setworldcoordinates(-300, -500, 500, 500) Ak by nebol obrázok na celý obraz kôli input veciam toto umožnuje scollovanie obrázku

controller = screen.getcanvas()
button = tk.Button(controller.master, text = "Spustiť", command = press, height=4)
button.pack(side=tk.RIGHT)

text = tk.Text(controller.master, height=5, width=40)
scroll = tk.Scrollbar(controller.master)
text.configure(yscrollcommand=scroll.set)
text.pack(side=tk.RIGHT)

scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

info = tk.Label(controller.master, text="Príkazy", fg='black', font=("Helvetica", 16)).pack(side=tk.LEFT,anchor=tk.N)
dopredu = tk.Label(controller.master, text="dopredu(vzdialenost) - Ide dopredu", fg='black', font=("Helvetica", 10)).pack(side=tk.BOTTOM,anchor=tk.W)
vlavo = tk.Label(controller.master, text="vlavo(uhol) - Otáča sa dolava", fg='black', font=("Helvetica", 10)).pack(side=tk.BOTTOM,anchor=tk.W)
vpravo = tk.Label(controller.master, text="vpravo(uhol) - Otáča sa doprava", fg='black', font=("Helvetica", 10)).pack(side=tk.BOTTOM,anchor=tk.W)
opakuj = tk.Label(controller.master, text="opakuj(kolko_krat,uhol,vzdialenost) - Otáča sa v smere hodinových ručičiek(doprava)", fg='black', font=("Helvetica", 10)).pack(side=tk.BOTTOM,anchor=tk.W)

# vytvorenie korytnacky a jej zakladne nastavenie
k = turtle.Turtle()
setupturtle()

# definicia vlastnych definicii aby sme pouzivali slovenske nazvy
def dopredu(vzdialenost):
   k.forward(vzdialenost)

def vlavo(uhol):
   k.lt(uhol)

def vpravo(uhol):
   k.rt(uhol)

def opakuj(kolko_krat,uhol,vzdialenost):  #otacame sa v smere hodinovych ruciciek (doprava)
   for i in range(kolko_krat):
    k.rt(uhol)
    k.forward(vzdialenost)
screen.mainloop()
