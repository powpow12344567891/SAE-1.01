# Déclaration des variables
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

val = 0  # Variable inutilisée
retourligne = 1  # Variable inutilisée

# Fonction pour afficher le plateau de jeu
def affichagemorpion():
    print("\n")
    print(tableau1[6],tableau1[7],tableau1[8],)
    print("\n")     
    print(tableau1[3],tableau1[4],tableau1[5],)
    print("\n")
    print(tableau1[0],tableau1[1],tableau1[2],)
# Fonction pour gérer le choix du joueur 1
def choixdujoueur1():
    affichagemorpion()
    print("\n")
    choix = int(input("choix de la case joueur 1 "))  # Demander une case au joueur 1
    print("\n")
    # Vérifier si le choix est valide
    while (choix > 9) or (tableau1[choix - 1] != "  -  "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 1 "))
    print("\n")
    tableau1[choix - 1] = str("  X  ")  # Marquer la case avec un "X"

# Fonction pour gérer le choix du joueur 2
def choixdujoueur2():
    affichagemorpion()
    print("\n")
    choix = int(input("choix de la case joueur 2 "))  # Demander une case au joueur 2
    print("\n")
    # Vérifier si le choix est valide
    while (choix > 9) or (tableau1[choix - 1] != "  -  "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 2 "))
    print("\n")
    tableau1[choix - 1] = str("  0  ")  # Marquer la case avec un "0"

# Fonction pour vérifier si un joueur a gagné
def victoire():
    global victoirej1, victoirej2  # Utilisation des variables globales
    # Vérification de toutes les combinaisons gagnantes
    for ligne in lignes_gagnantes: 
        if tableau1[ligne[0]] == tableau1[ligne[1]] == tableau1[ligne[2]] and tableau1[ligne[0]] != "  -  ":
            if tableau1[ligne[0]] == "  X  ":
                victoirej1 = True  # Joueur 1 gagne
            elif tableau1[ligne[0]] == "  0  ":
                victoirej2 = True  # Joueur 2 gagne

# Fonction principale pour gérer le jeu
def morpionj1():
    global tour
    # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixdujoueur1()  # Tour du joueur 1
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant

        # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixdujoueur2()  # Tour du joueur 2
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant
def morpionj2():
    global tour
    # Boucle principale du jeu
    while ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
        choixdujoueur2()  # Tour du joueur 2
        victoire()  # Vérifier la victoire
        tour += 1  # Passer au tour suivant

        # Si personne n'a gagné et qu'il reste des tours, c'est au joueur 2
        if ((victoirej1 == False) and (victoirej2 == False) and (tour <= 9)):
            choixdujoueur1()  # Tour du joueur 1 
            victoire()  # Vérifier la victoire
            tour += 1  # Passer au tour suivant
    # Vérification des résultats du jeu
    if victoirej1 == True:
        print("Victoire du joueur 1")
        affichagemorpion()
    elif victoirej2 == True:
        print("Victoire du joueur 2")
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()

def morpion():
    print("choix du joueur qui commence")
    print("j1 : 1")
    print("j2 : 2")
    choixtour = int(input("choix :"))
    while ((choixtour != 1) and (choixtour != 2)):
            choixtour = int(input("choix incorrecte :"))
    if(choixtour == 1):
        morpionj1()
    else :
        morpionj2()