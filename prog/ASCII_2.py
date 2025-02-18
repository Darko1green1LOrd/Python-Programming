import re
def checker():
    global i,v
    v,i="",input("Zadaj Znak: ")
    if not re.match(r"^[A-Za-z]+$", i):(print("Letters Only"),checker())
    if not len(i) == 1:(print("Must be 1 long"),checker())
    if i.isupper() == 1:v=ord(i)+32
    elif i.islower() == 1:v=ord(i)-32
checker()
print(f"{chr(v)}")
