from data import get_employe_by_code

class LoginController:
    def __init__(self, app):
        self.app = app

    def verifier_identifiants(self, code, mot_de_passe):
        employe = get_employe_by_code(code)
        if employe and employe.verifier_mot_de_passe(mot_de_passe):
            return employe
        return None






"""
from data import get_employe_by_code

class LoginController:
    def __init__(self, app):
        self.app = app  # pour naviguer entre login et home

    def verifier_identifiants(self, code, mot_de_passe):
        employe = get_employe_by_code(code)
        if employe and employe.verifier_mot_de_passe(mot_de_passe):
            return employe
        return None
"""

