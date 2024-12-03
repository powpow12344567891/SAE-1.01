# Importation du module Score (si utilisé pour la gestion des scores)
from Score import *

# Déclaration des variables globales
joueur1: int  # Score ou identification du joueur 1
joueur2: int  # Score ou identification du joueur 2
choix: int  # Choix de case pour le jeu
tour: int  # Compteur des tours
victoirej1: bool  # Indique si le joueur 1 a gagné
victoirej2: bool  # Indique si le joueur 2 a gagné
retourligne: int  # Variable pour formatage d'affichage
val: int  # Valeur temporaire pour manipulation
tableau1: list[str]  # Tableau du jeu morpion
ordre: int  # Ordre ou choix d'un joueur
choixtour: int  # Indique quel joueur commence la partie

# Initialisation des variables de jeu
victoirej1 = False  # Aucune victoire initialement
victoirej2 = False  # Aucune victoire initialement
tour = 1  # Premier tour
# Grille initiale du morpion
tableau1 = ["  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  "]
# Combinaisons gagnantes pour le jeu du morpion
lignes_gagnantes = [
    [0, 1, 2],  # Ligne 1
    [3, 4, 5],  # Ligne 2
    [6, 7, 8],  # Ligne 3
    [0, 3, 6],  # Colonne 1
    [1, 4, 7],  # Colonne 2
    [2, 5, 8],  # Colonne 3
    [0, 4, 8],  # Diagonale principale
    [2, 4, 6]   # Diagonale secondaire
]
# Fonction pour réinitialiser le plateau de jeu
def initialisationtableau():
    global tableau1, tour, victoirej1, victoirej2, ajoutscore
    # Réinitialisation des variables pour une nouvelle partie
    victoirej1 = False
    victoirej2 = False
    tour = 1
    tableau1 = ["  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  ", "  -  "]
    ajoutscore[4] = 0  # Réinitialisation des scores
    ajoutscore[5] = 0
# Fonction pour afficher le plateau de jeu
def affichagemorpion():
    print("tour", tour)  # Affiche le tour actuel
    print("\n")
    print(tableau1[6], tableau1[7], tableau1[8])  # Ligne supérieure
    print("\n")
    print(tableau1[3], tableau1[4], tableau1[5])  # Ligne centrale
    print("\n")
    print(tableau1[0], tableau1[1], tableau1[2])  # Ligne inférieure
# Fonction pour gérer le choix du joueur 1
def choixdujoueur1():
    affichagemorpion()  # Affiche le plateau avant le choix
    print("\n")
    choix = int(input("choix de la case joueur 1 "))  # Demander au joueur 1 de choisir une case
    print("\n")
    # Vérification de la validité du choix
    while (choix > 9) or (tableau1[choix - 1] != "  -  "):
        print("\n", "choix non valide")  # Erreur si choix invalide
        choix = int(input("choix de la case joueur 1 "))
    print("\n")
    tableau1[choix - 1] = "  X  "  # Marquer la case choisie avec un "X"

# Fonction pour gérer le choix du joueur 2
def choixdujoueur2():
    affichagemorpion()  # Affiche le plateau avant le choix
    print("\n")
    choix = int(input("choix de la case joueur 2 "))  # Demander au joueur 2 de choisir une case
    print("\n")
    # Vérification de la validité du choix
    while (choix > 9) or (tableau1[choix - 1] != "  -  "):
        print("\n", "choix non valide")  # Erreur si choix invalide
        choix = int(input("choix de la case joueur 2 "))
    print("\n")
    tableau1[choix - 1] = "  0  "  # Marquer la case choisie avec un "0"

# Fonction pour vérifier les conditions de victoire
def victoire():
    global victoirej1, victoirej2
    # Vérifier toutes les combinaisons gagnantes
    for ligne in lignes_gagnantes:
        if tableau1[ligne[0]] == tableau1[ligne[1]] == tableau1[ligne[2]] and tableau1[ligne[0]] != "  -  ":
            if tableau1[ligne[0]] == "  X  ":
                victoirej1 = True  # Joueur 1 gagne
            elif tableau1[ligne[0]] == "  0  ":
                victoirej2 = True  # Joueur 2 gagne
# Fonction principale pour le jeu lorsque le joueur 1 commence
def morpionj1():
    global tour
    while not (victoirej1 or victoirej2) and tour <= 9:  # Tant qu'il n'y a pas de victoire et qu'il reste des tours
        choixdujoueur1()
        victoire()
        tour += 1
        # Tour du joueur 2 si personne n'a gagné
        if not (victoirej1 or victoirej2) and tour <= 9:
            choixdujoueur2()
            victoire()
            tour += 1
    # Résultat de la partie
    if victoirej1:
        print("Victoire du joueur 1")
        affichagemorpion()
    elif victoirej2:
        print("Victoire du joueur 2")
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
# Fonction principale pour le jeu lorsque le joueur 2 commence
def morpionj2():
    global tour
    while not (victoirej1 or victoirej2) and tour <= 9:  # Tant qu'il n'y a pas de victoire et qu'il reste des tours
        choixdujoueur2()
        victoire()
        tour += 1
        # Tour du joueur 1 si personne n'a gagné
        if not (victoirej1 or victoirej2) and tour <= 9:
            choixdujoueur1()
            victoire()
            tour += 1
    # Résultat de la partie
    if victoirej1:
        print("Victoire du joueur 1")
        affichagemorpion()
    elif victoirej2:
        print("Victoire du joueur 2")
        affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
# Fonction pour lancer une partie de morpion
def morpion():
    initialisationtableau()  # Réinitialise le plateau
    print("choix du joueur qui commence")
    print("j1 : 1")
    print("j2 : 2")
    choixtour = int(input("choix :"))  # Demande qui commence
    while choixtour not in [1, 2]:
        choixtour = int(input("choix incorrecte :"))  # Validation du choix
    if choixtour == 1:
        morpionj1()  # Partie commence par joueur 1
    else:
        morpionj2()  # Partie commence par joueur 2
