import tkinter as tk


class FileMenu:
    def __init__(self, master):
        self.master = master

    def create_file_menu(self):
        menubar = tk.Menu(self.master, background='#000099', foreground='white',
                          activebackground='#004c99', activeforeground='white')
        file = tk.Menu(menubar,tearoff=0, background='#000099',foreground='white',activebackground='#004c99', activeforeground='white')

        file.add_command(label='Exit', underline=1, accelerator='Ctrl+Q', command=lambda: quit())

        menubar.add_cascade(label="File", menu=file)

        self.master.bind_all("<Control-q>",
                             lambda event: quit())

        self.master.config(menu=menubar)
