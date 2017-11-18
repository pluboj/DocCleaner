from tkinter import *
import tkinter.filedialog


class App:
    def __init__(self, master):
        master.minsize(width=520, height=100)
        master.maxsize(width=520, height=100)
        master.title('DocCleaner v1.0')

        Label(master, text="Directory:").grid(row=0, column=0, sticky='e')
        Entry(master, width=60).grid(row=0, column=1,
                                     padx=2, pady=2, sticky='we', columnspan=9)
        Button(master, text="Select File",
               command=self.open_file).grid(row=0, column=10, sticky='e' + 'w', padx=10, pady=2)

    @staticmethod
    def open_file():
        file_object = tkinter.filedialog\
            .askopenfile(mode='r', filetypes=[("All Files", "*.*"), ("MS Word", "*.doc;*.docx")])
        print(file_object)


parent = Tk()
app = App(parent)
parent.mainloop()
