# definition d'un client 

from model.personne import Personne
from datetime import datetime

class Client(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_inscription: str, courriel: str, password: str):
        super().__init__(nom, prenom, sexe)
        self.date_inscription = datetime.strptime(date_inscription, "%Y-%m-%d")  # format: "2023-12-25"
        self.courriel = courriel
        self.password = password
        self.cartes_credit = []  # liste de cartes

    def ajouter_carte_credit(self, carte):
        self.cartes_credit.append(carte)

    def __str__(self):
        return f"Client: {super().__str__()} - {self.courriel} (Inscrit le {self.date_inscription.date()})"
