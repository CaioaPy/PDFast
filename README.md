# PDFast
<b>PDFast</b> is a tool developed in Python for quick extraction, summarization, and translation of PDF document content. The application uses the Cohere API for abstractive summarization and the Translatepy library to translate the summarized text into the desired language.

# Features
- **Text Extraction**: Reads the content of PDF files while preserving their basic structure.
- **Abstractive Summarization**: Generates a coherent and concise summary of the extracted text using the Cohere API.
- **Text Translation**: Automatically translates the generated summary into Portuguese or another configured language.
- **Intuitive Interface**: Simple and functional graphical interface created with the tkinter library.

# Prerequisites
To run PDFast, you will need:

- **Python 3.10 or higher**: Ensure that Python is correctly installed on your system.
## Required Python Libraries:
- tkinter
- pymupdf
- cohere
- translatepy

# Installation
- Clone the repository: `git clone https://github.com/CaioaPy/PDFast.git`
## Install dependencies:
```pip install -r requirements.txt``` (tkinter, pymupdf, cohere, translatepy)

# How to Use
- Open the application `main.py`:  
Select a PDF: Click on "Choose PDF" and select the file you want to analyze.

- Configure your Cohere key:  
Enter your Cohere API key in the designated section and click "Save Key."  
You can obtain a key by creating an account on the Cohere dashboard.

- Analyze the PDF:  
Click on "Analyze PDF."  
The content will be extracted, summarized, and translated automatically.

# Technologies Used
- **Python**
- **tkinter**: Graphical interface.
- **PyMuPDF**: PDF text extraction.
- **Cohere**: Abstractive summarization.
- **Translatepy**: Text translation.
# APIs:
- Cohere API for generating abstractive summaries.

# License
This project is licensed under the MIT license. See the LICENSE file for more details.

# PDFast: Extract, summarize, and translate PDF content quickly and efficiently. 🚀
