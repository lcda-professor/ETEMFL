import tkinter as tk
from deep_translator import GoogleTranslator

def traduzir(cor):
    cor = GoogleTranslator(source='pt', target='en').translate(cor)
    return cor

def aplicarCor(cor):
    janela.config(bg=traduzir(cor))
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Lista 02 - Questão 03")
janela.geometry("700x300")
janela.bind("<Return>", lambda event: aplicarCor(entrada.get()))

label = tk.Label(janela, text=("Digite uma cor em Inglês - red, green, blue, etc."))
label.pack(pady=10)

entrada = tk.Entry(janela, justify="center")
entrada.pack(pady=10)

botao = tk.Button(janela, text="Aplicar cor", command=lambda: aplicarCor(entrada.get()))
botao.pack(pady=10)

janela.mainloop()