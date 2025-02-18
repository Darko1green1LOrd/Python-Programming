from string import ascii_lowercase
from random import choices
def randletter():return("".join(choices(ascii_lowercase,k=10)))

[print(randletter()) for i in range(10)]
