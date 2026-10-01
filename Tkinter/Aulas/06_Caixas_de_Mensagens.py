"""Para mais informações sobre este assunto, consulte a documentação oficial
em: https://docs.python.org/3/library/tkinter.messagebox.html"""

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Caixas de Mensagens")
janela.geometry("800x600")

def infoLabel(mensagem):
    labInfo.config(text=mensagem)

def caixaInfo(): #exibir uma mensagem de informação
    messagebox.showinfo("Informação", "Operação concluída com sucesso!")
    infoLabel("")

def caixaAviso(): #exibir um aviso
    messagebox.showwarning("Aviso", "Cuidado! Essa ação pode alterar os dados.")
    infoLabel("")

def caixaErro(): #exibir um erro
    messagebox.showerror("Erro", "Não foi possível salvar o arquivo.")
    infoLabel("")

def caixaConfir(): #confirmação do usuário com sim/não
    #askyesno() retorna True (Sim) ou False (Não).
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente excluir o item?")

    if resposta:
        infoLabel("Usuário confirmou a exclusão.")
    else:
       infoLabel("Usuário cancelou.")

def caixaMulOpt(): #caixa de pergunta com múltiplas opções
    #askquestion() retorna 'yes' ou 'no'
    resposta = messagebox.askquestion("Pergunta", "Deseja continuar o processo?")

    if resposta == "yes":
        infoLabel("Continuando...")
    else:
        infoLabel("Cancelado.")

def caixaOkCancel(): #caixa de confirmação OK/Cancelar
    resposta = messagebox.askokcancel("Confirmação", "Deseja salvar as alterações?")

    if resposta:
        infoLabel("Usuário clicou OK.")
    else:
        infoLabel("Usuário clicou Cancelar.")

def caixaRetryCancel(): #caixa de confirmação retry(tentar de novo) ou Cancelar
    resposta = messagebox.askretrycancel("Erro de conexão", "Falha ao conectar. Tentar novamente?")

    if resposta:
        infoLabel("Tentando novamente...")
    else:
        infoLabel("Cancelado pelo usuário.")

labTitulo = tk.Label(janela,text="Tipos de Caixas de Mensagens",font=("Sans", 20, "bold"))
labInfo = tk.Label(janela,text="",font=("Sans", 16, "bold"), fg="blue")
btnCaixaInfo = tk.Button(janela,text="Caixa de Informação",command=caixaInfo)
btnCaixaAviso = tk.Button(janela,text="Caixa de Aviso",command=caixaAviso)
btnCaixaErro = tk.Button(janela,text="Caixa de Erro",command=caixaErro)
btnCaixaConfirma = tk.Button(janela,text="Caixa de Confirmação",command=caixaConfir)
btnCaixaMultOpt = tk.Button(janela,text="Caixa de Múltiplas Opções",command=caixaMulOpt)
btnCaixaOkCancel = tk.Button(janela,text="Caixa de Conf. Ok/Cancel",command=caixaOkCancel)
btnCaixaRetryCancel = tk.Button(janela,text="Caixa de Conf. Retry/Cancel",command=caixaRetryCancel)

labTitulo.pack(pady=20)
btnCaixaInfo.pack(pady=10)
btnCaixaAviso.pack(pady=10)
btnCaixaErro.pack(pady=10)
btnCaixaConfirma.pack(pady=10)
btnCaixaMultOpt.pack(pady=10)
btnCaixaOkCancel.pack(pady=10)
btnCaixaRetryCancel.pack(pady=10)
labInfo.pack(pady=30)

janela.mainloop()
