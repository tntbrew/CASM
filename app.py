import tkinter as tk

from filemenu import FileMenu
from loginform import Login


class CanLineApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Can Line Assistant')
        # self.master.geometry('325x150')
        # self.master.resizable(0, 0)

        self.master.configure(bg='cadet blue')

        # maximize window
        self.master.state('zoomed')
        FileMenu(self.master).create_file_menu()
        # UserManager(self.master).create_new_user_form()
        self.login()

    def login(self):
        Login(self.master).create_login_window()


def main():
    root = tk.Tk()
    app = CanLineApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
