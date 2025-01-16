from Score import ajoutscore, ajout_val_score
import random

# Fonction pour demander une valeur numérique et gérer les erreurs
def demande_valeur(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

# Fonction qui gère le jeu de devinettes pour une manche
def devinnettesjoueur(choix: int, manche: int):
    """
    Fonction permettant de choisir et vérifier si le numéro choisi correspond ou non.
    """
    essai: int  # Valeur tentée par le joueur
    nombretours: int = 1  # Nombre de tentatives dans une manche

    # Détermine quel joueur doit entrer une valeur en fonction du numéro de la manche
    if manche % 2 == 1:
        essai = demande_valeur("J2, choisis une valeur : ")
    else:
        essai = demande_valeur("J1, choisis une valeur : ")

    # Boucle pour continuer tant que le joueur n'a pas trouvé la valeur choisie
    while essai != choix:
        print("Tour", nombretours)  # Affiche le numéro du tour
        nombretours += 1  # Incrémente le compteur de tours

        # Indique si la valeur entrée est plus petite ou plus grande que la valeur à trouver
        if essai < choix:
            print("La valeur", essai, "est plus petite que la valeur choisie.")
        elif essai > choix:
            print("La valeur", essai, "est plus grande que la valeur choisie.")

        essai = demande_valeur("Essayez encore : ")

    # Une fois la bonne valeur trouvée, affiche le nombre de tours pris
    print("La valeur est correcte, trouvée en", nombretours, "tours.")
    return nombretours  # Retourne le nombre de tours pris par le joueur

# Fonction qui gère le jeu de devinettes contre un bot
def devinettepve(choix: int, manche: int):
    """
    Fonction permettant de jouer contre un bot avec différents niveaux de difficulté.
    """
    nombretours: int = 1  # Nombre de tentatives dans une manche

    # Sélection de la difficulté du bot
    while True:
        try:
            diff = int(input("Choisissez la difficulté du bot (1: facile, 2: moyen, 3: difficile) : "))
            if diff not in [1, 2, 3]:
                print("Erreur : Veuillez choisir une difficulté valide (1, 2 ou 3).")
            else:
                break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier correspondant à une difficulté.")

    if manche % 2 == 1:  # Bot choisit et joueur humain devine
        essai = demande_valeur("J1, devinez la valeur choisie par le bot : ")
        choix_bot = random.randint(0, 1000)
        print("Le bot a choisi une valeur (cachée).")

        while essai != choix_bot:
            print("Tour", nombretours)  # Affiche le numéro du tour
            nombretours += 1

            if essai < choix_bot:
                print("La valeur", essai, "est plus petite que la valeur choisie.")
            elif essai > choix_bot:
                print("La valeur", essai, "est plus grande que la valeur choisie.")

            essai = demande_valeur("Essayez encore : ")

        print("La valeur est correcte, trouvée en", nombretours, "tours.")

    else:  # Joueur humain choisit et le bot devine
        print("Le bot essaie de deviner votre valeur.")

        if diff == 1:
            essai = random.randint(0, 1000)
        elif diff == 2:
            intervalle_min, intervalle_max = 0, 1000
            essai = (intervalle_min + intervalle_max) // 2
        else:
            intervalle_min, intervalle_max = 0, 1000
            essai = (intervalle_min + intervalle_max) // 2

        while essai != choix:
            print("Tour", nombretours)  # Affiche le numéro du tour
            nombretours += 1
            print(f"Le bot a proposé : {essai}")

            if essai < choix:
                print("La valeur", essai, "est plus petite que la valeur choisie.")
                intervalle_min = essai + 1
            elif essai > choix:
                print("La valeur", essai, "est plus grande que la valeur choisie.")
                intervalle_max = essai - 1

            if diff == 1:
                essai = random.randint(intervalle_min, intervalle_max)
            else:
                essai = (intervalle_min + intervalle_max) // 2

        print("La valeur est correcte, trouvée en", nombretours, "tours.")

    return nombretours  # Retourne le nombre de tours pris

# Fonction qui gère le jeu entre deux bots
def devinetteve():
    """
    Fonction permettant de jouer une manche entre deux bots.
    """
    choix = random.randint(0, 1000)
    print(f"Valeur à trouver (cachée) : {choix}")
    nombretours: int = 1

    while True:
        essai_bot1 = random.randint(0, 1000)
        print(f"Bot 1 a proposé : {essai_bot1}")

        if essai_bot1 == choix:
            print("Bot 1 a trouvé la valeur en", nombretours, "tours.")
            return nombretours

        if essai_bot1 < choix:
            print("La valeur", essai_bot1, "est plus petite que la valeur choisie.")
        elif essai_bot1 > choix:
            print("La valeur", essai_bot1, "est plus grande que la valeur choisie.")

        nombretours += 1

# Fonction de lancement et gestion des manches
def lancement():
    """
    Fonction de lancement et de gestion des manches et des scores.
    """
    manche: int = 0  # Compteur de manches
    nombretoursj1: int = 0  # Nombre total de tours pris par le joueur 1
    nombretoursj2: int = 0  # Nombre total de tours pris par le joueur 2

    # Demande à l'utilisateur de choisir un mode
    print("Choisir un mode :")
    print("1. 2 joueurs")
    print("2. 1 joueur 1 bot")
    print("3. 2 bots")

    while True:
        try:
            joueurbotbot = int(input("Choisir une option (1, 2 ou 3) : "))
            if joueurbotbot not in [1, 2, 3]:
                print("Erreur : Veuillez choisir une option valide (1, 2 ou 3).")
            else:
                break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier correspondant à une option.")

    # Demande le nombre total de manches
    manche_tt = demande_valeur("Entrez le nombre de manches que vous souhaitez réaliser (minimum 2 et paire) : ")
    while manche_tt < 2 or manche_tt % 2 == 1:
        manche_tt = demande_valeur("Erreur : La valeur doit être supérieure ou égale à 2 et paire. Entrez un nouveau nombre de manches : ")

    # Boucle pour jouer toutes les manches
    for i in range(manche_tt):
        manche += 1
        print("Manche", manche)
        choix = demande_valeur("Entrez la valeur à trouver (max 1000) : ")
        while choix > 1000:
            choix = demande_valeur("Erreur : La valeur doit être maximum 1000. Entrez un nouveau nombre : ")

        if joueurbotbot == 1:
            nombretours = devinnettesjoueur(choix, manche)
        elif joueurbotbot == 2:
            nombretours = devinettepve(choix, manche)
        else:
            nombretours = devinetteve()  # Fonction pour gérer les bots

        if manche % 2 == 1:
            nombretoursj1 += nombretours
        else:
            nombretoursj2 += nombretours

    # Affichage des scores finaux
    if nombretoursj1 > 14:
        print("Le joueur 1 a mis au moins 15 tours et ne gagne donc aucun point.")
    else:
        ajoutscore[0] = 15 - nombretoursj1
        print("Le joueur 1 a gagné", 15 - nombretoursj1, "points.")

    if nombretoursj2 > 14:
        print("Le joueur 2 a mis au moins 15 tours et ne gagne donc aucun point.")
    else:
        ajoutscore[1] = 15 - nombretoursj2
        print("Le joueur 2 a gagné", 15 - nombretoursj2, "points.")

    ajout_val_score()
    print("Fin du jeu !")

lancement()
