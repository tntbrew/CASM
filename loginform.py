import tkinter as tk
from tkinter import ttk

import bcrypt
import sqlite3

from adminmenu import AdminMenu
from canmakermenu import CanMakerMenu
from constants import USER_ACCESS_CODES, BACKGROUND, FONT_SIZE, BUTTON_BACKGROUND
from operatormenu import OperatorMenu
from usermanager import get_user_names


class Login:
    def __init__(self, master):
        self.user_password_textbox = None
        self.user_name_combo = None
        self.master = master
        self.root = tk.Toplevel(self.master)

    def disable_event(self):
        self.root.withdraw()
        self.master.focus_force()

    def validate_login(self, root):

        username = self.user_name_combo.get()
        temp_password = self.user_password_textbox.get()

        # Hash the encoded password and generate a salt:
        temp_password = temp_password.encode('utf-8')

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()
        DbCursor.execute("SELECT * FROM user where user_name = ?", (username,))

        user_record = DbCursor.fetchall()
        logged_on_user_name = self.user_name_combo.get()

        DbConnection.close()

        for user_login in user_record:

            if bcrypt.checkpw(temp_password, user_login[1]):

                # admin
                if user_login[2] == USER_ACCESS_CODES[2]:
                    AdminMenu(self.master, logged_on_user_name).create_admin_menu()

                    self.close_window(root, self.master)
                    return True

                # can maker
                if user_login[2] == USER_ACCESS_CODES[1]:
                    CanMakerMenu(self.master).create_canmaker_menu()
                    self.close_window()
                    return True

                # operator
                if user_login[2] == USER_ACCESS_CODES[0]:
                    OperatorMenu(self.master).create_operator_menu()
                    self.root.destroy()
                    # self.close_window()
                    return True

                return True

            else:
                tk.messagebox.showerror('Error', 'login failed.Try again', parent=self.root)
                self.user_password_textbox.delete(0, tk.END)
                return

    def close_window(self, root, main):
        root.withdraw()
        main.focus_force()

    def create_login_window(self):

        self.root.config(bg=BACKGROUND)
        self.root.title('Login')
        self.root.overrideredirect(True)  # turns off title bar, geometry
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.disable_event())
        self.root.geometry('350x150')
        self.root.resizable(0, 0)
        self.root.update_idletasks()

        # self.root.configure(bg='grey')
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 1)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()
        # self.root.configure(bg='snow2')

        users_name_list = list()

        # get user names from database table
        user_names = get_user_names()

        # UserManager.destroy()

        # loop thru user names and append them to the users_names list

        for user in user_names:
            users_name_list.append(user[0])

        # create labels for form
        user_name_label = tk.Label(self.root, text='User Name:', bg=BACKGROUND, font=FONT_SIZE)  # bg='grey',
        user_name_label.grid(row=0, column=0, padx=10, pady=10)

        user_password_label = tk.Label(self.root, text='Password:', bg=BACKGROUND, font=FONT_SIZE)  # ,bg='grey')
        user_password_label.grid(row=1, column=0, padx=10, pady=10)

        # create textboxes for form
        self.user_name_combo = ttk.Combobox(self.root, width=18, font=FONT_SIZE,state="readonly")
        self.user_name_combo['values'] = users_name_list

        # self.user_name_combo.current(0)
        self.user_name_combo.grid(row=0, column=1)

        self.user_password_textbox = tk.Entry(self.root, show='*', font=FONT_SIZE)
        self.user_password_textbox.grid(row=1, column=1)

        # create log on button
        submit_button = tk.Button(self.root, text="Login", bg=BUTTON_BACKGROUND, width=10,
                                  command=lambda: self.validate_login(self.root))
        submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=40, ipadx=90)
        self.root.bind('<Return>', lambda event: self.validate_login(self.root))
