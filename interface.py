import ssl
from tkinter import *
from time import *

"""
Cria um botão:
----botao = Button(janela, text="Iniciar", command= tarefas)

Adiciona a posição de um botão:
----botao.grid(column=0, row=1)

Adiciona um label:
----texto_teste = Label(janela, text="")

Indica posicao de um label:
----texto_teste.grid(column=0, row=2)

"""


def tarefas():
    janela2 = Tk()
    janela2.title("Tarefas")
    # Texto informando o nome da janela
    texto_tarefas = Label(janela2, text="Tarefas") 
    texto_tarefas.grid(column=1, row=0)

    # Botão que segue para alteração das tarefas difíceis
    botaoTD = Button(janela2, text="Tarefas Difíceis", command=tarefasDificeis)
    botaoTD.grid(column=0, row=1, padx=10, pady= 10)

    # Botão que segue para alteração das tarefas Faceis
    botaoTF = Button(janela2, text="Tarefas Faceis", command=tarefasFaceis)
    botaoTF.grid(column=1, row=1, padx=10, pady= 10)

    # Botão que segue para alteração das tarefas Fixas
    botaoTFi = Button(janela2, text="Tarefas Fixas", command=tarefasFixas)
    botaoTFi.grid(column=2, row=1, padx=10, pady= 10)
    janela2.mainloop()

def tarefasDificeis():
        janela4 = Tk()
        #titulo da janela
        janela4.title("Tarefas Dificeis")

        #Texto na janela
        texto_tarefasD = Label(janela4, text="Lista de Tarefas Dificeis")
        texto_tarefasD.grid(column=1, row=0)
        
        #Botao de remover
        botaoErase = Button(janela4, text="Remover", command= remover)
        botaoErase.grid(column=0, row= 1, padx=10, pady=10)

        #Botao de editar
        botaoEdit = Button(janela4, text="Editar", command= edit)
        botaoEdit.grid(column=0, row = 2, padx=10, pady=10)

        #Botao de adicionar
        botaoAdd = Button(janela4, text="Adicionar", command= add)
        botaoAdd.grid(column=2, row= 1, padx=10, pady=10)


        #Botao de salvar
        botaoSave = Button(janela4, text="Salvar", command= save)
        botaoSave.grid(column=2, row= 2, padx=10, pady=10)

        janela4.mainloop()

def tarefasFaceis():
        janela5 = Tk()
        janela5.title("Tarefas Fáceis")

        texto_tarefasF = Label(janela5, text="Lista de Tarefas Fáceis")
        texto_tarefasF.grid(column=1, row=0)

        #Botao de remover
        botaoErase = Button(janela5, text="Remover", command= remover)
        botaoErase.grid(column=0, row= 1, padx=10, pady=10)

        #Botao de editar
        botaoEdit = Button(janela5, text="Editar", command= edit)
        botaoEdit.grid(column=0, row = 2, padx=10, pady=10)


        #Botao de adicionar
        botaoAdd = Button(janela5, text="Adicionar", command= add)
        botaoAdd.grid(column=2, row= 1, padx=10, pady=10)


        #Botao de salvar
        botaoSave = Button(janela5, text="Salvar", command= save)
        botaoSave.grid(column=2, row= 2, padx=10, pady=10)

        janela5.mainloop()

def tarefasFixas():
        janela6 = Tk()
        janela6.title("Tarefas Fixas")

        texto_tarefasFix = Label(janela6, text="Lista de Tarefas Fixas")
        texto_tarefasFix.grid(column=1, row=0)
        
        #Botao de remover
        botaoErase = Button(janela6, text="Remover", command= remover)
        botaoErase.grid(column=0, row= 1, padx=10, pady=10)


        #Botao de editar
        botaoEdit = Button(janela6, text="Editar", command= edit)
        botaoEdit.grid(column=0, row = 2, padx=10, pady=10)


        #Botao de adicionar
        botaoAdd = Button(janela6, text="Adicionar", command= add)
        botaoAdd.grid(column=2, row= 1, padx=10, pady=10)


        #Botao de salvar
        botaoSave = Button(janela6, text="Salvar", command= save)
        botaoSave.grid(column=2, row= 2, padx=10, pady=10)

        janela6.mainloop()


def save():
    pass
def edit():
    pass
def remover():
    pass
def add():
    pass


def novarotina():
    janela3 = Tk()
    janela3.title("Nova_Rotina")
    # Texto informando o nome da janela
    texto_novarotina = Label(janela3, text="Selecione o tipo de rotina à ser criada:")
    texto_novarotina.grid(column=1, row=0)

    # Botão que cria um escopo de rotina PADRÃO
    botaoDefault = Button(janela3, text="Padrão", command=rotinaPadrao)
    botaoDefault.grid(column=0, row=1, padx=10, pady=10)

    # Botão que cria um escopo de rotina VAZIA
    botaoVazia = Button(janela3, text="Vazia", command=rotinaVazia)
    botaoVazia.grid(column=2, row=1, padx=10, pady=10)
    
   
    janela3.mainloop()

def rotinaPadrao():
     #adiciona janela principal 
    janelaPadrao = Tk()

    #Adiciona um título da janela invocada
    janelaPadrao.title("Rotina")

    #Informação na janela
    texto_inicial = Label(janelaPadrao, text="Gerador de Rotina") 
    texto_inicial.grid(column=2, row=0, padx=100, pady=200)

    #chama a tela de tarefa
    botao = Button(janelaPadrao, text="Tarefas", command= tarefas)
    botao.grid(column=3, row=3,padx= 10, pady = 10)

    #chama a tela de nova rotina
    botao = Button(janelaPadrao, text="Nova Rotina", command= novarotina)
    botao.grid(column=0, row=1, padx= 10, pady = 10)

    #chama a tela de organizar
    botao = Button(janelaPadrao, text="Organizar", command= organizar)
    botao.grid(column=0, row=3,padx= 10, pady = 10)

    # roda janela
    janelaPadrao.mainloop()

def rotinaVazia():
    #adiciona janela principal 
    janelaVazia = Tk()

    #Adiciona um título da janela invocada
    janelaVazia.title("Rotina")

    #Informação na janela
    texto_inicial = Label(janelaVazia, text="Gerador de Rotina") 
    texto_inicial.grid(column=2, row=0, padx=100, pady=200)

    #chama a tela de tarefa
    botao = Button(janelaVazia, text="Tarefas", command= tarefas)
    botao.grid(column=3, row=3,padx= 10, pady = 10)

    #chama a tela de nova rotina
    botao = Button(janelaVazia, text="Nova Rotina", command= novarotina)
    botao.grid(column=0, row=1, padx= 10, pady = 10)

    #chama a tela de organizar
    botao = Button(janelaVazia, text="Organizar", command= organizar)
    botao.grid(column=0, row=3,padx= 10, pady = 10)

    # roda janela
    janelaVazia.mainloop()


def organizar():
    pass



#adiciona janela principal 
janela = Tk()

#Adiciona um título da janela invocada
janela.title("Rotina")

#Informação na janela
texto_inicial = Label(janela, text="Gerador de Rotina") 
texto_inicial.grid(column=2, row=0, padx=100, pady=200)


#chama a tela de tarefa
botao = Button(janela, text="Tarefas", command= tarefas)
botao.grid(column=3, row=3,padx= 10, pady = 10)

#chama a tela de nova rotina
botao = Button(janela, text="Nova Rotina", command= novarotina)
botao.grid(column=0, row=1, padx= 10, pady = 10)

#chama a tela de organizar
botao = Button(janela, text="Organizar", command= organizar)
botao.grid(column=0, row=3,padx= 10, pady = 10)

# roda janela

janela.mainloop()