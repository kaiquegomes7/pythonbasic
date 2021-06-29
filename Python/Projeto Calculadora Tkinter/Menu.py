# -*- coding: UTF-8 -*-

from tkinter import*

class Application:
    def __init__(self,menu):
        
        self.menu=menu
        self.menu.title("Menu")

        self.botao=Button(text='Soma',width=8, command=self.appsom)
        self.botao.grid(row=5,column=1,padx=2,pady=3)

        self.botao=Button(text='Subtração',width=8, command=self.appsubt)
        self.botao.grid(row=5,column=2,padx=2,pady=3)

        self.botao=Button(text='Multiplicação',width=8, command=self.appmulti)
        self.botao.grid(row=5,column=3,padx=2,pady=3)

        self.botao=Button(text='Divisão',width=8, command=self.appdivi)
        self.botao.grid(row=5,column=4,padx=2,pady=3)

        self.botao1=Button(text='Sair',width=8,command=self.sair)
        self.botao1.grid(row=5,column=5,padx=2,pady=3)

    def appsom(self):
        from appsoma import appsoma

    def appsubt(self):
        from appsubtracao import appsubtracao
        
    def appmulti(self):
        from appmultiplicacao import appmultiplicacao

    def appdivi(self):
        from appdivisao import appdivisao

    def sair(self):
        self.menu.destroy()
        
inst=Tk()
Application(inst)
inst.mainloop()
