from Score import ajoutscore, ajout_val_score
import random

# Types des variables
grille : list[list[str]]
ligne : list[str] 
col : int
symbole : str 
colonnes_valides : list[int] 
choix : int 
symbole_j1 : str
symbole_j2 : str 
premier : int
joueurs : list[tuple[str, str]] 
joueur_courant : str 
symbole_courant : str 
tour : int 
def creer_grille():
    return [[' ' for _ in range(7)] for _ in range(6)]

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
    print("-" * 29)

def est_vide(grille, col):
    return grille[0][col] == ' '

def jouer(grille, col, symbole):
    for i in range(5, -1, -1):
        if grille[i][col] == ' ':
            grille[i][col] = symbole
            return
def choix_bot(grille):
    colonnes_valides = [col for col in range(7) if est_vide(grille, col)]
    return random.choice(colonnes_valides)
def verifier_victoire(grille, symbole):
    for i in range(6):
        for j in range(7):
            if grille[i][j] == symbole:
                # Horizontal
                if j + 3 < 7 and all(grille[i][j + k] == symbole for k in range(4)):
                    return True
                # Vertical
                if i + 3 < 6 and all(grille[i + k][j] == symbole for k in range(4)):
                    return True
                # Diagonale /
                if i + 3 < 6 and j - 3 >= 0 and all(grille[i + k][j - k] == symbole for k in range(4)):
                    return True
                # Diagonale \
                if i + 3 < 6 and j + 3 < 7 and all(grille[i + k][j + k] == symbole for k in range(4)):
                    return True
    return False

def choisir_mode():
    print("Choisissez le mode de jeu :")
    print("1. Jouer contre un autre humain")
    print("2. Jouer contre un bot ")
    choix = int(input("votre choix :"))
    try:
        if choix  not in [1, 2]:
            print("Erreur, veuillez choisir une option valide (1 ou 2).")
        else:
            return choix   # Retourne le choix valide
    except ValueError:
        print("Erreur, veuillez entrer un nombre entier correspondant à une option.")

def choisir_symboles():
    print("Joueur 1, voulez-vous jouer avec X ou O ?")
    symbole_j1 = str(input("votre choix :"))
    while symbole_j1 not in ['X', 'O']:
        print("Entrée invalide. Veuillez choisir entre X et O :")
        symbole_j1 = str(input("votre choix :"))
    if symbole_j1 == 'X':
        symbole_j2 = 'O' 
    else :
        symbole_j2 = 'X'
    print(f"Joueur 1 jouera avec {symbole_j1}, et Joueur 2 (ou le Bot) jouera avec {symbole_j2}.")
    return symbole_j1, symbole_j2

def choisir_premier_joueur():
    while True:  # Boucle pour demander à l'utilisateur jusqu'à ce qu'il fournisse une réponse valide
        try:
            premier = int(input("Qui commence ? (1 pour Joueur 1, 2 pour Joueur 2/Bot) : "))
            if premier not in [1, 2]:
                print("Erreur, veuillez choisir une option valide (1 ou 2).")
                premier = int(input("Qui commence ? (1 pour Joueur 1, 2 pour Joueur 2/Bot) : "))
            else:
                return premier  # Retourne le choix valide
        except ValueError:
            print("Erreur, veuillez entrer un nombre entier correspondant à une option.")




def jeuhumain_ou_bot():
    grille = creer_grille()
    mode = choisir_mode()
    symbole_j1, symbole_j2 = choisir_symboles()
    premier_joueur = choisir_premier_joueur()

    if mode == 2:
        joueurs = [('Joueur 1', symbole_j1), ('Bot', symbole_j2)]
    else:
        joueurs = [('Joueur 1', symbole_j1), ('Joueur 2', symbole_j2)]

    # Déterminer l'ordre des joueurs
    if premier_joueur == 2:
        joueurs.reverse()

    tour = 0

    while True:
        afficher_grille(grille)
        joueur_courant, symbole_courant = joueurs[tour % 2]

        if joueur_courant == 'Bot':
            print("Tour du Bot...")
            col = choix_bot(grille)
        else:
            print("Tour de {joueur_courant} ({symbole_courant})")
            try:
                col = int(input("Choisissez une colonne (0-6): "))
                if col < 0 or col > 6:
                    raise ValueError
            except ValueError:
                print("Entrée invalide, veuillez entrer un nombre entre 0 et 6.")
                continue

        if est_vide(grille, col):
            jouer(grille, col, symbole_courant)
            
            if verifier_victoire(grille, symbole_courant):
                afficher_grille(grille)
                print(joueur_courant, " a gagné !")
                 
                # Mise à jour du score
                if joueur_courant == 'Joueur 1':
                    ajoutscore[6] = 25 - tour  # J1 gagne
                    ajout_val_score()  # Appel de la fonction pour mettre à jour le score
                    print("il a donc gagné" ,ajoutscore[6]," points")    
                
                elif joueur_courant == 'Joueur 2':
                    ajoutscore[7] = 25 - tour  # J2 gagne
                    ajout_val_score()  # Appel de la fonction pour mettre à jour le score
                    print("il a donc gagné" ,ajoutscore[7]," points")   
                
                break

                break
            
            tour += 1
        else:
            print("Colonne pleine, essayez une autre colonne.")
