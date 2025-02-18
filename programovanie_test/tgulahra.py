import tkinter
from random import *
from tkinter import messagebox
import itertools
area = tkinter.Canvas()
area.pack()


def create_ball(x, y):
	area.create_oval(x-5, y-5, x+5, y+5, fill="red",tags="ball")

def output_points(points):
	area.create_text(200, 10, text=points,tags="points")

def timer():
	area.delete("points")
	global ball_x, ball_y, points, platform_size
	if points == 0:
		ball_speed = 1
		platform_size = 150
	elif points == 1:
		ball_speed = 1
		platform_size = 140
	elif points == 2:
		ball_speed = 1
		platform_size = 130
	elif points == 3:
		ball_speed = 1
		platform_size = 120
	elif points == 4:
		ball_speed = 1
		platform_size = 110
	elif points == 5:
		ball_speed = 1
		platform_size = 100
	elif points == 6:
		ball_speed = 1
		platform_size = 90
	elif points == 7:
		ball_speed = 1
		platform_size = 80
	elif points == 8:
		ball_speed = 1
		platform_size = 70
	elif points == 9:
		ball_speed = 1
		platform_size = 60
	elif points == 10:
		ball_speed = 1
		platform_size = 50
	elif points == 11:
		ball_speed = 1
		platform_size = 40
	elif points == 12:
		ball_speed = 1
		platform_size = 30
	else :
		ball_speed = 1
		platform_size = 20
	area.move("ball", 0, ball_speed)
	#Ball X
	ball_position_x_step1 = area.coords("ball")
	ball_position_x_step2 = ball_position_x_step1[:1]
	ball_position_x_step3 = ball_position_x_step2.pop()
	ball_position_x_step4 = int(ball_position_x_step3)
	#print(f"Ball X: {ball_position_x_step4}")
	#
	#Ball Y
	ball_position_y_step1 = area.coords("ball")
	ball_position_y_step2 = ball_position_y_step1[:2]
	ball_position_y_step3 = ball_position_y_step2.pop()
	ball_position_y_step4 = int(ball_position_y_step3)
	#print(f"Ball Y: {ball_position_y_step4}")
	#
	#Platform X
	platform_position_x_step1 = area.coords("cursor")
	platform_position_x_step2 = platform_position_x_step1[:1]
	platform_position_x_step3 = platform_position_x_step2.pop()
	platform_position_x_step4 = int(platform_position_x_step3)
	#print(f"Platform X: {platform_position_x_step4}")
	#
	#Platform Y
	platform_position_y_step1 = area.coords("cursor")
	platform_position_y_step2 = platform_position_y_step1[:2]
	platform_position_y_step3 = platform_position_y_step2.pop()
	platform_position_y_step4 = int(platform_position_y_step3)
	#print(f"Platform Y: {platform_position_y_step4}")
	output_points(points)
	area.coords("cursor", cursor_x-1, cursor_y-1, cursor_x+platform_size, cursor_y-1)
	if ball_position_y_step4==(platform_position_y_step4-10) and ball_position_x_step4 in range(platform_position_x_step4-5, (platform_position_x_step4+platform_size)+5):
		points = points + 1
		respawn_ball()
	if ball_position_y_step4==(platform_position_y_step4+5):
		points = points - 1
		respawn_ball()
	if points == -1:
		 output = messagebox.askyesno('Prehrali Ste', 'Chcete skusit znova?')
		 if output:
		 	points = 0
		 else:
		 	exit()
	area.after(20, timer)

def mouse_movement(coordinates):
	global cursor_x
	area.move("cursor", coordinates.x - cursor_x, 0)
	cursor_x = coordinates.x
	#print(f"Cursor X: {cursor_x}")
	#canvas.coords("cursor", 0, 0, event.width, event.height) resize

def firststart():
	area.create_text(100, 10, text="Počet získaných bodov:")
	area.create_oval(ball_x-5, ball_y-5, ball_x+5, ball_y+5, fill="red",tags="ball")
	area.create_line(cursor_x-1, cursor_y-1, cursor_x+150, cursor_y-1, fill="blue", width=5, tags="cursor")

def respawn_ball():
	ball_x = randrange(300)
	ball_y = 20
	area.delete("ball")
	area.create_oval(ball_x-5, ball_y-5, ball_x+5, ball_y+5, fill="red",tags="ball")


points = 0
ball_x = randrange(300)
ball_y = 20
cursor_x = 0
cursor_y = 250
firststart()

timer()
area.bind("<Motion>", mouse_movement)
area.mainloop()