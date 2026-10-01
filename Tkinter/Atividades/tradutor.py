import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def converter():
    sc = comboOrigem.get()
    tg = comboDestino.get()

    for i in idiomas:
        if i == sc:
            sc = idiomasTradutor[idiomas.index(i)]
        if i == tg:
            tg = idiomasTradutor[idiomas.index(i)]
    
    return sc, tg

def traduzir(texto):
    sc, tg = converter()
    textoTraduzido = GoogleTranslator(source=sc, target=tg).translate(texto)
    print(textoTraduzido)
    lblTextoTraduzido.config(text=textoTraduzido)
    campoTextoTraduzir.delete(0, tk.END)
    comboOrigem.set("Origem")
    comboDestino.set("Destino")
    return textoTraduzido

#principal
janela = tk.Tk()
janela.geometry("900x400")
janela.title("Tradutor 1.0")

frameUm = tk.Frame(janela, bd=3, relief="ridge")
frameDois = tk.Frame(janela, bd=3, relief="ridge")

idiomas = ["Português", "Inglês", "Espanhol"]
idiomasTradutor = ["pt", "en", "es"]

#definição dos componentes
lblTextoTraduzir = tk.Label(frameUm, text="Digite o que quer traduzir: ")
campoTextoTraduzir = tk.Entry(frameUm)

lblSetas = tk.Label(frameUm, text="<====>")

comboOrigem = ttk.Combobox(frameUm, values=idiomas, state="readonly")
comboOrigem.set("Idioma de origem")

comboDestino = ttk.Combobox(frameUm, values=idiomas, state="readonly")
comboDestino.set("Idioma de destino")

btnTraduzir = tk.Button(frameUm, text="Traduzir", bg="green", fg="white", command=lambda: traduzir(campoTextoTraduzir.get()))

lblTextoTraduzido = tk.Label(frameDois, text="")

#organização do layout
lblTextoTraduzir.grid(row=0, column=0, sticky="ew")
campoTextoTraduzir.grid(row=0, column=2, sticky="nsew")
comboOrigem.grid(row=1, column=0, sticky="ew")
lblSetas.grid(row=1, column=1, sticky="ew")
comboDestino.grid(row=1, column=2, sticky="ew")
btnTraduzir.grid(row=2, column=1)
lblTextoTraduzido.grid(row=0, column=0, sticky="ew")

frameUm.pack(fill="both", expand=True)
frameUm.columnconfigure(0, weight=1)
frameUm.columnconfigure(2, weight=1)
frameUm.rowconfigure(0, weight=1)
frameUm.rowconfigure(1, weight=1)

frameDois.pack(fill="both", expand=True)

janela.mainloop()
