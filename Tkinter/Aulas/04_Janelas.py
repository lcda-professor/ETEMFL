import tkinter as tk

def main():
    global janelaPrincipal
    janelaPrincipal = tk.Tk()
    janelaPrincipal.geometry("800x600")

    #esta é uma outra forma de criar componentes
    #deste jeito é possível criar o Label e o Button diretamente sem
    #a necessidade de uso de uma "variável"
    #além disso é possível incluir o pack diretamente no componente
    tk.Label(janelaPrincipal, text="Esta é a janela principal").pack(pady=20)
    tk.Button(janelaPrincipal, text="ir para outra janela", command=abrirNovaJanela).pack(pady=20)

    janelaPrincipal.mainloop()

def voltar(janelaAtual):
    janelaAtual.destroy()
    main()

def abrirNovaJanela():
    #o comando destroy() serve para fechar/retirar da memória a janela atual
    janelaPrincipal.destroy()

    segundaJanela = tk.Tk()
    segundaJanela.geometry("800x600")
    tk.Label(segundaJanela, text="Esta é a segunda janela").pack(pady=20)
    tk.Button(segundaJanela, text="Voltar", command=lambda: voltar(segundaJanela)).pack(pady=20)
    segundaJanela.mainloop()
    
main()