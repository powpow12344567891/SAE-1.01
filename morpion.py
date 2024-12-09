# Déclaration des variables
from Score import *
joueur1: int
joueur2: int
choix: int
tour: int
victoirej1: bool
victoirej2: bool
retourligne: int
val: int
tableau1: list[str]
ordre : int
choixtour : int
# Initialisation des variables
victoirej1 = False  # Indique si le joueur 1 a gagné
victoirej2 = False  # Indique si le joueur 2 a gagné
tour = 1  # Compteur des tours de jeu
tableau1 = ["  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  "]  # Grille initiale du morpion
# Liste des combinaisons gagnantes possibles
lignes_gagnantes = [
    [0, 1, 2],  # Ligne 1
    [3, 4, 5],  # Ligne 2
    [6, 7, 8],  # Ligne 3
    [0, 3, 6],  # Colonne 1
    [1, 4, 7],  # Colonne  2
    [2, 5, 8],  # Colonne 3
    [0, 4, 8],  # Diagonale principale
    [2, 4, 6]   # Diagonale secondaire
]
def initialisationtableau():
    global tableau1, tour, victoirej1, victoirej2, ajoutscore
    victoirej1 = False  # Indique si le joueur 1 a gagné
    victoirej2 = False  # Indique si le joueur 2 a gagné
    tour = 1 
    tableau1 = ["  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  "]
    ajoutscore[4] = 0
    ajoutscore[5] = 0
def affichagemorpion():# Fonction pour afficher le plateau de jeu
    print("tour", tour)
    print("\n")
    print(tableau1[6],tableau1[7],tableau1[8],)
    print("\n")     
    print(tableau1[3],tableau1[4],tableau1[5],)
    print("\n")
    print(tableau1[0],tableau1[1],tableau1[2],)
def choixdujoueur1():# Fonction pour gérer le choix du joueur 1
    global tableau1
    affichagemorpion()
    print("\n")
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            choix = int(input("Choix de la case joueur 1 (1 à 9) : "))  # Demander une case au joueur 1
            if 1 <= choix <= 9 and tableau1[choix - 1] == "  -  ":
                tableau1[choix - 1] = "  X  "  # Marquer la case avec un "X"
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
            else:
                print("Choix non valide, essayez à nouveau.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier entre 1 et 9.")
def choixdujoueur2():# Fonction pour gérer le choix du joueur 2
    global tableau1
    affichagemorpion()
    print("\n")
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            choix = int(input("Choix de la case joueur 2 (1 à 9) : "))  # Demander une case au joueur 2
            if 1 <= choix <= 9 and tableau1[choix - 1] == "  -  ":
                tableau1[choix - 1] = "  0  "  # Marquer la case avec un "0"
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
            else:
                print("Choix non valide, essayez à nouveau.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier entre 1 et 9.")
def victoire():# Fonction pour vérifier si un joueur a gagné

    global victoirej1, victoirej2  # Utilisation des variables globales
    # Vérification de toutes les combinaisons gagnantes
    for ligne in lignes_gagnantes: 
        if tableau1[ligne[0]] == tableau1[ligne[1]] == tableau1[ligne[2]] and tableau1[ligne[0]] != "  -  ":
            if tableau1[ligne[0]] == "  X  ":
                victoirej1 = True  # Joueur 1 gagne

            elif tableau1[ligne[0]] == "  0  ":
                victoirej2 = True  # Joueur 2 gagne
def morpionj1():# Fonction principale pour gérer le jeu
    global tour
    # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixdujoueur1()  # Tour du joueur 1
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant      
        ajout_val_score()                # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixdujoueur2()  # Tour du joueur 2
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant
    if victoirej1 == True:
        print("Victoire du joueur 1")
        affichagemorpion()
        ajoutscore[4] = 15-tour
        ajout_val_score()
        print("gain de", ajoutscore[4],"points au score")
    elif victoirej2 == True:
        print("Victoire du joueur 2")
        affichagemorpion()
        ajoutscore[5] = 15-tour
        ajout_val_score()
        print("gain de", ajoutscore[5],"points au score")
    else:
        print("égalité")
        affichagemorpion()
def morpionj2():
    global tour # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixdujoueur2()  # Tour du joueur 2
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant  
        # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixdujoueur1()  # Tour du joueur 1 
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant   # Vérification des résultats du jeu
    if victoirej1 == True:
        print("Victoire du joueur 1")
        ajoutscore[4] = 15-tour
        ajout_val_score()
        print("gain de", ajoutscore[4],"points au score")
        affichagemorpion()
    elif victoirej2 == True:
        print("Victoire du joueur 2")
        print("gain de", ajoutscore[5],"points au score")
        ajoutscore[5] = 15-tour
        ajout_val_score()
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
def morpion():
    initialisationtableau()
    print("Choix du joueur qui commence")
    print("1) Joueur 1 (X)")
    print("2) Joueur 2 (O)")
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            choixtour = int(input("Choix (1 ou 2) : "))
            if choixtour in [1, 2]:
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
                if choixtour == 1:
                    morpionj1()
                else:
                    morpionj2()
            else:
                print("Choix incorrect, veuillez entrer 1 ou 2.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier (1 ou 2).")