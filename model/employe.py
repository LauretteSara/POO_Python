from model.personne import Personne
from datetime import datetime
import hashlib

class Employe(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_embauche: str, code_utilisateur: str, password: str, type_acces: str):
        super().__init__(nom, prenom, sexe)
        self.date_embauche = datetime.strptime(date_embauche, "%Y-%m-%d")
        self.code_utilisateur = code_utilisateur
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.type_acces = type_acces  # "lecture" ou "total"

    def verifier_mot_de_passe(self, mot_de_passe: str) -> bool:
        return self.password_hash == hashlib.sha256(mot_de_passe.encode()).hexdigest()

    def __str__(self):
        return f"Employé: {super().__str__()} - Accès: {self.type_acces}"




"""
# classe definissant les employes 

from model.personne import Personne
from datetime import datetime

class Employe(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_embauche: str, code_utilisateur: str, password: str, type_acces: str):
        super().__init__(nom, prenom, sexe)
        self.date_embauche = datetime.strptime(date_embauche, "%Y-%m-%d")
        self.code_utilisateur = code_utilisateur
        self.password = password
        self.type_acces = type_acces  # "lecture" ou "total"

    def __str__(self):
        return f"Employé: {super().__str__()} - Accès: {self.type_acces}"
"""

