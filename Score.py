if __name__ == "__main__":
    # Initialisation des variables de score pour les deux joueurs
    scorejeu1j1: int
    scorejeu1j2: int
    scorejeu2j1: int
    scorejeu2j2: int
    scorejeu3j1: int
    scorejeu3j2: int
    ajoutscore1j1: int 
    ajoutscore1j2: int  
    ajoutscore2j1: int 
    ajoutscore2j2: int  
    ajoutscore3j1: int 
    ajoutscore3j2: int  
    lecteurscorej1: str
    lecteurscorej2: str
    
    # Fonction pour récupérer les scores actuels des joueurs depuis un fichier texte
def recup_val_score():
        # Ouverture du fichier en mode lecture avec encodage UTF-8
        file = open("score.txt", "r", encoding="utf8")
        # Lecture et conversion des scores pour chaque joueur
        scorejeu1j1 = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu1j2 = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu2j1 = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu2j2 = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu3j1 = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu3j2 = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        # Affichage des scores des joueurs
        print("Le score du joueur 1 sur les devinettes est :", scorejeu1j1)
        print("Le score du joueur 2 sur les devinettes est :", scorejeu1j2) 
        print("Le score du joueur 1 sur les allumettes est :", scorejeu2j1)
        print("Le score du joueur 2 sur les allumettes est :", scorejeu2j2) 
        print("Le score du joueur 1 sur le morpion est :", scorejeu3j1)
        print("Le score du joueur 2 sur le morpion est :", scorejeu3j2) 
        # Fermeture du fichier
        file.close()
        
    # Fonction pour ajouter une valeur aux scores des joueurs et sauvegarder les nouveaux scores
def ajout_de_val_score():
        # Ouverture du fichier en mode écriture pour remplacer les scores actuels
        file = open("score.txt", "w", encoding="utf8")
        # Écriture des nouveaux scores des joueurs dans le fichier
        file.write(str(scorejeu1j1 + ajoutscore1j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu1j2 + ajoutscore1j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu2j1 + ajoutscore2j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu2j2 + ajoutscore2j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu3j1 + ajoutscore3j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu3j2 + ajoutscore3j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.close() # Fermeture du fichier
