# modele pour les films 

class Film:
    def __init__(self, nom: str, duree: int, description: str):
        self.nom = nom
        self.duree = duree  # durée en minutes
        self.description = description
        self.categories = []  # liste des catégories du film
        self.acteurs = []     # liste des acteurs du film

    def ajouter_categorie(self, categorie):
        """Ajoute une catégorie à ce film."""
        if categorie not in self.categories:
            self.categories.append(categorie)

    def ajouter_acteur(self, acteur):
        """Ajoute un acteur à ce film."""
        if acteur not in self.acteurs:
            self.acteurs.append(acteur)

    def __str__(self):
        cat_str = ", ".join([cat.nom for cat in self.categories])
        return f"Film: {self.nom} ({self.duree} min) - Catégories: [{cat_str}]"
