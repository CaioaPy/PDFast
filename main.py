import tkinter as tk

janela = tk.Tk()
janela.geometry("300x300")
janela.title("PDFast")

grid_frame = tk.Frame(janela)
grid_frame.pack(expand=True, fill="both")

grid_frame.grid_rowconfigure([0, 1, 2], weight=1)
grid_frame.grid_columnconfigure([0, 1, 2], weight=1)

titulo = tk.Label(grid_frame, text="PDFast", font=("Arial", 24))
titulo.grid(row=0, column=1)

explicacao = tk.Label(grid_frame, text=" ")
titulo.grid(row=1, column=1)

botao = tk.Button(grid_frame, text="Escolher PDF")
botao.grid(row=2, column=1)

janela.mainloop()
