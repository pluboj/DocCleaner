from docx import Document


class TextExtractor:

    def __init__(self, filename):
        self.filename = filename

    def process_text(self):
        doc = Document(self.filename)
        for paragraph in doc.paragraphs:
            print(paragraph.text)
