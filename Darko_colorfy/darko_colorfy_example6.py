from turtle import fd,rt,done,pencolor,colormode,width,bgcolor,shape,shapesize
import darko_colorfy as colors

d = 2
colormode(255)
width(3)
bgcolor("#323b33")
shape("circle")
shapesize(0.5)
colors.set_orange(8)
pencolor(colors.rgb)

while d < 300:
    fd(d)
    rt(90)
    d += 5
done()