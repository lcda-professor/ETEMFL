import tkinter as tk
import tkinter.font as tkFont

janela = tk.Tk()
janela.title("Questão 2 - Lista 2")
janela.geometry("500x500")

fonteNormal = tkFont.Font(font=("Sams", 15))
fonteContraste = tkFont.Font(weight="bold", slant="italic")

label = tk.Label(janela, text=("Olá, turma!"))
label.pack(expand=True)

btnNormal = tk.Button(janela, text="Normal", command=lambda: label.config(font=fonteNormal))
btnNormal.pack(expand=True)

btnContraste = tk.Button(janela, text="Contraste", command=lambda: label.config(font=fonteContraste))
btnContraste.pack(expand=True)

janela.mainloop()
