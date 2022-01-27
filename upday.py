import random
from tkinter import *
from tkinter import messagebox



aleatoriedade = int(random.randint(1, 20))

def upday(rotinas):
    upd = Tk()
    upd.title("Hora do *UPday!*")

    updshow_label = Label(upd, text= "Quero saber de você, como deseja o *nível* da sua rotina?\n(3 - Pega Leve!) ou (4 - Vem monxxtrooo!)")
    updshow_label.pack()
  
    def choice():
        if choiceboxTXT.get(1.0, "end")=="\n":
            messagebox.showerror(title="Error", message="Escolha inválida!")
            upd.destroy()
        elif choiceboxTXT.get(1.0, "end-1c") > "4":
            messagebox.showwarning(title="Aviso!", message="Entrada inválida!")
            upd.destroy()
        elif choiceboxTXT.get(1.0,"end-1c") < "3":
            messagebox.showwarning(title="Aviso!", message="Entrada inválida!")
            upd.destroy()
        ch=choiceboxTXT.get(1.0, "end")
        dificuldade = int(ch)
        tamanho = len(rotinas)
        i=0
        while i <= tamanho:
             
            escolher_tarefa = rotinas[0]
            if escolher_tarefa == []:
                pass
            else: 
                nr = escolher_tarefa['nr']
                p = escolher_tarefa['p']
                d = escolher_tarefa['d']
                if (p) == 'Manha' or (p) == 'manha':
                    if (d) == 'Facil' or (d) == 'facil':
                        atividades_manhaf = ['Ler', 'Alongamento','Jogar','Dançar','Ouvir podcast','Arrumar quarto','Meditar/Orar', 'Compromissos na agenda', 'Jardinagem', 'Pesquise sobre fatos que te chamam atenção','SpaDay','Assistir Stand UP', 'Descanse', 'Você decide!']
                        atividades_manhaf.append(nr)
                        i+=1
                    else:
                        atividades_manhad = ['Tocar instrumento', 'Caminhar','Exercícios pesados (pós-Alogamento)','Tutorial sobre algo desconhecido', 'Arrumar casa', 'Organizar e-mail', 'Trabalho Manual', 'Você decide!']
                        atividades_manhad.append(nr)
                        i+=1
                
                elif (p) == 'Tarde' or (p) == 'tarde':
                    if (d) == 'Facil'or (d) == 'facil':
                        atividades_tardef = ['Tocar instrumento','Alongamento','Desenhar','Definir metas e prioridades da semana','Assistir a um filme/série', 'Brainstorming: anote o que imaginar','Rede social','Orçamento', 'Networking', 'Dançar', 'Tempo com família/amigos', 'Compromissos na agenda', 'SpaDay', 'Você decide!']
                        atividades_tardef.append(nr)
                        i+=1
                    else:
                        atividades_tarded = ['Exercícios pesados','Arrumar a casa','Aprender nova receita','Doar itens antigos','Correr','Linkedin','Participe de um Webinar', 'Ir ao cinema','Ir ao museu', 'Organizar e-mail', 'BackUP dos seus equipamentos', 'Você decide!']
                        atividades_tarded.append(nr)
                        i+=1
                
                elif (p) == 'Noite' or (p) == 'noite':
                    if (d) == 'Facil' or (d) == 'facil':
                        atividades_noitef = ['Escreva sobre o seu dia', 'Assistir Stand UP', 'Ler', 'Rede social', 'Jogar', 'Tutorial sobre algo desconhecido', 'Jardinagem', 'Tempo com família/amigos', 'Ouvir podcast', 'Meditar/Orar', 'Procure novas músicas', 'Você decide!']
                        atividades_noitef.append(nr)
                        i+=1
                    else:
                        atividades_noited = ['Exercícios pesados (pós-Alogamento)','Curso online','Aprender novo idioma','Aprender nova receita', 'Acompanhar Bolsa de Valores', 'BackUP dos seus equipamentos', 'Orçamento', 'Trabalho Manual', 'Organizar e-mail', 'Você decide!']
                        atividades_noited.append(nr)
                        i+=1
                else:
                    i+=1
                    pass

        atividades_manhaf = ['Ler', 'Alongamento','Jogar','Dançar','Ouvir podcast','Arrumar quarto','Meditar/Orar', 'Compromissos na agenda', 'Jardinagem', 'Pesquise sobre fatos que te chamam atenção','SpaDay','Assistir Stand UP', 'Descanse', 'Você decide!']
        atividades_manhad = ['Tocar instrumento', 'Caminhar','Exercícios pesados (pós-Alogamento)','Tutorial sobre algo desconhecido', 'Arrumar casa', 'Organizar e-mail', 'Trabalho Manual', 'Você decide!']
        atividades_tardef = ['Tocar instrumento','Alongamento','Desenhar','Definir metas e prioridades da semana','Assistir a um filme/série', 'Brainstorming: anote o que imaginar','Rede social','Orçamento', 'Networking', 'Dançar', 'Tempo com família/amigos', 'Compromissos na agenda', 'SpaDay', 'Você decide!']        
        atividades_tarded = ['Exercícios pesados','Arrumar a casa','Aprender nova receita','Doar itens antigos','Correr','Linkedin','Participe de um Webinar', 'Ir ao cinema','Ir ao museu', 'Organizar e-mail', 'BackUP dos seus equipamentos', 'Você decide!']
        atividades_noitef = ['Escreva sobre o seu dia', 'Assistir Stand UP', 'Ler', 'Rede social', 'Jogar', 'Tutorial sobre algo desconhecido', 'Jardinagem', 'Tempo com família/amigos', 'Ouvir podcast', 'Meditar/Orar', 'Procure novas músicas', 'Você decide!']
        atividades_noited = ['Exercícios pesados (pós-Alogamento)','Curso online','Aprender novo idioma','Aprender nova receita', 'Acompanhar Bolsa de Valores', 'BackUP dos seus equipamentos', 'Orçamento', 'Trabalho Manual', 'Organizar e-mail', 'Você decide!']
        if dificuldade == 3:
            if aleatoriedade>=10:
                easy = Tk()
                easy.title("Rotina Leve")
                easyshow1_label = Label(easy, text ="Acordar - 06:20h")
                easyshow2_label = Label(easy, text ="Banho - 06:40h")
                easyshow3_label = Label(easy, text ="Café da Manhã - 06:55h")
                easyshow4_label = Label(easy, text ="{} - 07:10h-08h".format(random.choice(atividades_manhaf)))
                easyshow5_label = Label(easy, text ="Aula/Estudo - 08h-10h")
                easyshow6_label = Label(easy, text ="Aula/Estudo - 10h-12h")
                easyshow7_label = Label(easy, text ="Almoço - 12h")
                easyshow8_label = Label(easy, text ="Aula/Estudo - 13h-15h")
                easyshow9_label = Label(easy, text ="Descanso - 15h-15:30h")
                easyshow10_label = Label(easy, text = "{} - 15:30h-16:45h".format(random.choice(atividades_tarded)))
                easyshow11_label = Label(easy, text ="{} - 16:50h-17:30h".format(random.choice(atividades_tardef)))
                easyshow12_label = Label(easy, text ="Revisar conteúdo - 17:40h")
                easyshow13_label = Label(easy, text ="Jantar - 18h")
                easyshow14_label = Label(easy, text ="{} - 18:40h-19:55h".format(random.choice(atividades_noited)))
                easyshow15_label = Label(easy, text ="{} - 20h-21:30h".format(random.choice(atividades_noitef)))
                easyshow16_label = Label(easy, text ="Hora de Dormir - 22h")
                easyshow1_label.pack()
                easyshow2_label.pack()
                easyshow3_label.pack()
                easyshow4_label.pack()
                easyshow5_label.pack()
                easyshow6_label.pack()
                easyshow7_label.pack()
                easyshow8_label.pack()
                easyshow9_label.pack()
                easyshow10_label.pack()
                easyshow11_label.pack()
                easyshow12_label.pack()
                easyshow13_label.pack()
                easyshow14_label.pack()
                easyshow15_label.pack()
                easyshow16_label.pack()
                easy.mainloop()
            else:
                easy = Tk()
                easy.title("Rotina Leve")
                easy2show1_label = Label(easy, text ="Acordar - 07h")
                easy2show2_label = Label(easy, text ="Banho - 07:15h")
                easy2show3_label = Label(easy, text ="Café da Manhã - 07:30h")
                easy2show4_label = Label(easy, text ="Aula/Estudo - 08h-10h")
                easy2show5_label = Label(easy, text ="Aula/Estudo - 10h-12h")
                easy2show6_label = Label(easy, text ="Almoço - 12h")
                easy2show7_label = Label(easy, text ="{} - 12:40h-13:40h".format(random.choice(atividades_tardef)))
                easy2show8_label = Label(easy, text ="{} - 13:50h-14:30h".format(random.choice(atividades_tarded)))
                easy2show9_label = Label(easy, text ="Descanso - 14:30h-15:30h")
                easy2show10_label = Label(easy, text = "{} - 15:30h-16:45h".format(random.choice(atividades_tardef)))
                easy2show11_label = Label(easy, text ="{} - 16:45h-18h".format(random.choice(atividades_tardef)))
                easy2show12_label = Label(easy, text ="Jantar - 18h")
                easy2show13_label = Label(easy, text ="{} - 18:40h-19:55h".format(random.choice(atividades_noitef)))
                easy2show14_label = Label(easy, text ="Revisar conteúdo - 20h-20:30h")
                easy2show15_label = Label(easy, text ="{} - 20:45h-21:30h".format(random.choice(atividades_noited)))
                easy2show16_label = Label(easy, text ="{} - 21:45h-22:20h".format(random.choice(atividades_noitef)))
                easy2show17_label = Label(easy, text= "Hora de Dormir - 23h")
                easy2show1_label.pack()
                easy2show2_label.pack()
                easy2show3_label.pack()
                easy2show4_label.pack()
                easy2show5_label.pack()
                easy2show6_label.pack()
                easy2show7_label.pack()
                easy2show8_label.pack()
                easy2show9_label.pack()
                easy2show10_label.pack()
                easy2show11_label.pack()
                easy2show12_label.pack()
                easy2show13_label.pack()
                easy2show14_label.pack()
                easy2show15_label.pack()
                easy2show16_label.pack()
                easy2show17_label.pack()
                easy.mainloop()
        elif dificuldade == 4:
            if aleatoriedade>=10:
                hard = Tk()
                hard.title("Rotina Monxtruosa!")
                hardshow1_label = Label(hard, text ="Acordar - 06:20h")
                hardshow2_label = Label(hard, text ="Banho - 06:40h")
                hardshow3_label = Label(hard, text ="Café da Manhã - 06:55h")
                hardshow4_label = Label(hard, text ="{} - 07:10h-08h".format(random.choice(atividades_manhaf)))
                hardshow5_label = Label(hard, text ="Aula/Estudo - 08h-10h")
                hardshow6_label = Label(hard, text ="Aula/Estudo - 10h-12h")
                hardshow7_label = Label(hard, text ="Almoço - 12h")
                hardshow8_label = Label(hard, text ="Aula/Estudo - 13h-14h")
                hardshow9_label = Label(hard, text ="Descanso - 14h-14:30h")
                hardshow10_label = Label(hard, text = "{} - 14:45h-15:20h".format(random.choice(atividades_tardef)))
                hardshow11_label = Label(hard, text ="{} - 15:25h-16:45h".format(random.choice(atividades_tarded)))
                hardshow12_label = Label(hard, text ="{} - 16:50h-17:30h".format(random.choice(atividades_tarded)))
                hardshow13_label = Label(hard, text ="Jantar - 18h")
                hardshow14_label = Label(hard, text ="{} - 18:40h-19:55h".format(random.choice(atividades_noited)))
                hardshow15_label = Label(hard, text ="{} - 20h-21:30h".format(random.choice(atividades_noitef)))
                hardshow16_label = Label(hard, text ="Hora de Dormir - 22h")
                hardshow1_label.pack()
                hardshow2_label.pack()
                hardshow3_label.pack()
                hardshow4_label.pack()
                hardshow5_label.pack()
                hardshow6_label.pack()
                hardshow7_label.pack()
                hardshow8_label.pack()
                hardshow9_label.pack()
                hardshow10_label.pack()
                hardshow11_label.pack()
                hardshow12_label.pack()
                hardshow13_label.pack()
                hardshow14_label.pack()
                hardshow15_label.pack()
                hardshow16_label.pack()
                hard.mainloop()
            else:
                hard2 = Tk()
                hard2.title("Rotina Monxtruosa!")
                hard2show1_label = Label(hard2, text ="Acordar - 07h")
                hard2show2_label = Label(hard2, text ="Banho - 07:15h")
                hard2show3_label = Label(hard2, text ="Café da Manhã - 07:30h")
                hard2show4_label = Label(hard2, text ="Aula/Estudo - 08h-10h")
                hard2show5_label = Label(hard2, text ="Aula/Estudo - 10h-12h")
                hard2show6_label = Label(hard2, text ="Almoço - 12h")
                hard2show7_label = Label(hard2, text ="{} - 12:40h-13:40h".format(random.choice(atividades_tarded)))
                hard2show8_label = Label(hard2, text ="{} - 13:50h-14:30h".format(random.choice(atividades_tarded)))
                hard2show9_label = Label(hard2, text ="Descanso - 14:30h-15:30h")
                hard2show10_label = Label(hard2, text = "{} - 15:30h-16:45h".format(random.choice(atividades_tardef)))
                hard2show11_label = Label(hard2, text ="{} - 16:45h-18h".format(random.choice(atividades_tarded)))
                hard2show12_label = Label(hard2, text ="Jantar - 18h")
                hard2show13_label = Label(hard2, text ="{} - 18:40h-19:55h".format(random.choice(atividades_noitef)))
                hard2show14_label = Label(hard2, text ="Revisar conteúdo - 20h-20:30h")
                hard2show15_label = Label(hard2, text ="{} - 20:45h-21:30h".format(random.choice(atividades_noited)))
                hard2show16_label = Label(hard2, text ="{} - 21:45h-22:20h".format(random.choice(atividades_noited)))
                hard2show17_label = Label(hard2, text= "Hora de Dormir - 23h")
                hard2show1_label.pack()
                hard2show2_label.pack()
                hard2show3_label.pack()
                hard2show4_label.pack()
                hard2show5_label.pack()
                hard2show6_label.pack()
                hard2show7_label.pack()
                hard2show8_label.pack()
                hard2show9_label.pack()
                hard2show10_label.pack()
                hard2show11_label.pack()
                hard2show12_label.pack()
                hard2show13_label.pack()
                hard2show14_label.pack()
                hard2show15_label.pack()
                hard2show16_label.pack()
                hard2show17_label.pack()
                hard2.mainloop()

        
        else: messagebox.showerror(title="Error", message="Isso... com certeza não é uma opção...")

    choiceboxTXT = Text(upd, height = 0, width=12)
    choiceboxTXT.pack(pady = 30)
    choicebotao1 = Button(upd, text= "Pronto!", command = choice)
    choicebotao1.pack(pady = 30)

