import sqlite3
from tkinter import ttk
import tkinter as tk
import bcrypt
from constants import USER_ACCESS_CODES, FONT_SIZE, BACKGROUND, BUTTON_BACKGROUND


def encrypt_user_password(user_password):
    # converting password to array of bytes
    password_bytes = user_password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    password_hash = bcrypt.hashpw(password_bytes, salt)

    return password_hash


def get_user_names():
    try:
        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()

        DbCursor.execute("SELECT user_name FROM user")
        records = DbCursor.fetchall()

        DbConnection.commit()
        DbConnection.close()
        return records

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


class UserManager:
    def __init__(self, master):

        self.tree = None
        self.delete_button = None
        self.delete_textbox = None
        self.submit_button = None
        self.user_access_combobox = None
        self.user_confirm_password_textbox = None
        self.user_password_textbox = None
        self.user_name_textbox = None
        self.root = None
        self.master = master

    def create_new_user_form(self):
        self.root = tk.Toplevel(self.master)
        self.root.title('User Editor')
        self.root.config(bg=BACKGROUND)

        self.root.geometry('815x700')

        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        cache = list()

        for row in USER_ACCESS_CODES:
            cache.append(row)

        self.root.attributes("-topmost", True)

        # create labels for form
        user_name_label = tk.Label(self.root, font=FONT_SIZE, bg=BACKGROUND, text='User Name:')
        user_name_label.grid(row=0, column=0, padx=10, pady=10)

        user_password_label = tk.Label(self.root, font=FONT_SIZE, bg=BACKGROUND, text='Password:')
        user_password_label.grid(row=1, column=0, padx=10, pady=10)

        user_confirm_password_label = tk.Label(self.root, font=FONT_SIZE, bg=BACKGROUND, text='Confirm Password:')
        user_confirm_password_label.grid(row=2, column=0, padx=10, pady=10)

        user_access_label = tk.Label(self.root, font=FONT_SIZE, bg=BACKGROUND, text='Access:')
        user_access_label.grid(row=3, column=0, pady=10)

        delete_label = tk.Label(self.root, font=FONT_SIZE, bg=BACKGROUND, text='Record Id:')
        delete_label.grid(row=5, column=0, padx=10)

        # create input controls
        self.user_name_textbox = tk.Entry(self.root, font=FONT_SIZE)
        self.user_name_textbox.grid(row=0, column=1)

        self.user_password_textbox = tk.Entry(self.root, show='*', font=FONT_SIZE)
        self.user_password_textbox.grid(row=1, column=1)

        self.user_confirm_password_textbox = tk.Entry(self.root, show='*', font=FONT_SIZE)
        self.user_confirm_password_textbox.grid(row=2, column=1)

        self.user_access_combobox = ttk.Combobox(self.root, width=18, font=FONT_SIZE)
        self.user_access_combobox['values'] = cache
        self.user_access_combobox.current(0)
        self.user_access_combobox.grid(row=3, column=1)

        self.submit_button = tk.Button(self.root, text="Add Record", bg=BUTTON_BACKGROUND,
                                       command=lambda: self.save_user_to_database(),
                                       font=FONT_SIZE)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

        self.delete_textbox = tk.Entry(self.root, width=10, font=FONT_SIZE)
        self.delete_textbox.grid(row=5, column=1)

        self.delete_button = tk.Button(self.root, text='Delete', bg='red', font=FONT_SIZE,
                                       command=lambda: self.delete_user())
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=60)

        self.display_users_on_form()

    def delete_user(self):

        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')
            DbCursor = DbConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            DbCursor.execute("select sqlite_version();")
            record = DbCursor.fetchall()
            print("SQLite Database Version is: ", record)

            DbCursor.execute("DELETE from user WHERE oid=" + self.delete_textbox.get())

            DbConnection.commit()
            DbConnection.close()
            self.delete_textbox.delete(0, tk.END)
            self.tree = None
            self.display_users_on_form()
            return True

        except sqlite3.Error as error:
            print("Failed to delete record from a database table", error)

            return False

    def display_users_on_form(self):

        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3"), show='headings')
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')
            DbCursor = DbConnection.cursor()

            DbCursor.execute("SELECT user_name,user_access,oid FROM user")

            records = DbCursor.fetchall()

            for record in records:
                self.tree.insert("", tk.END, values=record)

            self.tree.column("#1", anchor=tk.CENTER)

            self.tree.heading("#1", text="NAME")

            self.tree.column("#2", anchor=tk.CENTER)

            self.tree.heading("#2", text="ACCESS")

            self.tree.column("#3", anchor=tk.CENTER)

            self.tree.heading("#3", text="ID")

            self.tree.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

            DbConnection.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def save_user_to_database(self):

        flag = False
        encryptedpass = encrypt_user_password(self.user_password_textbox.get())

        try:

            DbConnection = sqlite3.connect('canlinedb.mdf')
            DbCursor = DbConnection.cursor()

            DbCursor.execute("INSERT INTO user VALUES (:name, :password,:access)",
                             {

                                 'name': self.user_name_textbox.get(),
                                 'password': encryptedpass,
                                 'access': self.user_access_combobox.get()

                             })
            DbConnection.commit()
            DbConnection.close()
            self.tree = None
            self.display_users_on_form()
            self.clear_inputs()
            self.user_name_textbox.focus()

            flag = True
            return flag
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    def clear_inputs(self):
        self.user_name_textbox.delete(0, tk.END)
        self.user_password_textbox.delete(0, tk.END)
        self.user_confirm_password_textbox.delete(0, tk.END)
