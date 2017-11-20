from docx import Document


class TextExtractor:

    def __init__(self, filename):
        self.filename = filename

    def process_text(self):
        doc = Document(self.filename)
        for paragraph in doc.paragraphs:
            item = []
            for run in paragraph.runs:
                if run.bold:
                    item.append("<b>"+run.text+"</b>")
                elif run.italic:
                    item.append("<i>" + run.text + "</i>")
                elif run.underline:
                    item.append("<u>" + run.text + "</u>")
                else:
                    item.append(run.text)

            joined_item = "".join(item)
            print(joined_item.replace("</b><b>", ""))
