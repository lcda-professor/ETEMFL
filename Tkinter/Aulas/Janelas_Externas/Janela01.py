import tkinter as tk
import Janela02 as j2

def abrirJanela():
    global janela01
    janela01 = tk.Tk()
    janela01.geometry("800x600")

    tk.Label(janela01, text="Esta é a janela 01").pack(pady=20)
    tk.Button(janela01, text="ir para outra janela", command=abrirNovaJanela).pack(pady=20)

    janela01.mainloop()

def abrirNovaJanela():
    janela01.destroy()
    j2.abrirJanela()