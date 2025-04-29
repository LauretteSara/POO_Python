from datetime import datetime, timedelta
from model.acteur import Acteur
from model.carte_credit import CarteCredit
from model.categorie import Categorie
from model.client import Client
from model.employe import Employe
from model.film import Film
from model.personne import Personne

def generate_unique_credit_card_numbers(count):
    base_num = 453201680371120  # Numéro de base valide (Visa)
    return [str(base_num + i).zfill(15) for i in range(count)]

def generate_unique_passwords(count):
    base_passwords = [
        "SecurePass123!", "MovieLover456@", "CinemaFan789#",
        "FilmBuff012$", "SilverScreen345%", "Hollywood678^",
        "Blockbuster901&", "Director234*", "Actor567(", 
        "Producer890)", "Oscar123_", "Award456+",
        "Festival789=", "Theatre012|", "Projector345~"
    ]
    return base_passwords[:count]

credit_card_numbers = generate_unique_credit_card_numbers(14)
passwords = generate_unique_passwords(14)

# ========== CATÉGORIES ==========
categories = [
    Categorie("Action", "Films avec scènes de combat et poursuites"),
    Categorie("Comédie", "Films humoristiques et divertissants"),
    Categorie("Drame", "Histoires émotionnelles sérieuses"),
    Categorie("Science-Fiction", "Univers futuristes et technologies avancées"),
    Categorie("Horreur", "Films conçus pour effrayer"),
    Categorie("Romance", "Histoires d'amour"),
    Categorie("Thriller", "Suspense et tension psychologique")
]

# ========== ACTEURS ==========
acteurs = [
    Acteur("Doe", "John", "M", "James Bond", "2020-01-15", "2023-12-31", 5000000),
    Acteur("Smith", "Will", "M", "Agent J", "2019-05-20", "2024-06-30", 8000000),
    Acteur("Jolie", "Angelina", "F", "Lara Croft", "2018-11-10", "2025-03-15", 7500000),
    Acteur("DiCaprio", "Leonardo", "M", "Jack Dawson", "2021-02-28", "2024-11-20", 9000000),
    Acteur("Portman", "Natalie", "F", "Padmé Amidala", "2020-07-15", "2023-10-31", 6000000),
    Acteur("Pitt", "Brad", "M", "Tyler Durden", "2019-09-05", "2024-04-18", 8500000),
    Acteur("Lawrence", "Jennifer", "F", "Katniss Everdeen", "2021-03-12", "2025-01-10", 7000000)
]

# ========== FILMS ==========
films = [
    Film("Mission Impossible 7", 148, "Nouvelle mission de l'équipe IMF"),
    Film("Matrix Resurrections", 148, "Retour dans la Matrice"),
    Film("Tomb Raider 2", 125, "Nouvelles aventures de Lara Croft"),
    Film("Inception 2", 142, "Nouveau voyage dans les rêves"),
    Film("Star Wars: New Hope", 138, "Suite de la saga galactique"),
    Film("Fight Club 2", 135, "Retour des règles du Fight Club"),
    Film("Hunger Games: Prequel", 140, "Origines des Hunger Games")
]

# Établir les relations films <-> catégories
films[0].ajouter_categorie(categories[0])  # Action
films[0].ajouter_categorie(categories[5])  # Romance
films[1].ajouter_categorie(categories[0])  # Action
films[1].ajouter_categorie(categories[3])  # Science-Fiction
films[2].ajouter_categorie(categories[0])  # Action
films[2].ajouter_categorie(categories[1])  # Comédie
films[3].ajouter_categorie(categories[3])  # Science-Fiction
films[3].ajouter_categorie(categories[6])  # Thriller
films[4].ajouter_categorie(categories[3])  # Science-Fiction
films[4].ajouter_categorie(categories[2])  # Drame
films[5].ajouter_categorie(categories[2])  # Drame
films[5].ajouter_categorie(categories[6])  # Thriller
films[6].ajouter_categorie(categories[0])  # Action
films[6].ajouter_categorie(categories[2])  # Drame

# Établir les relations films <-> acteurs
for i in range(7):
    films[i].ajouter_acteur(acteurs[i])
    if i < 6:
        films[i].ajouter_acteur(acteurs[i+1])

# Établir les relations acteurs <-> films
for i, acteur in enumerate(acteurs):
    acteur.ajouter_film(films[i])
    if i < 6:
        acteur.ajouter_film(films[i+1])

# ========== CARTES DE CRÉDIT ==========
cartes_credit = [
    CarteCredit(credit_card_numbers[0], "2025-12", "123"),
    CarteCredit(credit_card_numbers[1], "2024-10", "456"),
    CarteCredit(credit_card_numbers[2], "2026-03", "789"),
    CarteCredit(credit_card_numbers[3], "2025-08", "321"),
    CarteCredit(credit_card_numbers[4], "2024-11", "654"),
    CarteCredit(credit_card_numbers[5], "2026-05", "987"),
    CarteCredit(credit_card_numbers[6], "2025-07", "135"),

     # Ajout de 7 cartes supplémentaires
    CarteCredit(credit_card_numbers[7], "2026-01", "246"),
    CarteCredit(credit_card_numbers[8], "2025-06", "357"),
    CarteCredit(credit_card_numbers[9], "2024-09", "468"),
    CarteCredit(credit_card_numbers[10], "2026-02", "579"),
    CarteCredit(credit_card_numbers[11], "2025-11", "680"),
    CarteCredit(credit_card_numbers[12], "2024-12", "791"),
    CarteCredit(credit_card_numbers[13], "2026-04", "802")
]

# ========== CLIENTS ==========
clients = [
    Client("Tremblay", "Jean", "M", "2022-01-15", "jean.tremblay@email.com", passwords[0]),
    Client("Gagnon", "Marie", "F", "2022-02-20", "marie.gagnon@email.com", passwords[1]),
    Client("Roy", "Pierre", "M", "2022-03-10", "pierre.roy@email.com", passwords[2]),
    Client("Côté", "Sophie", "F", "2022-04-05", "sophie.cote@email.com", passwords[3]),
    Client("Bouchard", "Luc", "M", "2022-05-12", "luc.bouchard@email.com", passwords[4]),
    Client("Morin", "Julie", "F", "2022-06-18", "julie.morin@email.com", passwords[5]),
    Client("Lavoie", "Marc", "M", "2022-07-22", "marc.lavoie@email.com", passwords[6])
]

# Assigner des cartes de crédit aux clients
for i, client in enumerate(clients):
    client.ajouter_carte_credit(cartes_credit[i])
    if i % 2 == 0:  # Clients avec index pair (0, 2, 4, 6) reçoivent une 2ème carte
        client.ajouter_carte_credit(cartes_credit[i+7])  # On utilise les cartes supplémentaires

# ========== EMPLOYÉS ==========
employes = [
    Employe("Admin", "Super", "M", "2020-01-10", "admin", passwords[7], "total"),
    Employe("Lire", "Seulement", "F", "2021-03-15", "lecture", passwords[8], "lecture"),
    Employe("Manager", "Cinema", "M", "2020-05-20", "manager", passwords[9], "total"),
    Employe("Vendeur", "Ticket", "M", "2021-07-12", "vendeur1", passwords[10], "lecture"),
    Employe("Vendeuse", "Billets", "F", "2021-08-18", "vendeur2", passwords[11], "lecture"),
    Employe("Technicien", "Projection", "M", "2020-09-25", "tech1", passwords[12], "total"),
    Employe("Nettoyeur", "Salle", "M", "2021-11-30", "nettoyeur1", passwords[13], "lecture")
]

def get_employe_by_code(code_utilisateur: str):
    return next((e for e in employes if e.code_utilisateur == code_utilisateur), None)

def get_all_data():
    return {
        "categories": categories,
        "acteurs": acteurs,
        "films": films,
        "cartes_credit": cartes_credit,
        "clients": clients,
        "employes": employes
    }

def display_data():
    print("="*50)
    print("CATÉGORIES")
    print("="*50)
    for cat in categories:
        print(cat)
    
    print("\n" + "="*50)
    print("ACTEURS")
    print("="*50)
    for act in acteurs:
        print(f"{act} - Films: {', '.join([f.nom for f in act.films])}")
    
    print("\n" + "="*50)
    print("FILMS")
    print("="*50)
    for film in films:
        print(f"{film} - Acteurs: {', '.join([str(a) for a in film.acteurs])}")
    
    print("\n" + "="*50)
    print("CLIENTS")
    print("="*50)

    for client in clients:
        # Afficher l'ID de chaque carte de crédit associée à ce client
        carte_ids = [carte.id_carte for carte in client.cartes_credit]  # Liste des IDs des cartes
        print(f"{client} - Cartes: {', '.join(map(str, carte_ids))}")
    
    print("\n" + "="*50)
    print("EMPLOYÉS")
    print("="*50)
    for emp in employes:
        print(emp)
    
    print("\n" + "="*50)
    print("CARTES DE CRÉDIT")
    print("="*50)
    for carte in cartes_credit:
        print(carte)

if __name__ == "__main__":
    display_data()