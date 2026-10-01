import tkinter as tk

janela = tk.Tk()
janela.title("Lista 2 - Questão 5")
janela.geometry("500x200")

texto = tk.StringVar()

campo = tk.Entry(janela, textvariable=texto)
campo.pack(pady=20)

label = tk.Label(janela, textvariable=texto, fg="blue")
label.pack(pady=20)

janela.mainloop()