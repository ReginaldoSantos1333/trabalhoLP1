from cgitb import text
from doctest import master
from tkinter import *
from tkinter import messagebox
from upday import upday

def existe_rotina(rotinas, id):
    if len(rotinas)>0:
        for tarefa in rotinas:
            if tarefa['id'] == id:
                return True
        return False
    return False


def inserir(rotinas):

    insere = Tk()
    insere.title("Inserindo rotina!")
    insere_label = Label(insere, text = "Insira o código exclusivo dessa rotina: ")
    insere_label.pack(pady=30)
    def ingetnome():
        def inexit():
            insere.destroy()
            messagebox.showinfo(title="UP!!!!", message="UP-UP! A tarefa foi cadastrada com sucesso!")
        
        
        while True:
            if not existe_rotina(rotinas, id):
                break
            else:
                messagebox.showerror(title="Error", message="Esse código já está sendo utilizado.")
                messagebox.showerror(title="Error", message="Por favor, tente um novo e-mail.")
        if idboxTXT.get("1.0", END)=="\n":
            messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
            insere.destroy()    
        varid=idboxTXT.get(1.0,"end")
        tff = Toplevel()
        tff.grab_set()
        tff.title("Upday!")
        idlb = Label(tff, text = "Escreva uma nova tarefa para sua rotina!")
        idlb.pack(pady=20)
        def ingetnome2():
            if tfboxTXT.get("1.0", END)=="\n":
                messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                insere.destroy()
            vartf = tfboxTXT.get(1.0, "end")
            pp = Toplevel()
            pp.grab_set()
            pp.title("Upday!")
            pplb = Label(pp, text = "Para qual período do dia (Manha/Tarde/Noite) você gostaria de fazer essa tarefa?")
            pplb.pack(pady=20)
            def ingetnome3():
                if ppboxTXT.get("1.0", END)=="\n":
                    messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                    insere.destroy()
                varpp = ppboxTXT.get(1.0, "end")
                dd = Toplevel()
                dd.grab_set()
                dd.title("Upday!")
                ddlb = Label(dd, text = "Como você classifica essa atividade (Facil/Dificil)?")
                ddlb.pack(pady=20)
                def ingetnome4():
                    if ddboxTXT.get("1.0", END)=="\n":
                        messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                        insere.destroy()
                    vardd = ddboxTXT.get(1.0, "end")
                    tarefa = {"nr":vartf,"p":varpp,"d":vardd,"id":varid}
                    rotinas.append(tarefa)
                    inexit()
                ddboxTXT = Text(dd, height = 0, width=12)
                ddboxTXT.pack(pady = 30)
                in4botao1 = Button(dd, text= "Pronto!", command = ingetnome4)
                in4botao1.pack(pady = 30)
            ppboxTXT = Text(pp, height = 0, width=12)
            ppboxTXT.pack(pady = 30)
            in3botao1 = Button(pp, text= "Pronto!", command = ingetnome3)
            in3botao1.pack(pady = 30)
        tfboxTXT = Text(tff, height = 0, width=12)
        tfboxTXT.pack(pady = 30)
        in2botao1 = Button(tff, text= "Pronto!", command = ingetnome2)
        in2botao1.pack(pady = 30)
    idboxTXT = Text(insere, height = 0, width=12)
    idboxTXT.pack(pady = 30)
    inbotao1 = Button(insere, text= "Pronto!", command = ingetnome)
    inbotao1.pack(pady = 30)
    def on_closing():
            if messagebox.askokcancel("", "Deseja mesmo cancelar ?"):
                insere.destroy()

    insere.protocol("WM_DELETE_WINDOW", on_closing)     
    insere.mainloop()

def editar(rotinas):
    if len(rotinas) > 0:
        edita = Tk()
        edita.title("== Vamos mudar algumas coisas ==")
        edita_label = Label(edita, text = "Insira o id da tarefa a ser alterada: ")
        edita_label.pack(pady=30)
        def edgetnome():
            def edexit():
                edita.destroy()
                messagebox.showinfo(title="UP!!!!", message="UP-UP! Os dados foram alterados com sucesso!")
            if edboxTXT.get("1.0", END)=="\n":
                messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                edita.destroy()
            edvarid=edboxTXT.get(1.0,"end")
            id = edvarid
            if existe_rotina(rotinas, id):
                edinfo = Toplevel()
                show_label = Label(edinfo, text= "O id foi encontrado. Seguem abaixo as informações da tarefa:")
                show_label.pack()
                for tarefa in rotinas:
                    if tarefa['id'] == id:
                        edshow = Toplevel()
                        tfshow_label = Label(edshow, text ="Tarefa: {}".format(tarefa['nr']))
                        ppshow_label = Label(edshow, text="Período: {}".format(tarefa['p']))
                        ddshow_label = Label(edshow, text="Dificuldade: {}".format(tarefa['d']))
                        idshow_label = Label(edshow, text="Identificação: {}".format(tarefa['id']))
                        barshow_label = Label(edshow, text="=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        tfshow_label.pack(pady=20)
                        ppshow_label.pack(pady=20)
                        ddshow_label.pack(pady=20)
                        idshow_label.pack(pady=20)
                        barshow_label.pack(pady=20)
                        newrtn = Tk()
                        newrtn.title("Mudando algumas coisas.. ")
                        newrtn_label = Label(newrtn, text = "Insira a nova rotina: ")
                        newrtn_label.pack(pady=30)
                        def newrtngetnome():
                            if newrtnboxTXT.get("1.0", END)=="\n":
                                messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                                edita.destroy()
                            newrtnf=newrtnboxTXT.get
                            print({"nr"}) in rotinas[0]
                            #rotinas[0] = newrtnf

                            pprtn = Toplevel()
                            pprtn_label = Label(pprtn, text = "Insira o novo período: ")
                            pprtn_label.pack(pady=30)
                            def pprtngetnome():
                                if pprtnboxTXT.get("1.0", END)=="\n":
                                    messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                                    edita.destroy()
                                pprtnf=pprtnboxTXT.get
                                #rotinas[1] = pprtnf
                                ddrtn = Toplevel()
                                ddrtn_label = Label(ddrtn, text = "Insira a nova dificuldade: ")
                                ddrtn_label.pack(pady=30)
                                def ddrtngetnome():
                                    if ddrtnboxTXT.get("1.0", END)=="\n":
                                        messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                                        edita.destroy()
                                    ddrtnf=ddrtnboxTXT.get
                                    #rotinas[2] = ddrtnf
                                    edexit()
                                ddrtnboxTXT = Text(ddrtn, height = 0, width=12)
                                ddrtnboxTXT.pack(pady = 30)
                                ddrtnbotao1 = Button(ddrtn, text= "Pronto!", command = ddrtngetnome)
                                ddrtnbotao1.pack(pady = 30)
                            pprtnboxTXT = Text(pprtn, height = 0, width=12)
                            pprtnboxTXT.pack(pady = 30)
                            pprtnbotao1 = Button(pprtn, text= "Pronto!", command = pprtngetnome)
                            pprtnbotao1.pack(pady = 30)
                        newrtnboxTXT = Text(newrtn, height = 0, width=12)
                        newrtnboxTXT.pack(pady = 30)
                        newrtnbotao1 = Button(newrtn, text= "Pronto!", command = newrtngetnome)
                        newrtnbotao1.pack(pady = 30)
                        newrtn.mainloop()
            else:messagebox.showerror(title="Error", message="Por favor, tente um novo e-mail.")            
        edboxTXT = Text(edita, height = 0, width=12)
        edboxTXT.pack(pady = 30)
        edbotao1 = Button(edita, text= "Pronto!", command = edgetnome)
        edbotao1.pack(pady = 30)
        def on_closing():
            if messagebox.askokcancel("", "Deseja mesmo cancelar ?"):
                edita.destroy()

        edita.protocol("WM_DELETE_WINDOW", on_closing)     
        edita.mainloop()

    else:
        messagebox.showerror(title="Error", message="Não existe nenhuma tarefa cadastrada no roteiro.")    
            

def buscar(rotinas):
    if len(rotinas) > 0:
        busca = Tk()
        busca.title("== Onde estão aquelas Tarefas?! ==")
        busca_label = Label(busca, text = "Digite o Id da tarefa a ser encontrada: ")
        busca_label.pack(pady=30)
        def bgetnome():
            bvar=bboxTXT.get(1.0,"end")
            id = bvar
            if existe_rotina(rotinas, id):
                busca_label = Label(busca, text = "A tarefa foi localizada. As informações sobre tal são: ")
                busca_label.pack(pady=30)
                for tarefa in rotinas:
                    if tarefa['id'] == id:
                        bshow = Toplevel()
                        tfbshow_label = Label(bshow, text ="Tarefa: {}".format(tarefa['nr']))
                        ppbshow_label = Label(bshow, text="Período: {}".format(tarefa['p']))
                        ddbshow_label = Label(bshow, text="Dificuldade: {}".format(tarefa['d']))
                        idbshow_label = Label(bshow, text="Identificação: {}".format(tarefa['id']))
                        #barbshow_label = Label(bshow, text="=-=-=-=-=-=-=-=-=-=-=\n")
                        tfbshow_label.pack(pady=30)
                        ppbshow_label.pack(pady=30)
                        ddbshow_label.pack(pady=30)
                        idbshow_label.pack(pady=30)
                        #barbshow_label.pack(pady=30)
            else: messagebox.showerror(title="Error", message="Não existe tarefa cadastrada no sistema com esse id ! ")
        bboxTXT = Text(busca, height = 0, width=12)
        bboxTXT.pack(pady = 30)
        bbotao1 = Button(busca, text= "Pronto!", command = bgetnome)
        bbotao1.pack(pady = 30)
        def on_closing():
            if messagebox.askokcancel("", "Deseja mesmo cancelar ?"):
                busca.destroy()

        busca.protocol("WM_DELETE_WINDOW", on_closing)         
        busca.mainloop()

    else: messagebox.showerror(title="Error", message="Não existe nenhuma tarefa cadastrada no roteiro.")

def visualizar(rotinas):
    if len(rotinas) > 0:
        visualiza = Tk()
        visualiza.title("Minhas tarefas: ")
        visu_label = Label(visualiza, text = "== Estoque de Tarefas == ")
        visu_label.pack(pady=30)
        for i, tarefa in enumerate(rotinas):
            idvshow_label = Label(visualiza, text ="Tarefa Nº{}:".format(i+1))
            tfvshow_label = Label(visualiza, text ="Tarefa: {}".format(tarefa['nr']))
            ppvshow_label = Label(visualiza, text="Período: {}".format(tarefa['p']))
            ddvshow_label = Label(visualiza, text="Dificuldade: {}".format(tarefa['d']))
            idvshow_label = Label(visualiza, text="Identificação: {}".format(tarefa['id']))
            idvshow_label.pack(pady=30)
            tfvshow_label.pack(pady=30)
            ppvshow_label.pack(pady=30)
            ddvshow_label.pack(pady=30)

            qtdshow_label = Label(visualiza, text ="Quantidade de Tarefas Registradas: {}\n".format(len(rotinas)))
            qtdshow_label.pack(pady=30)
        def vexit ():
            visualiza.destroy()
        visubotao1 = Button(visualiza, text= "Ok!", command = vexit)
        visubotao1.pack(pady = 30)
        def on_closing():
            if messagebox.askokcancel("", "Deseja mesmo cancelar ?"):
                visualiza.destroy()

        visualiza.protocol("WM_DELETE_WINDOW", on_closing)     
        visualiza.mainloop()
    else: messagebox.showerror(title="Error", message="Não foi encontrado nenhuma rotina no nosso sistema :( ")


def apagar(rotinas):
    if len(rotinas) > 0:
        apaga = Tk()
        apaga.title("Ficou monótono ? :/")
        visu_label = Label(apaga, text = "Digite a numeração da tarefa a ser deletada: ")
        visu_label.pack(pady=30)
        def agetnome():
            if aboxTXT.get("1.0", END)=="\n":
                messagebox.showerror(title="Error", message="Não são permitidas tarefas vazias")
                apaga.destroy()
            agetid = aboxTXT.get(1.0,"end")
            id = agetid
            if existe_rotina(rotinas, id): 
                vmostra = Toplevel()
                visu_label = Label(apaga, text = "Tarefa encontrada! As informações da mesma se apresentam abaixo: ")
                visu_label.pack(pady=30)
                for i, tarefa in enumerate(rotinas):
                    if tarefa['id'] == id:
                        idvshow_label = Label(vmostra, text ="Tarefa Nº{}:".format(i+1))
                        tfvshow_label = Label(vmostra, text ="Tarefa: {}".format(tarefa['nr']))
                        ppvshow_label = Label(vmostra, text="Período: {}".format(tarefa['p']))
                        ddvshow_label = Label(vmostra, text="Dificuldade: {}".format(tarefa['d']))
                        idvshow_label = Label(vmostra, text="Identificação: {}".format(tarefa['id']))
                        idvshow_label.pack(pady=30)
                        tfvshow_label.pack(pady=30)
                        ppvshow_label.pack(pady=30)
                        ddvshow_label.pack(pady=30)
                        
                        
                        del rotinas[i]
                        def apagan ():
                            messagebox.showinfo(title="UP!!!!", message="UP-UP! A rotina foi deletada com sucesso!")
                            apaga.destroy()
                        visubotao1 = Button(vmostra, text= "Ok!", command = apagan)
                        visubotao1.pack(pady = 30) 
                        
            else: messagebox.showerror(title="Error", message="Não existe nenhuma tarefa com essa numeração :( ")

        aboxTXT = Text(apaga, height = 0, width=12)
        aboxTXT.pack(pady = 30)
        abotao1 = Button(apaga, text= "Pronto!", command = agetnome)
        abotao1.pack(pady = 30)

        def on_closing():
            if messagebox.askokcancel("Fechar", "Deseja mesmo cancelar ?"):
                apaga.destroy()

        apaga.protocol("WM_DELETE_WINDOW", on_closing) 
        apaga.mainloop()   
         
    else: messagebox.showerror(title="Error", message="Me parece que você ainda não adicionou nenhuma tarefa ainda... só acho... ")
    

        
   

#As funções estão reunidas em outro código para organização

#Aqui é a base central do funcionamento do aplicativo
def principal():
    
    #Dicionário
    rotinas = []

    
    janela1 = Tk()
    def exit():
        janela1.destroy()
    text_label = Label(janela1, text = """Olá! Bem vindo(a) à UPday!")
    Juntos podemos dar um 'Up' no seu dia ;)")
        Primeiramente, seria ótimo te conhecer mais um pouco. Vamos começar?!
        =====================================================
    """)
    text_label.pack()
    botao1 = Button(janela1, text= "Ok!", command = exit)
    botao1.pack()

    janela1.mainloop()
    
    def refresh():
        janela2 = Tk()
        def exit():
            janela2.destroy()
        def getnome():
            if boxTXT.get(1.0, "end")=="\n":
                messagebox.showerror(title="Error", message="Vamos lá! Nos conte seu nome :)")
                janela2.destroy()
                refresh()
            var=boxTXT.get(1.0,"end")
            result = var
            wcm = Toplevel()
            wcm.title("Bem Vindo!")
            l2 = Label(wcm, text = "Ficamos muito felizes em te conhecer {}".format(result))
            l2.pack(pady=20)
            l3 = Label(wcm ,text = "Agora, vamos começar a dar o 'UP' que sua rotina precisa :)")
            l3.pack(pady=20)
            l4 = Label(wcm, text = "Aqui está o menu do seu gerador de rotina pessoal, {}".format(result))
            l4.pack(pady=20)
            l5 = Label(wcm, text = "Experimente!")
            l5.pack(pady=20)
            botaoOk = Button(wcm, text = "Ok!", command= exit)
            botaoOk.pack(pady=20)
        janela2.title("Bem Vindo!")
        text_label = Label (janela2, text= "Digite seu nome :")
        text_label.pack(padx=60)    
        boxTXT = Text(janela2, height = 0, width=12)
        boxTXT.pack()
        botao1 = Button(janela2, text= "Pronto!", command = getnome)
        botao1.pack()
    
    refresh()

    mainW = Tk()
    # Muda a corda janela principal
    mainW.configure(background="lightblue")
    # Titulo da janela
    mainW.title("UPday")
    # Traz janela para frente 
    mainW.lift()
    #Label com o nome do app, cor de fundo,texto e sua fonte
    texto_inicial = Label(mainW, text = "UPday",bg = "lightblue",fg = "black")
    texto_inicial.configure(font=("Segoe Print", 60))
    texto_inicial.grid(column=1,row=0, padx = 100,pady = 300)
    # Botão de inserção
    insert = Button(mainW, text = "Nova Rotina", command= lambda: inserir(rotinas))
    insert.grid(column=0,row=6, padx = 10,pady = 10)
    # Botão de edição
    edit = Button(mainW, text= "Editar Rotina", command=lambda: editar(rotinas))
    edit.grid(column=0,row=7, padx = 10,pady = 10)
    # Botão de buscar
    search = Button(mainW, text= "Buscar Rotina", command=lambda:buscar(rotinas))
    search.grid(column=0,row=8, padx = 10,pady = 10)
    # Botão de visualiza
    check = Button(mainW, text= "Ver Rotina", command=lambda: visualizar(rotinas))
    check.grid(column=2,row=6, padx = 10,pady = 10)
    # Botão de upday
    Upd = Button(mainW, text = "UPday Rotina", command=lambda: upday(rotinas))
    Upd.grid(column=2,row=7, padx = 10,pady = 10)
    # Botão de apagar
    erase = Button(mainW, text = "Apagar Rotina", command=lambda: apagar(rotinas))
    erase.grid(column=2,row=8, padx = 10,pady = 10)

    def on_closing():
        if messagebox.askokcancel("Fechar", "Quer mesmo sair ?"):
            messagebox.showinfo(title="Até logo!", message="Lembre-se, sempre há tempo para dar um 'UP' na sua vida!")
            mainW.destroy()

    mainW.protocol("WM_DELETE_WINDOW", on_closing)
    mainW.mainloop()
    

principal()
