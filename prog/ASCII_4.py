base,inp="",input("Type Something: ")
for char in inp:base = base+chr(ord(char)+1)
print(f"Šifra je {base}")
