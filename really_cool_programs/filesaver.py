from sys import argv,exit
from os.path import exists,isfile,basename

print(
'''
  _____             _
 |  __ \           | |
 | |  | | __ _ _ __| | _____
 | |  | |/ _` | '__| |/ / _ |
 | |__| | (_| | |  |   < (_) |
 |_____/ \__,_|_|  |_|\_\___/
 |  ____(_) |
 | |__   _| | ___  ___  __ ___   _____ _ __
 |  __| | | |/ _ \/ __|/ _` \ \ / / _ \ '__|
 | |    | | |  __/\__ \ (_| |\ V /  __/ |
 |_|    |_|_|\___||___/\__,_| \_/ \___|_|


This script can copy bytes of any file (exe,png....... all types of files) and creates python file that recreates the file you selected
useful for making python files create files they need

Usage:
python3 filesaver.py path_to_file or dynamic location

Examples :
python3 filesaver.py /home/kubuntu/Dokumenty/file.png/
python3 filesaver.py file.png
''') #This website was used to generate that ascii art text https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
Filedir = ""


def createf(f_bytes,fileloc,filename):
    scr=(fileloc.split(filename)[0]+(filename+" builder.py").replace(" ","_"))
    with open(scr, 'w') as f:
        f.writelines(f'''
with open('{filename}', 'wb') as g:
    g.write({f_bytes})
print('Done')
''')
    print("Done")


try:
    argv[1];del argv[0:1]
    for each in argv:Filedir+=f"{each} "
    Filedir=Filedir.rstrip()

    if exists(Filedir) and isfile(Filedir):
        with open(Filedir, 'rb') as getbytes:
            createf(getbytes.read(),Filedir,basename(Filedir))
    else:exit(f"File {Filedir} doesnt exist, exitting")
except IndexError:
    exit("No file selected, exitting")
