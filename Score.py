    # Initialisation des variables de score pour les deux joueurs
  # Fonction pour récupérer les scores actuels des joueurs depuis un fichier texte
def recup_val_score():
        scorejeu :list[int]
        scorejeu=[0,1,2,3,4,5]
        # Ouverture du fichier en mode lecture avec encodage UTF-8
        file = open("score.txt", "r", encoding="utf8")
        # Lecture et conversion des scores pour chaque joueur
        scorejeu[0] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[1] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[2] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[3] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[4]= int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[5] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        # Affichage des scores des joueurs
        print("Le score du joueur 1 sur les devinettes est :", scorejeu[0])
        print("Le score du joueur 2 sur les devinettes est :", scorejeu[1]) 
        print("Le score du joueur 1 sur les allumettes est :", scorejeu[2])
        print("Le score du joueur 2 sur les allumettes est :", scorejeu[3]) 
        print("Le score du joueur 1 sur le morpion est :", scorejeu[4])
        print("Le score du joueur 2 sur le morpion est :", scorejeu[5]) 
        # Fermeture du fichier
        file.close()
    # Fonction pour ajouter une valeur aux scores des joueurs et sauvegarder les nouveaux scores
def ajout_de_val_score():
        scorejeu :list[int]
        scorejeu=[0,1,2,3,4,5]   
        ajoutscore1j1: int 
        ajoutscore1j2: int  
        ajoutscore2j1: int 
        ajoutscore2j2: int  
        ajoutscore3j1: int 
        ajoutscore3j2: int         
        file = open("score.txt", "r", encoding="utf8")
        # Lecture et conversion des scores pour chaque joueur
        scorejeu[0] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[1] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[2] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[3] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[4]= int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[5] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        # Affichage des scores des joueurs
        # Fermeture du fichier
        file.close()
        # Ouverture du fichier en mode écriture pour remplacer les scores actuels
        file = open("score.txt", "w", encoding="utf8")
        # Écriture des nouveaux scores des joueurs dans le fichier
        file.write(str(scorejeu[0] + ajoutscore1j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[1] + ajoutscore1j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[2] + ajoutscore2j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[3] + ajoutscore2j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[4] + ajoutscore3j1))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[5] + ajoutscore3j2))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.close() # Fermeture du fichier
