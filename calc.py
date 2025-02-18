import sys 

c1 = float(input("Num 1\n"))
operation = (input("Znak (+ - * :)\n"))
c2 = float(input("Num 2\n"))

if operation == "+":
    output = c1+c2
elif operation == "-":
    output = c1-c2
elif operation == "*":
    output = c1*c2
elif operation == ":":
    if c2 == 0.0:
      sys.exit("Cannot divide by 0")
    output = c1/c2

print("\n",c1,"",operation,"",c2,"je",output,"\n")
