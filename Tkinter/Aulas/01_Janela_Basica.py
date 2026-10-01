import tkinter as tk
# 'tk' é um apelido para a biblioteca tkinter, assim não precisamos escrever 'tkinter' toda vez

# Função para exibir o texto na label mensagem
def exibirMensagem():
    msg = entrada.get()
    mensagem.config(text=(f"Olá,{msg}"))

# estrutura básica da janela
janela = tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("600x400")

# Widgets (componentes da interface)
texto = tk.Label(janela, text="Digite o seu nome:") #isto é um rótulo/texto fixo (Label)
entrada = tk.Entry(janela) #isto é um campo de entrada (Entry)
botao = tk.Button(janela, text="Clique aqui", command=exibirMensagem) #isso é um botão (Button) 
#chamando a função exibirMensagem()
mensagem = tk.Label(janela, text="")

# Organizando os componentes (widgets) na janela com pack
# O método "pack" organiza os elementes em uma direção
# O padrão do "pack" é top -> botton
texto.pack(pady=10) 
entrada.pack(pady=10)
botao.pack(pady=10)
mensagem.pack(pady=10)

#Função que inicializa a janela
janela.mainloop()