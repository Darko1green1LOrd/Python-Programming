class imports:
    def __init__(self):
        global os,exit,choice,datetime,messagebox,tk,ttk,askopenfilename,vlc,timezone,re,executable,argv,subprocess,platform,webbrowser
        import os
        from sys import platform,exit,executable,argv
        import webbrowser
        from random import choice
        from datetime import datetime
        import re
        import subprocess
        try:
            if platform == "linux" or platform == "linux2":
                subprocess.check_output("which pip", shell=True, text=True)
                subprocess.check_output("which vlc", shell=True, text=True)
            from tkinter import messagebox
            import tkinter as tk
            import tkinter.ttk as ttk
            from tkinter.filedialog import askopenfilename
            import vlc
            from pytz import timezone

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
                os.system(instcmd)
                os.execv(executable, ['python3'] + argv)
            elif askinst.lower() == "n":exit(f"\nPríkaz čo môžete použit na manuálnu inštaláciu:\n{instcmd}")
            else:print("\nProsím napíšte Y alebo N");inst(packname,instcmd)

        if type(errormsg) == ModuleNotFoundError:
            modulename=re.search("No module named '(.*)'", str(errormsg)).group(1)
            if modulename == "tkinter":inst(modulename,"sudo apt update&&sudo apt --yes install python3-tk")
            if modulename == "vlc":inst(modulename,"pip install python-vlc")
            if modulename == "pytz":inst(modulename,"pip install pytz")
        if type(errormsg) == subprocess.CalledProcessError:
            if str(errormsg) == "Command 'which pip' returned non-zero exit status 1.":inst("pip","sudo apt update&&sudo apt --yes install python3-pip")
            if str(errormsg) == "Command 'which vlc' returned non-zero exit status 1.":inst("vlc","sudo apt update&&sudo apt --yes remove vlc*&&sudo apt --yes install vlc*")

    def windows_e(self,errormsg):
        def exitmsg(msg):
            messagebox.showinfo(title="SOS Zvonček", message=msg)
            exit("")

        if type(errormsg) == ModuleNotFoundError:
            modulename=re.search("No module named '(.*)'", str(errormsg)).group(1)
            if modulename == "tkinter":exit("Chýba vám tkinter")
            if modulename == "vlc":exitmsg("Chýba vám modul python-vlc\n\nDá sa nainštalovať pomocou pip install python-vlc")
            if modulename == "pytz":exitmsg("Chýba vám modul pytz\nDá sa nainštalovať pomocou pip install pytz")
        elif type(errormsg) == FileNotFoundError and "libvlc.dll" in str(errormsg):
            ask = messagebox.askyesno(title="SOS Zvonček", message="Nemáte 64 Bitový vlc media player, ktorý je potrebný pre funkčnosť.\nChcete ho nainštalovať?")
            if ask:
                if os.path.exists("vlc-3.0.17.4-win64.exe"):
                    os.system("vlc-3.0.17.4-win64.exe")
                    os.execv(executable, ['python3'] + argv)
                else:webbrowser.open('https://get.videolan.org/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe')
            else:exit()

imports()
if platform == "win32":
    cfgname="zvoncek_cfg-win.txt"
    soundmain = vlc.Instance()
elif platform == "linux" or platform == "linux2":
    cfgname="zvoncek_cfg-lin.txt"
    soundmain = vlc.Instance("--aout pulse")
else:
    cfgname="zvoncek_cfg.txt"
    soundmain = vlc.Instance()
soundplayer = soundmain.media_player_new()

class Functions:
    def st(self,time_input):
        return datetime.strptime(time_input, "%H:%M:%S")

    def timeint(self,time_input):
        total = int(time_input.strftime('%S'))
        total += int(time_input.strftime('%M')) * 60
        total += int(time_input.strftime('%H')) * 60 * 60
        return total

    def gettime(self,timetype):
        if timetype == "TIMEZONE":
            time_var = datetime.now(timezone('Europe/Bratislava')).strftime("%H:%M:%S")
        elif timetype == "LOCAL":
            time_var = datetime.now().strftime("%H:%M:%S")
        return time_var

    def playsound(self,sound,vol):
        global soundmain,soundplayer
        if self.fe(sound):
                if type(soundplayer.get_media()) == "NoneType":soundplayer.stop()
                soundplayer.set_media(soundmain.media_new(sound))
                soundplayer.audio_set_volume(int(vol))
                soundplayer.play()
        else:messagebox.showinfo(title="SOS Zvonček", message=f"Zvuk:\n{sound}\nNeexistuje.")

    def fe(self,path):
        if os.path.exists(path) and os.path.isfile(path):return True
        else:return False

    def explore(self):
        try:
            filesel = askopenfilename()
            if self.fe(filesel): return filesel
        except Exception:return False

class Files:
    def __init__(self):
        self.fs=Functions()
    def setconfig(self,time_cfg,sound_cfg,volume_cfg,bells):
        if time_cfg=="":
            time_cfg="cfg_cas:TIMEZONE"
        if sound_cfg=="":
            sound_cfg="scfg_zvuk:"
            for each in ["Zvuky/zvuk1.mp3","Zvuky/zvuk2.mp3","Zvuky/zvuk3.mp3","Zvuky/zvuk4.mp3"]:
                if self.fs.fe(each):sound_cfg+=each+","
            if len(sound_cfg) == 10:messagebox.showinfo(title="SOS Zvonček", message=f"Nebolo možné pridať žiadny zvuk do nastavenia zukov pretože ani jeden z štyroch pôvodných zvukov sa nenašiel.\nAk si nenastavíte zvuky program nebude robiť zvuk.")
            else:sound_cfg=sound_cfg[:-1]
        if sound_cfg=="scfg_zvuk:empty":
            sound_cfg="scfg_zvuk:"
        if volume_cfg=="":
            volume_cfg="cfg_hlas:80"
        if bells=="":
            bells=""
            for each in ["7:00 Nultá Hodina","7:45 Prestávka","7:50 Prvá Hodina","8:35 Prestávka","8:40 Druhá Hodina","9:25 Prestávka","9:35 Tretia Hodina","10:20 Prestávka","10:25 Štvrtá Hodina","11:10 Prestávka","11:15 Piata Hodina","12:00 Veľká Prestávka","12:30 Šiesta Hodina","13:15 Prestávka","13:20 Siedma Hodina","14:05 Koniec --zvuk:Zvuky/zvuk4.mp3"]:
                if each.count("--zvuk:") == 1:
                    if self.fs.fe(each.split("--zvuk:", 1)[1]):
                        bells+=each+"\n"
                    else:
                        bells+=(each.replace(f"--zvuk:{each.split('--zvuk:', 1)[1]}","")).rstrip()+"\n"
                else:bells+=each+"\n"
            bells=bells.rstrip()
        if os.path.isdir(cfgname):os.rmdir(cfgname)
        with open(cfgname, 'w') as f:
                f.writelines(f"#Nastavenie SOŠ Zvončeka\n#\n#\n#Nastavenie Času:\n{time_cfg}\n#\n#TIMEZONE - použije Bratislava timezone čas\n#LOCAL - použije čas nastavený v počítači\n#\n#\n#\n#Nastavenie Zvuku:\n{sound_cfg}\n{volume_cfg}\n#\n#Názov súboru - Súbor musí byť v tom istom priečinku ako program\n#Cesta k súboru - Napr: C:\WINDOWS\system32\Ahoj.mp3\n#Nastavenie hlasitosti 0 až 125\n#Ak chcete aby program náhodne vybral z viacerých zvukov, Napíšte tam viac ciest/názvov\n#Napr:   cfg_zvuk:zvuk.mp3,Zvuky/zvuk2.mp,zvuk3.mp3\n#\n#\n#\n#Nastavenie Zvonenia:\n{bells}\n#\n#Čas Názov - Je potrebná medzera medzi časom a názvom\n#Hodiny:Minúty Názov\n#\n#\n#Pokročilejšie nastavenia:\n#Hodiny:Minúty:Sekundy Názov\n#\n#Môžete nastavit špeciálny zvuk pre konkrétny čas:\n#Hodiny:Minúty Názov --zvuk:zvuk.mp3\n#Hodiny:Minúty:Sekundy Názov --zvuk:zvuk.mp3\n#\n#Názov súboru - Súbor musí byť v tom istom priečinku ako program\n#Cesta k súboru - Napr: C:\WINDOWS\system32\Ahoj.mp3\n#\n#\n#\n#Tento súbor musí byť v tom istom priečinku ako program")
    def geticon(self): #to convert pngs to base64 : https://onlinepngtools.com/convert-png-to-base64
        icon="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"
        return icon

class Variables:
    def __init__(self):
        reset=Files()
        self.fs=Functions()
        try:self.create()
        except Exception as e:
            ask = messagebox.askyesno(title="SOS Zvonček", message=f"{cfgname} má niečo špatne nastavené alebo niaky nastavený zvuk neexistuje\n\nChcete obnoviť nastavenia na pôvodné?\n\n\nChyba:\n{e}")
            if ask:
                reset.setconfig("","","","")
                os.execv(executable, ['python3'] + argv)
            else:exit()

    def create(self):
        global configs,times,timesint,names,spsounds,getsounds,time,sounds,volume,sc_volume,time_config
        configs,times,names,timesint,spsounds,getsounds=[],[],[],[],[],0
        self.nobells=True
        with open(cfgname, 'r') as f:
            cfg_text = [line.strip() for line in f]
            for each in cfg_text:
                if each.startswith("#"):pass
                elif each.startswith("cfg"):configs.append(each)
                elif each.startswith("scfg"):
                    soundscmd=each.split(":",1)[0]+":"
                    if soundscmd != "scfg_zvuk:":raise Exception(f"Nastavenie zvukov nemá na začiatku\nscfg_zvuk:")
                    sounds = ((each.split(":",1)[1]).split(","))
                elif not each.startswith(("#","cfg","scfg")):
                    self.nobells=False
                    try:
                        if (each.split("--zvuk:", 1)[0]).count(":") == 1:
                            times.append((each.split("--zvuk:", 1)[0]).split(" ", 1)[0]+":00")
                            timesint.append(self.fs.timeint(self.fs.st((each.split("--zvuk:", 1)[0]).split(" ", 1)[0]+":00")))
                        elif (each.split("--zvuk:", 1)[0]).count(":") == 2:
                            times.append((each.split("--zvuk:", 1)[0]).split(" ", 1)[0])
                            timesint.append(self.fs.timeint(self.fs.st((each.split("--zvuk:", 1)[0]).split(" ", 1)[0])))
                        names.append((each.split("--zvuk:", 1)[0]).split(" ", 1)[0]+" "+(each.split("--zvuk:", 1)[0]).split(" ", 1)[1])
                        if each.count("--zvuk:") == 1:
                            spsounds.append(each.split("--zvuk:", 1)[1])
                        else:
                            spsounds.append("Nothing")
                    except Exception as e:
                        if type(e) == ValueError:
                            oute=re.search("time data '(.*)' does not match format '%H:%M:%S'", str(e)).group(1)
                            errormsg=f"V Nastavení zvonenia\nčas {oute}\nNemá formát hodiny:minúty:sekundy ani hodiny:minúty"
                        elif type(e) == IndexError:errormsg=f"Nemáte žiadne zvonenia nastavené"
                        else:errormsg=f"Neočakávaná chyba:\n\n{type(e)}"
                        raise Exception(errormsg)
        if self.nobells:raise Exception(f"Nemáte žiadne zvonenia nastavené")
        volume = int(configs[1].split(":",1)[1])
        sc_volume = volume
        time_config = configs[0].split(":",1)[1]
        self.verify()

    def verify(self):
        if sounds==['']:messagebox.showinfo(title="SOS Zvonček", message=f"Nemáte nastavený žiadny zvuk pre zvonenie\n\nProgram bude fungovat ale bude iba ukazovat kedy zvoní")
        else:
            for each in sounds:
                if self.fs.fe(each) == False:raise Exception(f"V Nastavení zvuky\n{each} Neexistuje.")
        for each in spsounds:
            if each != "Nothing":
                if self.fs.fe(each) == False:raise Exception(f"V Nastavení zvonenia\n{each} Neexistuje.")
        if configs[0] not in ("cfg_cas:TIMEZONE","cfg_cas:LOCAL"):raise Exception(f"{configs[0]} Není správne\nPoužitie:\ncfg_cas:TIMEZONE alebo cfg_cas:LOCAL")
        if not configs[1].startswith("cfg_hlas:"):raise Exception(f"Nastavenie hlasitosti nemá na začiatku\ncfg_hlas:")
        volumeam = configs[1][9:len(configs[1])]
        if volumeam in ([str(nm) for nm in range(0,126)]):pass
        else:raise Exception(f"V Nastavení hlasitosti:\n\n{volumeam} Je {'Nad max hodnotou 125' if int(volumeam) > 0 else 'Pod min hodnotou 0'}")

class Gui:
    def __init__(self):
        self.func=Functions()
        self.fs=Files()
        self.timet=self.soundt=self.bellt=True

        self.current_mode = True
        self.maing=self.cmaingui("SOŠ Zvonček",1100,500)
        self.mainbell=self.mode_display(self.maing.maingui)
        self.mainbell.add_button("Nastavenia",self.toggle_modes,"right")
        self.mainbell.add_button("Mini Verzia",self.create_minib,"left")
        self.maing.maingui.protocol("WM_DELETE_WINDOW", self.closeall)
        self.maing.maingui.bind("<Map>", self.hs_controller)
        self.maing.maingui.bind("<Unmap>", self.hs_controller)
        self.maing.maingui.bind("<Configure>", self.move_controller)
        self.create_controller()
        self.contr.wm_withdraw()

        self.configs=self.settings_display(self.maing.mainf)

        self.loop(self.maing.maingui)

        self.maing.maingui.mainloop()


    def loop(self,owner):
        self.configs.time.tc_change()
        actime=self.func.st(self.func.gettime(configs[0].split(":",1)[1]))
        timev=self.func.timeint(actime)
        closest_time = min(timesint, key=lambda t: t - timev if t >= timev else float("inf"))

        for num in range (len(timesint)):
            if timesint[num] == closest_time:
                if max(timesint) < timev:
                    self.mainbell.maintext.config(text = "Pre dnešok\nKoniec")
                    try:self.minitext.config(text = "Pre dnešok\nKoniec")
                    except Exception:pass
                elif timesint[num] == timev:
                    if spsounds[num] == "Nothing":
                        if sounds==['']:pass
                        else:self.func.playsound(choice(sounds),volume)
                    else:self.func.playsound(spsounds[num],volume)

                else:
                    self.mainbell.maintext.config(text = f"{names[num].split(' ', 1)[1]} ({names[num].split(' ', 1)[0]})\nZačína o {self.func.st(times[num])-actime}")
                    try:self.minitext.config(text = f"{names[num].split(' ', 1)[1]} ({names[num].split(' ', 1)[0]}) Začína o {self.func.st(times[num])-actime}")
                    except Exception:pass
        owner.after(1000, lambda: self.loop(owner))

    def toggle_modes(self):
        self.current_mode = not self.current_mode
        if self.current_mode:
            self.maing.maingui.title("SOŠ Zvonček")
            self.mainbell.bd.pack(side="top", fill="both", expand=True, padx=20, pady=20)

            self.maing.mainf.pack_forget()
            self.contr.wm_withdraw()
            try:self.minibell.wm_deiconify()
            except Exception:pass
            self.maing.maingui.attributes('-topmost',False)
        else:
            self.maing.maingui.title("SOŠ Zvonček Nastavenia")
            self.mainbell.bd.pack_forget()

            try:self.minibell.wm_withdraw()
            except Exception:pass
            self.maing.mainf.pack(side="top", fill="both", expand=True)
            self.maing.maingui.attributes('-topmost',True)

    def closeall(self):
        self.maing.maingui.destroy()
        try:self.minibell.destroy()
        except Exception:pass
        try:self.contr.destroy()
        except Exception:pass

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
        settings_save = tk.Button(controls, text ='Uložiť', command = self.cont_save,width=8,bg="#4edb1a",fg="black",activebackground='#68e83a',activeforeground="#1c1c1c",bd=0)
        settings_exit = tk.Button(controls, text ='Zrušiť', command = self.cont_exit,width=8,bg="#db910f",fg="black",activebackground='#e8a738',activeforeground="#1c1c1c",bd=0)
        settings_reset = tk.Button(controls, text ='Obnoviť\nPôvodné', command = self.cont_reset,width=8,bg="#cc1010",fg="black",activebackground='#c72a2a',activeforeground="#1c1c1c",bd=0)
        settings_save.grid(row=0,pady=10)
        settings_exit.grid(row=1)
        settings_reset.grid(row=2,pady=10)
        controls.grid(row=0,column=0,padx=12,pady=10)

        toggles = tk.Frame(self.contrf,bg="#2e2d2d")
        self.settings_ttime = tk.Button(toggles, text ='Čas', command = lambda: self.cont_toggle("t","self.configs.time.time_config_frame",self.settings_ttime),width=8,bg="#8aff7d",activebackground='#46fa32',activeforeground="#1c1c1c")
        self.settings_tsound = tk.Button(toggles, text ='Zvuk', command = lambda: self.cont_toggle("s","self.configs.sound.sound_config_frame",self.settings_tsound),width=8,bg="#8aff7d",activebackground='#46fa32',activeforeground="#1c1c1c")
        self.settings_tbell = tk.Button(toggles, text ='Zvonenia', command = lambda: self.cont_toggle("b","self.configs.bells.bell_config_frame",self.settings_tbell),width=8,bg="#8aff7d",activebackground='#46fa32',activeforeground="#1c1c1c")
        self.settings_ttime.grid(row=0)
        self.settings_tsound.grid(row=1,pady=3)
        self.settings_tbell.grid(row=2)
        toggles.grid(row=1,column=0)
        self.contrf.pack(side="top", fill="both", expand=True, padx=15, pady=15)

    def hs_controller(self,var):
        if not self.current_mode:
            if self.maing.maingui.state() == "iconic":self.contr.wm_withdraw()
            else:self.contr.wm_deiconify()

    def move_controller(self,var):
        if not self.current_mode:
            self.contr.geometry(f"+{int(1100+self.maing.maingui.winfo_x())}+{(int(self.maing.maingui.winfo_y()))}")
            self.contr.wm_deiconify()

    def cont_save(self):
        noerrors = True
        sounds_ts = ""
        bellsvar= ""
        for num in range(self.configs.sound.sc_count):
            dirv=self.configs.sound.ssounds[num].get()
            if self.func.fe(dirv):sounds_ts = sounds_ts+dirv+","
            else:
                messagebox.showinfo(title="SOS Zvonček Nastavenia", message=f"Problém v nastavení Zvuk\n\nSúbor {dirv} Neexistuje")
                noerrors = False

        if self.configs.sound.sc_count == 0:sounds_ts="emptyy"

        for num in range(self.configs.bells.bc_count):
            hours,minutes,secondsvar = self.configs.bells.bh[num].get(),self.configs.bells.bm[num].get(),self.configs.bells.bs[num].get()
            name = self.configs.bells.bnames[num].get().rstrip()
            spsound = self.configs.bells.bssounds[num].get()
            if len(name) == 0:
                messagebox.showinfo(title="SOS Zvonček Nastavenia", message=f"Problém v nastavení Zvonenia\n\nNiektoré Zvončeky nemajú pomenovania")
                noerrors = False

            if len(spsound) != 0:
                if self.func.fe(spsound):
                    specialsound= "--zvuk:"+spsound
                else:
                    messagebox.showinfo(title="SOS Zvonček Nastavenia", message=f"Problém v nastavení Zvonenia\n\nSúbor {spsound} Neexistuje")
                    noerrors = False
                    specialsound= "NotExisting"
            else:specialsound= ""

            if secondsvar != "00":
                seconds = ":"+secondsvar
            else:
                seconds = ""
            bellsvar = bellsvar+f"{hours}:{minutes}{seconds} {name} {specialsound}\n"

        if self.configs.bells.bc_count == 0:
            messagebox.showinfo(title="SOS Zvonček Nastavenia", message=f"Problém v nastavení Zvonenia\n\nNemáte ani jedno zvonenie nastavené")
            noerrors = False

        if noerrors:
            sounds_ts=sounds_ts[:-1]
            time_cfg = f"cfg_cas:{self.configs.time.tc_mainsel.get()}"
            sound_cfg = f"scfg_zvuk:{sounds_ts}"
            volume_cfg = f"cfg_hlas:{self.configs.sound.sc_volumecfg.get()}"
            bells = bellsvar.rstrip()
            self.fs.setconfig(time_cfg,sound_cfg,volume_cfg,bells)
            Variables()
            self.toggle_modes()

    def cont_exit(self):
        self.configs.time.tc_mainsel.set(time_config)
        self.configs.sound.sc_volumecfg.set(volume)
        self.toggle_modes()

        for num in range(self.configs.sound.sc_count):self.configs.sound.sc_del_line()
        for num in range(len(sounds)):self.configs.sound.sc_add_line(True)

        for num in range(self.configs.bells.bc_count):self.configs.bells.bc_del_line()
        for num in range(len(times)):self.configs.bells.bc_add_line(True)

    def cont_reset(self):
        ask = messagebox.askyesno(title="SOS Zvonček", message="Ste si istý že checte obnovit nastavenie na pôvodné?\n\nVarovanie: Táto akcia navždy vymaže vaše aktuálne nastavenie!")
        if ask:
            self.fs.setconfig("","","","")
            Variables()
            self.cont_exit()

    def cont_toggle(self,tp,window,button):
        if tp == "t":self.timet = not self.timet;var=self.timet
        elif tp == "s":self.soundt = not self.soundt;var=self.soundt
        elif tp == "b":self.bellt = not self.bellt;var=self.bellt
        if var:
            exec(f"{window}.grid()")
            button.config(bg="#8aff7d",activebackground='#46fa32')
        else:
            exec(f"{window}.grid_remove()")
            button.config(bg="#ff7d7d",activebackground='#fa3232')

    def create_minib(self):
        try:self.minibell.destroy()
        except Exception:pass
        self.minibell = tk.Tk()
        self.minibell.title("SOŠ Zvonček Mini")
        self.minibell.resizable(False, False)
        self.minibell.config(bg="#2e2d2d")
        self.minibell.attributes('-topmost',True)

        self.miniframe = tk.Frame(self.minibell,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
        self.minitext = tk.Label(self.miniframe, text="", font='Helvetica 20',bg="#2e2d2d",fg="#e3e3e3")

        self.miniframe.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        self.minitext.pack(fill="none", expand=True,padx=10,pady=10)

    class cmaingui:
        def __init__(self,name,geow,geoh):
            self.fs=Files()
            self.func=Functions()
            self.maingui = tk.Tk()
            self.maingui.title(name)
            y = (self.maingui.winfo_screenheight()/2) - (500/2)
            self.maingui.geometry(f"{geow}x{geoh}+{0}+{(int(y))}")
            self.maingui.resizable(False, False)
            self.maingui.config(bg="#1a1a1a")

            self.maingui.wm_iconphoto(False, tk.PhotoImage(data=self.fs.geticon()))

            self.mainf = tk.Frame(self.maingui,width=geow,height=geoh)

    class mode_display:
        def __init__(self,owner):
            self.bd = tk.Frame(owner,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
            self.bd.pack(side="top", fill="both", expand=True, padx=20, pady=20)

            self.maintext = tk.Label(self.bd, text="", font='Helvetica 60',bg="#2e2d2d",fg="#e3e3e3")
            self.maintext.pack(fill="none", expand=True,ipadx=10,ipady=10)

        def add_button(self,name,command,side):
            buttonf = tk.Frame(self.bd,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d",bd=0)
            button = tk.Button(buttonf, text=name, command = command,bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3",bd=0)
            buttonf.pack(side=side,pady=20,padx=20)
            button.pack(side=side)

    class settings_display:
        def __init__(self,owner):
            sframe = self.sf(owner)
            self.time=self.settings_time(sframe.frame)
            self.sound=self.settings_sound(sframe.frame)
            self.bells=self.settings_bells(sframe.frame)
            sframe.update()

        class settings_time:
            def __init__(self,owner):
                self.fs=Files()
                self.time_config_frame = tk.Frame(owner,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
                self.time_config_frame.grid(row=1,column=0,sticky="w",padx=10,pady=10)

                tc_maintext = tk.Label(self.time_config_frame, text=f"Čas", font='Helvetica 20',bg="#2e2d2d",fg="#e3e3e3").grid(row=0,column=0,ipady=10,sticky="w")
                self.tc_mainsel = tk.StringVar()
                self.tc_mainsel.set(time_config)
                self.tc_mainsel.trace("w", self.tc_change)
                tc_selection = tk.OptionMenu(self.time_config_frame, self.tc_mainsel, "TIMEZONE", "LOCAL")
                tc_selection.grid(row=1,column=0,sticky="w",padx=10)
                tc_selection.config(bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3",bd=0)
                tc_selection["menu"].config(bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3")
                self.tc_infotext = tk.Label(self.time_config_frame, text="", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3")
                self.tc_timetext = tk.Label(self.time_config_frame, text="", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3")
                self.tc_infotext.grid(row=1,column=1)
                self.tc_timetext.grid(row=2,column=1)

            def tc_change(self,*args):
                tc_cfg = self.tc_mainsel.get()
                self.func=Functions()
                if tc_cfg == "TIMEZONE":
                    tc_info = "Použije Bratislava timezone čas\n\nAk nemáte internet použije čas nastavený v počítači\n\nAk toto nastavenie ukazuje špatný čas\nupdatujte python pytz modul pomocou\npip install pytz --upgrade\n"
                else:
                    tc_info = "Použije čas nastavený v počítači"
                self.tc_infotext.config(text=tc_info)
                self.tc_timetext.config(text=f"Aktuálny čas: {self.func.gettime(tc_cfg)}")

        class settings_sound:
            def __init__(self,owner):
                self.funcs=Functions()
                self.sound_config_frame = tk.Frame(owner,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
                self.sc_volumef = tk.Frame(self.sound_config_frame,bg="#2e2d2d")
                self.sc_soundf = tk.Frame(self.sound_config_frame,bg="#2e2d2d")
                self.sound_config_frame.grid(row=2,column=0,sticky="w",padx=10,pady=10)
                self.sc_volumef.grid(row=1,column=0,sticky="w")
                self.sc_soundf.grid(row=6,column=0,sticky="w")

                self.tc_maintext = tk.Label(self.sound_config_frame, text=f"Zvuk", font='Helvetica 20',bg="#2e2d2d",fg="#e3e3e3").grid(row=0,column=0,ipady=10,sticky="w")
                def volume_change(*args):
                    global sc_volume
                    sc_volume = self.sc_volumecfg.get()
                sc_volumetext = tk.Label(self.sc_volumef, text="Hlasitosť: ", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3").grid(row=1,column=0)
                self.sc_volumecfg=ttk.Combobox(self.sc_volumef, values=list(range(0, 126)),width=5,state = "readonly")
                self.sc_volumecfg.set(volume)
                self.sc_volumecfg.bind('<<ComboboxSelected>>', volume_change)
                self.sc_volumecfg.grid(row=1,column=1)


                sc_audiotext = tk.Label(self.sc_volumef, text="Zvuky: ", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3").grid(row=3,column=0,ipady=10,sticky="w")
                self.sc_addb = tk.Button(self.sc_soundf, text ='+',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = lambda: self.sc_add_line(False), font='Helvetica 15 bold')
                sc_infob = tk.Button(self.sc_volumef, text ='Info',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = self.sc_info)
                self.sc_delb = tk.Button(self.sc_soundf, text ='-',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = self.sc_del_line, font='Helvetica 15 bold')
                sc_infob.grid(row=3,column=1,sticky="w")


                self.sframes,self.ssounds,self.sc_count=[],[],0
                for num in range(len(sounds)):
                    self.sc_add_line(True)

            def sc_info(self):
                messagebox.showinfo(title="SOS Zvonček Nastavenia", message="Ak vyberiete viac zvukov\nkeď zazvoní vyberie to jeden z nich náhodne\n\nMôžete použit relatívnu alebo absolútnu cestu k súboru\n\nAk vám nestačí miesto v textových poliach lavou a pravou šipkou sa v nich môžete posúvať")

            def sc_add_line(self,preload):
                sc_soundsubf = tk.Frame(self.sc_soundf,bg="#2e2d2d")
                self.sframes.append(sc_soundsubf)

                sc_soundsubf.grid(row=self.sc_count+2,column=0,sticky='w')
                sc_sound = tk.Entry(sc_soundsubf,width=100,bg="#474646",fg="#e3e3e3")
                self.ssounds.append(sc_sound)

                current_count=self.sc_count
                sc_selb = tk.Button(sc_soundsubf, text ='Vyskúšať',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = lambda: self.funcs.playsound(sc_sound.get(),sc_volume))
                sc_playb = tk.Button(sc_soundsubf, text ='Vybrať',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = lambda: self.sf_explore(eval(f"{current_count}")))
                if preload:
                    try:sc_sound.insert(0, sounds[self.sc_count])
                    except Exception:pass

                sc_sound.grid(row=self.sc_count+2,column=0)
                sc_selb.grid(row=self.sc_count+2,column=1)
                sc_playb.grid(row=self.sc_count+2,column=2)

                self.move_sc_buttons()
                self.sc_count+=1

            def sc_del_line(self):
                if self.sc_count > 0:
                    self.sframes[-1].destroy()
                    del self.sframes[-1]
                    del self.ssounds[-1]
                    self.sc_count-=1

            def move_sc_buttons(self):
                self.sc_addb.grid(row=self.sc_count+3,column=1,sticky='w')
                self.sc_delb.grid(row=self.sc_count+3,column=2,sticky='w')

            def sf_explore(self,num):
                out=(self.funcs.explore())
                if out:
                    self.ssounds[num].delete(0, 'end')
                    self.ssounds[num].insert(0, out)

        class settings_bells:
            def __init__(self,owner):
                self.funcs=Functions()
                self.bell_config_frame = tk.Frame(owner,highlightbackground="#62c78a", highlightthickness=2,bg="#2e2d2d")
                self.bell_config_frame.grid(row=3,column=0,sticky="w",padx=10,pady=10)
                self.bc_bellf = tk.Frame(self.bell_config_frame,bg="#2e2d2d")
                self.bc_bellf.grid(row=4,column=0,sticky="w")

                tc_maintext = tk.Label(self.bell_config_frame, text=f"Zvonenia", font='Helvetica 20',bg="#2e2d2d",fg="#e3e3e3").grid(row=0,column=0,ipady=10,sticky="w")
                bc_infotext = tk.Label(self.bell_config_frame, text=f"        Čas                     Názov                                         Špeciálny Zvuk", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3").grid(row=2,column=0,ipady=3,sticky="w")
                bc_infospectext = tk.Label(self.bell_config_frame, text=f"(Hodiny,Minúty,Sekundy)               (Povinné)                                                                     (Dobrovoľné)", font='Helvetica 10',bg="#2e2d2d",fg="#e3e3e3").grid(row=3,column=0,sticky="w")
                bc_infob = tk.Button(self.bell_config_frame, text ='Info', command = self.bc_info,bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3")
                bc_infob.grid(row=1,column=0,sticky="w")

                self.bc_addb = tk.Button(self.bc_bellf, text ='+', command = lambda: self.bc_add_line(False), font='Helvetica 15 bold',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3")
                self.bc_delb = tk.Button(self.bc_bellf, text ='-', command = self.bc_del_line, font='Helvetica 15 bold',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3")

                self.mrange = self.srange = ["%02d" % x for x in range(60)]
                self.bframes,self.bh,self.bm,self.bs,self.bnames,self.bssounds,self.bc_count=[],[],[],[],[],[],0
                for num in range(len(times)):
                    self.bc_add_line(True)

            def bc_info(self):
                messagebox.showinfo(title="SOS Zvonček Nastavenia", message="Napísať názov zvončeku je povinné\n\nŠpeciálny zvuk:\nJe dobrovoľný\nAk určíte špeciálny zvuk tak v ten čas zvonenia bude hrať zvuk čo vyberiete\nNení možné vybrať viac ako 1 zvuk\nMôžete použit absolútnu alebo relatívnu cestu k súboru\n\nAk vám nestačí miesto v textových poliach lavou a pravou šipkou sa v nich môžete posúvať")

            def bc_add_line(self,preload):
                bc_bellsubf = tk.Frame(self.bc_bellf,bg="#2e2d2d")
                self.bframes.append(bc_bellsubf)

                name_text = tk.StringVar()
                bc_h = ttk.Combobox(bc_bellsubf,values=list(range(0, 24)),width=3,state = 'readonly')
                bc_m = ttk.Combobox(bc_bellsubf,values=list(self.mrange),width=3,state = 'readonly')
                bc_s = ttk.Combobox(bc_bellsubf,values=list(self.srange),width=3,state = 'readonly')
                bc_namet = tk.Entry(bc_bellsubf,width=30,bg="#474646",fg="#e3e3e3",textvariable = name_text)
                bc_specsound = tk.Entry(bc_bellsubf,width=40,bg="#474646",fg="#e3e3e3")
                self.bh.append(bc_h)
                self.bm.append(bc_m)
                self.bs.append(bc_s)
                self.bnames.append(bc_namet)
                self.bssounds.append(bc_specsound)

                current_count=self.bc_count
                name_text.trace("w", lambda *args: self.char_limit(name_text))
                bc_tests = tk.Button(bc_bellsubf,text ='Vyskúšať',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = lambda: self.funcs.playsound(bc_specsound.get(),sc_volume))
                bc_sels = tk.Button(bc_bellsubf,text ='Vybrať',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = lambda: self.bc_explore(eval(f"{current_count}")))


                bc_bellsubf.grid(row=self.bc_count+2,column=0,sticky='w')

                if preload:
                    h=times[self.bc_count].split(':')[0]
                    m=times[self.bc_count].split(':')[1]
                    s=times[self.bc_count].split(':')[2]
                    name=names[self.bc_count].split(" ",1)[1]
                    if spsounds[self.bc_count] == "Nothing":
                        specialsound=""
                    else:
                        specialsound=spsounds[self.bc_count]
                else:
                    specialsound,name,h="","Názov",0
                    m=s=f"{0:02}"

                bc_namet.insert(0, name)
                bc_specsound.insert(0, specialsound)
                bc_h.set(h)
                bc_m.set(m)
                bc_s.set(s)
                bc_h.grid(row=1,column=1,padx=1)
                bc_m.grid(row=1,column=2,padx=1)
                bc_s.grid(row=1,column=3,padx=1)
                bc_namet.grid(row=1,column=4,padx=1)
                bc_specsound.grid(row=1,column=5,padx=1)
                bc_tests.grid(row=1,column=6,padx=1)
                bc_sels.grid(row=1,column=7,padx=1)

                self.move_bc_buttons()
                self.bc_count+=1

            def bc_del_line(self):
                if self.bc_count > 0:
                    self.bframes[-1].destroy()
                    del self.bframes[-1]
                    del self.bh[-1]
                    del self.bm[-1]
                    del self.bs[-1]
                    del self.bnames[-1]
                    del self.bssounds[-1]
                    self.bc_count-=1

            def move_bc_buttons(self):
                self.bc_addb.grid(row=self.bc_count+3,column=1,sticky='w')
                self.bc_delb.grid(row=self.bc_count+3,column=2,sticky='w')

            def bc_explore(self,num):
                out=(self.funcs.explore())
                if out:
                    self.bssounds[num].delete(0, 'end')
                    self.bssounds[num].insert(0, out)

            def char_limit(self,obj):
                if len(obj.get()) > 0:
                    obj.set(obj.get()[:15])

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
        filesc=Files()
        if os.path.isdir(cfgname):os.rmdir(cfgname)
        if not os.path.exists(cfgname):filesc.setconfig("","","","")
        Variables()
        Gui()


try:start()
except Exception as e:
    messagebox.showinfo(title="SOS Zvonček", message=f"Chyba:\n{e}")
    exit(f"Chyba: {e}")
