import tkinter as tk
from tkinter import messagebox

def infoLabel(mensagem):
    labInfo.config(text=mensagem)

def abrir_login():
    #cria a janela de login (filha)
    janela.withdraw()
    login = tk.Toplevel(janela)
    login.title("Login")
    login.geometry("300x300")
    login.resizable(True, False) #bloqueia o redimensionamento da janela (largura,altura)
    login.grab_set() #enquanto a janela de login estiver aberta, 
                    #bloqueia interação com a janela principal (modo modal)

    tk.Label(login, text="Usuário:").pack(pady=5)
    campoUsuario = tk.Entry(login)
    campoUsuario.pack()

    tk.Label(login, text="Senha:").pack(pady=5)
    campoSenha = tk.Entry(login, show="*")
    campoSenha.pack()

    #função interna para verificar o login
    def verificar():
        usuario = campoUsuario.get()
        senha = campoSenha.get()

        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Acesso permitido", parent=login)
            login.destroy() #retira da memoria/mata a janela de login
            janela.deiconify() #restaura a janela principal que estava oculta
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def cancelar():
        messagebox.showwarning("Login", "Login cancelado", parent=login)
        login.destroy()
        janela.deiconify() #restaura a janela principal que estava oculta

    tk.Button(login, text="Entrar", command=verificar, width=10).pack(pady=10)
    tk.Button(login, text="Cancelar", command=cancelar, width=10).pack()

    #espera a janela ser fechada antes de continuar
    login.wait_window() #pausa aqui até o login ser fechado
    janela.deiconify() #restaura a janela principal que estava oculta
    infoLabel("A janela de login foi fechada — o programa continua.")


#janela principal
janela = tk.Tk()
janela.title("Janelas Top level")
janela.geometry("400x300")

tk.Label(janela, text="Exemplo de uso de janelas TopLevel", font=("Arial", 14)).pack(pady=20)
tk.Button(janela, text="Abrir Login", command=abrir_login, width=20).pack(pady=10)
tk.Button(janela, text="Fechar Aplicação", command=janela.destroy, width=20).pack(pady=10)
labInfo = tk.Label(janela, text="", font=("Arial", 13), fg="green").pack(pady=15)

janela.mainloop()