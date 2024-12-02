import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import Label
import os
import pymupdf
import cohere
from translatepy import Translator

caminho_arquivo = None
nome_arquivo = None
texto_arquivo = None
chave_api = None

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
    out = open(nome_arquivo + "_output.txt", "w", encoding="utf-8")
    texto_arquivo = nome_arquivo + "_output.txt"
    for page in doc:
        text = page.get_text()
        out.write(text)
        out.write("\f")
    out.close()
    texto_resumo = ResumirExtrato()
    texto_resumo = TraduzirTexto(texto_resumo)
    janela_extrair = Toplevel()
    janela_extrair.geometry("700x500")
    janela_extrair.title("Análise PDF")
    resumo_texto_final = tk.Text(janela_extrair, wrap="word")
    resumo_texto_final.pack(fill="both", expand="true", padx="15", pady="15")
    resumo_texto_final.insert("1.0", texto_resumo)

def habilitar_botao():
    if nome_arquivo != None and chave_api != None:
        botaoenviar.config(state="normal")

def ResumirExtrato():
    global chave_api
    global texto_arquivo

    co = cohere.Client(chave_api)

    with open(texto_arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()


    resposta = co.summarize(
        text=texto,
        length="long"
    )

    return resposta.summary

def GetChave():
    global chave_api

    chave = chave_campo.get()
    chave_api = chave
    habilitar_botao()

def TraduzirTexto(texto):
    translator = Translator()
    traducao = translator.translate(texto, "portuguese")
    return traducao.result
    
janela = tk.Tk()
janela.geometry("760x350")
janela.title("PDFast")

grid_frame = tk.Frame(janela)
grid_frame.pack(expand=True, fill="x")

grid_frame.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
grid_frame.grid_columnconfigure([0, 1, 2, 3, 4], weight=1)

titulo = tk.Label(grid_frame, text="PDFast", font=("Arial", 24))
titulo.grid(row=0, column=1)

escolher_botao = tk.Button(grid_frame, text="Escolher PDF", command=EscolherPDF)
escolher_botao.grid(row=3, column=1)

chave_campo = tk.Entry(grid_frame)
chave_campo.grid(row=2, column=0)

chave_botao = tk.Button(grid_frame, text="Salvar Chave", command=GetChave)
chave_botao.grid(row=3, column=0)

explicacao = tk.Label(grid_frame, text="Para fazer a analise do PDF crie\n e insira uma chave do Cohere,\n você pode obter uma acessando o\n dashboard, criando uma conta no\n site oficial. (dashboard.cohere.com)", font=("Arial", 12))
explicacao.grid(row=1, column=2)

selecionado_texto = tk.StringVar()
selecionado_texto.set(" ")
selecionado = tk.Label(grid_frame, textvariable=selecionado_texto)
selecionado.grid(row=4, column=1)

botaoenviar = tk.Button(grid_frame, text="Analizar pdf", command=Extrair, state="disabled")
botaoenviar.grid(row=5, column=1)

janela.mainloop()