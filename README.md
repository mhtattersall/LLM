# LLM

This repo demonstrates a Retrieval Augmented Generation pipeline in python.  
The data is a 4-page pdf of a document issued by the UK Office for Budget Responsibility concerning public sector finances.  
The first part of the program is an ipython file used in Colab. This program uses pdfplumber to load a pdf document and pytesseract to read the contents using OCR, and saves each page in a list. Colab is a good environment for running Google's Tesseract-OCR Engine.   
The second part of the program (lists.py) is a python file, which creates three lists.  It requires you to run the Ollama platform with the Phi-3 LLM on your local machine.  Only the first page of the pdf is used to reduce the compute time.  
The third part of program (db.py) is a pyhton file, which loads three lists to the chroma graph db. It queries chroma to create RAG context, that is subsequently used to chat with the Phi-3 LLM on the Ollama platform.  

https://github.com/jsvine/pdfplumber  
https://pypi.org/project/pytesseract/  
https://ollama.com/  
https://docs.trychroma.com/   
https://medium.com/towards-data-science/genai-with-python-rag-with-llm-complete-tutorial-c276dda6707b  
