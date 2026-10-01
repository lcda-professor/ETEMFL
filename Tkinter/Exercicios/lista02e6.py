import tkinter as tk

janela = tk.Tk()
janela.title("Lista 02 - Questão 6")
janela.geometry("1000x250")

lblUsuario = tk.Label(janela, text="Usuário", font=("Sans", 12, "bold"))
lblUsuario.pack(side="left", padx=10)

campousuario = tk.Entry(janela)
campousuario.pack(side="left", fill="x", expand=True, padx=10)

lblSenha = tk.Label(janela, text="Senha", font=("Sans", 12, "bold"))
lblSenha.pack(side="left", padx=10)

campoSenha = tk.Entry(janela, show="*")
campoSenha.pack(side="left", fill="x", expand=True, padx=10)

btnLogar = tk.Button(janela, text="Login", command=lambda: lblSaida.config(text="Logado!", fg="green"))
btnLogar.pack(side="left", fill="x", expand=True, padx=10)

lblSaida = tk.Label(janela, text="")
lblSaida.pack(side="left", fill="x", expand=True, padx=10)

janela.mainloop()