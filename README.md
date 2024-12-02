# PDFast
<b>PDFast</b> é uma ferramenta desenvolvida em Python para extração, resumo e tradução rápida do conteúdo de documentos PDF. A aplicação utiliza a API do Cohere para realizar resumos abstrativos e a biblioteca Translatepy para traduzir o texto resumido para o idioma desejado.

# Funcionalidades
- Extração de texto: Lê o conteúdo de arquivos PDF preservando sua estrutura básica.
- Resumo abstrativo: Gera um resumo coerente e conciso do texto extraído utilizando a API do Cohere.
- Tradução de texto: Traduz automaticamente o resumo gerado para o português ou outro idioma configurado.
- Interface intuitiva: Interface gráfica simples e funcional criada com a biblioteca tkinter.

# Pré-requisitos
Para executar o PDFast, você precisará ter instalado:

- Python 3.10 ou superior: Certifique-se de que o Python está corretamente instalado no sistema.
## Bibliotecas Python necessárias:
- tkinter
- pymupdf
- cohere
- translatepy

# Como instalar
- Clone o repositório (git clone https://github.com/seu-usuario/PDFast.git)
## Instale as dependências:
- ```tkinter```
- ```pymupdf```
- ```cohere```
- ```translatepy```

# Como usar
- Abra a aplicação ```main.py```: <br>
Selecione um PDF: Clique em "Escolher PDF" e escolha o arquivo que deseja analisar.

- Configure sua chave do Cohere:
Insira sua chave API do Cohere na seção indicada e clique em "Salvar Chave".
Você pode obter uma chave criando uma conta no dashboard do Cohere.

- Analise o PDF:
Clique em "Analisar PDF".
O conteúdo será extraído, resumido e traduzido automaticamente.

# Tecnologias Utilizadas
- Python
- tkinter: Interface gráfica.
- PyMuPDF: Extração de texto de PDFs.
- Cohere: Resumo abstrativo.
- Translatepy: Tradução de texto.
# APIs:
- Cohere API para gerar resumos abstrativos.

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

# PDFast: Extraia, resuma e traduza conteúdo de PDFs de forma rápida e eficiente. 🚀
