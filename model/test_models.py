# Permet de creer plusieurs instances de nos modeles et voir comment ils fonctionnent entre eux 


import sys
import os

# Ajoute le dossier parent du fichier courant dans les chemins d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from model.client import Client
from model.carte_credit import CarteCredit
from model.film import Film
from model.categorie import Categorie
from model.acteur import Acteur
from model.employe import Employe

# Création d'un client avec une carte de crédit
client = Client("Dupont", "Alice", "F", "2025-04-01", "alice.dupont@example.com", "motdepasse123")
carte = CarteCredit("1234-5678-9012-3456", "2026-09", "789")
client.ajouter_carte_credit(carte)
print(client)
print(carte)
print("Carte valide ?", carte.est_valide())

# Création d'un film et ajout de catégories
film = Film("Une Aventure", 120, "Film d'aventure épique")
categorie1 = Categorie("Action", "Films d'action et aventures")
categorie2 = Categorie("Comédie", "Moments drôles et divertissement")

film.ajouter_categorie(categorie1)
film.ajouter_categorie(categorie2)
print(film)

# Création d'un acteur et association au film
acteur = Acteur("Martin", "Bob", "M", "Héros", "2024-01-01", "2025-12-31", 5000.0)
film.ajouter_acteur(acteur)
print(acteur)

# Création d'un employé
employe = Employe("Lefevre", "Claire", "F", "2024-02-15", "emp001", "secret", "total")
print(employe)
