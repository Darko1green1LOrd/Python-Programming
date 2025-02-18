import random
base,inp="",input("Type Something: ")
chars = list(inp.strip(" "))
random.shuffle(chars)
base ="".join(chars)
print(f"{base}")
