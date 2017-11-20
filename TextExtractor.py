from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph


class TextExtractor:

    def __init__(self, filename):
        self.filename = filename

    def process_text(self):
        document = Document(self.filename)

        for block in self.iter_block_items(document):

            # print(block.text if isinstance(block, Paragraph) else '<table>')
            if isinstance(block, Paragraph):
                self.add_markups(block.runs)
            elif isinstance(block, Table):
                for row in block.rows:
                    row_data = []
                    for cell in row.cells:
                        for paragraph in cell.paragraphs:
                            # row_data.append(paragraph.text)
                            self.add_markups(paragraph.runs)
            print("\n")

    @staticmethod
    def iter_block_items(parent):

        if isinstance(parent, _Document):
            parent_elm = parent.element.body
        elif isinstance(parent, _Cell):
            parent_elm = parent._tc
        elif isinstance(parent, _Row):
            parent_elm = parent._tr
        else:
            raise ValueError("something's not right")
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl):
                yield Table(child, parent)

    @staticmethod
    def add_markups(chunk):
        item = []
        for run in chunk:
            formatted_run = run.text
            if run.underline:
                formatted_run = "<u>" + formatted_run + "</u>"
            if run.bold:
                formatted_run = "<b>" + formatted_run + "</b>"
            if run.italic:
                formatted_run = "<i>" + formatted_run + "</i>"

            item.append(formatted_run)
        joined_item = "".join(item)
        print(joined_item.replace("</b><b>", ""))

