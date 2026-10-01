import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - Questão 4")
janela.geometry("400x300")

frame = tk.Frame(janela, relief="raised", bd=5)
frame.pack(fill="both", expand=True)

campo1 = tk.Entry(frame)
campo2 = tk.Entry(frame)

campo1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
campo2.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
frame.columnconfigure(0, weight=1)

btn = tk.Button(janela, text="Preencher", command=lambda:
                (campo1.insert(0,"Este é o campo 1"), campo2.insert(0,"Este é o campo 2")))
btn.pack(fill="x", padx=5, pady=5)

janela.mainloop()
