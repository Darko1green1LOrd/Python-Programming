import tkinter
from random import *
from tkinter import messagebox
area = tkinter.Canvas()
area.pack()

def create_ball(x, y):
	area.create_oval(x-5, y-5, x+5, y+5, fill="red")

def output_points(points):
	area.create_text(100, 10, text="Points Gained:")
	area.create_text(200, 10, text=points)

def timer():
	area.delete("all")
	global ball_x, ball_y, points, platform_size
	if points == 0:
		ball_y = ball_y + 0.5
		platform_size = 150
	elif points == 1:
		ball_y = ball_y + 1
		platform_size = 140
	elif points == 2:
		ball_y = ball_y + 1.5
		platform_size = 130
	elif points == 3:
		ball_y = ball_y + 2
		platform_size = 120
	elif points == 4:
		ball_y = ball_y + 2.5
		platform_size = 110
	elif points == 5:
		ball_y = ball_y + 3
		platform_size = 100
	elif points == 6:
		ball_y = ball_y + 3.5
		platform_size = 90
	elif points == 7:
		ball_y = ball_y + 4
		platform_size = 90
	elif points == 8:
		ball_y = ball_y + 4.5
		platform_size = 80
	elif points == 9:
		ball_y = ball_y + 5
		platform_size = 70
	elif points == 10:
		ball_y = ball_y + 6
		platform_size = 50
	elif points == 11:
		ball_y = ball_y + 6
		platform_size = 40
	elif points == 12:
		ball_y = ball_y + 6
		platform_size = 30
	else :
		ball_y = ball_y + 6
		platform_size = 20
	create_ball(ball_x, ball_y)
	area.create_line(cursor_x-1, cursor_y-1, cursor_x+platform_size, cursor_y-1, fill="blue", width=5)
	output_points(points)
	if cursor_x<ball_x<cursor_x+platform_size and cursor_y-10<ball_y<cursor_y:
		points = points + 1
		ball_x = randrange(300)
		ball_y = 20
	if ball_y>300:
		points = points - 1
		ball_x = randrange(300)
		ball_y = 20
	if points == -1:
		 output = messagebox.askyesno('You Lost', 'Want to try again?')
		 if output:
		 	points = 0
		 else:
		 	exit()
	area.after(20, timer)

def mouse_movement(coordinates):
	global points, cursor_x
	cursor_x = coordinates.x-25
	area.delete("all")
	create_ball(ball_x, ball_y)
	area.create_line(cursor_x-1, cursor_y-1, cursor_x+platform_size, cursor_y-1, fill="blue", width=5)
	output_points(points)

points = 0
ball_x = randrange(300)
ball_y = 20
cursor_x = 150
cursor_y = 250

timer()
area.bind("<Motion>", mouse_movement)
area.mainloop()
