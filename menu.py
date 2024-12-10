import os  # Pour interagir avec le système d'exploitation
from Score import affichescore  # Importer uniquement la fonction `affichescore` du module `Score`
from morpion import morpion  # Importer uniquement la fonction `morpion` du module `morpion`
from devinette import lancement  # Importer uniquement la fonction `lancement` du module `devinette`
from allumette import allumette  # Importer uniquement la fonction `allumette` du module `allumette`

# Fonction pour effacer l'écran de la console
def clear():
    os.system('cls')  # Commande spécifique à Windows pour nettoyer la console

# Fonction principale du menu
def menu():
    clear()  # Efface l'écran au début de l'exécution du menu
    while True:  # Boucle infinie pour afficher le menu jusqu'à ce que l'utilisateur quitte
        # Affichage du menu principal
        print("***********************************************************************************************")
        print("*                                         MENU                                                *")
        print("*                                    1) DEVINETTE                                             *")
        print("*                                    2) ALLUMETTE                                             *")
        print("*                                    3) MORPION                                               *")
        print("*                                    4) SCORE                                                 *")
        print("*                                    5) QUITTER                                               *")
        print("***********************************************************************************************")
        
        try:
            choix = int(input("Choisir une option : "))  # Lecture de l'option choisie par l'utilisateur
            # Vérifie si l'option choisie est valide
            if choix not in [1, 2, 3, 4, 5]:
                print("Erreur, veuillez choisir une option valide (1, 2, 3, 4 ou 5).")
                continue  # Recommence la boucle en cas de choix invalide
        except ValueError:
            # Gestion de l'erreur si l'entrée n'est pas un entier
            print("Erreur, veuillez entrer un nombre entier correspondant à une option.")
            continue  # Recommence la boucle en cas d'erreur

        # Exécute une action en fonction du choix de l'utilisateur
        if choix == 1:
            clear()  # Efface l'écran
            lancement()  # Appelle la fonction `lancement` (probablement liée au jeu DEVINETTE)
        elif choix == 2:
            clear()  # Efface l'écran
            # Demande les noms des deux joueurs pour le jeu ALLUMETTE
            joueur1 = input("Entrez le nom du joueur 1: ")
            joueur2 = input("Entrez le nom du joueur 2: ")
            allumette(joueur1, joueur2)  # Lance le jeu ALLUMETTE avec les noms des joueurs
        elif choix == 3:
            clear()  # Efface l'écran
            morpion()  # Lance le jeu MORPION
        elif choix == 4:
            clear()  # Efface l'écran
            affichescore()  # Appelle la fonction pour afficher le score

        # Option pour quitter le programme
        elif choix == 5:
            clear()  # Efface l'écran
            print("Merci d'avoir joué ! À bientôt.")  # Message de fin
            break  # Sort de la boucle, terminant ainsi le programme

# Point d'entrée du programme
if __name__ == "__main__":
    menu()  # Appelle la fonction `menu` pour démarrer l'application
