import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - Questão 5")
janela.geometry("800x600")

frame = tk.Frame(janela, relief="ridge", bd=3)
frame.pack(expand=True, fill="both")

lbl_1 = tk.Label(frame, bg="blue", text="Label")
lbl_1.grid(row=0, column=0, sticky="nsew")
lbl_2 = tk.Label(frame, bg="yellow", text="Label")
lbl_2.grid(row=0, column=1, sticky="nsew")
lbl_3 = tk.Label(frame, bg="green", text="Label")
lbl_3.grid(row=0, column=2, sticky="nsew")
lbl_4 = tk.Label(frame, bg="red", text="Label")
lbl_4.grid(row=1, column=0, sticky="nsew")
lbl_5 = tk.Label(frame, bg="pink", text="Label")
lbl_5.grid(row=1, column=1, sticky="nsew")
lbl_6 = tk.Label(frame, bg="orange", text="Label")
lbl_6.grid(row=1, column=2, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=5)
frame.rowconfigure(1, weight=1)

janela.mainloop()

