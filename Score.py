if __name__ == "__main__":
    # Initialisation des variables de score pour les deux joueurs
    scorej1: int
    scorej2: int
    ajoutscorej1: int 
    ajoutscorej2: int  
    lecteurscorej1: str
    lecteurscorej2: str
    
    # Fonction pour récupérer les scores actuels des joueurs depuis un fichier texte
def recup_val_score():
        # Ouverture du fichier en mode lecture avec encodage UTF-8
    file = open("score.txt", "r", encoding="utf8")
        # Lecture et conversion des scores pour chaque joueur
    scorej1 = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
    scorej2 = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        # Affichage des scores des joueurs
    print("Le score du joueur 1 est :", scorej1)
    print("Le score du joueur 2 est :", scorej2) 
        # Fermeture du fichier
    file.close()
        
    # Fonction pour ajouter une valeur aux scores des joueurs et sauvegarder les nouveaux scores
def ajout_de_val_score():
     # Ouverture du fichier en mode écriture pour remplacer les scores actuels
    file = open("score.txt", "w", encoding="utf8")
        # Écriture des nouveaux scores des joueurs dans le fichier
    file.write(str(scorej1 + ajoutscorej1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
    file.write("\n") 
    file.write(str(scorej2 + ajoutscorej2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
    file.close() # Fermeture du fichier
