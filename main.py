import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import Label
import os
import pymupdf

janela = tk.Tk()
janela.geometry("250x250")
janela.title("PDFast")

caminho_arquivo = None
nome_arquivo = None
texto_arquivo = None

def EscolherPDF():
    global caminho_arquivo 
    global nome_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    if caminho_arquivo:
        nome_arquivo = os.path.basename(caminho_arquivo)
    selecionado_texto.set(nome_arquivo)
    habilitar_botao()

def Extrair():
    global texto_arquivo
    global nome_arquivo
    doc = pymupdf.open(caminho_arquivo)
    nome_arquivo = nome_arquivo.rstrip(".pdf")
    out = open(nome_arquivo + "_output.txt", "wb")
    texto_arquivo = nome_arquivo + "_output.txt"
    for page in doc:
        text = page.get_text().encode("utf8") 
        out.write(text)
        out.write(bytes((12,)))
    out.close()
    janela_extrair = Toplevel()
    janela_extrair.geometry("500x500")
    janela_extrair.title("Análise PDF")
    resumo_label = Label(janela_extrair,text="aaa")
    resumo_label.pack()

def habilitar_botao():
    if nome_arquivo != None:
        botaoenviar.config(state="normal")

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

botaoenviar = tk.Button(grid_frame, text="Analizar pdf", command=Extrair, state="disabled")
botaoenviar.grid(row=4, column=1)

janela.mainloop()