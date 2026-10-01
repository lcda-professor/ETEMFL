import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - Questão 1")
janela.geometry("400x100")

frame = tk.Frame(janela, bd=3, relief="ridge")
frame.pack(fill="both", expand=True)

lblNome = tk.Label(frame, text="Nome:")
lblEmail = tk.Label(frame, text="E-mail: ")
campoNome = tk.Entry(frame)
campoEmail = tk.Entry(frame)

lblNome.grid(row=0, column=0, padx=5, pady=5)
lblEmail.grid(row=1, column=0, padx=5, pady=5)
campoNome.grid(row=0, column=1, padx=5, pady=5)
campoEmail.grid(row=1, column=1, padx=5, pady=5)

janela.mainloop()