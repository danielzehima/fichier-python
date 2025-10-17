import random

#nombre_secret
nombre_secret=random.randint(10,100)

#Le nombre de tentatives et essais
tentatives=5
essais=0
score=0
gain=10

print("\n"+"="*50)
print("\nDEVINETTE:JEU DE RECHERCHE D'UN NOMBRE SECRET\n")
print("Les indices : Tapez Q por quitter \n")
print("-"*50)
while essais<tentatives:
    choix=input("Veuillez entrer un ngombre compris entre 10 et 100 : ")
    
    if choix.upper()=='Q':
        print("Dommage, vos avez quitter l'application")
        break
    essais+=1
    score+=2
    try:
        nombre_choisi=int(choix)
        if nombre_choisi<nombre_secret:
            print("Le nombre est pls grand ")
        elif nombre_choisi>nombre_secret:
            print("lLe nombre est plus petit")
        elif nombre_choisi==nombre_secret:
            print(f"\nBravo, vous avez trové le nombre secret qui est : {nombre_secret}")
            print(f"Avec {essais} tentatives\nScore : {gain-score} ")
            break
        # si le nombre d'essais est egal a nomngre de tentatives
        if essais==tentatives:
            print(f"Dommage, vous avez atteint les {tentatives} essais \nScore: {gain-score}")
            print(f"Le nombre secret etait : {nombre_secret}")
            break # sortir de la boucle
    except ValueError:
        #reinitialiser l'essai
        essais-=1
        score-=2
        print("\nErreur! La valeur choisie est invalide ")
    print(f"Il vous reste {tentatives-essais} essais \n")
    
print("\nMerci d'avoir joué,  au revoir !!!")
    