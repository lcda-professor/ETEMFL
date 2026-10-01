import tkinter as tk
from tkinter import messagebox

# ------------------ Funções ------------------

def validar_campos():
    """Verifica se todos os campos estão preenchidos e abre a janela de confirmação."""
    nome = entry_nome.get().strip()
    inst = entry_inst.get().strip()
    cpf = entry_cpf.get().strip()

    if not nome or not inst or not cpf:
        messagebox.showerror("Erro no cadastro", "Preencha todos os campos antes de continuar.")
        return

    abrir_janela_confirmacao(nome, inst, cpf)


def abrir_janela_confirmacao(nome, inst, cpf):
    """Abre uma nova janela (Toplevel) com os dados cadastrados."""
    janela_conf = tk.Toplevel(root)
    janela_conf.title("Confirmação de Cadastro")
    janela_conf.configure(bg="#f0f0f0")
    janela_conf.geometry("350x200")
    janela_conf.resizable(False, False)

    lbl_msg = tk.Label(
        janela_conf,
        text="Cadastro realizado com sucesso!\n\n"
             f"Nome: {nome}\nInstituição: {inst}\nCPF: {cpf}",
        bg="#f0f0f0",
        fg="#202020",
        font=("Arial", 11)
    )
    lbl_msg.pack(padx=20, pady=20)

    btn_fechar = tk.Button(
        janela_conf,
        text="Fechar",
        command=janela_conf.destroy,
        bg="#d9534f",
        fg="white",
        relief="raised",
        width=10
    )
    btn_fechar.pack(pady=10)


def confirmar_saida():
    """Pergunta ao usuário se deseja sair do sistema."""
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair do sistema?")
    if resposta:
        root.destroy()

# ------------------ Janela principal ------------------

root = tk.Tk()
root.title("Cadastro de Visitante")
root.geometry("400x300")
root.configure(bg="#e8f0fe")

# Permitir redimensionamento proporcional
for i in range(3):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)

# ------------------ Frame do título ------------------
frame_titulo = tk.Frame(root, bg="#1a73e8")
frame_titulo.pack(fill="x")

lbl_titulo = tk.Label(
    frame_titulo,
    text="Cadastro de Visitante",
    bg="#1a73e8",
    fg="white",
    font=("Arial", 16, "bold"),
    pady=10
)
lbl_titulo.pack()

# ------------------ Frame do formulário ------------------
frame_form = tk.Frame(root, bg="#e8f0fe")
frame_form.pack(pady=10, padx=20, fill="x")

# Labels e Entrys organizados com grid
tk.Label(frame_form, text="Nome:", bg="#e8f0fe", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, sticky="we", padx=5, pady=5)

tk.Label(frame_form, text="Instituição:", bg="#e8f0fe", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_inst = tk.Entry(frame_form, width=30)
entry_inst.grid(row=1, column=1, sticky="we", padx=5, pady=5)

tk.Label(frame_form, text="CPF:", bg="#e8f0fe", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_cpf = tk.Entry(frame_form, width=30)
entry_cpf.grid(row=2, column=1, sticky="we", padx=5, pady=5)

# Ajuste de layout com rowconfigure/columnconfigure
frame_form.columnconfigure(1, weight=1)

# ------------------ Frame dos botões ------------------
frame_botoes = tk.Frame(root, bg="#e8f0fe")
frame_botoes.pack(pady=15)

btn_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    command=validar_campos,
    bg="#34a853",
    fg="white",
    relief="raised",
    width=12
)
btn_cadastrar.pack(side="left", padx=10)

btn_sair = tk.Button(
    frame_botoes,
    text="Sair",
    command=confirmar_saida,
    bg="#ea4335",
    fg="white",
    relief="raised",
    width=12
)
btn_sair.pack(side="left", padx=10)

# ------------------ Execução ------------------
root.mainloop()