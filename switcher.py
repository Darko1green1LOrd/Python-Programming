string = input("Type Something here.\n")
stringwords = []
for letter in string:
    stringwords.append(letter)
for i in range(len(stringwords)):
    if stringwords[i] == 'o':
        stringwords[i] = '*'

    if stringwords[i] == 'O':
        stringwords[i] = '*'
string = ""
for x in stringwords:
    string += ""+x
print(string)
