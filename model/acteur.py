# defition des acteurs 

from model.personne import Personne
from datetime import datetime

class Acteur(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, nom_personnage: str, debut_emploi: str, fin_emploi: str, cachet: float):
        super().__init__(nom, prenom, sexe)
        self.nom_personnage = nom_personnage
        self.debut_emploi = datetime.strptime(debut_emploi, "%Y-%m-%d")
        self.fin_emploi = datetime.strptime(fin_emploi, "%Y-%m-%d")
        self.cachet = cachet
        self.films = []  # Liste de films dans lesquels l'acteur a joué

    def ajouter_film(self, film):
        self.films.append(film)

    def __str__(self):
        return f"Acteur: {super().__str__()} - Personnage: {self.nom_personnage}"
