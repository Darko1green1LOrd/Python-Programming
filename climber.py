import tkinter as tk
from time import sleep
from math import sqrt

class pather:
    def __init__(self):
        self.path,self.up,self.down,self.total,self.tcount,self.ps,self.prsd,self.txtvars = (10,250,80,200,300,250,100,400,100,200),0,0,0,1,False,False,[]

        self.main = tk.Tk();self.main.geometry("500x600-100-100")
        self.runb = tk.Button(self.main, text ='Launch', command = self.runsim);self.runb.grid(row=2,sticky='e',padx=20)
        self.pathpt = tk.Button(self.main, text ='Path Draw',bg="#ff7d7d",activebackground="#fa3232",activeforeground="#1c1c1c", command = self.paint_toggle);self.pathpt.grid(row=3,sticky='e',padx=20)
        self.canb = tk.Button(self.main, text ='Cancel', command = self.cancel);self.canb.grid(row=2,sticky='e',padx=20);self.canb.grid_remove()
        self.lineg = tk.Canvas(self.main,width=500,height=500,bg="#c2c2c2");self.lineg.grid(row=0)
        self.b("ButtonPress-1",[self.leftp,self.paint]);self.b("ButtonRelease-1",[self.leftr,self.paint])
        self.b("Motion",[self.paint])

        self.addt(self.up,"Going Up")
        self.addt(self.down,"Going Down")
        self.addt(self.total,"Total")

        self.render()

        self.main.mainloop()

    def addt(self,var,text):
        exec(f"self.textvar_{self.tcount}=tk.StringVar()")
        tk.Label(self.main,textvariable=eval(f"self.textvar_{self.tcount}")).grid(row=self.tcount,sticky="w")
        eval(f"self.textvar_{self.tcount}").set(f"{text}: {var}")
        self.txtvars.append(eval(f"self.textvar_{self.tcount}"))
        self.tcount += 1

    def b(self,action,commands):
        for each in commands:self.lineg.bind(f"<{action}>",commands[commands.index(each)],add="+")

    def render(self):
        up,self.down,self.total=0,0,0
        self.lineg.delete("all")
        for each in [a-b for a,b in zip(self.path[3::2],self.path[:-1][1::2])]:
            if each < 0:self.up += -each
            else:self.down += each
        self.total = int(((self.path[-4::2][0]-self.path[-4::2][1])**2 + (self.path[-3::2][0]-self.path[-3::2][1])**2)**0.5)
        self.lineg.create_line(self.path,width=4)
        self.txtvars[0].set(f"{self.txtvars[0].get().split(':',1)[0]}: {self.up}")
        self.txtvars[1].set(f"{self.txtvars[1].get().split(':',1)[0]}: {self.down}")
        self.txtvars[2].set(f"{self.txtvars[2].get().split(':',1)[0]}: {self.total}")

    def paint_toggle(self):
        self.ps = not self.ps
        self.lineg.delete("all")
        if self.ps:
            self.pathpt.config(bg="#8aff7d",activebackground="#46fa32")
            self.runb.grid_remove();self.canb.grid()
            self.lineg.create_line(self.path,width=4,fill="#8a8787")
            self.main.config(cursor="dotbox")
            self.newpath,self.save = [],True
        else:
            self.pathpt.config(bg="#ff7d7d",activebackground="#fa3232")
            self.runb.grid();self.canb.grid_remove()
            self.main.config(cursor="")
            if len(self.newpath) >= 4 and self.save:
                self.path = tuple(self.newpath)
                self.render()
            else:self.lineg.create_line(self.path,width=4)

    def cancel(self):
        self.save=False
        self.paint_toggle()
    def leftp(self,v):self.prsd=True
    def leftr(self,v):self.prsd=False
    def paint(self,coords):
        w,h=self.lineg.winfo_width()-2,self.lineg.winfo_height()-2

        if self.ps and self.prsd:
            if coords.x <= w-5 and coords.y <= h-5 and coords.x >= 5 and coords.y >= 5:
                self.newpath.append(coords.x)
                self.newpath.append(coords.y)
                if len(self.newpath) >= 4:
                    self.lineg.delete("all")
                    self.lineg.create_line(self.path,width=4,fill="#8a8787")
                    self.lineg.create_line(self.newpath,width=4)


    def runsim(self):
        self.runb.grid_remove();self.pathpt.grid_remove()
        x,y=self.path[:2][0],self.path[:2][1]
        self.paths=[self.path[i*2:i*2+2] for i in range(len(self.path)//2)];del self.paths[0]

        self.runner = self.lineg.create_oval(x-4, y-4, x+4, y+4, fill="red")

        def start():
            if self.paths:
                currentpos = (self.lineg.coords(self.runner))
                xpos,xpath,ypos,ypath = int(currentpos[:2][0]),self.paths[0][0]-4,int(currentpos[:2][1]),self.paths[0][1]-4
                if xpath==xpos and ypath == ypos:del self.paths[0]
                else:
                    vector = (xpath - xpos, ypath - ypos)
                    vector_length = sqrt(vector[0]**2+vector[1]**2)
                    normalized_vector = (vector[0]/vector_length, vector[1]/vector_length)
                    movement_vector = (normalized_vector[0] * 1, normalized_vector[1] * 1)
                    self.lineg.move(self.runner,movement_vector[0],movement_vector[1]);self.lineg.update()
                self.main.after(5, start)
            else:
                sleep(0.5)
                self.lineg.delete(self.runner)
                self.runb.grid();self.pathpt.grid()
        start()


func = pather()
