from abc import ABC, abstractmethod

# --- 1. ABSTRACTION & HÉRITAGE ---
class Personne(ABC):
    """
    Classe de base abstraite pour toutes les personnes du système.
    """
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    @abstractmethod
    def afficher_details(self):
        """Méthode abstraite qui sera implémentée par les classes filles."""
        pass

# Classe fille qui hérite de Personne
class Adherent(Personne):
    compteur_adherents = 0
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        Adherent.compteur_adherents += 1
        self.id_adherent = f"A{Adherent.compteur_adherents:03d}"
        self.livres_empruntes = [] # Agrégation (livres empruntés)
        
    # Polymorphisme : Implémentation spécifique de la méthode abstraite
    def afficher_details(self):
        return (f"Adhérent ID: {self.id_adherent}, Nom: {self.nom} {self.prenom}, "
                f"Livres empruntés: {len(self.livres_empruntes)}")

# --- 2. COMPOSITION & ENCAPSULATION ---

class Exemplaire:
    """
    Représente une copie physique d'un livre. 
    Dépend du Livre pour exister (Composition).
    """
    def __init__(self, cote):
        self.cote = cote # Numéro unique pour localiser l'exemplaire
        self.est_disponible = True
        
    def __del__(self):
        # Pour illustrer la Composition
        # print(f"\t[Composition] Exemplaire de cote {self.cote} est détruit.")
        pass


class Livre:
    def __init__(self, titre, auteur, isbn, nb_exemplaires):
        self.titre = titre
        self.auteur = auteur
        # Encapsulation : attribut privé
        self.__isbn = isbn 
        
        # Composition : La liste des exemplaires est créée et gérée ici
        self.exemplaires = []
        for i in range(1, nb_exemplaires + 1):
            cote = f"{isbn[:4]}-{i:02d}"
            self.exemplaires.append(Exemplaire(cote))
            
    # Getter pour l'attribut privé
    def get_isbn(self):
        return self.__isbn

    # Polymorphisme : Méthode d'affichage
    def afficher_details(self):
        nb_dispo = sum(1 for e in self.exemplaires if e.est_disponible)
        return (f"Livre: '{self.titre}' par {self.auteur} (ISBN: {self.__isbn}). "
                f"Exemplaires totaux: {len(self.exemplaires)}, Disponibles: {nb_dispo}")

# --- 3. GESTION DES EXCEPTIONS ---

class InventaireError(Exception):
    """Classe de base pour toutes les erreurs d'inventaire de la bibliothèque."""
    pass

class LivreIndisponibleError(InventaireError):
    """Levée si aucun exemplaire n'est disponible pour l'emprunt."""
    def __init__(self, titre):
        super().__init__(f"Tous les exemplaires du livre '{titre}' sont déjà empruntés.")

class LivreNonTrouveError(InventaireError):
    """Levée si le titre n'est pas dans l'inventaire principal."""
    def __init__(self, titre):
        super().__init__(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")


# --- 4. AGRÉGATION & LOGIQUE D'APPLICATION ---

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        # Agrégation : Les livres et adhérents sont créés ailleurs et ajoutés ici
        self.inventaire_livres = {} # {isbn: Livre_object}
        self.liste_adherents = {} # {id: Adherent_object}
        
    # --- Méthodes d'Agrégation ---
    def ajouter_livre(self, livre):
        self.inventaire_livres[livre.get_isbn()] = livre
        print(f"\n[OK] Livre '{livre.titre}' ajouté à l'inventaire.")

    def enregistrer_adherent(self, adherent):
        self.liste_adherents[adherent.id_adherent] = adherent
        print(f"\n[OK] Adhérent {adherent.nom} enregistré avec ID {adherent.id_adherent}.")
        
    # --- Méthode de Logique avec Exception ---
    def emprunter_livre(self, titre, adherent_id):
        # 1. Trouver le Livre
        livre_cible = next((l for l in self.inventaire_livres.values() if l.titre == titre), None)
        
        if not livre_cible:
            # Lever l'exception si le livre n'est pas trouvé
            raise LivreNonTrouveError(titre)
            
        # 2. Trouver un Exemplaire disponible (Composition/Agrégation)
        exemplaire_dispo = next((e for e in livre_cible.exemplaires if e.est_disponible), None)
        
        if not exemplaire_dispo:
            # Lever l'exception si le livre est indisponible
            raise LivreIndisponibleError(titre)

        # 3. Logique d'emprunt
        adherent = self.liste_adherents.get(adherent_id)
        if not adherent:
             print(f"\n[ERREUR] Adhérent ID {adherent_id} non trouvé.")
             return

        exemplaire_dispo.est_disponible = False
        adherent.livres_empruntes.append(exemplaire_dispo)
        print(f"\n[EMPRUNT OK] '{livre_cible.titre}' (Cote: {exemplaire_dispo.cote}) emprunté par {adherent.prenom}.")

    # --- Méthode de Polymorphisme ---
    def afficher_inventaire(self):
        print("\n" + "="*40)
        print(f"Inventaire de la {self.nom} ({len(self.inventaire_livres)} titres)")
        print("="*40)
        for livre in self.inventaire_livres.values():
            # Polymorphisme : Appel de la méthode afficher_details() du Livre
            print(livre.afficher_details())
        
        print("\n--- Adhérents ---")
        for adherent in self.liste_adherents.values():
            # Polymorphisme : Appel de la méthode afficher_details() de l'Adherent
            print(adherent.afficher_details())
            

# --- 5. DÉMONSTRATION GLOBALE ---

# 1. Initialisation
ma_bibliotheque = Bibliotheque("Médiathèque du Savoir")

# 2. Agrégation d'Adhérents
alice = Adherent("Durand", "Alice")
bob = Adherent("Lefevre", "Bob")
ma_bibliotheque.enregistrer_adherent(alice)
ma_bibliotheque.enregistrer_adherent(bob)

# 3. Agrégation de Livres (avec Composition d'Exemplaires)
livre_poo = Livre("Maîtriser la POO", "P. Code", "P001", 2) # 2 exemplaires
livre_python = Livre("Python pour Tous", "G. Van", "PYT1", 1) # 1 exemplaire
ma_bibliotheque.ajouter_livre(livre_poo)
ma_bibliotheque.ajouter_livre(livre_python)

ma_bibliotheque.afficher_inventaire()


# 4. Test des Exceptions et de la Logique d'Emprunt
print("\n" + "#"*40)
print("# Test de la logique d'Emprunt et des Exceptions #")
print("#"*40)

try:
    # Test 1 : Emprunt réussi (Exemplaire 1 de POO)
    ma_bibliotheque.emprunter_livre("Maîtriser la POO", alice.id_adherent)
    
    # Test 2 : Emprunt réussi (Livre Python - 1 seul exemplaire)
    ma_bibliotheque.emprunter_livre("Python pour Tous", bob.id_adherent)
    
    # Test 3 : Emprunt d'un livre inexistant (Lève LivreNonTrouveError)
    ma_bibliotheque.emprunter_livre("Le Code Perdu", alice.id_adherent)
    
except LivreIndisponibleError as e:
    # Gère l'indisponibilité
    print(f"\n[GESTION ERREUR] Problème d'inventaire : {e}")

except LivreNonTrouveError as e:
    # Gère le livre non trouvé (intercepté par le test 3)
    print(f"\n[GESTION ERREUR] Problème de catalogue : {e}")

# Test 4 : Tentative d'emprunter un livre indisponible (Exemplaire 2 de POO)
print("\n--- Test d'indisponibilité ---")
try:
    ma_bibliotheque.emprunter_livre("Maîtriser la POO", bob.id_adherent) # Exemplaire 1 déjà pris
    ma_bibliotheque.emprunter_livre("Maîtriser la POO", alice.id_adherent) # Exemplaire 2 pris par Alice!
    # Bob essaie le dernier exemplaire (sera pris)
    ma_bibliotheque.emprunter_livre("Maîtriser la POO", bob.id_adherent) 
    
    # Tente d'emprunter le 3e (qui n'existe pas) - Lève LivreIndisponibleError
    ma_bibliotheque.emprunter_livre("Maîtriser la POO", alice.id_adherent) 
    
except LivreIndisponibleError as e:
    # Gère l'indisponibilité (intercepté ici)
    print(f"\n[GESTION ERREUR] Problème d'inventaire : {e}")
except LivreNonTrouveError as e:
    pass # Ne devrait pas se produire ici

# 5. État Final
ma_bibliotheque.afficher_inventaire()