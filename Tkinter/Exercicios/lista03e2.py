import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - Questão 2")
janela.geometry("400x300")

frame = tk.Frame(janela, bd=3, relief="ridge")
frame.pack(fill="both", expand=True)

campo = tk.Entry(frame)
campo.config(bg="lightyellow")
campo.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
frame.grid_columnconfigure(0, weight=1)

janela.mainloop()