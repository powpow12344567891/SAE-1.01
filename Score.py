scorejeu :list[int]
ajoutscore: list[int]
scorejeu=[0,1,2,3,4,5, 6, 7]
ajoutscore=[0,0,0,0,0,0,0,0]    # Initialisation des variables de score pour les deux joueurs
# Fonction pour récupérer les scores actuels des joueurs depuis un fichier texte
def recup_val_score(): # Ouverture du fichier en mode lecture avec encodage UTF-8
        file = open("score.txt", "r", encoding="utf8")# Lecture et conversion des scores pour chaque joueur
        scorejeu[0] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[1] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[2] = int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[3] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[4]= int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[5] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        scorejeu[6]= int(file.readline())  # Lire la première ligne et convertir en entier pour scorej1
        scorejeu[7] = int(file.readline())  # Lire la seconde ligne et convertir en entier pour scorej2
        file.close()# Affichage des scores des joueurs
def affichescore():
        recup_val_score()
        file = open("score.txt", "r", encoding="utf8")
        print("Le score du joueur 1 sur les devinettes est :", scorejeu[0])
        print("Le score du joueur 2 sur les devinettes est :", scorejeu[1]) 
        print("Le score du joueur 1 sur les allumettes est :", scorejeu[2])
        print("Le score du joueur 2 sur les allumettes est :", scorejeu[3]) 
        print("Le score du joueur 1 sur le morpion est :", scorejeu[4])
        print("Le score du joueur 2 sur le morpion est :", scorejeu[5]) # Fermeture du fichier
        print("Le score du joueur 1 sur le puissance 4 est :", scorejeu[6])
        print("Le score du joueur 2 sur le puissance 4 est :", scorejeu[7])
        file.close() # Fonction pour ajouter une valeur aux scores des joueurs et sauvegarder les nouveaux scores
def ajout_val_score():    
        recup_val_score()
        file = open("score.txt", "w", encoding="utf8")# Écriture des nouveaux scores des joueurs dans le fichier
        file.write(str(scorejeu[0] + ajoutscore[0]))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[1] + ajoutscore[1]))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[2] + ajoutscore[2]))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[3] + ajoutscore[3]))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n") 
        file.write(str(scorejeu[4] + ajoutscore[4]))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n")
        file.write(str(scorejeu[5] + ajoutscore[5]))  # Ajoute ajoutscorej2 au score actuel de joueur 2 et l'écrit
        file.write("\n")  
        file.write(str(scorejeu[6] + ajoutscore[6]))  # Ajoute ajoutscorej1 au score actuel de joueur 1 et l'écrit
        file.write("\n")
        file.write(str(scorejeu[7] + ajoutscore[7])) 
        file.close() # Fermeture du fichier
