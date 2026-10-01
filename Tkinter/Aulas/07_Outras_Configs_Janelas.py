import tkinter as tk

def ocultar():
    janela.withdraw()  # Oculta a janela
    print("Janela oculta (withdraw). Use o botão na janela auxiliar para restaurar.")
    abrir_restaurar()

def restaurar():
    janela.deiconify()  # Mostra novamente
    janela_aux.destroy()
    print("Janela restaurada (deiconify).")

def abrir_restaurar():
    global janela_aux
    janela_aux = tk.Toplevel()
    janela_aux.title("Janela Auxiliar")
    janela_aux.geometry("250x120+300+300")
    janela_aux.attributes("-topmost", True)
    tk.Label(janela_aux, text="A janela principal está oculta.").pack(pady=10)
    tk.Button(janela_aux, text="Restaurar janela principal", command=restaurar).pack(pady=10)

def minimizar():
    janela.iconify()
    print("Janela minimizada (iconify).")

def transparencia():
    valor = janela.attributes("-alpha")
    novo_valor = 0.5 if valor == 1.0 else 1.0
    janela.attributes("-alpha", novo_valor)
    print(f"Transparência ajustada para {novo_valor}")

def topo():
    atual = janela.attributes("-topmost")
    janela.attributes("-topmost", not atual)
    print(f"Sempre no topo: {not atual}")

def tela_cheia():
    atual = janela.attributes("-fullscreen")
    janela.attributes("-fullscreen", not atual)
    print(f"Tela cheia: {not atual}")

def tamanho_fixo():
    janela.resizable(False, False)
    print("Tamanho fixado (não redimensionável).")

def tamanho_livre():
    janela.resizable(True, True)
    print("Tamanho liberado (redimensionável).")

def fechar():
    janela.destroy()
    print("Janela fechada (destroy).")

# --- Janela principal ---
janela = tk.Tk()
janela.title("Controle de Janelas - Tkinter Demo")
janela.geometry("400x600")

tk.Label(janela, text="🎛️ Controle de Janelas Tkinter", font=("Arial", 12, "bold")).pack(pady=15)

# --- Botões de ação ---
botoes = [
    ("Ocultar janela (withdraw)", ocultar),
    ("Minimizar (iconify)", minimizar),
    ("Alternar transparência", transparencia),
    ("Alternar 'sempre no topo'", topo),
    ("Alternar tela cheia", tela_cheia),
    ("Fixar tamanho", tamanho_fixo),
    ("Liberar tamanho", tamanho_livre),
    ("Fechar (destroy)", fechar),
]

for texto, comando in botoes:
    tk.Button(janela, text=texto, width=30, command=comando).pack(pady=4)

janela.mainloop()