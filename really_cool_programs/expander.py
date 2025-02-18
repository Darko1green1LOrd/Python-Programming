import os.path

filename = input("Welcome to Darko s text expander made to troll copy paste train texts\n\nThis adds X characters to each character in text, but doesnt change how they look\nhttps://wordcounter.net/ can be used to check the output\nthis can only see files in the same folder as the python script is in\n\nPlease specify file to expand text in\nMake sure to specify if its .txt or whatever filetype it is\nAlso , capital letters matter\nExample: filE.txt\n\nFile: ")


file_existing = os.path.exists(filename)
if file_existing == True:
    pass
else:
    print("Specified file doesnt exist, exitting")
    exit()


file = open(filename, "r")
string = (file.read())

invischar = "឵"
stringletters = []
print(f"\nCurrent Length: {len(string)-1}")
valid = False

while not valid:
    try:
        multiplier = int(input("\nHow many characters to add to each character ? (Number): "))
        valid = True
    except ValueError:
        print("Please only enter numbers")
for letter in string:
    stringletters.append(letter+invischar*multiplier)
del stringletters[-1]
string = ""
for x in stringletters:
    string += ""+x
print(f"\nNew Length: {len(string)}")

checker = input("\nApply changes?\nAnswer Y or N: ").lower()
if checker == "y":
    with open(filename, 'w') as f:
        f.write(string)
elif checker == "n":exit()
else:print("Please enter Y or N.")
