#on crée ne classe mère Animal

class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def faire_un_son(self):
        return f"(.........)"
    
    def se_presenter(self):
        return f"Je suis {self.nom}, un(e) {self.espece}."

class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom, "Chien")
        self.race = race    
    def faire_un_son(self):
        return "Woof Woof!" 
    def se_presenter(self):
        return f"Je suis {self.nom}, j'aboie: {self.faire_un_son()}"
    
class Chat(Animal):
    def __init__(self, nom, couleur):
        super().__init__(nom, "Chat")
        self.couleur = couleur    
    def faire_un_son(self):
        return "Miaou Miaou!" 
    def se_presenter(self):
        return f"Je suis {self.nom}, je miaule: {self.faire_un_son()}"

class Vehicule:
    def __init__(self, marque, modele,vitese=0):
        self.marque = marque
        self.modele = modele
        self.vitesse= vitese
        
    def demarrer(self):
        return f"Le véhicule démarre.."
class Voiture(Vehicule):
          
    def demarrer(self):
        return f"La voiture {self.marque} {self.modele} démarre avec un vrombissement! et roule à une vitesse de {self.vitesse} km/h."

voitre1 = Voiture("Toyota", "Corolla",vitese=420)

print(voitre1.demarrer())


animal1=Chien("Rex", "Berger Allemand")
animal2=Chat("Whiskers", "Gris")    
print(animal1.se_presenter())
print(animal2.se_presenter())   
print(f"{animal1.nom} est de race {animal1.race}.")
print(f"{animal2.nom} est de couleur {animal2.couleur}.")
