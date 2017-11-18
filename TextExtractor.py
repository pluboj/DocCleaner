from docx import Document

class TextExtractor:

    def __init__(self, filename):
        self.filename = filename

    def process_text(self):
       doc = Document(self.filename)
       for para in doc.paragraphs:
           print(para.text);

