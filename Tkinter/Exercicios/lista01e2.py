import tkinter as tk

def verificar():
    numero = int(entradaNumero.get())
    if numero % 2 == 0:
        lblResultado.configure(text=f"O número {numero} é par")
    else:
        lblResultado.configure(text=f"O número {numero} é ímpar")

janela = tk.Tk()
janela.title("Par ou Ímpar")
janela.geometry("600x400")

lblNumero = tk.Label(janela, text="Digite o número: ")
lblNumero.pack(pady=10)

entradaNumero = tk.Entry(janela, justify="center")
entradaNumero.pack(pady=10)

btnVerificar = tk.Button(janela, text="Verificar", command=verificar)
btnVerificar.pack(pady=10)

lblResultado = tk.Label(janela, text="")
lblResultado.pack(pady=10)

janela.mainloop()