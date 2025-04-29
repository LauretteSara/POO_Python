from tkinter import Tk
from view.login_view import LoginView
from controller.login_controller import LoginController
from view.main_view import MainView

class Application:
    def __init__(self, root):
        self.root = root
        self.login_view = LoginView(root, self)  # 👈 on passe self pour pouvoir appeler `ouvrir_fenetre_principale`

    def ouvrir_fenetre_principale(self, employe):
        self.login_view.frame.destroy()
        self.main_view = MainView(self.root, employe, self)

    def retour_login(self):
        self.main_view.frame.destroy()
        self.login_view = LoginView(self.root, self)

def main():
    root = Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()





"""
from tkinter import Tk
from view.login_view import LoginView

def main():
    root = Tk()
    app = LoginView(root)  # pas besoin de passer de contrôleur ici
    root.mainloop()

if __name__ == "__main__":
    main()


"""



"""
import tkinter as tk
from controller.login_controller import LoginController
from view.login_view import LoginView
from view.client_view import ClientView
from view.film_view import FilmView

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de films et clients")
        self.login_controller = LoginController(self)
        self.login_view = LoginView(root, self.login_controller)

    def ouvrir_fenetre_principale(self, employe):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.menu.add_command(label="Se déconnecter", command=self.retour_login)
        self.menu.add_command(label="Quitter", command=self.root.quit)

        self.client_view = ClientView(self.root, role=employe.role)
        self.film_view = FilmView(self.root, controller=self.client_view.controller)  # ou son propre controller

    def retour_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
"""










"""
import tkinter as tk
from controller.client_controller import ClientController
from controller.film_controller import FilmController
from view.client_view import ClientView
from view.film_view import FilmView

def main():
    root = tk.Tk()
    root.title("Application de gestion")
    root.geometry("900x600")

    client_ctrl = ClientController()
    film_ctrl = FilmController()

    ClientView(root, client_ctrl)
    FilmView(root, film_ctrl)

    root.mainloop()

if __name__ == "__main__":
    main()

"""











"""
# main.py

import tkinter as tk
from controller.film_controller import FilmController
from view.film_view import FilmView

def main():
    root = tk.Tk()
    root.title("Liste des Films")
    root.geometry("800x400")
    
    controller = FilmController()
    app = FilmView(root, controller)

    root.mainloop()

if __name__ == "__main__":
    main()

"""
