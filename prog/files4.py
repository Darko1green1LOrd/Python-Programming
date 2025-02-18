from Darkofilem import darkof
from random import choices,shuffle
from string import ascii_lowercase,ascii_uppercase
filemanager = darkof

pws,nums,big,small,repeat="",[num for num in range(0,10)],ascii_uppercase,ascii_lowercase,int(input("Amount of passwords: "))
def add(source,goal,amount):
    for each in choices(source,k=amount):goal.append(each)

for num in range(repeat):
    pw,strpw = [],""
    add(nums,pw,3)
    add(big,pw,1)
    add(small,pw,4)
    shuffle(pw)
    for each in pw:strpw+=str(each)
    pws+="\n"+strpw

output = f"-------------------------------\nAmount of Passwords: {repeat}\n{pws}\n-------------------------------\n\n"
filemanager.save("passwords.txt",output,False)
