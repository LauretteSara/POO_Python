# classe mere qui defini le comportement general des classes qui en herite

class Personne:
    def __init__(self, nom: str, prenom: str, sexe: str):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.sexe})"
