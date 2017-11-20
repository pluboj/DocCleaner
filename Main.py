from tkinter import *
import tkinter.filedialog
from TextExtractor import TextExtractor


class App:
    file_name = None
    input_dir = None

    def __init__(self, master):
        master.minsize(width=520, height=100)
        master.maxsize(width=520, height=100)
        master.title('DocCleaner v1.0')

        Label(master, text="Directory:").grid(row=0, column=0, sticky='e')
        global input_dir
        input_dir = Entry(master, width=60)
        input_dir.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)
        Button(master, text="Select File",
               command=self.open_file).grid(row=0, column=10, sticky='e' + 'w', padx=10, pady=2)
        Button(master, text="Process File",
               command=self.submit_file).grid(row=1, column=10, sticky='e' + 'w', padx=10, pady=2)

    @staticmethod
    def open_file(event=None):
        input_file_name = tkinter.filedialog\
            .askopenfilename(filetypes=[("All Files", "*.*"), ("MS Word", "*.doc;*.docx")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            input_dir.delete(0, END)
            input_dir.insert(0, file_name)

    @staticmethod
    def submit_file():
        global input_dir
        if input_dir.get() != "":
            tc = TextExtractor(file_name)
            tc.process_text()


root = Tk()
app = App(root)
root.mainloop()
