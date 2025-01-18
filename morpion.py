# Déclaration des variables
import random
from Score import ajoutscore, ajout_val_score
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
choixmode : int
diffbot : int
diffbot = 3

# Initialisation des variables
victoirej1 = False  # Indique si le joueur 1 a gagné
victoirej2 = False  # Indique si le joueur 2 a gagné
tour = 1  # Compteur des tours de jeu
tableau1 = ["  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  "]  # Grille initiale du morpion
 # Marquer que le choix est valide pour sortir de la boucle
# Liste des combinaisons gagnantes possibles
lignes_gagnantes = [
    [0, 1, 2],  # Ligne 1
    [3, 4, 5],  # Lige 2
    [6, 7, 8],  # Ligne 3
    [0, 3, 6],  # Colonne 1
    [1, 4, 7],  # Colonne  2
    [2, 5, 8],  # Colonne 3
    [0, 4, 8],  # Diagonale
    [2, 4, 6]   # Diagonale
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
            choix = int(input("Choix de la case joueur 1 (1 à 9 comme un pavé numerique) : "))  # Demander une case au joueur 1
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
            choix = int(input("Choix de la case joueur 2 (1 à 9 comme un pavé numerique) : "))  # Demander une case au joueur 2
            if 1 <= choix <= 9 and tableau1[choix - 1] == "  -  ":
                tableau1[choix - 1] = "  0  "  # Marquer la case avec un "0"
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
            else:
                print("Choix non valide, essayez à nouveau.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier entre 1 et 9.")
def choixbot1():
    global tableau1
    affichagemorpion()
    print("\n")
    if diffbot == 1: 
        choix_valide = False  # Indicateur pour vérifier si le choix est valide
        while choix_valide == False:
            choix = random.randint(1, 9)
            if 1 <= choix <= 9 and tableau1[choix - 1] == "  -  ":
                tableau1[choix - 1] = "  0  "  # Marquer la case avec un "0"
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
    if diffbot == 2: 
     # Jouer au centre si possible
        if tableau1[4] == "  -  ":
            tableau1[4] = "  0  "
        else:
            # Liste des coins et des bords
            coins = [0, 2, 6, 8]
            bords = [1, 3, 5, 7]
            
            # Prioriser les coins disponibles
            for coin in coins:
                if tableau1[coin] == "  -  ":
                    tableau1[coin] = "  0  "
                    return
            
            # Jouer sur les bords disponibles si aucun coin libre
            for bord in bords:
                if tableau1[bord] == "  -  ":
                    tableau1[bord] = "  0  "
                    return
    elif diffbot == 3:  # Très Difficile : Stratégie plus complexe
        # 1. Vérifier si le bot peut gagner
        for ligne in lignes_gagnantes:
            cases = [tableau1[i] for i in ligne]
            if cases.count("  0  ") == 2 and cases.count("  -  ") == 1:
                tableau1[ligne[cases.index("  -  ")]] = "  0  "
                return

        # 2. Bloquer l'adversaire s'il peut gagner
        for ligne in lignes_gagnantes:
            cases = [tableau1[i] for i in ligne]
            if cases.count("  X  ") == 2 and cases.count("  -  ") == 1:
                tableau1[ligne[cases.index("  -  ")]] = "  0  "
                return

        # 3. Jouer au centre si disponible
        if tableau1[4] == "  -  ":
            tableau1[4] = "  0  "
            return

        # 4. Jouer sur un coin disponible
        coins = [0, 2, 6, 8]
        for coin in coins:
            if tableau1[coin] == "  -  ":
                tableau1[coin] = "  0  "
                return

        # 5. Jouer sur un bord disponible
        bords = [1, 3, 5, 7]
        for bord in bords:
            if tableau1[bord] == "  -  ":
                tableau1[bord] = "  0  "
                return
def choixbot2():
    global tableau1
    affichagemorpion()
    print("\n")
    
    if diffbot == 1:  # Facile : Choisir une case aléatoire
        choix_valide = False  # Indicateur pour vérifier si le choix est valide
        while choix_valide == False:
            choix = random.randint(1, 9)
            if 1 <= choix <= 9 and tableau1[choix - 1] == "  -  ":
                tableau1[choix - 1] = "  X  "  # Marquer la case avec un "X" pour Bot 2
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
    
    elif diffbot == 2:  # Moyen : Prioriser le centre, coins et bords
        # Jouer au centre si possible
        if tableau1[4] == "  -  ":
            tableau1[4] = "  X  "
        else:
            # Liste des coins et des bords
            coins = [0, 2, 6, 8]
            bords = [1, 3, 5, 7]
            
            # Prioriser les coins disponibles
            for coin in coins:
                if tableau1[coin] == "  -  ":
                    tableau1[coin] = "  X  "
                    return
            
            # Jouer sur les bords disponibles si aucun coin libre
            for bord in bords:
                if tableau1[bord] == "  -  ":
                    tableau1[bord] = "  X  "
                    return
    
    elif diffbot == 3:  # Difficile : Stratégie avancée pour bloquer et gagner
        # 1. Vérifier si le bot peut gagner
        for ligne in lignes_gagnantes:
            cases = [tableau1[i] for i in ligne]
            if cases.count("  X  ") == 2 and cases.count("  -  ") == 1:
                tableau1[ligne[cases.index("  -  ")]] = "  X  "
                return

        # 2. Bloquer l'adversaire s'il peut gagner
        for ligne in lignes_gagnantes:
            cases = [tableau1[i] for i in ligne]
            if cases.count("  O  ") == 2 and cases.count("  -  ") == 1:
                tableau1[ligne[cases.index("  -  ")]] = "  X  "
                return

        # 3. Jouer au centre si disponible
        if tableau1[4] == "  -  ":
            tableau1[4] = "  X  "
            return

        # 4. Jouer sur un coin disponible
        coins = [0, 2, 6, 8]
        for coin in coins:
            if tableau1[coin] == "  -  ":
                tableau1[coin] = "  X  "
                return

        # 5. Jouer sur un bord disponible
        bords = [1, 3, 5, 7]
        for bord in bords:
            if tableau1[bord] == "  -  ":
                tableau1[bord] = "  X  "
                return       
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
        ajoutscore[4] = 15-tour# le score est de 15 a la base et diminue d'un point par tour
        ajout_val_score()
        print("gain de", ajoutscore[4],"points au score") #affichage du score
        affichagemorpion()
    elif victoirej2 == True:
        print("Victoire du joueur 2")
        ajoutscore[5] = 15-tour
        print("gain de", ajoutscore[5],"points au score") #affichage du score
        ajout_val_score()
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
def morpionbotj1():# Fonction principale pour gérer le jeu
    global tour
    # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixdujoueur1()  # Tour du joueur 1
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant      
        ajout_val_score()                # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixbot1()  # Tour du joueur 2
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
def morpionbotj2():  # Fonction principale pour gérer le jeu
    global tour # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixbot2()  # Tour du joueur 2
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant  
        # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixdujoueur2()  # Tour du joueur 1 
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant   # Vérification des résultats du jeu
    if victoirej1 == True:
        print("Victoire du joueur 1")
        ajoutscore[4] = 15-tour# le score est de 15 a la base et diminue d'un point par tour
        ajout_val_score()
        print("gain de", ajoutscore[4],"points au score") #affichage du score
        affichagemorpion()
    elif victoirej2 == True:
        print("Victoire du joueur 2")
        ajoutscore[5] = 15-tour
        print("gain de", ajoutscore[5],"points au score") #affichage du score
        ajout_val_score()
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
def menumorpion():
    initialisationtableau()
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            print("choix du mode de jeu ")
            print("1) joueur contre joueur")
            print("2) joueur contre bot")
            print("3) bot contre bot")
            choixmode = int(input("votre choix : "))
            if choixmode in [1, 2, 3]:
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
                if choixmode == 1:
                    morpion()
                elif choixmode == 2:
                    morpionbot()
                else:
                    morpionbotbot()
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier (1 2 ou 3).")
def morpionbotbot():# Fonction principale pour gérer le jeu
    global tour
    # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixbot1()  # Tour du joueur 1
        affichagemorpion()
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant      
        ajout_val_score() 
        # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixbot2()  # Tour du joueur 2
            affichagemorpion()
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant
    if victoirej1 == True:
        
        affichagemorpion()
        ajoutscore[4] = 15-tour
        ajout_val_score()
        print("gain de", ajoutscore[4],"points au score")
    elif victoirej2 == True:
        
        affichagemorpion()
        ajoutscore[5] = 15-tour
        ajout_val_score()
        print("gain de", ajoutscore[5],"points au score")
    else:
        print("égalité")
        affichagemorpion()    
def morpion():                
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
def morpionbot():
    global diffbot                
    print("Choisisez quand commencer ")
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            print(" 1) premier ")
            print(" 2) deuxieme ")
            choixtour = int(input("Votre choix : "))
            if choixtour in [1, 2]:
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier (1 ou 2).")
    print("1) facile")
    print("2) moyen")
    print("3) difficile")
    choix_valide = False  # Indicateur pour vérifier si le choix est valide
    while not choix_valide:
        try:
            diffbot = int(input("Choix (1, 2 ou 3) : "))
            if diffbot in [1, 2, 3]:
                choix_valide = True  # Marquer que le choix est valide pour sortir de la boucle
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier (1, 2 ou 3).")
    if choixtour == 1:
        morpionbotj1()
    else :
        morpionbotj2()
