import tkinter as tk

def somar():
    soma = int(campo1.get())+int(campo2.get())
    if soma >= 0:
        lblSoma.config(text=soma, fg="white", bg="blue")
    else:
        lblSoma.config(text=soma, fg="red", bg="green")

janela = tk.Tk()
janela.title("Somar")
janela.geometry("400x400")

lblNum1 = tk.Label(janela, text="1º Número:")
lblNum1.pack(pady=10)

campo1 = tk.Entry(janela)
campo1.pack(pady=10)

lblNum2 = tk.Label(janela, text="2º Número:")
lblNum2.pack(pady=10)

campo2 = tk.Entry(janela)
campo2.pack(pady=10)

btnSomar = tk.Button(janela, text="Somar", command=somar)
btnSomar.pack(pady=10)

lblSoma = tk.Label(janela, text="", font=('Sans', 25))
lblSoma.pack(pady=10)

janela.mainloop()