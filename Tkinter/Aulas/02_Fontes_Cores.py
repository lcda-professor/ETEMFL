import tkinter as tk
import tkinter.font as tkFont #Biblioteca tkinter para fontes

janela = tk.Tk()
janela.title("Janela Colorida")
janela.geometry("1000x450")

lb1 = tk.Label(janela, text="Texto com fonte Sans tamanho 20!", font=("Sans",20))

lb2 = tk.Label(janela,text="Texto com fonte Sans tamanho 20 em negrito!", 
               font=("Sans", 20, "bold"))

lb3 = tk.Label(janela, text="Texto com fonte Sams tamanho 20 em negrito e azul!",
               font=("Sans",20, "bold"), fg="#0d4497")

#Definição de uma fonte personalizada e reutilizável
fonteLabels = tkFont.Font(family="Sans", size=15, weight="bold", slant="italic")

lb4 = tk.Label(janela, text="Texto com fonte personalizada na cor verde!", 
               font=fonteLabels, fg="blue", bg="yellow")
lb5 = tk.Label(janela, text="Texto com fonte personalizada na cor vermelha!",
               font=fonteLabels, fg="red")

#Outros elementos com fonte e cor personalizados
fontePersona = tkFont.Font(family="Sans", size=15, weight="bold", slant="italic")

entrada1 = tk.Entry(janela, font=("Sans",12),fg="green")
entrada2 = tk.Entry(janela, font=fontePersona, fg="white", bg="blue")

btn1 = tk.Button(janela, text="Clique aqui 1", font=("Sans",13), fg="orange", command="")
btn2 = tk.Button(janela, text="Clique aqui 2", font=fontePersona, fg="white", bg="brown", command="")

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()
lb5.pack()
entrada1.pack()
entrada2.pack()
btn1.pack()
btn2.pack()

janela.mainloop()