from tkinter import *
from time import *


janela = Tk()
janela.geometry("320x400")
janela.title("contagem Regressiva")
janela.configure()

Label1 = Label(janela, text="Contagem")
Label1.place(x=10, y=10)

label2 = Label(janela, text="")
label2.place(x=20, y=40)

sec = int(20)


def Contagem():


     global sec


     if sec == None:
                sec['Text'] = "TENTE NOVAMENTE|"
     if sec == 0:

               label2['text'] = 'BOOOOOOOMMM'
               sec = int(20)
     else:
            sec = int(sec - 1)
            label2['text'] = sec
            label2.after(1000, Contagem)




botao = Button(janela, text="Confirma", command=Contagem)
botao.place(x=30, y=60)


mainloop()