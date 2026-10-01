import tkinter as tk
import Janela01 as j1

def abrirJanela():
    global janela02
    janela02 = tk.Tk()
    janela02.geometry("800x600")

    tk.Label(janela02, text="Esta é a janela 02").pack(pady=20)
    tk.Button(janela02, text="ir para outra janela", command=abrirNovaJanela).pack(pady=20)

    janela02.mainloop()

def abrirNovaJanela():
    janela02.destroy()
    j1.abrirJanela()