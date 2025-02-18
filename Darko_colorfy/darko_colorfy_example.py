import darko_colorfy as colors
from time import sleep

colors.random_colors()
print(f"{colors.red} {colors.green} {colors.blue} {colors.rgb} {colors.hex}")
sleep(5)
colors.reset_colors()

colors.random_colors(("g","b"))
print(f"{colors.red} {colors.green} {colors.blue} {colors.rgb} {colors.hex}")
sleep(5)
colors.reset_colors()

colors.random_colors(("r"))
print(f"{colors.red} {colors.green} {colors.blue} {colors.rgb} {colors.hex}")
sleep(5)
colors.reset_colors()

while True:
    print(f"{colors.red} {colors.green} {colors.blue} {colors.rgb} {colors.hex}")
    colors.advance_rainbow_grad()
    sleep(0.01)