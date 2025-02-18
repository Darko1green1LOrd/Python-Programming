from turtle import fd,rt,done,pencolor,colormode,width,bgcolor,shape,shapesize
import darko_colorfy as colors

d = 2
colormode(255)
width(3)
bgcolor("#323b33")
shape("circle")
shapesize(0.5)

while d < 300:
    for i in range(1*d):
        colors.random_colors()
        pencolor(colors.rgb)
        fd(1)
    rt(90)
    d += 5
done()