import string
base,chars,inp,add="",list(string.ascii_lowercase),input("Type Something: "),int(input("Move by amount(Number): "))
newchars = chars[-add:] + chars[:-add]
for num in range (len(inp)):base = base+chr(ord(newchars[num]))
print(f"{base}")
