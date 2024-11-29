import tkinter as tk
from tkinter import filedialog
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


grid_frame = tk.Frame(janela)
grid_frame.pack(expand=True, fill="both")

grid_frame.grid_rowconfigure([0, 1, 2, 3], weight=1)
grid_frame.grid_columnconfigure([0, 1, 2, 3], weight=1)

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

janela.mainloop()
