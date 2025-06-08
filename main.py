import pyttsx3
import pdfplumber
import logging
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Suppress CropBox warnings
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Hide the root Tk window
Tk().withdraw()

# Ask for file
book = askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

# Init TTS engine
engine = pyttsx3.init(driverName='nsss')  # macOS
engine.setProperty('rate', 150)

# Read and speak
with pdfplumber.open(book) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f"Reading Page {i+1}...")
            engine.say(text)
            engine.runAndWait()
