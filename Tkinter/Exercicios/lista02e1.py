import tkinter as tk

janela = tk.Tk()
janela.title("Lsta 2 - Questão 1")
janela.geometry("500x500")

def mudar_cor(cor):
    janela.config(bg=cor)

btnVermelho = tk.Button(janela, text="Vermelho", command=lambda: mudar_cor("red"))
btnVermelho.pack(side="left", fill="none", expand=True)

btnVerde = tk.Button(janela, text="Verde", command=lambda: mudar_cor("green"))
btnVerde.pack(side="left", fill="none", expand=True)

btnAzul = tk.Button(janela, text="Azul", command=lambda:mudar_cor("blue"))
btnAzul.pack(side="left", fill="none", expand=True)

janela.mainloop()