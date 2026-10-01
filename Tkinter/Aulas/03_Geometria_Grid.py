import tkinter as tk

# Criando janela com frame e widgets

janela = tk.Tk()
janela.title("Janela  com frame e widgets")
janela.geometry("450x400")

# Frames tradicional e com label -> observe que os frames vão dentro da janela.
# Os demais elementos agora irão dentro dos frames
frame_1 = tk.LabelFrame(janela, bd=5, relief="solid", text="Dados Pessoais")
# O parâmetro relief define o tipo de borda do frame
frame_2 = tk.Frame(janela, bd=5, relief="ridge")

# Observe que os widgets vem dentro dos frames
lblNome = tk.Label(frame_1, text="Nome: ", font=("Sams",10))
lblSenha = tk.Label(frame_1, text="Senha:", font=("Sams", 10))

campoNome = tk.Entry(frame_1)
campoSenha = tk.Entry(frame_1, show="*")

btnEnviar = tk.Button(frame_2, text="Enviar", command="")

# Os frames estão na geometria "pack" dentro das janela

frame_1.pack(fill="both", expand=True) #fill="both" preenche largura e altura conforme a janela permite
frame_2.pack(fill="both", expand=True) #expand=True garante que se redimensionar a janela, o frame vai junto

# Os widgets estão na geometria "grid" dentro dos frames

lblNome.grid(row=0, column=0, padx=5, pady=5)
campoNome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
# O campoNome recebeu o parâmetro sticky="ew", significando que o campo nome pode
# expandir tanto para esqueda quanto para a direita. Mas como o campo está em uma
# grid que está dentro de frame, então essa expansão do campo depende de ajuste 
# na expansão da coluna do frame cuja grid está inserida (ver abaixo) 

frame_1.grid_columnconfigure(1,weight=1)
frame_1.grid_rowconfigure(1,weight=1)
# aqui o frame_1 cujos campos estão inseridos, tem a coluna configurada pelo método
# grid_columnconfigure passando como parâmetros o valor 1 (coluna 1, onde estão os
# campos) e weight=1 que é o peso da expansão

lblSenha.grid(row=1, column=0, padx=5, pady=5)
campoSenha.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

btnEnviar.pack(fill="none", expand=True)

# Loop
janela.mainloop()