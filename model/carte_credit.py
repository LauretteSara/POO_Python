
from datetime import datetime

class CarteCredit:
    _id_counter = 1  # Compteur statique pour générer des IDs uniques
    
    def __init__(self, numero: str, date_expiration: str, code_secret: str):
        self.id_carte = CarteCredit._id_counter  # Assigner un ID unique
        CarteCredit._id_counter += 1  # Incrémenter le compteur pour la prochaine carte
        self.numero = numero
        self.date_expiration = datetime.strptime(date_expiration, "%Y-%m")
        self.code_secret = code_secret

    def est_valide(self) -> bool:
        """Vérifie si la carte n'est pas expirée."""
        return self.date_expiration > datetime.now()

    def __str__(self):
        expiration = self.date_expiration.strftime("%Y-%m")
        return f"ID: {self.id_carte} - Carte: {self.numero}, Expire le: {expiration}"



"""# modele de la carte de credit 

from datetime import datetime

class CarteCredit:
    def __init__(self, numero: str, date_expiration: str, code_secret: str):
        self.numero = numero
        # On attend un format "YYYY-MM" par exemple "2026-09"
        self.date_expiration = datetime.strptime(date_expiration, "%Y-%m")
        self.code_secret = code_secret

    def est_valide(self) -> bool:
        #Vérifie si la carte n'est pas expirée.
        return self.date_expiration > datetime.now()

    def __str__(self):
        expiration = self.date_expiration.strftime("%Y-%m")
        return f"Carte: {self.numero}, Expire le: {expiration}"


# est valide est utilisee pour verifie si la carte est valide lors de l'utilisation en cours """