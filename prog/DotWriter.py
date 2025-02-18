v1,i1=".",input("Write Something: ")
v2=v1*(len(i1)+1)
for i in range(len(i1)):
    print(f"{v2[(i+1):]}{i1[0:(i+1)]}")
