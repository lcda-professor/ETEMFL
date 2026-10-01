"""Criar formulário dividido em seções com LabelFrame
Requisitos:
 · Crie uma janela com dois LabelFrame:
·	O primeiro, chamado "Dados Pessoais", deve conter dois campos: "Nome" e "Idade" (Labels e Entries).
·	O segundo, chamado "Endereço", deve conter três campos: "Rua", "Cidade" e “Outras Informações” (Labels e Entries).
 · Use grid dentro de cada LabelFrame para organizar os campos em três linhas e duas colunas.
 · O campo “Outras Informações” deve ter largura e altura correspondentes ao tamanho da janela e os demais campos apenas a largura. Use campo.grid(sticky=”ew”) para apenas largura e campo.grid(sticky=”nsew”) para altura e largura.
 · Posicione os dois LabelFrame na janela principal usando pack(side=LEFT, padx=10, pady=10) e pack(side=RIGHT, padx=10, pady=10).
 · Adicione um botão "Confirmar" abaixo dos frames (no pack principal), que ao ser clicado exibe em um Label o texto "Dados salvos com sucesso!" e limpa todos os dados das Entries.
Dica: use LabelFrame(janela, text="Título") para criar uma seção com borda e título.
Dica: use entry.delete(0, END) para limpar.
"""
import tkinter as tk

janela = tk.Tk()
janela.title("Lista 3 - Questão 6")
janela.geometry("800x400")

janela.columnconfigure(0, weight=1, uniform="col")
janela.columnconfigure(1, weight=1, uniform="col")
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)

frame1 = tk.LabelFrame(janela, text="Dados Pessoais", relief="ridge", bd=3)
frame1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

labelNome = tk.Label(frame1, text="Nome")
labelNome.grid(row=0, column=0, padx=5, pady=5)
labelIdade = tk.Label(frame1, text="Idade")
labelIdade.grid(row=1, column=0, padx=5, pady=5)
campoNome = tk.Entry(frame1)
campoNome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
campoIdade = tk.Entry(frame1)
campoIdade.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

frame2 = tk.LabelFrame(janela, text="Endereço", relief="ridge", bd=3)
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

labelRua = tk.Label(frame2, text="Rua")
labelRua.grid(row=0, column=0, padx=5, pady=5)
labelCidade = tk.Label(frame2, text="Cidade")
labelCidade.grid(row=1, column=0, padx=5, pady=5)
labelOutras = tk.Label(frame2, text="Outras")
labelOutras.grid(row=2, column=0, padx=5, pady=5)
campoRua = tk.Entry(frame2)
campoRua.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
campoCidade = tk.Entry(frame2)
campoCidade.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
CampoOutras = tk.Entry(frame2)
CampoOutras.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

btnConfirmar = tk.Button(janela, text="Confirmar")
btnConfirmar.grid(row=1, column=1, padx=5, pady=5, sticky="e")

janela.mainloop()