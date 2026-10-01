import tkinter as tk

janela = tk.Tk()
janela.title("Fomrulário com BD")
janela.geometry("500x500")

frame = tk.LabelFrame(janela, text="Dados do Cliente", relief="ridge", bd=3)
frame.pack(fill="both", expand=True)