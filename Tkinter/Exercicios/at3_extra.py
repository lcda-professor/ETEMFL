import tkinter as tk
from tkinter import messagebox

def abrir_modal():
    # Captura o texto digitado no Entry
    texto_digitado = entrada.get()
    
    # Abre uma janela modal de informação
    messagebox.showinfo(
        title="Informação",
        message=f"Você digitou: {texto_digitado}"
    )

# === Janela Principal ===
janela = tk.Tk()
janela.title("AT3 Extra")
janela.geometry("350x200")
janela.configure(bg="#cce6ff")  # Cor de fundo (uso de cor obrigatório)

# Label
label = tk.Label(janela, text="Digite algo e clique no botão:", bg="#cce6ff")
label.pack(pady=10)

# Caixa de Texto (Entry)
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

# Botão que abre a janela modal
botao = tk.Button(janela, text="Mostrar mensagem", command= abrir_modal)
botao.pack(pady=10)

# Loop principal da interface
janela.mainloop()