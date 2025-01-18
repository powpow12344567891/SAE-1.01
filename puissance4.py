def creer_grille():
    return [[' ' for _ in range(7)] for _ in range(6)]

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
    print("-" * 29)

def est_vide(grille, col):
    return grille[0][col] == ' '

def jouer(grille, col, joueur):
    for i in range(5, -1, -1):
        if grille[i][col] == ' ':
            grille[i][col] = joueur
            return
def bot()
    
def verifier_victoire(grille, joueur):
    for i in range(6):
        for j in range(7):
            if grille[i][j] == joueur:
                # Horizontal
                if j + 3 < 7 and all(grille[i][j + k] == joueur for k in range(4)):
                    return True
                # Vertical
                if i + 3 < 6 and all(grille[i + k][j] == joueur for k in range(4)):
                    return True
                # Diagonale /
                if i + 3 < 6 and j - 3 >= 0 and all(grille[i + k][j - k] == joueur for k in range(4)):
                    return True
                # Diagonale \
                if i + 3 < 6 and j + 3 < 7 and all(grille[i + k][j + k] == joueur for k in range(4)):
                    return True
    return False

def jeuhumain():
    grille = creer_grille()
    joueurs = ['X', 'O']
    tour = 0

    while True:
        afficher_grille(grille)
        joueur_courant = joueurs[tour % 2]
        print(f"Tour du joueur {joueur_courant}")
        
        try:
            col = int(input("Choisissez une colonne (0-6): "))
            if col < 0 or col > 6:
                raise ValueError
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre entre 0 et 6.")
            continue

        if est_vide(grille, col):
            jouer(grille, col, joueur_courant)
            
            if verifier_victoire(grille, joueur_courant):
                afficher_grille(grille)
                print(f"Le joueur {joueur_courant} a gagné!")
                break
            
            tour += 1
        else:
            print("Colonne pleine, essayez une autre colonne.")

jeuhumain()
