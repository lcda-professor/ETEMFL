import tkinter as tk

def somar():
    numero = int(lblResultado.cget("text"))
    numero+=1
    lblResultado.config(text=numero)

def subtrair():
    numero = int(lblResultado.cget("text"))
    numero-=1
    lblResultado.config(text=numero)

janela = tk.Tk()
janela.title("Contador")
janela.geometry("400x400")

lblResultado = tk.Label(janela, text="0")
lblResultado.pack(pady=10)

btnSoma = tk.Button(janela, text="+", command=somar)
btnSoma.pack()

btnSubtrair = tk.Button(janela, text="-", command=subtrair)
btnSubtrair.pack()

janela.mainloop()