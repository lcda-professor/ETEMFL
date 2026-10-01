import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - questão 3")
janela.geometry("400x300")

frame = tk.Frame(janela, relief="ridge", bd=3)
frame.pack(fill="both", expand=True)

botao = tk.Button(frame, text="Mudar cor", command=lambda:frame.config(bg="lightblue"))
botao.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame.rowconfigure(0, weight=1)

janela.mainloop()