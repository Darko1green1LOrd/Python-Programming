def func():
    global inc1, inc2, i3
    inc1 = ""
    inc2 = ""
    i3 = ""
    if len(i1) < len(i2):
        inc1 = i1
        for i in range(len(i2)):
            if i+1 <= len(i1):
                inc2 += ""+i2[i]
            if i+1 > len(i1):
                i3 += ""+i2[i]
    else:
        inc1 = i2
        for i in range(len(i1)):
            if i+1 <= len(i2):
                inc2 += ""+i1[i]
            if i+1 > len(i2):
                i3 += ""+i1[i]

def askuser():
    global i1, i2, incorrect
    incorrect = False
    i1 = input(f"\nWrite Something: ")
    i2 = input(f"\nWrite Something: ")
    if len(i1) != len(i2):
        incorrect = True
        func()



askuser()
if incorrect == False:
    print(f"{i1} {i2}")
else:
    print(f"{inc1} {inc2} {i3}")
