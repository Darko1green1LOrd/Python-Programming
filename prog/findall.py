import re
i1=input("Text: ")
for match in re.finditer("a", i1):
    print(f"{i1[match.span()[0]:match.span()[1]]} at start {match.start()} end {match.end()}")
