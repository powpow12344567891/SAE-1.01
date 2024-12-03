# Fonction qui gère le jeu de devinettes pour une manche
from Score import *
def devinnettes(choix: int, manche: int):
    """
    Fonction permettant de choisir et verifier si le numéro choisie correspond ou non.
    """
    essai: int  # Valeur tentée par le joueur
    nombretours: int = 1  # Nombre de tentatives dans une manche
    
    # Détermine quel joueur doit entrer une valeur en fonction du numéro de la manche
    if manche % 2 == 1:
        essai = int(input("J2 choisis une valeur: "))
    else:
        essai = int(input("J1 choisis une valeur: "))
    
    # Boucle pour continuer tant que le joueur n'a pas trouvé la valeur choisie
    while essai != choix:
        print("Tour", nombretours)  # Affiche le numéro du tour
        nombretours += 1  # Incrémente le compteur de tours
        
        # Indique si la valeur entrée est plus petite ou plus grande que la valeur à trouver
        if essai < choix:
            print("La valeur", essai, "est plus petite que la valeur choisie.")
        elif essai > choix:
            print("La valeur", essai, "est plus grande que la valeur choisie.")
        
        # Demande au même joueur d'entrer une nouvelle valeur
        if manche % 2 == 1:
            essai = int(input("J2 choisis une valeur: "))
        else:
            essai = int(input("J1 choisis une valeur: "))
    
    # Une fois la bonne valeur trouvée, affiche le nombre de tours pris
    print("La valeur est correcte, trouvée en", nombretours, "tours.")
    return nombretours  # Retourne le nombre de tours pris par le joueur

# Fonction principale qui gère l'ensemble des manches
def lancement():
    """
    Fonction de lancement et de gestion des manches et du scores (principalement du visuel).
    """
    manche_tt: int  # Nombre total de manches
    manche: int = 0  # Compteur de manches
    choix: int  # Valeur à deviner pour la manche
    nombretoursj1: int = 0  # Nombre total de tours pris par le joueur 1
    nombretoursj2: int = 0  # Nombre total de tours pris par le joueur 2

    # Demande à l'utilisateur de saisir le nombre total de manches
    manche_tt = int(input("Entrez le nombre de manches que vous souhaitez réaliser: "))
    while(manche_tt < 2):
        manche_tt = int(input(" erreur valeur inferieur a 2 Entrez le nombre de manches que vous souhaitez réaliser: "))

    # Boucle pour jouer toutes les manches
    for i in range(manche_tt):
        manche += 1  # Incrémente le numéro de la manche
        print("Round", i + 1)  # Affiche le numéro du round
        print("manche", manche)

        # Indique quel joueur choisit la valeur à deviner
        if manche % 2 == 1:
            print("Tour du joueur 1")
        else:
            print("Tour du joueur 2")
        
        # Demande au joueur actif d'entrer la valeur à deviner
        choix = int(input("Entrez la valeur à trouver: "))
        
        # Joue la manche et récupère le nombre de tours pris
        nombretours = devinnettes(choix, manche)
        
        # Met à jour les scores totaux en fonction du joueur actif
        if manche % 2 == 1:
            nombretoursj2 += nombretours
        else:
            nombretoursj1 += nombretours
        
        print("-----------------------------------------------------------------")

    # Affiche les résultats finaux des deux joueurs
    ajoutscore[0] = 15 - nombretoursj1
    ajoutscore[1] = 15 - nombretoursj2
    ajout_val_score()
    print("Le joueur 1 a pris un total de", nombretoursj1, "tours, tandis que le joueur 2 a pris un total de", nombretoursj2, "tours.")
