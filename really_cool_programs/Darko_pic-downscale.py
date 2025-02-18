class imports:
    def __init__(self):
        global path,system,walk,messagebox,tk,ttk,askopenfilename,askdirectory,Image,UnidentifiedImageError,search,exit,executable,check_call,check_output,CalledProcessError,execv,argv
        from os import path,system,remove,walk,execv
        from sys import platform,exit,executable,argv
        from re import search
        from subprocess import check_call,check_output,CalledProcessError
        try:
            if platform == "linux" or platform == "linux2":
                check_output("which pip", shell=True, text=True)
            from tkinter import messagebox
            import tkinter as tk
            import tkinter.ttk as ttk
            from tkinter.filedialog import askopenfilename,askdirectory
            from PIL import Image,UnidentifiedImageError

        except Exception as e:
            #print(f"{type(e)}\n{e}\n")
            if platform == "win32":self.windows_e(e)
            elif platform == "linux" or platform == "linux2":self.linux_e(e)
            else:
                exit(f"Vyskytla sa chyba, automatická oprava nemožná lebo máte neznámy operačný systém\nChyba:\n\n{e}")


    def linux_e(self,errormsg):
        def inst(packname,instcmd):
            askinst = input(f"Chýba vám {packname} Chcete ho nainštalovať automaticky?\nY/N: ")
            if askinst.lower() == "y":
                system(instcmd)
                execv(executable, ['python3'] + argv)
            elif askinst.lower() == "n":exit(f"\nPríkaz čo môžete použit na manuálnu inštaláciu:\n{instcmd}")
            else:print("\nProsím napíšte Y alebo N");inst(packname,instcmd)

        if type(errormsg) == ModuleNotFoundError:
            modulename=search("No module named '(.*)'", str(errormsg)).group(1)
            if modulename == "tkinter":inst(modulename,"sudo apt update&&sudo apt --yes install python3-tk")
            if modulename == "PIL":inst(modulename,"pip install Pillow")
        if type(errormsg) == subprocess.CalledProcessError:
            if str(errormsg) == "Command 'which pip' returned non-zero exit status 1.":inst("pip","sudo apt update&&sudo apt --yes install python3-pip")

    def windows_e(self,errormsg):
        def inst(packname,packinst):
            askinst = messagebox.askyesno(title="Image Shrinker", message=f"Chýba vám {packname}\nChcete ho nainštalovať automaticky?")
            try:
                if askinst:check_call([executable, "-m", "pip", "install", packinst])
                else:
                    messagebox.showinfo(title="Image Shrinker", message=f"Príkaz čo môžete použit na manuálnu inštaláciu:\npip install {packinst}")
                    exit("")

            except Exception as e:
                messagebox.showinfo(title="Image Shrinker", message=f"Vyskytla sa chyba\n\nPríkaz čo môžete použit na manuálnu inštaláciu:\n{packinst}\n\nChyba:\n{e}")
                exit(f"Chyba: {e}")

        if type(errormsg) == ModuleNotFoundError:
            modulename=search("No module named '(.*)'", str(errormsg)).group(1)
            if modulename == "tkinter":exit("Chýba vám tkinter")
            if modulename == "PIL":inst(modulename,"Pillow")

imports()
perc = 0

class Gui:
    def __init__(self):
        self.overwrite = False
        self.overwrite_ask = True

        self.maing=self.cmaingui("Image Shrinker",1100,500)
        self.runfunc=self.main_display(self.maing.mainf)
        self.maing.maingui.protocol("WM_DELETE_WINDOW", self.closeall)
        self.maing.maingui.bind("<Map>", self.hs_controller)
        self.maing.maingui.bind("<Unmap>", self.hs_controller)
        self.maing.maingui.bind("<Configure>", self.move_controller)
        self.create_controller()
        self.maing.mainf.pack(side="top", fill="both", expand=True)

        self.maing.maingui.mainloop()


    def closeall(self):
        self.maing.maingui.destroy()
        try:self.minibell.destroy()
        except Exception:pass
        try:self.contr.destroy()
        except Exception:pass

    def hs_controller(self,var):
        if self.maing.maingui.state() == "iconic":self.contr.wm_withdraw()
        else:self.contr.wm_deiconify()

    def move_controller(self,var):
        self.contr.geometry(f"+{int(1100+self.maing.maingui.winfo_x())}+{(int(self.maing.maingui.winfo_y()))}")
        self.contr.wm_deiconify()


    def create_controller(self):
        try:self.contr.destroy()
        except Exception:pass
        self.contr = tk.Tk()
        self.contr.title("Ovládač")
        self.contr.geometry("150x500")
        self.contr.resizable(False, False)
        self.contr.overrideredirect(1)
        self.contr.config(bg="#1a1a1a")

        self.contrf = tk.Frame(self.contr,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")

        controls = tk.Frame(self.contrf,bg="#2e2d2d")
        contr_panel_shrink = tk.Button(controls, text ='Zmenšiť', command = self.run,width=8,bg="#4edb1a",fg="black",activebackground='#68e83a',activeforeground="#1c1c1c",bd=0)
        contr_panel_clear = tk.Button(controls, text ='Vyčistiť', command = self.clear,width=8,bg="#db910f",fg="black",activebackground='#e8a738',activeforeground="#1c1c1c",bd=0)
        contr_panel_shrink.grid(row=0,pady=10)
        contr_panel_clear.grid(row=1)
        controls.grid(row=0,column=0,padx=12,pady=10)

        toggles = tk.Frame(self.contrf,bg="#2e2d2d")
        self.ow_ask_toggle = tk.Button(toggles, text ='Opýtať sa\nPred\nPrepísaním', command = lambda: self.cont_toggle("a",self.ow_ask_toggle),width=8,bg="#8aff7d",activebackground='#46fa32',activeforeground="#1c1c1c")
        self.ow_ask_toggle.grid(row=1,pady=5)
        self.ow_ask_toggle.grid_remove()
        self.overwrite_toggle = tk.Button(toggles, text ='Prepísať\nSúbor', command = lambda: self.cont_toggle("o",self.overwrite_toggle,self.ow_ask_toggle),width=8,bg="#ff7d7d",activebackground='#fa3232',activeforeground="#1c1c1c")
        self.overwrite_toggle.grid(row=0)
        toggles.grid(row=1,column=0)
        self.contrf.pack(side="top", fill="both", expand=True, padx=15, pady=15)

    def run(self):
        done = False
        run = True
        def deletion():
            for each in self.runfunc.picture.fileframes:
                ind = self.runfunc.picture.fileframes.index(each)
                fileloc = self.runfunc.picture.sfiles[ind].get()
                try:
                    with Image.open(fileloc) as isimage:pass
                except UnidentifiedImageError:
                    self.runfunc.picture.pic_delline(each)
                    deletion()
        deletion()
        for each in self.runfunc.picture.sfiles:
            fileloc = each.get()
            img = Image.open(fileloc)

            w,h = img.width,img.height
            neww,newh = w-(int(perc)*(w//100)),h-(int(perc)*(h//100))

            newimg = img

            newimg.thumbnail((neww,newh), Image.LANCZOS)
            actual_neww,actual_newh = newimg.width,newimg.height

            if self.overwrite:
                if self.overwrite_ask:
                    ask = messagebox.askyesno(title="Image Shrinker", message="Máte zapnuté Prepisovanie Súborov\n\nNamiesto vytvorenia kópie s velkostou v názve\nbudú prepísané originálne obrázky\n\nChcete pokračovať?")
                    if not ask:run = False
            else:
                fileloc = path.join(path.split(fileloc)[0],f"{path.splitext(path.split(fileloc)[1])[0]}-resized_{actual_neww}x{actual_newh}{path.splitext(fileloc)[1]}")
            if run:
                try:
                    newimg.save(fileloc)
                    newimg.close()
                    img.close()
                    done = True
                except OSError:
                    print(f"{path.split(fileloc)[1]} Has been converted to .png To keep Alpha Layer")
                    fileloc = f"{path.splitext(fileloc)[0]}.png"
                    newimg.save(fileloc)
                    done = True
                if done:messagebox.showinfo(title="Image Shrinker", message=f"Hotovo")
                else:messagebox.showinfo(title="Image Shrinker", message=f"Nemáte v zozname žiadny obrázok")

    def clear(self):
        self.runfunc.picture.pic_clear()

    def cont_toggle(self,tp,button,window=None):
        if tp == "o":self.overwrite = not self.overwrite;var=self.overwrite
        if tp == "a":self.overwrite_ask = not self.overwrite_ask;var=self.overwrite_ask
        if var:
            if window != None:window.grid()
            button.config(bg="#8aff7d",activebackground='#46fa32')
        else:
            if window != None:window.grid_remove()
            button.config(bg="#ff7d7d",activebackground='#fa3232')

    class cmaingui:
        def __init__(self,name,geow,geoh):
            self.maingui = tk.Tk()
            self.maingui.title(name)
            y = (self.maingui.winfo_screenheight()/2) - (500/2)
            self.maingui.geometry(f"{geow}x{geoh}+{0}+{(int(y))}")
            self.maingui.resizable(False, False)
            self.maingui.config(bg="#1a1a1a")

            self.mainf = tk.Frame(self.maingui,width=geow,height=geoh)


    class main_display:
        def __init__(self,owner):
            picframe = self.sf(owner)
            self.picture=self.files(picframe.frame)
            picframe.update()



        class files:
            def __init__(self,owner):
                self.pct=owner
                self.picture_frame = tk.Frame(owner,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
                self.pic_mainf = tk.Frame(self.picture_frame,bg="#2e2d2d")
                self.pic_filef = tk.Frame(self.picture_frame,bg="#2e2d2d")
                self.picture_frame.grid(row=2,column=0,sticky="w",padx=10,pady=10)
                self.pic_mainf.grid(row=1,column=0,sticky="w")
                self.pic_filef.grid(row=6,column=0,sticky="w")

                self.tc_maintext = tk.Label(self.picture_frame, text=f"Súbory", font='Helvetica 20',bg="#2e2d2d",fg="#e3e3e3").grid(row=0,column=0,ipady=10,sticky="w")
                def volume_change(*args):
                    global perc
                    perc = self.pic_percentage.get()
                pic_resize = tk.Label(self.pic_mainf, text="Zmenšiť o ", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3").grid(row=1,column=0)
                self.pic_percentage=ttk.Combobox(self.pic_mainf, values=list(range(1, 100)),width=5,state = "readonly")
                self.pic_percentage.set(0)
                self.pic_percentage.bind('<<ComboboxSelected>>', volume_change)
                self.pic_percentage.grid(row=1,column=1)
                pic_perc = tk.Label(self.pic_mainf, text=" %", font='15',bg="#2e2d2d",fg="#e3e3e3").grid(row=1,column=2,sticky="w")

                pic_opentext = tk.Label(self.pic_mainf, text="Otvoriť: ", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3").grid(row=3,column=0,ipady=10,sticky="w")
                pic_fileopen = tk.Button(self.pic_mainf, text ='Súbor',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = self.file_open)
                pic_folderopen = tk.Button(self.pic_mainf, text ='Priečinok',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = self.folder_open)
                pic_fileopen.grid(row=3,column=1,sticky="w",padx=4)
                pic_folderopen.grid(row=3,column=2,sticky="w",padx=4)

                self.fileframes,self.sfiles,self.files_count=[],[],0

                self.sc_add_line("")
                self.pic_filef.update()
                self.pic_clear()

            def file_open(self):
                loc = askopenfilename()
                if loc != "" and isinstance(loc, str):
                    self.sc_add_line(loc)

            def folder_open(self):
                loc = askdirectory()
                if loc != "" and isinstance(loc, str):
                    for each in walk(loc):
                        for item in each[2]:
                            self.sc_add_line(path.join(each[0],item))

            def sc_add_line(self,giventext):
                filelist_subf = tk.Frame(self.pic_filef,bg="#2e2d2d")
                self.fileframes.append(filelist_subf)

                entry_text = tk.StringVar()
                filelist_subf.grid(row=self.files_count+2,column=0,sticky='w')
                pic_loc = tk.Entry(filelist_subf,width=110,bg="#474646",fg="#e3e3e3",textvariable=entry_text)
                entry_text.set(giventext)
                self.sfiles.append(pic_loc)

                def delfunc():
                    var = self.fileframes.index(filelist_subf)
                    self.fileframes[var].destroy()
                    del self.fileframes[var]
                    del self.sfiles[var]
                    self.files_count-=1
                pic_delb = tk.Button(filelist_subf, text ='Del',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = delfunc)

                pic_loc.grid(row=self.files_count+2,column=0,padx=4)
                pic_delb.grid(row=self.files_count+2,column=1,padx=4,pady=2)

                self.files_count+=1

            def pic_clear(self):
                for each in self.fileframes:
                    each.destroy()
                    self.pic_filef.update()
                self.fileframes = []
                self.sfiles = []
                self.files_count = 0

            def pic_delline(self,line):
                var = self.fileframes.index(line)
                self.fileframes[var].destroy()
                self.pic_filef.update()
                del self.fileframes[var]
                del self.sfiles[var]
                self.files_count-=1


        class sf:
            def __init__(self, master):
                style=ttk.Style()
                style.theme_use('classic')
                style.configure("Vertical.TScrollbar", background="#62c78a", bordercolor="#62c78a", arrowcolor="#62c78a",troughcolor="#616060")

                self.vscrollbar = self.asb(master)
                self.vscrollbar.grid(row=0, column=1, sticky="n"+"s")
                self.hscrollbar = self.asb(master, orient="horizontal")
                self.hscrollbar.grid(row=1, column=0, sticky="e"+"w")

                self.canvas = tk.Canvas(master, yscrollcommand=self.vscrollbar.set,xscrollcommand=self.hscrollbar.set)
                self.canvas.grid(row=0, column=0, sticky="n"+"s"+"e"+"w")
                self.canvas.config(bg="#1a1a1a")

                self.vscrollbar.config(command=self.canvas.yview)
                self.hscrollbar.config(command=self.canvas.xview)

                master.grid_rowconfigure(0, weight=1)
                master.grid_columnconfigure(0, weight=1)

                self.frame = tk.Frame(self.canvas)
                self.frame.rowconfigure(1, weight=1)
                self.frame.columnconfigure(1, weight=1)
                self.frame.config(bg="#1a1a1a")
                self.frame.bind("<Configure>", self.reset_scrollregion)

            def update(self):
                self.canvas.create_window(0, 0, anchor="nw", window=self.frame)
                self.frame.update_idletasks()
                self.canvas.config(scrollregion=self.canvas.bbox("all"))

                if self.frame.winfo_reqwidth() != self.canvas.winfo_width():
                    self.canvas.config(width = self.frame.winfo_reqwidth())
                if self.frame.winfo_reqheight() != self.canvas.winfo_height():
                    self.canvas.config(height = self.frame.winfo_reqheight())
            def reset_scrollregion(self, event):
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))

            class asb(ttk.Scrollbar):
                def set(self, x, y):
                    if float(x) <= 0.0 and float(y) >= 1.0:
                        self.tk.call("grid", "remove", self)
                    else:
                        self.grid()
                    ttk.Scrollbar.set(self, x, y)

class start:
    def __init__(self):
        Gui()


try:start()
except Exception as e:
    messagebox.showinfo(title="SOS Zvonček", message=f"Chyba:\n{e}")
    exit(f"Chyba: {e}")
