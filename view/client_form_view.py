# fichier: view/client_form_view.py


import tkinter as tk
from tkinter import messagebox
from model.client import Client
from datetime import date
import re

class ClientFormView(tk.Toplevel):
    def __init__(self, root, controller, client_view, client_existant=None):
        super().__init__(root)
        self.title("Modifier un client" if client_existant else "Créer un client")
        self.controller = controller
        self.client_view = client_view
        self.client_existant = client_existant  # Peut être None

        self.entries = {}

        champs = [
            "Nom", "Prénom",
            "Courriel", "Mot de passe", 
            "Carte(s) de crédit (séparées par des virgules)"
        ]

        # Nom
        tk.Label(self, text="Nom").pack()
        nom_entry = tk.Entry(self)
        nom_entry.pack()
        self.entries["Nom"] = nom_entry

        # Prénom
        tk.Label(self, text="Prénom").pack()
        prenom_entry = tk.Entry(self)
        prenom_entry.pack()
        self.entries["Prénom"] = prenom_entry

        # Sexe
        tk.Label(self, text="Sexe").pack()
        self.sexe_var = tk.StringVar(self)
        self.sexe_var.set("Homme")
        sexe_menu = tk.OptionMenu(self, self.sexe_var, "Homme", "Femme", "Autre")
        sexe_menu.pack()

        # Courriel
        tk.Label(self, text="Courriel").pack()
        courriel_entry = tk.Entry(self)
        courriel_entry.pack()
        self.entries["Courriel"] = courriel_entry

        # Mot de passe
        tk.Label(self, text="Mot de passe").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()
        self.entries["Mot de passe"] = password_entry

        # Cartes crédit
        tk.Label(self, text="Carte(s) de crédit (séparées par des virgules)").pack()
        cartes_entry = tk.Entry(self)
        cartes_entry.pack()
        self.entries["Carte(s) de crédit (séparées par des virgules)"] = cartes_entry

        # Pré-remplir si modification
        if client_existant:
            self.entries["Nom"].insert(0, client_existant.nom)
            self.entries["Prénom"].insert(0, client_existant.prenom)
            self.sexe_var.set(client_existant.sexe)
            self.entries["Courriel"].insert(0, client_existant.courriel)
            self.entries["Courriel"].config(state="disabled")  # Courriel non modifiable
            self.entries["Mot de passe"].insert(0, client_existant.password)
            cartes = ",".join(str(c.id_carte) for c in client_existant.cartes_credit)
            self.entries["Carte(s) de crédit (séparées par des virgules)"].insert(0, cartes)

        tk.Button(self, text="Valider", command=self.valider_formulaire).pack(pady=10)

    def valider_formulaire(self):
        nom = self.entries["Nom"].get().strip()
        prenom = self.entries["Prénom"].get().strip()
        sexe = self.sexe_var.get()
        courriel = self.entries["Courriel"].get().strip()
        password = self.entries["Mot de passe"].get().strip()

        cartes_ids = [int(c.strip()) for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        if not all([nom, prenom, sexe, courriel, password]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

         # 📍 AJOUT ICI ➔ Validation correcte des cartes de crédit
        if not self.client_existant:
            # Cas création : interdit d'utiliser cartes déjà attribuées
            if self.controller.cartes_credit_existent_deja(cartes_ids):
                messagebox.showerror("Erreur", "Cartes déjà utilisées.")
                return
        else:
            # Cas modification : autoriser ses propres cartes
            cartes_ids_autorisees = {carte.id_carte for carte in self.client_existant.cartes_credit}
            if self.controller.cartes_credit_existent_deja(cartes_ids, cartes_ids_autorisees):
                messagebox.showerror("Erreur", "Certaines cartes sont déjà utilisées par d'autres clients.")
                return
        
        if len(password) < 8:
            messagebox.showerror("Erreur", "Mot de passe trop court (minimum 8 caractères).")
            return

        if not self.email_valide(courriel):
            messagebox.showerror("Erreur", "Format du courriel invalide.")
            return

        if not self.client_existant and self.controller.courriel_existe(courriel):
            messagebox.showerror("Erreur", "Courriel déjà existant.")
            return

        if self.controller.cartes_credit_existent_deja(cartes_ids) and not self.client_existant:
            messagebox.showerror("Erreur", "Cartes déjà utilisées.")
            return

        try:
            nouveau_client = Client(nom, prenom, sexe, date.today().strftime("%Y-%m-%d"), courriel, password)
            
            # Si modification, définir les cartes autorisées (ses cartes existantes)
            cartes_ids_autorisees = set()
            if self.client_existant:
                cartes_ids_autorisees = {carte.id_carte for carte in self.client_existant.cartes_credit}

            for carte_id in cartes_ids:
                carte = self.controller.get_carte_by_id(carte_id, cartes_ids_autorisees)
                if carte:
                    nouveau_client.ajouter_carte_credit(carte)
                else:
                    raise ValueError(f"La carte ID {carte_id} est introuvable ou déjà attribuée.")
                        
            if self.client_existant:
                self.controller.update_client(self.client_existant, nouveau_client)
                messagebox.showinfo("Succès", "Client modifié avec succès.")
            else:
                self.controller.ajouter_client(nouveau_client)
                messagebox.showinfo("Succès", "Client ajouté avec succès.")

            self.client_view.rafraichir_liste()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def email_valide(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        return re.match(pattern, email) is not None




"""import tkinter as tk
from tkinter import messagebox
from controller.client_controller import ClientController
from model.client import Client
from datetime import date
import re  # pour valider l'email

class ClientFormView(tk.Toplevel):
    def __init__(self, root, controller, client_view):
        super().__init__(root)
        self.title("Nouveau client")
        self.controller = controller
        self.client_view = client_view

        # Champs texte
        self.entries = {}

        champs = [
            "Nom", "Prénom",
            "Courriel", "Mot de passe", 
            "Carte(s) de crédit (séparées par des virgules)"
        ]

        # Nom
        tk.Label(self, text="Nom").pack()
        nom_entry = tk.Entry(self)
        nom_entry.pack()
        self.entries["Nom"] = nom_entry

        # Prénom
        tk.Label(self, text="Prénom").pack()
        prenom_entry = tk.Entry(self)
        prenom_entry.pack()
        self.entries["Prénom"] = prenom_entry

        # Sexe (menu déroulant)
        tk.Label(self, text="Sexe").pack()
        self.sexe_var = tk.StringVar(self)
        self.sexe_var.set("Homme")  # valeur par défaut
        sexe_menu = tk.OptionMenu(self, self.sexe_var, "Homme", "Femme", "Autre")
        sexe_menu.pack()

        # Courriel
        tk.Label(self, text="Courriel").pack()
        courriel_entry = tk.Entry(self)
        courriel_entry.pack()
        self.entries["Courriel"] = courriel_entry

        # Mot de passe
        tk.Label(self, text="Mot de passe").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()
        self.entries["Mot de passe"] = password_entry

        # Carte(s) de crédit
        tk.Label(self, text="Carte(s) de crédit (séparées par des virgules, utilisez uniquement les IDs)").pack()
        cartes_entry = tk.Entry(self)
        cartes_entry.pack()
        self.entries["Carte(s) de crédit (séparées par des virgules)"] = cartes_entry

        tk.Button(self, text="Valider", command=self.valider_formulaire).pack(pady=10)

    def valider_formulaire(self):
        nom = self.entries["Nom"].get().strip()
        prenom = self.entries["Prénom"].get().strip()
        sexe = self.sexe_var.get()
        courriel = self.entries["Courriel"].get().strip()
        password = self.entries["Mot de passe"].get().strip()

        cartes_ids = [int(c.strip()) for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        #cartes_ids = [c.strip() for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        date_inscription = date.today().strftime("%Y-%m-%d")

        if not all([nom, prenom, sexe, courriel, password]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        if len(password) < 8:
            messagebox.showerror("Erreur", "Mot de passe incorrect : il doit contenir au moins 8 caractères.")
            return

        if not self.email_valide(courriel):
            messagebox.showerror("Erreur", "Format du courriel invalide.")
            return

        if self.controller.courriel_existe(courriel):
            messagebox.showerror("Erreur", "Courriel déjà existant.")
            return

        # Vérifier si les cartes IDs existent déjà
        if self.controller.cartes_credit_existent_deja(cartes_ids):
            messagebox.showerror("Erreur", "Une ou plusieurs cartes sont déjà attribuées à un autre client.")
            return

        try:
            nouveau_client = Client(nom, prenom, sexe, date_inscription, courriel, password)

            for carte_id in cartes_ids:
                carte = self.controller.get_carte_by_id(carte_id)
                if carte:
                    nouveau_client.ajouter_carte_credit(carte)
                else:
                    raise ValueError(f"La carte avec l'ID {carte_id} n'existe pas.")
            
            self.controller.ajouter_client(nouveau_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès.")
            self.client_view.rafraichir_liste()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue : {e}")

    def email_valide(self, email):
        #Validation simple du format email avec une expression régulière.
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        return re.match(pattern, email) is not None

"""





"""import tkinter as tk
from tkinter import messagebox
from controller.client_controller import ClientController
from model.client import Client
from datetime import date
import re  # pour valider l'email

class ClientFormView(tk.Toplevel):
    def __init__(self, root, controller, client_view):
        super().__init__(root)
        self.title("Nouveau client")
        self.controller = controller
        self.client_view = client_view

        # Champs texte
        self.entries = {}

        champs = [
            "Nom", "Prénom",
            "Courriel", "Mot de passe", 
            "Carte(s) de crédit (séparées par des virgules)"
        ]

        # Nom
        tk.Label(self, text="Nom").pack()
        nom_entry = tk.Entry(self)
        nom_entry.pack()
        self.entries["Nom"] = nom_entry

        # Prénom
        tk.Label(self, text="Prénom").pack()
        prenom_entry = tk.Entry(self)
        prenom_entry.pack()
        self.entries["Prénom"] = prenom_entry

        # Sexe (menu déroulant)
        tk.Label(self, text="Sexe").pack()
        self.sexe_var = tk.StringVar(self)
        self.sexe_var.set("Homme")  # valeur par défaut
        sexe_menu = tk.OptionMenu(self, self.sexe_var, "Homme", "Femme", "Autre")
        sexe_menu.pack()

        # Courriel
        tk.Label(self, text="Courriel").pack()
        courriel_entry = tk.Entry(self)
        courriel_entry.pack()
        self.entries["Courriel"] = courriel_entry

        # Mot de passe
        tk.Label(self, text="Mot de passe").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()
        self.entries["Mot de passe"] = password_entry

        # Carte(s) de crédit
        tk.Label(self, text="Carte(s) de crédit (séparées par des virgules)").pack()
        cartes_entry = tk.Entry(self)
        cartes_entry.pack()
        self.entries["Carte(s) de crédit (séparées par des virgules)"] = cartes_entry

        tk.Button(self, text="Valider", command=self.valider_formulaire).pack(pady=10)

    def valider_formulaire(self):
        nom = self.entries["Nom"].get().strip()
        prenom = self.entries["Prénom"].get().strip()
        sexe = self.sexe_var.get()  # récupéré du menu déroulant
        courriel = self.entries["Courriel"].get().strip()
        password = self.entries["Mot de passe"].get().strip()
        cartes = [c.strip() for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        # Date automatique
        date_inscription = date.today().strftime("%Y-%m-%d")

        #date_inscription = date.today()

        # Vérification des champs
        if not all([nom, prenom, sexe, courriel, password]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        if len(password) < 8:
            messagebox.showerror("Erreur", "Mot de passe incorrect : il doit contenir au moins 8 caractères.")
            return

        if not self.email_valide(courriel):
            messagebox.showerror("Erreur", "Format du courriel invalide.")
            return

        if self.controller.courriel_existe(courriel):
            messagebox.showerror("Erreur", "Courriel déjà existant.")
            return

        if self.controller.cartes_credit_existent_deja(cartes):
            messagebox.showerror("Erreur", "Une ou plusieurs cartes sont déjà attribuées à un autre client.")
            return

        try:
            nouveau_client = Client(nom, prenom, sexe, date_inscription, courriel, password)
            for carte in cartes:
                nouveau_client.ajouter_carte_credit(carte)

            self.controller.ajouter_client(nouveau_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès.")
            self.client_view.rafraichir_liste()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue : {e}")

    def email_valide(self, email):
        #Validation simple du format email avec une expression régulière.
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        return re.match(pattern, email) is not None
"""
"""import tkinter as tk
from tkinter import messagebox
from controller.client_controller import ClientController
from model.client import Client

class ClientFormView(tk.Toplevel):
    def __init__(self, root, controller, client_view):
        super().__init__(root)
        self.title("Nouveau client")
        self.controller = controller
        self.client_view = client_view

        # Champs du formulaire
        self.entries = {}
        champs = [
            "Nom", "Prénom", "Sexe",
            "Date d'inscription (YYYY-MM-DD)", 
            "Courriel", "Mot de passe", 
            "Carte(s) de crédit (séparées par des virgules)"
        ]
        for champ in champs:
            tk.Label(self, text=champ).pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries[champ] = entry

        tk.Button(self, text="Valider", command=self.valider_formulaire).pack(pady=10)

    def valider_formulaire(self):
        nom = self.entries["Nom"].get().strip()
        prenom = self.entries["Prénom"].get().strip()
        sexe = self.entries["Sexe"].get().strip()
        date_inscription = self.entries["Date d'inscription (YYYY-MM-DD)"].get().strip()
        courriel = self.entries["Courriel"].get().strip()
        password = self.entries["Mot de passe"].get().strip()
        cartes = [c.strip() for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        if not all([nom, prenom, sexe, date_inscription, courriel, password]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        if len(password) < 8:
            messagebox.showerror("Erreur", "Mot de passe incorrect : il doit contenir au moins 8 caractères.")
            return

        if self.controller.courriel_existe(courriel):
            messagebox.showerror("Erreur", "Courriel déjà existant.")
            return

        if self.controller.cartes_credit_existent_deja(cartes):
            messagebox.showerror("Erreur", "Une ou plusieurs cartes sont déjà attribuées à un autre client.")
            return

        try:
            nouveau_client = Client(nom, prenom, sexe, date_inscription, courriel, password)
            for carte in cartes:
                nouveau_client.ajouter_carte_credit(carte)

            self.controller.ajouter_client(nouveau_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès.")
            self.client_view.rafraichir_liste()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue : {e}")
"""



"""# fichier: view/client_form_view.py

import tkinter as tk
from tkinter import messagebox
from controller.client_controller import ClientController
from model.client import Client

class ClientFormView(tk.Toplevel):
    def __init__(self, root, main_view):
        super().__init__(root)
        self.title("Nouveau client")
        self.main_view = main_view
        self.controller = ClientController()

        # Champs du formulaire
        self.entries = {}
        champs = ["Nom", "Prénom", "Sexe", "Date d'inscription (YYYY-MM-DD)", "Courriel", "Mot de passe", "Carte(s) de crédit (séparées par des virgules)"]
        for champ in champs:
            tk.Label(self, text=champ).pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries[champ] = entry

        tk.Button(self, text="Valider", command=self.valider_formulaire).pack(pady=10)

    def valider_formulaire(self):
        nom = self.entries["Nom"].get().strip()
        prenom = self.entries["Prénom"].get().strip()
        sexe = self.entries["Sexe"].get().strip()
        date_inscription = self.entries["Date d'inscription (YYYY-MM-DD)"].get().strip()
        courriel = self.entries["Courriel"].get().strip()
        password = self.entries["Mot de passe"].get().strip()
        cartes = [c.strip() for c in self.entries["Carte(s) de crédit (séparées par des virgules)"].get().split(',') if c.strip()]

        # 🔎 Vérifie que tous les champs sont remplis
        if not all([nom, prenom, sexe, date_inscription, courriel, password]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        # 🔒 Vérifie mot de passe
        if len(password) < 8:
            messagebox.showerror("Erreur", "Mot de passe incorrect : il doit contenir au moins 8 caractères.")
            return

        # 📧 Vérifie unicité du courriel
        if self.controller.courriel_existe(courriel):
            messagebox.showerror("Erreur", "Courriel déjà existant.")
            return

        # 💳 Vérifie unicité des cartes
        if self.controller.cartes_credit_existent_deja(cartes):
            messagebox.showerror("Erreur", "Une ou plusieurs cartes sont déjà attribuées à un autre client.")
            return

        try:
            nouveau_client = Client(nom, prenom, sexe, date_inscription, courriel, password)
            for carte in cartes:
                nouveau_client.ajouter_carte_credit(carte)

            self.controller.ajouter_client(nouveau_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès.")
            self.main_view.rafraichir_clients()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue : {e}")
"""