from Score import ajoutscore, ajout_val_score
import random

def choix_pvpve():
    choixMode:int
    print("Entrez 1 pour jouer contre un autre joueur local.")
    print("Entrez 2 pour jouer contre un bot à difficultée variable.")
    print("Entrez 3 pour faire jouer un bot contre un autre avec difficultée variable.")
    choixMode=int(input("Entrez votre choix: "))
    if choixMode==1:
        joueur1 = input("Entrez le nom du joueur 1: ")
        joueur2 = input("Entrez le nom du joueur 2: ")
        allumette(joueur1, joueur2, choixMode)
    elif choixMode==2:
        joueur1 = input("Entrez le nom du joueur 1: ")
        joueur2 = "Ordinateur_1"
        allumette(joueur1, joueur2, choixMode)
    elif choixMode==3:
        joueur1 = "Ordinateur_1"
        joueur2 = "Ordinateur_2"
        allumette(joueur1, joueur2, choixMode)

def allumette(joueur1: str, joueur2: str, choixMode:int):
    choixj1: int
    choixj2: int
    allumette: int = 20
    perdant: int = 0  # Affiche le nombre initial d'allumettes
    print("Il y a un total de", allumette, "allumettes.")
    print("|" * allumette)
    while allumette > 0:  
        # Tour du joueur 1
        print(f"{joueur1}, c'est votre tour.")
        if choixMode==1 or choixMode==2:
            choixj1 = demande_allumettes(f"{joueur1}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        else:
            choixj1=random.randint(1,3)
        
        while choixj1 > allumette:
            print("Erreur, il n'y a pas la quantité d'allumette que vous souhaité retirer.")
            choixj1 = demande_allumettes(f"{joueur1}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        allumette -= choixj1

        if allumette <= 0:
            print("Vous avez retiré la dernière allumette.")
            perdant = 1
            cond_vic(perdant, joueur1, joueur2)
            break

        print(f"{joueur1} a pris {choixj1} allumettes.")
        if allumette > 1:
            print("Il reste", allumette, "allumettes.")
        else:
            print("Il reste", allumette, "allumette.")
        print("|" * allumette)

        # Tour du joueur 2
        print("C'est au tour de",f"{joueur2}")
        if choixMode==1:
            choixj2 = demande_allumettes(f"{joueur2}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
            while choixj2 > allumette:
                print("Erreur, il n'y a pas la quantité d'allumette que vous souhaité retirer.")
                choixj2 = demande_allumettes(f"{joueur2}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
            allumette -= choixj2
        else:
            choixj2=random.randint(1,3)
            while choixj2 > allumette:
                choixj2 = random.randint(1,allumette)
            allumette -= choixj2
            
        if allumette <= 0:
            print("Vous avez retiré la dernière allumette.")
            perdant = 2
            cond_vic(perdant, joueur1, joueur2)
            break

        print(f"{joueur2} a pris {choixj2} allumettes.")
        if allumette > 1:
            print("Il reste", allumette, "allumettes.")
        else:
            print("Il reste", allumette, "allumette.")
        print("|" * allumette)
# Affichage des résultats
def cond_vic(perdant:int, joueur1: str, joueur2: str):
    if perdant == 1:
        ajoutscore[3] = 10
        ajout_val_score()
        print(f"{joueur2} a gagné et remporte {ajoutscore[3]} points !")
        print(f"{joueur1} a perdu.")
    elif perdant == 2:
        ajoutscore[2] = 10
        ajout_val_score()
        print(f"{joueur1} a gagné et remporte {ajoutscore[2]} points !")
        print(f"{joueur2} a perdu.")
    

# Fonction pour demander un nombre valide d'allumettes
def demande_allumettes(message: str):
    while True:
        try:
            choix = int(input(message))
            if 1 <= choix <= 3:
                return choix
            else:
                print("Erreur : Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")