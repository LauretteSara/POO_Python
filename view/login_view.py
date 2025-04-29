import tkinter as tk
from tkinter import messagebox
from controller.login_controller import LoginController

class LoginView:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # 👈 application principale
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.controller = LoginController(self)

        self.creer_interface()
    
    def creer_interface(self):
        tk.Label(self.frame, text="Code").pack()
        self.entree_code = tk.Entry(self.frame)
        self.entree_code.pack()

        tk.Label(self.frame, text="Mot de passe").pack()
        self.entree_password = tk.Entry(self.frame, show="*")
        self.entree_password.pack()

        tk.Button(self.frame, text="Connexion", command=self.se_connecter).pack(pady=10)


    def se_connecter(self):
        code = self.entree_code.get()
        mot_de_passe = self.entree_password.get()
        employe = self.controller.verifier_identifiants(code, mot_de_passe)
        if employe:
            self.app.ouvrir_fenetre_principale(employe)  # 👈 c’est maintenant correct
        else:
            messagebox.showerror("Erreur", "Identifiants invalides")













"""
import tkinter as tk
from tkinter import messagebox
from controller.login_controller import LoginController

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")
        self.controller = LoginController(self)
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Code utilisateur").pack()
        self.entry_code = tk.Entry(self.frame)
        self.entry_code.pack()

        tk.Label(self.frame, text="Mot de passe").pack()
        self.entry_mdp = tk.Entry(self.frame, show="*")
        self.entry_mdp.pack()

        tk.Button(self.frame, text="Se connecter", command=self.se_connecter).pack(pady=10)

    def se_connecter(self):
        code = self.entry_code.get()
        mdp = self.entry_mdp.get()

        employe = self.controller.verifier_identifiants(code, mdp)
        if employe:
            self.frame.destroy()
            self.controller.app.ouvrir_fenetre_principale(employe)
        else:
            messagebox.showerror("Erreur", "Code ou mot de passe incorrect")
"""