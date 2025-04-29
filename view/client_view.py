import tkinter as tk
from tkinter import ttk, messagebox
from view.client_form_view import ClientFormView
from controller.client_controller import ClientController

class ClientView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.frame = tk.LabelFrame(parent, text="Liste des clients", padx=10, pady=10)
        self.frame.pack(fill="both", expand=True, padx=10, pady=5)

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(anchor="w")
        tk.Button(btn_frame, text="➕ Créer un client", command=self.ouvrir_formulaire_creation).pack(pady=5)

        # 🌳 Tableau
        self.tree = ttk.Treeview(self.frame, columns=("Nom", "Prénom", "Sexe", "Courriel", "Date inscription", "Actions"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both")

        self.tree.bind("<Double-1>", self.double_click_action)

        self.rafraichir_liste()

    def rafraichir_liste(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        clients = self.controller.get_all_clients()
        for client in clients:
            self.tree.insert("", "end", values=(
                client.nom, client.prenom, client.sexe, client.courriel, client.date_inscription, "Modifier / Supprimer"))

    def ouvrir_formulaire_creation(self):
        ClientFormView(self.parent, self.controller, self)

    def double_click_action(self, event):
        # Quand on double clique sur une ligne -> propose Modifier ou Supprimer
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        courriel = values[3]

        client = self.controller.get_client_by_courriel(courriel)
        if not client:
            return

        action = messagebox.askquestion("Action", "Voulez-vous modifier ce client ?", icon='question')

        if action == "yes":
            ClientFormView(self.parent, self.controller, self, client_existant=client)
        else:
            confirm = messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer ce client ?")
            if confirm:
                self.controller.delete_client(client)
                messagebox.showinfo("Succès", "Client supprimé avec succès.")
                self.rafraichir_liste()



"""import tkinter as tk
from tkinter import ttk
from view.client_form_view import ClientFormView  # À créer
from controller.client_controller import ClientController

class ClientView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.frame = tk.LabelFrame(parent, text="Liste des clients", padx=10, pady=10)
        self.frame.pack(fill="both", expand=True, padx=10, pady=5)

        # 🔘 Bouton de création
        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(anchor="w")
        tk.Button(btn_frame, text="➕ Créer un client", command=self.ouvrir_formulaire).pack(pady=5)

        # 🌳 Tableau des clients
        self.tree = ttk.Treeview(self.frame, columns=("Nom", "Prénom", "Sexe", "Courriel", "Date inscription"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both")

        # Rafraîchir la liste des clients
        self.rafraichir_liste()

    def rafraichir_liste(self):
        # 🧹 Nettoyage de l'ancien contenu
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Récupérer les clients
        clients = self.controller.get_all_clients()
        for client in clients:
            self.tree.insert("", "end", values=(
                client.nom, client.prenom, client.sexe, client.courriel, client.date_inscription.date()))  

    def ouvrir_formulaire(self):
        # 📤 Ouvre la fenêtre de formulaire pour créer un client
        ClientFormView(self.parent, self.controller, self)

"""



"""import tkinter as tk
from tkinter import ttk, messagebox
from view.client_form_view import ClientFormView  # 👈 à créer
from controller.client_controller import ClientController

class ClientView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.frame = tk.LabelFrame(parent, text="Liste des clients", padx=10, pady=10)
        self.frame.pack(fill="both", expand=True, padx=10, pady=5)

        # 🔘 Bouton de création
        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(anchor="w")
        tk.Button(btn_frame, text="➕ Créer un client", command=self.ouvrir_formulaire).pack(pady=5)

        #🌳 Tableau des clients
        self.tree = ttk.Treeview(self.frame, columns=("Nom", "Prénom", "Sexe", "Courriel", "Date inscription"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both")


        self.rafraichir_liste()
    

    def rafraichir_liste(self):
        # 🧹 Nettoyage de l'ancien contenu
        for row in self.tree.get_children():
            self.tree.delete(row)

        clients = self.controller.get_all_clients()
        for client in clients:
            self.tree.insert("", "end", values=(
                client.nom, client.prenom, client.sexe, client.courriel, client.date_inscription.date()))

    def ouvrir_formulaire(self):
        # 📤 Ouvre la fenêtre de formulaire
        ClientFormView(self.parent, self.controller, self)
"""


"""import tkinter as tk
from tkinter import ttk

class ClientView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = tk.LabelFrame(parent, text="Liste des clients", padx=10, pady=10)
        self.frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.build_ui()

    def build_ui(self):
        clients = self.controller.get_all_clients()
        tree = ttk.Treeview(self.frame, columns=("Nom", "Prénom", "Sexe", "Courriel", "Date inscription"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        for client in clients:
            tree.insert("", "end", values=(client.nom, client.prenom, client.sexe, client.courriel, client.date_inscription.date()))
        tree.pack(expand=True, fill="both")
"""