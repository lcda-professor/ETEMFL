import tkinter as tk

estado=True

def mudarTexto():
    global estado
    if estado:
        btn.config(text="Modo Escuro")
        janela.config(bg="black")
        estado = False
    else:
        btn.config(text="Modo Claro")
        janela.config(bg="white")
        estado = True

janela = tk.Tk()
janela.title("Lista 3 - Questão 4")
janela.geometry("500x300")
janela.config(bg="white")

btn = tk.Button(janela, text="Modo Claro", command=mudarTexto)
btn.pack(pady=20)

janela.mainloop()

