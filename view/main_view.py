
import tkinter as tk

from view.client_view import ClientView
from view.film_view import FilmView
from controller.client_controller import ClientController
from controller.film_controller import FilmController

class MainView:
    def __init__(self, root, employe, app):
        self.root = root
        self.employe = employe
        self.app = app  # 👈 on récupère l'instance principale

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=5, pady=3)

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        # Menu principal
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.quit_app)

        # Ajouter la barre des boutons en haut de la fenêtre
        button_frame = tk.Frame(self.frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        # Bouton Déconnexion
        deconnexion_button = tk.Button(button_frame, text="Déconnexion", command=self.deconnexion)
        deconnexion_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Bouton Quitter
        quitter_button = tk.Button(button_frame, text="Quitter", command=self.quit_app)
        quitter_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Affichage des clients et des films
        ClientView(self.frame, ClientController())
        tk.Label(self.frame, text="").pack()
        FilmView(self.frame, FilmController())

    def deconnexion(self):
        self.frame.destroy()  # Ferme la fenêtre principale
        self.app.retour_login()  # Retour à la page de connexion

    def quit_app(self):
        self.root.quit()  # Quitte l'application




"""import tkinter as tk
from view.client_view import ClientView
from view.film_view import FilmView
from controller.client_controller import ClientController
from controller.film_controller import FilmController

class MainView:
    def __init__(self, root, employe, app):
        self.root = root
        self.employe = employe
        self.app = app

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        # Menu principal
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.quitter_app)

        # Frame principale
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Barre des boutons (en haut)
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        deconnexion_button = tk.Button(button_frame, text="Déconnexion", command=self.deconnexion)
        deconnexion_button.pack(side=tk.LEFT, padx=2, pady=2)

        quitter_button = tk.Button(button_frame, text="Quitter", command=self.quitter_app)
        quitter_button.pack(side=tk.LEFT, padx=4, pady=4)

        # 2. Contenu principal
        content_frame = tk.Frame(self.main_frame)
        content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # ClientView
        client_frame = tk.Frame(content_frame)
        client_frame.pack(side=tk.TOP, fill=tk.X, pady=(3, 1))
        ClientView(client_frame, ClientController())

        # FilmView
        film_frame = tk.Frame(content_frame)
        film_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(2, 3))
        FilmView(film_frame, FilmController())

    def deconnexion(self):
        self.destroy()
        self.app.retour_login()

    def quitter_app(self):
        self.root.destroy()

    def destroy(self):
        self.main_frame.destroy()

"""

"""import tkinter as tk
from view.client_view import ClientView
from view.film_view import FilmView
from controller.client_controller import ClientController
from controller.film_controller import FilmController

class MainView:
    def __init__(self, root, employe, app):
        self.root = root
        self.employe = employe
        self.app = app

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.root.quit)

        # FRAME PRINCIPALE
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Barre des boutons
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        deconnexion_button = tk.Button(button_frame, text="Déconnexion", command=self.deconnexion)
        deconnexion_button.pack(side=tk.LEFT, padx=2, pady=2)

        quitter_button = tk.Button(button_frame, text="Quitter", command=self.root.quit)
        quitter_button.pack(side=tk.LEFT, padx=4, pady=4)

        # 2. Contenu principal
        content_frame = tk.Frame(self.main_frame)
        content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # ➡️ ClientView
        client_frame = tk.Frame(content_frame)
        client_frame.pack(side=tk.TOP, fill=tk.X, pady=(3, 1))  # Moins de marge
        ClientView(client_frame, ClientController())

        # ➡️ FilmView
        film_frame = tk.Frame(content_frame)
        film_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(2, 3))  # FilmView peut s'étendre
        FilmView(film_frame, FilmController())

    def deconnexion(self):
        self.main_frame.destroy()
        self.app.retour_login()
"""

"""import tkinter as tk

from view.client_view import ClientView
from view.film_view import FilmView
from controller.client_controller import ClientController
from controller.film_controller import FilmController

class MainView:
    def __init__(self, root, employe, app):
        self.root = root
        self.employe = employe
        self.app = app  # 👈 on récupère l'instance principale

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.root.quit)


        # Affichage des clients et des films
        ClientView(self.frame, ClientController())
        tk.Label(self.frame, text="").pack()
        FilmView(self.frame, FilmController())

    def deconnexion(self):
        self.frame.destroy()
        self.app.retour_login()  # 👈 retour à la page de connexion

"""
"""import tkinter as tk
from view.client_view import afficher_clients
from view.film_view import afficher_films

class MainView:
    def __init__(self, root, employe):
        self.root = root
        seimport tkinter as tk

from view.client_view import ClientView
from view.film_view import FilmView
from controller.client_controller import ClientController
from controller.film_controller import FilmController

class MainView:
    def __init__(self, root, employe, app):
        self.root = root
        self.employe = employe
        self.app = app  # 👈 on récupère l'instance principale

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.root.quit)


        # Affichage des clients et des films
        ClientView(self.frame, ClientController())
        tk.Label(self.frame, text="").pack()
        FilmView(self.frame, FilmController())

    def deconnexion(self):
        self.frame.destroy()
        self.app.retour_login()  # 👈 retour à la page de connexion
lf.employe = employe

        self.root.title(f"Bienvenue {employe.prenom} {employe.nom} — Accès : {employe.type_acces.upper()}")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Barre de menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        compte_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Compte", menu=compte_menu)
        compte_menu.add_command(label="Déconnexion", command=self.deconnexion)
        compte_menu.add_command(label="Quitter", command=self.root.quit)

        # Afficher le tableau des clients
        afficher_clients(self.frame)

        # Espacement
        tk.Label(self.frame, text="").pack()

        # Afficher le tableau des films
        afficher_films(self.frame)

    def deconnexion(self):
        self.frame.destroy()
        from view.login_view import LoginView
        LoginView(self.root)
"""