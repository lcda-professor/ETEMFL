import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 06 - StringVar em tempo real")
janela.geometry("400x200")

# Criando uma StringVar (variável do Tkinter)
texto = tk.StringVar()

# Entry ligado à StringVar
entrada = tk.Entry(janela, textvariable=texto, font=("Sans", 14))
entrada.pack(pady=10)

# Label também ligado à mesma StringVar
label = tk.Label(janela, textvariable=texto, font=("Sans", 16), fg="blue")
label.pack(pady=10)

janela.mainloop()
