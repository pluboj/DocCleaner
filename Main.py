from tkinter import *
import tkinter.filedialog
from TextExtractor import TextExtractor
from tkinter.ttk import Progressbar
import time
import threading


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
        self.btn = Button(master, text="Process File", command=self.submit_file)
        self.btn.grid(row=1, column=10, sticky='e' + 'w', padx=10, pady=2)
        self.progress = Progressbar(master, orient=HORIZONTAL, length=300, mode='indeterminate')

    @staticmethod
    def open_file(event=None):
        input_file_name = tkinter.filedialog\
            .askopenfilename(filetypes=[("All Files", "*.*"), ("MS Word", "*.doc;*.docx")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            input_dir.delete(0, END)
            input_dir.insert(0, file_name)

    def submit_file(self):
        def real_progress():
            self.progress.grid(row=1, column=1, sticky='e')
            self.progress.start()
            global input_dir
            if input_dir.get() != "":
                tc = TextExtractor(file_name)
                tc.process_text()
            time.sleep(5)
            self.progress.stop()
            self.progress.grid_forget()
            input_dir.delete(0, END)

            self.btn['state'] = 'normal'

        self.btn['state'] = 'disabled'
        threading.Thread(target=real_progress).start()


root = Tk()
app = App(root)
root.mainloop()
