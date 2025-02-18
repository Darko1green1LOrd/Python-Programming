from Darkofilem import darkof

filemanager = darkof
filemanager.save("files2_file.txt","File Created at first launch\nlaunches:\n",True,True)
var = filemanager.read("files2_file.txt")
try:addition = int(var[-1].split(' ')[1])
except:addition = 0
filemanager.save("files2_file.txt",f"\nLaunch {addition+1}",False)
for each in filemanager.read("files2_file.txt"):print(each)
