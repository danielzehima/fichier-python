from abc import ABC, abstractmethod

class Vehicule(ABC):
    
    @abstractmethod
    def demarrer(self):
        pass

class Voiture(Vehicule):
    def demarrer(self):
        return "La voiture démarre avec un vrombissement!"

class Moto(Vehicule):
    def demarrer(self):
        return "La moto démarre avec un rugissement!"


voiture1 = Voiture()
moto1 = Moto()
print(moto1.demarrer())
print(voiture1.demarrer())  