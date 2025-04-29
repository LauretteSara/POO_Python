import tkinter as tk
from tkinter import ttk
from utils.tooltip import Tooltip

class FilmView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = tk.LabelFrame(parent, text="Liste des films", padx=2, pady=2)
        self.frame.pack(fill="both", expand=True, padx=3, pady=1)

        self.film_mapping = {}  # Map item_id -> film
        self.detail_label = None

        self.build_ui()

    def build_ui(self):
        films = self.controller.get_all_films()

        columns = ("Nom", "Durée", "Catégories", "Action")
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140)

        for film in films:
            cat_str = ", ".join([cat.nom for cat in film.categories])
            item_id = self.tree.insert("", "end", values=(film.nom, film.duree, cat_str, "Voir acteurs"))
            self.film_mapping[item_id] = film

        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.pack(expand=True, fill="both")

        # Zone de détail (acteurs)
        self.detail_label = tk.Label(self.frame, text="", font=("Arial", 10), fg="blue", justify="left", anchor="w")
        self.detail_label.pack(fill="x", pady=2)

    def on_double_click(self, event):
        item = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)

        if not item or col != '#4':  # Vérifie si clic sur la colonne "Action"
            return

        film = self.film_mapping.get(item)
        if film:
            acteurs_str = "\n".join([str(act) for act in film.acteurs])
            self.detail_label.config(text=f"Acteurs du film \"{film.nom}\" :\n{acteurs_str}")





















"""
import tkinter as tk
from tkinter import ttk
from utils.tooltip import Tooltip

class FilmView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = tk.LabelFrame(parent, text="Liste des films", padx=10, pady=10)
        self.frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.build_ui()

    def build_ui(self):
        films = self.controller.get_all_films()
        tree = ttk.Treeview(self.frame, columns=("Nom", "Durée", "Catégories"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        for film in films:
            cat_str = ", ".join([cat.nom for cat in film.categories])
            item_id = tree.insert("", "end", values=(film.nom, film.duree, cat_str))
            Tooltip(tree, "\n".join([str(act) for act in film.acteurs]))
        tree.pack(expand=True, fill="both")


"""





"""
# view/film_view.py

import tkinter as tk
from tkinter import ttk

class FilmView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        films = self.controller.get_films()

        # Créer un tableau avec ttk.Treeview
        columns = ("nom", "duree", "description", "categories")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Définir les titres de colonnes
        self.tree.heading("nom", text="Nom du Film")
        self.tree.heading("duree", text="Durée (min)")
        self.tree.heading("description", text="Description")
        self.tree.heading("categories", text="Catégories")

        # Insérer les données
        for film in films:
            cat_names = ", ".join([cat.nom for cat in film.categories])
            self.tree.insert("", "end", values=(film.nom, film.duree, film.description, cat_names))
        
        self.tree.pack(expand=True, fill="both")

"""
