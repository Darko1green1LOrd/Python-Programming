class paint:
    import os
    import tkinter as tk

    def __init__(self):
        self.size,self.savenmame=5,"file5_save.txt"
        self.main = paint.tk.Tk();self.main.geometry("600x600-100-100")
        self.paintarea = paint.tk.Canvas(self.main,width=600,height=600,bg="#c2c2c2");self.paintarea.grid(row=0)
        self.b("ButtonPress-1",[self.create_dot])
        self.b("space",[self.clear])

        self.loadsave()

        self.main.mainloop()


    def b(self,action,commands):
        for each in commands:self.paintarea.bind_all(f"<{action}>",commands[commands.index(each)],add="+")


    def create_dot(self,coords,save=True,inp=[]):
        if save:
            x,y=coords.x,coords.y
            self.saveddots.append([coords.x,coords.y])
        else:x,y=inp[0],inp[1]

        self.paintarea.create_oval(x-self.size,y-self.size,x+self.size,y+self.size,fill="red",outline="")
        self.save(self.savenmame,f"{self.saveddots}")


    def clear(self,var):
        self.paintarea.delete("all")
        paint.os.remove(self.savenmame)


    def loadsave(self):
        save = self.read(self.savenmame)[0]
        if save != "n":self.saveddots = eval(save)
        else:self.saveddots = []
        for each in self.saveddots:
            self.create_dot(0,False,each)



    def save(self,filevar,text,overwrite=True,onlynew=False):
        if paint.os.path.isdir(filevar):paint.os.rmdir(filevar)
        if overwrite and not onlynew:
            with open(filevar, 'w') as f:
                f.writelines(text)


    def read(self,filevar):
        if paint.os.path.isdir(filevar):paint.os.rmdir(filevar)
        if paint.os.path.exists(filevar):
            with open(filevar, 'r') as f:
                lines = [line.strip() for line in f]
                return lines
        else:return "n"

paint()
