from data import clients, cartes_credit

class ClientController:
    def __init__(self):
        self.clients = []  # Liste des clients dynamiquement ajoutés

    def ajouter_client(self, client):
        self.clients.append(client)

    def get_all_clients(self):
        return clients + self.clients

    
    def cartes_credit_existent_deja(self, cartes_ids, cartes_ids_autorisees=None):
        ids_cartes_connues = {carte.id_carte for carte in cartes_credit}
        ids_cartes_attribuees = set()
        for client in clients + self.clients:
            ids_cartes_attribuees.update(carte.id_carte for carte in client.cartes_credit)

        # Les cartes autorisées doivent être retirées du contrôle
        if cartes_ids_autorisees:
            ids_cartes_attribuees -= set(cartes_ids_autorisees)

        for carte_id in cartes_ids:
            if carte_id not in ids_cartes_connues:
                return True
            if carte_id in ids_cartes_attribuees:
                return True
        return False
    

    def courriel_existe(self, courriel):
        """
        Vérifie si un courriel existe déjà parmi les clients existants 
        et ceux ajoutés dynamiquement.
        """
        # Fusionner les courriels des clients de data.py et des clients dynamiques
        courriels_existants = []

        # Ajouter les courriels des clients provenant de data.py
        for client in clients:
            courriels_existants.append(client.courriel)

        # Ajouter les courriels des clients ajoutés dynamiquement
        for client in self.clients:
            courriels_existants.append(client.courriel)

        # Vérifier si le courriel existe déjà
        return courriel in courriels_existants


    def get_carte_by_id(self, carte_id, cartes_ids_autorisees=None):
        """
        Récupère une carte libre (non attribuée) par son ID parmi les cartes existantes dans data.py.
        Autorise certaines cartes déjà attribuées si elles font partie des cartes_ids_autorisees.
        """

        try:
            carte_id = int(carte_id)
        except ValueError:
            return None  # Pas un entier

        # Chercher uniquement dans les cartes de data.py
        for carte in cartes_credit:
            if carte.id_carte == carte_id:
                # Vérifier si elle est déjà utilisée
                ids_cartes_attribuees = set()
                for client in clients + self.clients:
                    ids_cartes_attribuees.update(c.id_carte for c in client.cartes_credit)

                # Autoriser les cartes qui sont déjà dans cartes_ids_autorisees
                if cartes_ids_autorisees:
                    ids_cartes_attribuees -= set(cartes_ids_autorisees)

                if carte_id in ids_cartes_attribuees:
                    return None  # Carte déjà prise par un autre
                return carte  # Carte disponible ou autorisée

        return None  # Carte non trouvée


    
    def get_client_by_courriel(self, courriel):
        for client in clients + self.clients:
            if client.courriel == courriel:
                return client
        return None

    def delete_client(self, client_to_delete):
        # Cherche si le client est dans la liste statique (clients de data.py)
        if client_to_delete in clients:
            clients.remove(client_to_delete)
        elif client_to_delete in self.clients:
            self.clients.remove(client_to_delete)

    def update_client(self, ancien_client, nouveau_client):
        if ancien_client in clients:
            index = clients.index(ancien_client)
            clients[index] = nouveau_client
        elif ancien_client in self.clients:
            index = self.clients.index(ancien_client)
            self.clients[index] = nouveau_client

    
"""from data import clients

class ClientController:
    def get_all_clients(self):
        return clients"""