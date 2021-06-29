# -*- coding: UTF-8 -*-

from tkinter import*

class appsmultiplicacao:
    def __init__ (self,f):
        self.f=f
        self.f.title('Multiplicação')
        
        Label(self.f,text='Numero 1').grid(row=1,column=1,sticky=W,pady=3)
        Label(self.f,text='numero 2').grid(row=2,column=1,sticky=W,pady=3)
        
        self.msg=Label(self.f,text= "")
        self.msg.grid(row=3,column=1,columnspan=2)
        
        self.campo1=Entry(self.f,width=10)
        self.campo1.grid(row=1,column=2,sticky=E+W,pady=3)
        self.campo1.focus_force()
        
        self.campo2=Entry(self.f,width=10)
        self.campo2.grid(row=2,column=2,sticky=E+W,pady=3)
        
        self.botao=Button(text='Multiplicar',width=8,command=self.multiplicar)
        self.botao.grid(row=4,column=1,padx=2,pady=3)
        
        self.botao1=Button(text='Sair',width=8,command=self.sair)
        self.botao1.grid(row=4,column=2,padx=2,pady=3)
        
    def multiplicar(self):
        campo1=self.campo1.get()
        campo2=self.campo2.get()
        campo1=int(campo1)
        campo2=int(campo2)
        s=campo1*campo2
        s=float(s)
        self.msg['text']= 'A multiplicação e %d'%(s)
    
    def sair(self):
        self.f.destroy()
        
inst=Tk()
appsmultiplicacao(inst)
inst.mainloop()
