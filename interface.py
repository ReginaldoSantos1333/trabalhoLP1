from distutils import command
from tkinter import *
from tkinter import messagebox
from tkinter import Tk


def mensagem(tipomsg,aba):
            messagebox.showinfo(title ="UPday", message = "Bom te conhecer {}".format(tipomsg))
            aba.destroy()
        


#inserçãorotina


def inserir():
    pass

    #editar rotina

def editar():
    pass


    #buscar rotina
 
def buscar():
    pass


    #visualizar rotina

def ver():
    pass



    # upday rotina
   
def upday():
    pass



#apagar rotina
def apagar():
    pass


    #encerrar sessão


#Boas-vindas

welcome = Tk()
vnum_cstexto = StringVar()
# Mensagem de boas vindas
welcome.title("Bem vindo ao UPday!")
welcomelbl = Label(welcome, text= """Olá! Bem vindo(a) à UPday!
Juntos podemos dar um 'Up' no seu dia ;)
Primeiramente, seria ótimo te conhecer mais um pouco.
        Vamos começar?!""")
welcomelbl.grid(column=0,row=0)
# Caixa de inserção
welcometab = Entry(welcome, textvariable=vnum_cstexto)
welcometab.grid(column=0, row= 3)
# Mensagem na caixa de texto
vnum_cstexto.set("Nos diga o seu nome!")
# Botão de inserção
welcomebtn = Button(welcome, text="Mostrar mensagem", command=lambda:mensagem(vnum_cstexto.get(),welcome))
welcomebtn.grid(column =0, row = 4)
welcome.mainloop()

# Janela principal

mainwindow = Tk()
# Muda a corda janela principal
mainwindow.configure(background="lightblue")
# Titulo da janela
mainwindow.title("UPday")
# Tamanho janela principal
#mainwindow.geometry("1280x720")
# Traz janela para frente 
mainwindow.lift()
#Label com o nome do app, cor de fundo,texto e sua fonte
texto_inicial = Label(mainwindow, text = "UPday",bg = "lightblue",fg = "black")
texto_inicial.configure(font=("Segoe Print", 25))
texto_inicial.grid(column=1,row=0, padx = 100,pady = 300)

# Botão de inserção
insert = Button(mainwindow, text = "Nova Rotina", command= inserir)
insert.grid(column=0,row=6, padx = 10,pady = 10)
# Botão de edição
edit = Button(mainwindow, text= "Editar Rotina", command= editar)
edit.grid(column=0,row=7, padx = 10,pady = 10)
# Botão de buscar
search = Button(mainwindow, text= "Buscar Rotina", command=buscar)
search.grid(column=0,row=8, padx = 10,pady = 10)
# Botão de visualiza
check = Button(mainwindow, text= "Ver Rotina", command=ver)
check.grid(column=2,row=6, padx = 10,pady = 10)
# Botão de upday
Upd = Button(mainwindow, text = "UPday Rotina", command=upday)
Upd.grid(column=2,row=7, padx = 10,pady = 10)
# Botão de apagar
erase = Button(mainwindow, text = "Apagar Rotina", command=apagar)
erase.grid(column=2,row=8, padx = 10,pady = 10)

mainwindow.mainloop()
