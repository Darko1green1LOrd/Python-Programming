from random import randint

red,green,blue = 0,0,0
rgb = (red,green,blue)
hex = f"#{red:02x}{green:02x}{blue:02x}"


redup,greenup,blueup = True,True,True
current_color = 0


def advance_rainbow_grad():
    global current_color,red,green,blue,rgb,redup,greenup,blueup,hex
    if current_color > 2:current_color = 0

    if current_color != 0:
        if red <= 0:redup = True
        elif red >= 255:
            redup = False
            current_color += 1
        red = 1+red if redup else red-1

    if current_color != 1:
        if green <= 0:greenup = True
        elif green >= 255:
            greenup = False
            current_color += 1
        green = 1+green if greenup else green-1

    if current_color != 2:
        if blue <= 0:blueup = True
        elif blue >= 255:
            blueup = False
            current_color += 1
        blue = 1+blue if blueup else blue-1

    rgb = (red,green,blue)
    hex = f"#{red:02x}{green:02x}{blue:02x}"


def advance_wave_grad(which=("r","g","b")):
    global red,green,blue,rgb,redup,greenup,blueup,hex

    if "r" in which:
        if red <= 0:redup = True
        elif red >= 255:redup = False
        red = 1+red if redup else red-1

    if "g" in which:
        if green <= 0:greenup = True
        elif green >= 255:greenup = False
        green = 1+green if greenup else green-1

    if "b" in which:
        if blue <= 0:blueup = True
        elif blue >= 255:blueup = False
        blue = 1+blue if blueup else blue-1

    rgb = (red,green,blue)
    hex = f"#{red:02x}{green:02x}{blue:02x}"


def random_colors(which=("r","g","b")):
    global current_color,red,green,blue,rgb,redup,greenup,blueup,hex

    if "r" in which:
        red = int(f"{randint(0, 255):02}")
        if red <= 0:redup = True
        elif red >= 255:redup = False

    if "g" in which:
        green = int(f"{randint(0, 255):02}")
        if green <= 0:greenup = True
        elif green >= 255:greenup = False

    if "b" in which:
        blue = int(f"{randint(0, 255):02}")
        if blue <= 0:blueup = True
        elif blue >= 255:blueup = False

    rgb = (red,green,blue)
    hex = f"#{red:02x}{green:02x}{blue:02x}"


def reset_colors():
    global current_color,red,green,blue,rgb,redup,greenup,blueup,hex

    red,green,blue = 0,0,0
    rgb = (red,green,blue)
    hex = f"#{red:02x}{green:02x}{blue:02x}"

    redup,greenup,blueup = True,True,True
    current_color = 0


def set_custom_color(r,g,b):
    global red,green,blue,rgb,hex

    red,green,blue = r,g,b
    rgb = (red,green,blue)
    hex = f"#{red:02x}{green:02x}{blue:02x}"

    redup,greenup,blueup = True,True,True
    current_color = 0

def set_red(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(51,0,0)
    elif brightness__1_to_9 == 2:set_custom_color(102,0,0)
    elif brightness__1_to_9 == 3:set_custom_color(153,0,0)
    elif brightness__1_to_9 == 4:set_custom_color(204,0,0)
    elif brightness__1_to_9 == 5:set_custom_color(255,0,0)
    elif brightness__1_to_9 == 6:set_custom_color(255,51,51)
    elif brightness__1_to_9 == 7:set_custom_color(255,102,102)
    elif brightness__1_to_9 == 8:set_custom_color(255,153,153)
    elif brightness__1_to_9 == 9:set_custom_color(255,204,204)

def set_orange(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(51,25,0)
    elif brightness__1_to_9 == 2:set_custom_color(102,51,0)
    elif brightness__1_to_9 == 3:set_custom_color(153,76,0)
    elif brightness__1_to_9 == 4:set_custom_color(204,102,0)
    elif brightness__1_to_9 == 5:set_custom_color(255,128,0)
    elif brightness__1_to_9 == 6:set_custom_color(255,153,51)
    elif brightness__1_to_9 == 7:set_custom_color(255,178,102)
    elif brightness__1_to_9 == 8:set_custom_color(255,204,153)
    elif brightness__1_to_9 == 9:set_custom_color(255,229,204)

def set_yellow(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(51,51,0)
    elif brightness__1_to_9 == 2:set_custom_color(102,102,0)
    elif brightness__1_to_9 == 3:set_custom_color(153,153,0)
    elif brightness__1_to_9 == 4:set_custom_color(204,204,0)
    elif brightness__1_to_9 == 5:set_custom_color(255,255,0)
    elif brightness__1_to_9 == 6:set_custom_color(255,255,51)
    elif brightness__1_to_9 == 7:set_custom_color(255,255,102)
    elif brightness__1_to_9 == 8:set_custom_color(255,255,153)
    elif brightness__1_to_9 == 9:set_custom_color(255,255,204)

def set_lime(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(25,51,0)
    elif brightness__1_to_9 == 2:set_custom_color(51,102,0)
    elif brightness__1_to_9 == 3:set_custom_color(76,153,0)
    elif brightness__1_to_9 == 4:set_custom_color(102,204,0)
    elif brightness__1_to_9 == 5:set_custom_color(128,255,0)
    elif brightness__1_to_9 == 6:set_custom_color(153,255,51)
    elif brightness__1_to_9 == 7:set_custom_color(178,255,102)
    elif brightness__1_to_9 == 8:set_custom_color(204,255,153)
    elif brightness__1_to_9 == 9:set_custom_color(229,255,204)

def set_green(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(0,51,0)
    elif brightness__1_to_9 == 2:set_custom_color(0,102,0)
    elif brightness__1_to_9 == 3:set_custom_color(0,153,0)
    elif brightness__1_to_9 == 4:set_custom_color(0,204,0)
    elif brightness__1_to_9 == 5:set_custom_color(0,255,0)
    elif brightness__1_to_9 == 6:set_custom_color(51,255,51)
    elif brightness__1_to_9 == 7:set_custom_color(102,255,102)
    elif brightness__1_to_9 == 8:set_custom_color(153,255,153)
    elif brightness__1_to_9 == 9:set_custom_color(204,255,204)

def set_teel(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(0,51,25)
    elif brightness__1_to_9 == 2:set_custom_color(0,102,51)
    elif brightness__1_to_9 == 3:set_custom_color(0,153,76)
    elif brightness__1_to_9 == 4:set_custom_color(0,204,102)
    elif brightness__1_to_9 == 5:set_custom_color(0,255,128)
    elif brightness__1_to_9 == 6:set_custom_color(51,255,153)
    elif brightness__1_to_9 == 7:set_custom_color(102,255,178)
    elif brightness__1_to_9 == 8:set_custom_color(153,255,204)
    elif brightness__1_to_9 == 9:set_custom_color(204,255,229)

def set_lightblue(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(0,51,51)
    elif brightness__1_to_9 == 2:set_custom_color(0,102,102)
    elif brightness__1_to_9 == 3:set_custom_color(0,153,153)
    elif brightness__1_to_9 == 4:set_custom_color(0,204,204)
    elif brightness__1_to_9 == 5:set_custom_color(0,255,255)
    elif brightness__1_to_9 == 6:set_custom_color(51,255,255)
    elif brightness__1_to_9 == 7:set_custom_color(102,255,255)
    elif brightness__1_to_9 == 8:set_custom_color(153,255,255)
    elif brightness__1_to_9 == 9:set_custom_color(204,255,255)

def set_cyan(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(0,25,51)
    elif brightness__1_to_9 == 2:set_custom_color(0,51,102)
    elif brightness__1_to_9 == 3:set_custom_color(0,76,153)
    elif brightness__1_to_9 == 4:set_custom_color(0,102,204)
    elif brightness__1_to_9 == 5:set_custom_color(0,128,255)
    elif brightness__1_to_9 == 6:set_custom_color(51,153,255)
    elif brightness__1_to_9 == 7:set_custom_color(102,178,255)
    elif brightness__1_to_9 == 8:set_custom_color(153,204,255)
    elif brightness__1_to_9 == 9:set_custom_color(204,229,255)

def set_blue(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(0,0,51)
    elif brightness__1_to_9 == 2:set_custom_color(0,0,102)
    elif brightness__1_to_9 == 3:set_custom_color(0,0,153)
    elif brightness__1_to_9 == 4:set_custom_color(0,0,204)
    elif brightness__1_to_9 == 5:set_custom_color(0,0,255)
    elif brightness__1_to_9 == 6:set_custom_color(51,51,255)
    elif brightness__1_to_9 == 7:set_custom_color(102,102,255)
    elif brightness__1_to_9 == 8:set_custom_color(153,153,255)
    elif brightness__1_to_9 == 9:set_custom_color(204,204,255)

def set_blueish(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(25,0,51)
    elif brightness__1_to_9 == 2:set_custom_color(51,0,102)
    elif brightness__1_to_9 == 3:set_custom_color(76,0,153)
    elif brightness__1_to_9 == 4:set_custom_color(102,0,204)
    elif brightness__1_to_9 == 5:set_custom_color(127,0,255)
    elif brightness__1_to_9 == 6:set_custom_color(153,51,255)
    elif brightness__1_to_9 == 7:set_custom_color(178,102,255)
    elif brightness__1_to_9 == 8:set_custom_color(204,153,255)
    elif brightness__1_to_9 == 9:set_custom_color(229,204,255)

def set_purple(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(51,0,51)
    elif brightness__1_to_9 == 2:set_custom_color(102,0,102)
    elif brightness__1_to_9 == 3:set_custom_color(153,0,153)
    elif brightness__1_to_9 == 4:set_custom_color(204,0,204)
    elif brightness__1_to_9 == 5:set_custom_color(255,0,255)
    elif brightness__1_to_9 == 6:set_custom_color(255,51,255)
    elif brightness__1_to_9 == 7:set_custom_color(255,102,255)
    elif brightness__1_to_9 == 8:set_custom_color(255,153,255)
    elif brightness__1_to_9 == 9:set_custom_color(255,204,255)

def set_pink(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    if brightness__1_to_9 == 1:set_custom_color(51,0,25)
    elif brightness__1_to_9 == 2:set_custom_color(102,0,51)
    elif brightness__1_to_9 == 3:set_custom_color(153,0,76)
    elif brightness__1_to_9 == 4:set_custom_color(204,0,102)
    elif brightness__1_to_9 == 5:set_custom_color(255,0,127)
    elif brightness__1_to_9 == 6:set_custom_color(255,51,153)
    elif brightness__1_to_9 == 7:set_custom_color(255,102,178)
    elif brightness__1_to_9 == 8:set_custom_color(255,153,204)
    elif brightness__1_to_9 == 9:set_custom_color(255,204,229)

def set_graywhite(brightness__1_to_9):
    if brightness__1_to_9 < 1 or brightness__1_to_9 > 9:raise ValueError("Brightness has to be set between 1 and 9")
    elif brightness__1_to_9 == 1:set_custom_color(0,0,0)
    elif brightness__1_to_9 == 2:set_custom_color(32,32,32)
    elif brightness__1_to_9 == 3:set_custom_color(64,64,64)
    elif brightness__1_to_9 == 4:set_custom_color(96,96,96)
    elif brightness__1_to_9 == 5:set_custom_color(128,128,128)
    elif brightness__1_to_9 == 6:set_custom_color(160,160,160)
    elif brightness__1_to_9 == 7:set_custom_color(192,192,192)
    elif brightness__1_to_9 == 8:set_custom_color(224,224,224)
    elif brightness__1_to_9 == 9:set_custom_color(255,255,255)