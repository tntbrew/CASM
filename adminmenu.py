from usermanager import UserManager
from weldingrollchange import WeldingRollChange
from weldingrollspecs import WeldingRollSpecifications
from productionline import ProductionLine
import tkinter as tk


class AdminMenu:

    def __init__(self, master, username):
        self.menu_bar = None
        self.master = master
        self.username = username

    def create_admin_menu(self):
        self.menu_bar = tk.Menu(self.master, background='#ff8000', foreground='black', activebackground='white',
                                activeforeground='black')

        file = tk.Menu(self.menu_bar)

        file.add_command(label='Exit', underline=1, accelerator='Ctrl+Q', command=quit)

        self.menu_bar.add_cascade(label="File", menu=file)

        self.master.bind_all("<Control-q>", lambda event: quit())

        self.master.config(menu=self.menu_bar)

        roll_change = tk.Menu(self.menu_bar)

        roll_change.add_command(label='New', command=lambda: WeldingRollChange(self.master).create_roll_change_form())

        self.menu_bar.add_cascade(label="Welding Roll Change", menu=roll_change)

        self.master.config(menu=self.menu_bar)

        canmaker = tk.Menu(self.menu_bar)
        canmaker.add_command(label='Welding Roll Specs', command=lambda: WeldingRollSpecifications(self.master,
                                                                                                   self.username).create_welding_roll_specs_form)

        self.menu_bar.add_cascade(label="Specifications", menu=canmaker)

        tools = tk.Menu(self.menu_bar)

        tools.add_command(label='Add User', command=lambda: UserManager(self.master).create_new_user_form())

        tools.add_command(label='Add City')

        tools.add_command(label='New Code Change tk.Labels')

        tools.add_command(label='Add Country')

        tools.add_command(label='Add Branch')

        tools.add_command(label='Add Line', command=lambda: ProductionLine(self.master).add_line_form())

        self.menu_bar.add_cascade(label="Tools", menu=tools)
