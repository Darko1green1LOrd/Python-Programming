import tkinter as tk
from random import randint
from os import path
todel = []
savefile = "3Dices_results.txt"

main = tk.Tk()
main.geometry("600x700-0-0")
main.config(bg="#2e2d2d")
main.title("3 Kocky")
main.resizable(False, False)

statarea = tk.Frame(main,width=600,height=600,bg="#1c1a1a")
statarea.grid(row=0)

def generate():
    roll = [randint(1,6) for i in range(3)]
    rollsum = sum(roll)

    save_roll = " ".join(str(item) for item in ["".join(str(each) for each in roll),rollsum])
    save_list = [roll,rollsum]
    return save_roll,save_list

def repeat(rep,sumoutvar,pillarsvar,sizesvar,sizesval):
    value = sumoutvar[rep-1]
    indexnum = value-3

    bn = len(str(max(sizesval)))
    bd = max(sizesval)
    pillar_limiter = 2 if bd < 1000 else bn * (bd // 1000)

    sizesval[indexnum] += 1
    for i,each in enumerate(sizesval):
        ctl = len(str(each))
        pillarsvar[i].config(height=int(each/pillar_limiter))
        sizesvar[i].config(text=each,font=f'Helvetica {int(15 if ctl < 3 else 10 if ctl < 6 else 5)}')
        
    rep -= 1
    if rep > 0:main.after(2,lambda:repeat(rep,sumoutvar,pillarsvar,sizesvar,sizesval))
    else:runb.grid(row=3,column=0,ipady=5,sticky="s",pady=3)

def run(given_values=False,tofile=None,towork=None,sumout=None):
    try:
        try:repeats = int(rolls.get().strip())
        except NameError:
            if given_values:repeats = 1
            else:pass
        if repeats > 0:
            runb.grid_remove()
            pillars,sizes = [],[]
            sizes_vals=[0]*16
            if not given_values:
                tofile,towork,sumout = [],[],[]

                for each in [generate() for i in range(repeats)]:
                    tofile.append(each[0])
                    towork.append(each[1])
                    sumout.append(each[1][1])

            if len(todel) != 0:
                todel[0].destroy()
                del todel[0]
            stats = tk.Frame(statarea,highlightbackground="#e3e3e3", highlightthickness=2,bg="#474545")
            stats.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            todel.append(stats)
            for i,each in enumerate([num for num in range(3,19)]):
                tk.Label(stats, text=each, font='Helvetica 15',bg="#474545",fg="#e3e3e3").grid(row=2,column=each,padx=7,sticky="s")
                frame_ = tk.Frame(stats,bg='#474545')
                frame_.grid(row=0,column=each,sticky='s')

                pillar_ = tk.Frame(frame_,bg='#a4f542',width=18,height=sizes_vals[i])
                pillar_.grid(row=1,column=0,sticky='s')

                amount_ = tk.Label(frame_, text=sizes_vals[i], font='Helvetica 15',bg='#474545',fg='#e3e3e3')
                amount_.grid(row=0,column=0,sticky='s')
                pillars.append(pillar_)
                sizes.append(amount_)
            repeat(len(sumout),sumout,pillars,sizes,sizes_vals)
            if not given_values:
                if path.isdir(savefile):rmdir(savefile)
                with open(savefile, 'w') as f:
                    f.writelines("\n".join(str(each) for each in tofile))


    except ValueError:pass

runb = tk.Button(main, text ='SPUSTI',bg="#474646",fg="#e3e3e3",activebackground='#616060',activeforeground="#e3e3e3", command = run, font='Helvetica 10 bold',bd=0)
if path.isdir(savefile):rmdir(savefile)
if path.exists(savefile):
    with open(savefile, 'r') as f:
        fileval= [line.strip() for line in f]
    workval= [[[int(line.strip().split(" ")[0][0]),int(line.strip().split(" ")[0][1]),int(line.strip().split(" ")[0][1])],int(line.strip().split(" ")[1])] for line in fileval]
    sumval = [int(line.strip().split(" ")[1]) for line in fileval]
    try:run(True,fileval,workval,sumval)
    except Exception:runb.grid(row=3,column=0,ipady=5,sticky="s",pady=3)
else:runb.grid(row=3,column=0,ipady=5,sticky="s",pady=3)

info_t = tk.Label(main, text="Zadaj počet hodov:", font='Helvetica 15',bg="#2e2d2d",fg="#e3e3e3")
rolls = tk.Entry(main,width=60,bg="#474646",fg="#e3e3e3")

info_t.grid(row=1,column=0,ipady=1,sticky="s")
rolls.grid(row=2,ipady=4,sticky="s")

main.mainloop()