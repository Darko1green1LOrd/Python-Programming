from os import path,rmdir,remove,mkdir,listdir,walk,get_terminal_size
from sys import platform
from time import sleep
from math import floor,log,pow
try:from psutil import disk_partitions
except ImportError:raise ImportError("This program requires psutil\nuse this command to install it\npip install psutil")

if platform == "win32":plat = "win"
elif platform == "linux" or platform == "linux2":plat = "lin"
if plat == "win":
    try:from curses import wrapper
    except ImportError:raise ImportError("This program requires curses(It isnt standard library for windows)\nuse this command to install it\npip install windows-curses")
    d,r,g,y,b,m,c,w="","","","","","","",""
elif plat == "lin":
    from curses import wrapper
    try:from colorama import Fore
    except ImportError:raise ImportError("This program requires colorama\nuse this command to install it\npip install colorama")
    d,r,g,y,b,m,c,w=Fore.BLACK,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN,Fore.WHITE



print(f'''
{g}
 /$$$$$$$                      /$$
| $$__  $$                    | $$
| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$
| $$  | $$ |____  $$ /$$__  $$| $$  /$$/ /$$__  $$
| $$  | $$  /$$$$$$$| $$  \__/| $$$$$$/ | $$  \ $$
| $$  | $$ /$$__  $$| $$      | $$_  $$ | $$  | $$
| $$$$$$$/|  $$$$$$$| $$      | $$ \  $$|  $$$$$$/
|_______/  \_______/|__/      |__/  \__/ \______/

 /$$   /$$           /$$
| $$  | $$          | $$
| $$  | $$  /$$$$$$$| $$$$$$$
| $$  | $$ /$$_____/| $$__  $$
| $$  | $$|  $$$$$$ | $$  \ $$
| $$  | $$ \____  $$| $$  | $$
|  $$$$$$/ /$$$$$$$/| $$$$$$$/
 \______/ |_______/ |_______/

  /$$$$$$
 /$$__  $$
| $$  \__/  /$$$$$$   /$$$$$$  /$$   /$$
| $$       /$$__  $$ /$$__  $$| $$  | $$
| $$      | $$  \ $$| $$  \ $$| $$  | $$
| $$    $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$$
 \______/  \______/ | $$____/  \____  $$
                    | $$       /$$  | $$
                    | $$      |  $$$$$$/
                    |__/       \______/

{y}This script checks for new usbs and if it hasnt copied its files yet , then it does so.{w}
''') #This website was used to generate that ascii art text https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

config_file_name = "Darko_usbcopy.duccfg"
if path.isdir(config_file_name):rmdir(config_file_name)
if path.exists(config_file_name):
    cfg_loc = path.join(path.dirname(path.realpath(__file__)),config_file_name)

else:
    cfg_loc = input(f"{c}Cannot find the configuration file\n{y}If you have a configuration file but its renamed or in different folder , please enter its path and press enter\nIf you dont, dont type in anything and just {m}press enter{y} to generate a new one\n{r}WARNING: If you select a file with same location and name as folder , the folder will get deleted\nExample: to create File.exe file File.exe,folder will get deleted{w}\n{g}File: {w}").strip()

    if cfg_loc == "":cfg_loc = None
    else:
        if not cfg_loc.endswith('.duccfg'): raise Exception(f"{r}Invalid file extension , it has to be .duccfg{w}")
        if path.isdir(config_file_name): raise Exception(f"{r}You have given path to folder , not to a file.{w}")
        elif path.exists(config_file_name): raise Exception(f"{r}File doesnt exist.{w}")

if cfg_loc == None:
    interval_given = abs(float(input(f"\n{y}Please enter scan interval value\nThis determines how often will the program checks usbs to see if any new one is plugged in\nThe interval is in seconds, you can also do stuff like 1.2 or 0.4{w}\n{g}Scan Interval: {w}")))

    savefolder_given = input(f"\n{c}Do you want to set custom save folder?\n{y}This determines where the program checks for already copied usbs\nand also copies new detected usb data here\nif you dont want to specify a folder just {m}press enter{y} and the folder will be created in the same folder as the program\nif you select already existing folder it will use that\nRelative file locations to the python file work aswell\n{r}WARNING: If you select a file with same location and name as file , the file will get deleted\nExample: to create File.exe,folder File.exe file will get deleted{w}\n{g}Path to save folder: {w}").strip()
    if savefolder_given == "":savefolder_given = "None"

    limit_given = input(f"\n{y}If you want to copy for example only maximally {m}5 MB{y} files then you type here 5 MB\nIf you dont want any limit , just press enter withouth typing anything in\nyou can also do stuff like 1.2 or 0.4\n{m}Accepted formats :\nB {c}(Byte)\n{m}KB {c}(Kilo Byte)\n{m}MB {c}(Mega Byte)\n{m}GB {c}(Giga Byte)\n{m}TB {c}(Tera Byte)\n{m}PB {c}(Peta Byte)\n{m}EB {c}(Exa Byte)\n{m}ZB {c}(Zetta Byte)\n{m}YB {c}(Yotta Byte){w}\n{g}File Size Limit: {w}").strip()
    if limit_given == "":limit_given = "None"
    else:
        cfg_check = limit_given.split(" ",1)
        try:float(cfg_check[0])
        except:raise Exception(f"{cfg_check[0]} Is not a number")
        if float(cfg_check[0]) < 0:raise Exception(f"{cfg_check[0]} Is less than allowed minimum (0)")
        if cfg_check[1].lower() not in ["b","kb","mb","gb","tb","pb","eb","zb","yb"]:raise Exception(f"{r}{limit_given[1]} Is not in B,KB,MB,GB,TB,PB,EB,ZB,YB{w}")


    wblist_given = int(input(f"\n{c}Do you want to have:\n{m}Blacklist(1) - Select what file extensions to not copy\n{y}Whitelist(2) - Only copy selected file extensions\n{b}All Filetpyes(3) - Dont filter file extensions in any way{w}\n{g}Your Input: {w}"))
    if wblist_given == 1:
        wblist_given = [input(f"\n{c}Please enter file extensions sperated with ,\n{b}Example: exe,txt,pwp{w}\n{g}Extensions: {w}"),"BL"]
    elif wblist_given == 2:
        wblist_given = [input(f"\n{c}Please enter file extensions sperated with ,\n{b}Example: exe,txt,pwp{w}\n{g}Extensions: {w}"),"WL"]
    elif wblist_given == 3:wblist_given = [""]
    else:raise Exception(f"{r}{wblist_given} Is not either one of 1,2,3{w}")


    with open(config_file_name, 'w') as f:
        f.writelines(f"#This file can be renamed but if you will rename it , program wont be able to detect it automaticly\n#and you will have to specifiy it everytime you will start it\n\n\n\n#Every config goes like this configname: configvalue\n#You need to include that space\n\n\n\nscan_interval: {interval_given}\n\n#How often will the program checks usbs to see if any new one is plugged in\n#The interval is in seconds, you can also do stuff like 1.2 or 0.4\n\n\n\nsavefolder: {savefolder_given}\n\n#This determines where the program checks for already copied usbs\nand also copies new detected usb data here\n#if set to None the folder will be created in the same folder as the program\n#if you select already existing folder it will use that\n#Relative file locations to the python file work aswell\n\n\n\nfilesize_limit: {limit_given}\n\n#If you want to copy for example only maximally 5 MB files then you type here 5 MB\n#If you dont want any limit , type None\n#you can also do stuff like 1.2 or 0.4\n#Accepted formats :\n#B  (Byte)\n#KB (Kilo Byte)\n#MB (Mega Byte)\n#GB (Giga Byte)\n#TB (Tera Byte)\n#PB (Peta Byte)\n#EB (Exa Byte)\n#ZB (Zetta Byte)\n#YB (Yotta Byte)\n\n\n\n{f'blacklist: {wblist_given[0].strip()}' if 'BL' in wblist_given else '#blacklist: pwp'}\n{f'whitelist: {wblist_given[0].strip()}' if 'WL' in wblist_given else '#whitelist: exe,txt'}\n\n#Blacklist or Whitelist\n#Only one of these can be enabled at once\n#used to specifiy which file types to copy or not copy")
    cfg_loc = path.join(path.dirname(path.realpath(__file__)),config_file_name)


with open(cfg_loc, 'r') as f:
    bl_list,wh_list = None,None
    lines = [line.strip() for line in f]
    for each in lines:
        if each.startswith("scan_interval:"):
            scan_interval = float(each.split(":",1)[1].strip())
        if each.startswith("savefolder:"):
            folder_loc = each.split(":",1)[1].strip()
        if each.startswith("filesize_limit:"):
            fs_limit = each.split(":",1)[1].strip().split(" ",1)
            if fs_limit[0] == "None":fs_limit = None
            else:fs_limit[0] = float(fs_limit[0])
        if each.startswith("blacklist:") and each.startswith("whitelist:"):raise Exception(f"Whitelist and Blacklist are on at the same time")

        if each.startswith("blacklist:"):
            bl_list = each.split(":",1)[1].strip().split(",")
        if each.startswith("whitelist:"):
            wh_list = each.split(":",1)[1].strip().split(",")

if folder_loc == "None":folder_loc = "Darko_usbcopy_f"
if path.exists(folder_loc):
    if not path.isdir(folder_loc):
        remove(folder_loc)
if not path.exists(folder_loc):mkdir(folder_loc)


#print(f"{scan_interval}\n{folder_loc}\n{fs_limit}\n{bl_list}\n{wh_list}")

def wprint(text,pos,window_var):
    window_var.addstr(pos, 0, text)
    window_var.clrtoeol()
    window_var.refresh()

def progressbar(it, prefix="", size=60, window="", pos=0):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        wprint(f"{prefix}┃{u'█'*x}{('.'*(size-x))}┃ {j}/{count}",pos,window)
    show(0)

    for i, item in enumerate(it):
        yield item
        show(i+1)


def get_bytes(path_to_file):
    with open(path_to_file, 'rb') as getbytes:
        fbytes = getbytes.read()
    return fbytes

def from_bytes(size_bytes):
    if size_bytes == 0:return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(floor(log(size_bytes, 1024)))
    p = pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def to_bytes(size_any):
    if size_any[0] == 0:return 0
    if size_any[1] == "B":return size_any[0]
    elif size_any[1] == "KB":return size_any[0]*(1000**1)
    elif size_any[1] == "MB":return size_any[0]*(1000**2)
    elif size_any[1] == "GB":return size_any[0]*(1000**3)
    elif size_any[1] == "TB":return size_any[0]*(1000**4)
    elif size_any[1] == "PB":return size_any[0]*(1000**5)
    elif size_any[1] == "EB":return size_any[0]*(1000**6)
    elif size_any[1] == "ZB":return size_any[0]*(1000**7)
    elif size_any[1] == "YB":return size_any[0]*(1000**8)

def list_files(pathvar):
    #files = [[(path.join(each[0],item)).split(pathvar)[1],path.getsize(path.join(each[0],item)),get_bytes(path.join(each[0],item))] for each in walk(pathvar) for item in each[2]]
    files = []
    def sorter(e):
        return e[1]
    for each in walk(pathvar):
        for item in each[2]:
            append = True
            fileloc = (path.join(each[0],item)).split(pathvar)[1]
            filesize = path.getsize(path.join(each[0],item))
            extension = path.splitext(fileloc)[1]

            if fs_limit != None:
                if filesize > to_bytes(fs_limit):append = False
            if bl_list != None:
                if extension[1:] in bl_list:append = False
            if wh_list != None:
                if extension[1:]  not in wh_list:append = False

            if append:
                displaysize = from_bytes(filesize)
                filebytes = get_bytes(path.join(each[0],item))
                files.append([fileloc,filesize,displaysize,filebytes])

    files.sort(key=sorter)
    return files

def list_folders(pathvar):
    folders = [each[0].split(pathvar,1)[1] for each in walk(pathvar)]
    for i,item in enumerate(folders):
        if item == "":del folders[i]
    return folders

def scanfor_usbs():
        values = []
        ignore = ["/boot","/snap","/var"]
        partitions = disk_partitions(all=False)
        for partition in partitions:
            append = True
            device = [partition.device,path.basename(partition.mountpoint),partition.mountpoint,partition.fstype,partition.opts]
            if plat == "lin":
                if partition.fstype not in ["vfat","exfat"]:append = False
                if partition.device.startswith("/dev/sda"):append = False
                if any(map(partition.mountpoint.startswith, ignore)):append = False
            elif plat == "win":
                if partition.fstype not in ["FAT32","exFAT"]:append = False
                if not partition.opts.endswith("removable"):append = False
            if append:values.append(device)

        for i,item in enumerate(values):
            if plat == "lin":values[i] = [item[1],item[2]]
            elif plat == "win":values[i] = [item[2][0],item[2]]
        return values

items = [0,1,2,3,4,5,6,7]
def terminal_gui(window):
    try:
        while True:
            ter_size = get_terminal_size()[1]
            wprint(f"Current Settings:",ter_size-10,window)
            wprint(f"Scan Interval: {scan_interval}",ter_size-9,window)
            wprint(f"Save Folder: {folder_loc}",ter_size-8,window)
            wprint("Size Limit: None" if fs_limit == None else f"Size Limit: {fs_limit[0]} {fs_limit[1]}",ter_size-7,window)
            wprint(f"Blacklist: {','.join(bl_list)}" if bl_list != None else f"Whitelist: {','.join(wh_list)}" if wh_list != None else "Blacklist/Whitelist: None",ter_size-6,window)
            wprint(f"",ter_size-5,window)
            wprint(f"",ter_size-4,window)
            wprint(f"",ter_size-3,window)
            wprint(f"",ter_size-2,window)
            wprint("Press Ctrl+C To Stop the program",ter_size-1,window)
            window.refresh()
            for each in scanfor_usbs():
                usb_path = path.join(folder_loc,each[0])
                if not path.exists(usb_path):
                    mkdir(usb_path)
                    usb_folders = list_folders(each[1])
                    for inp_folder in progressbar(usb_folders, "Vytváram Priečinky: ", 40,window,ter_size-3):
                        folder_path = path.join(usb_path,str(inp_folder)[1:] if inp_folder.startswith("/") else str(inp_folder))
                        mkdir(folder_path)
                        wprint(inp_folder[1:],ter_size-4,window)

                    usb_files = list_files(each[1])
                    for inp_file in progressbar(usb_files, "Vytváram Súbory: ", 40,window,ter_size-3):
                        usb_filepath = inp_file[0]
                        usb_displsize = inp_file[2]
                        usb_filebytes = inp_file[3]
                        file_path = path.join(usb_path,str(usb_filepath)[1:] if usb_filepath.startswith("/") else str(usb_filepath))
                        with open(file_path, 'wb') as g:
                            g.write(usb_filebytes)
                        wprint(f"{usb_filepath} ({usb_displsize})",ter_size-4,window)

            sleep(scan_interval)
    except Exception as e:raise Exception(f"{r}Error: {e}\nThis error was possibly caused if your terminal s height wasnt big enough, it needs atleast 10 Lines{w}")

try:
    wrapper(terminal_gui)
except KeyboardInterrupt:print(f"{r}Exitting{w}")
