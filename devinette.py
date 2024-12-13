# Fonction qui gère le jeu de devinettes pour une manche
from Score import ajoutscore, ajout_val_score
def devinnettes(choix: int, manche: int):
    """
    Fonction permettant de choisir et vérifier si le numéro choisi correspond ou non.
    """
    essai: int  # Valeur tentée par le joueur
    nombretours: int = 1  # Nombre de tentatives dans une manche
    # Détermine quel joueur doit entrer une valeur en fonction du numéro de la manche
    if manche % 2 == 1:
        essai = demande_valeur("J2 choisis une valeur: ")
    else:
        essai = demande_valeur("J1 choisis une valeur: ")
    
    # Boucle pour continuer tant que le joueur n'a pas trouvé la valeur choisie
    while essai != choix:
        print("Tour", nombretours)  # Affiche le numéro du tour
        nombretours += 1  # Incrémente le compteur de tours # Indique si la valeur entrée est plus petite ou plus grande que la valeur à trouver
        if essai < choix:
            print("La valeur", essai, "est plus petite que la valeur choisie.")
        elif essai > choix:
            print("La valeur", essai, "est plus grande que la valeur choisie.")
        
        # Demande au même joueur d'entrer une nouvelle valeur
        if manche % 2 == 1:
            essai = demande_valeur("J2 choisis une valeur: ")
        else:
            essai = demande_valeur("J1 choisis une valeur: ")
    
    # Une fois la bonne valeur trouvée, affiche le nombre de tours pris
    print("La valeur est correcte, trouvée en", nombretours, "tours.")
    return nombretours  # Retourne le nombre de tours pris par le joueur
# Fonction pour demander une valeur numérique et gérer les erreurs
def demande_valeur(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
def lancement():
    """
    Fonction de lancement et de gestion des manches et des scores.
    """
    manche_tt: int  # Nombre total de manches
    manche: int = 0  # Compteur de manches
    choix: int  # Valeur à deviner pour la manche
    nombretoursj1: int = 0  # Nombre total de tours pris par le joueur 1
    nombretoursj2: int = 0  # Nombre total de tours pris par le joueur 2
    # Demande à l'utilisateur de saisir le nombre total de manches
    manche_tt = demande_valeur("Entrez le nombre de manches que vous souhaitez réaliser minimum 2 et paire : ")
    while (manche_tt < 2) or (manche_tt % 2 == 1):
        manche_tt = demande_valeur("Erreur : La valeur doit être supérieure ou égale à 2 ou impaire. Entrez un nouveau nombre de manches : ")
    
    # Boucle pour jouer toutes les manches
    for i in range(manche_tt):
        if i % 2 == 0: 
            manche += 1  # Incrémente le numéro de la manche
        print("Round", i + 1)  # Affiche le numéro du round
        print("Manche", manche)
        # Indique quel joueur choisit la valeur à deviner
        if manche % 2 == 1:
            print("Tour du joueur 1")
        else:
            print("Tour du joueur 2")     
        # Demande au joueur actif d'entrer la valeur à deviner
        choix = demande_valeur("Entrez la valeur à trouver (max 1000): ")
        while choix > 1000:
           choix = demande_valeur("Erreur : La valeur doit être maximum 1000. Entrez un nouveau nombre : ")
        # Joue la manche et récupère le nombre de tours pris
        nombretours = devinnettes(choix, manche)
        # Met à jour les scores totaux en fonction du joueur actif
        if manche % 2 == 1:
            nombretoursj2 += nombretours
        else:
            nombretoursj1 += nombretours
        print("-----------------------------------------------------------------")
    # Affiche les résultats finaux des deux joueurs
   
    if (nombretoursj1 > 14): 
        print("joueur 1 a mis au moins 15 tour il ne gagne donc aucun points")
    else:
        ajoutscore[0] = 15 - nombretoursj1
    if (nombretoursj2 > 14): 
        print("joueur 2 a mis au moins 15 tour il ne gagne donc aucun points")
    else:
        ajoutscore[1] = 15 - nombretoursj1
    ajout_val_score()
    print("Le joueur 1 a pris un total de", nombretoursj1, "tours, tandis que le joueur 2 a pris un total de", nombretoursj2, "tours.")
