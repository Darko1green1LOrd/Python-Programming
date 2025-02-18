import time
import math
import re


equation = "n*n+4*(n-1)+a[n-2]+a[n-3]"    #I
automatic = 0   #I
n = 3  #I
a = [5,8]  #I
increment = 1   #I



#recursive math
#
#I = Input
#If automatic is 0  press enter to continue
#
#For number before n do
#(n-1), (n-2) ...
#Zlomky = (Top)/(Bottom)
#Sinus = math.sin(number)
#Cosinus = math.cos(number)
#Tangens = math.tan(number)
#Na druhú, tretiu atd = number**number   example = 5**2
#a = previous outputs
#n = starting value
#use  .  instead of  ,   for stuff like 0.5
#to clear a just do []

#Pre použite predošlého výsledku =  a[n-2]  a[n-3]  a[n-4]  a[n-5] ...
#a[n-2] je o 1 dozadu
#Ak sa budú používat predošlé výsledky musí sa zmenit a aj n
#v štartovných hodnotách
#Pre pridanie viac čísel do štartovnej hodnoty a = [5,6,8,9]
#n musí byt o 1 viac než počet čisel v a napr : 
#a = [4,6]   
#n = 3




def calc():
    global n, increment, a
    progress = equation
    for match in re.findall(r'(a\[n-\d+])', progress):
        #print(f'Progress: {progress}, Match: {match}, Eval: {str(eval(match))}')
        progress = progress.replace(match, str(eval(match)), 1)
        #print(progress)
    equation_progress2 = progress.replace("n", f"{n}")
    output = eval(equation)
    a.insert(n,output)
    print(f'A{n} = {equation_progress2} = {output}')
    n=n+increment


while True:
    calc()
    if automatic == 1:
        time.sleep(0.1)
    else:
        input("")