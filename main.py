import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import Label
import os

janela = tk.Tk()
janela.geometry("300x300")
janela.title("PDFast")

caminho_arquivo = None

def EscolherPDF():
    global caminho_arquivo 
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    if caminho_arquivo:
        arquivo_nome = os.path.basename(caminho_arquivo)
    selecionado_texto.set(arquivo_nome)

def Resumo():
    janela_resumo = Toplevel()
    janela_resumo.geometry("500x500")
    janela_resumo.title("Análise PDF")
    resumo_label = Label(janela_resumo,text="aaa")
    resumo_label.pack()


grid_frame = tk.Frame(janela)
grid_frame.pack(expand=True, fill="both")

grid_frame.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
grid_frame.grid_columnconfigure([0, 1, 2, 3, 4], weight=1)

titulo = tk.Label(grid_frame, text="PDFast", font=("Arial", 24))
titulo.grid(row=0, column=1)

holder = tk.Label(grid_frame, text=" ")
holder.grid(row=1, column=0)

botao = tk.Button(grid_frame, text="Escolher PDF", command=EscolherPDF)
botao.grid(row=2, column=1)

selecionado_texto = tk.StringVar()
selecionado_texto.set(" ")
selecionado = tk.Label(grid_frame, textvariable=selecionado_texto)
selecionado.grid(row=3, column=1)

botaoenviar = tk.Button(grid_frame, text="Analizar pdf", command=Resumo)
botaoenviar.grid(row=4, column=1)

janela.mainloop()