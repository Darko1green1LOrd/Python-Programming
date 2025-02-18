import tkinter
from random import *
from tkinter import messagebox
from venv import create

points = 0
ball_x = randrange(300)
ball_y = 20

platform_x = 0
platform_y = 250

area = tkinter.Canvas()
area.pack()

def output_points():
    area.delete("pointtext")
    area.delete("points")
    area.create_text(100, 10, text="Počet získaných bodov:",tags="pointtext")
    area.create_text(200, 10, text=points,tags="points")

def reset_ball():
    global ball_x, ball_y
    new_x = randrange(300)
    area.move("ball", new_x-ball_x, 20-ball_y)
    ball_x = new_x
    ball_y = 20

def create_platform():
    area.delete("platform")
    platform = platform_width()
    half = platform / 2
    area.create_line(platform_x-half, platform_y, platform_x+half, platform_y, fill="blue", width=5, tags="platform")

def move_ball():
    global ball_y, platform_x, points
    speed = ball_speed()
    ball_y += speed
    area.move("ball", 0, speed)
    if ball_y + 5 >= platform_y:
        platform = platform_width()
        half = platform / 2
        if platform_x - half <= ball_x <= platform_x + half:
            points += 1
        else:
            points -= 1
        reset_ball()
        create_platform()

def ball_speed():
    return min(6,(points+1)*.5)

def platform_width():
    return max(20, 150-10*points)

def timer():
    global points
    move_ball()
    output_points()
    if points == -1:
        output = messagebox.askyesno('Prehrali Ste', 'Chcete skusit znova?')
        if output:
            points = 0
        else:
            exit()
    area.after(20, timer)

def mouse_movement(coordinates):
    global platform_x
    area.move("platform", coordinates.x - platform_x, 0)
    platform_x = coordinates.x


if __name__ == '__main__':
    create_platform()
    area.create_oval(ball_x-5, ball_y-5, ball_x+5, ball_y+5, fill="red",tags="ball")

    timer()
    area.bind("<Motion>", mouse_movement)
    area.mainloop()