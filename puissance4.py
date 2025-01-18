import random

class Puissance4:
    def __init__(self):
        # Créer une grille de 6 lignes et 7 colonnes
        self.grille = [[' ' for _ in range(7)] for _ in range(6)]

    def afficher_grille(self):
        for ligne in self.grille:
            print(" | ".join(ligne))

    def est_vide(self, col):
        # Vérifier si la colonne est vide (est-ce qu'il y a de l'espace dans la colonne)
        return self.grille[0][col] == ' '

    def jouer(self, col, joueur):
        # Placer le jeton dans la colonne
        for i in range(5, -1, -1):
            if self.grille[i][col] == ' ':
                self.grille[i][col] = joueur
                break

    def verifier_victoire(self, joueur):
        # Vérification horizontale, verticale et diagonale
        for i in range(6):
            for j in range(7):
                if self.grille[i][j] == joueur:
                    # Horizontal
                    if j + 3 < 7 and all(self.grille[i][j+k] == joueur for k in range(4)):
                        return True
                    # Vertical
                    if i + 3 < 6 and all(self.grille[i+k][j] == joueur for k in range(4)):
                        return True
                    # Diagonale /
                    if i + 3 < 6 and j - 3 >= 0 and all(self.grille[i+k][j-k] == joueur for k in range(4)):
                        return True
                    # Diagonale \
                    if i + 3 < 6 and j + 3 < 7 and all(self.grille[i+k][j+k] == joueur for k in range(4)):
                        return True
        return False

    def obtenir_colonne_bot(self):
        # Choisir une colonne au hasard parmi celles qui sont encore disponibles
        col = random.choice([c for c in range(7) if self.est_vide(c)])
        return col

def jeu():
    jeu = Puissance4()
    joueurs = ['X', 'O']
    tour = 0

    while True:
        jeu.afficher_grille()
        joueur_courant = joueurs[tour % 2]
        print(f"Tour du joueur {joueur_courant}")
        
        if joueur_courant == 'O':
            col = jeu.obtenir_colonne_bot()  # Le bot joue ici
        else:
            col = int(input("Choisissez une colonne (0-6): "))
        
        if jeu.est_vide(col):
            jeu.jouer(col, joueur_courant)
            
            if jeu.verifier_victoire(joueur_courant):
                jeu.afficher_grille()
                print(f"Le joueur {joueur_courant} a gagné!")
                break
            
            tour += 1
        else:
            print("Colonne pleine, essayez une autre colonne.")

jeu()
