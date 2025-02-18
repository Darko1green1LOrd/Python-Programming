import tkinter as tk
from random import choice

class paint():
    def __init__(self):
        self.colors,self.line,self.action=("blue"),(),0
        self.paintg = tk.Canvas(width=400,height=400);self.paintg.grid()
        self.b("ButtonPress-1",[self.leftp,self.mainfunc]);self.b("ButtonRelease-1",[self.leftr,self.mainfunc])
        self.b("ButtonPress-2",[self.middlep,self.mainfunc]);self.b("ButtonRelease-2",[self.middler,self.mainfunc])
        self.b("ButtonPress-3",[self.rightp,self.mainfunc]);self.b("ButtonRelease-3",[self.rightr,self.mainfunc])
        self.b("Motion",[self.mainfunc])
        self.paintg.mainloop()
    def mainfunc(self,pos):
        if self.action != 0:self.paintg.delete("all")
        if self.action == 1:
            self.line = self.line + (pos.x,pos.y)
            if len(self.line) >= 4:self.paintg.create_line(self.line,fill=self.colors,width=4)
        elif self.action == 2:
            self.colors=choice(("blue","red","purple","yellow"))
            if len(self.line) >= 4:self.paintg.create_line(self.line,fill=self.colors,width=4)
        elif self.action == 3:
            self.altline = [elem / 2 for idx, elem in enumerate(self.line)]
            self.altline2 = [elem + (200 if idx % 2 == 0 else 0) for idx, elem in enumerate(self.altline)]
            if len(self.line) >= 4:
                self.paintg.create_line(self.altline,fill="blue",width=4)
                self.paintg.create_line(self.altline2,fill="red",width=4)
    def b(self,action,commands):
        list(map(lambda elem: self.paintg.bind(f"<{action}>",commands[commands.index(elem)],add="+"), commands))
    def leftr(self,v):self.action=0
    def rightr(self,v):self.action=0
    def middler(self,v):self.action=0
    def leftp(self,v):self.action=1
    def rightp(self,v):self.action=2
    def middlep(self,v):self.action=3


paintgui = paint()
