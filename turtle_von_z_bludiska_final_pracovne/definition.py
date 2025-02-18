# zakladne nastavenie okna 
import turtle

okno_width = 1920
okno_height = 1080
screen = turtle.Screen()
screen.title("Von z bludiska")
screen.setup(okno_width-350,okno_height-5)
screen.bgcolor("gray")
screen.bgpic('mapa.png')

# vytvorenie korytnacky a jej zakladne nastavenie
k = turtle.Turtle()
k.shape("turtle")
k.color("yellow")
k.shapesize(1.5,1.5,3)
k.pensize(10)
k.speed(20)
k.setheading(270)

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
