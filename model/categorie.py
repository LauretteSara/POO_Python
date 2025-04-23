# modele pour les categories des films 

class Categorie:
    def __init__(self, nom: str, description: str):
        self.nom = nom
        self.description = description

    def __str__(self):
        return f"Catégorie: {self.nom} - {self.description}"
