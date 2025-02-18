import random
passw=""
for var in range(9):
    if 0 <= var <= 2:
        passw+=chr(random.randrange(65,90))
    elif 3 <= var <= 4:
        passw+=chr(random.randrange(48,57))
    elif 5 <= var <= 7:
        passw+=chr(random.randrange(97,122))
print(passw)
