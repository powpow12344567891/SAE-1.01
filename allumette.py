from Score import ajoutscore, ajout_val_score
def allumette(joueur1: str, joueur2: str):
    choixj1: int
    choixj2: int
    allumette: int = 20
    perdant: int = 0  # Affiche le nombre initial d'allumettes
    print("Il y a un total de", allumette, "allumettes.")
    print("|" * allumette)
    while allumette > 0:  
        # Tour du joueur 1
        print(f"{joueur1}, c'est votre tour.")
        choixj1 = demande_allumettes(f"{joueur1}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        
        while choixj1 > allumette:
            print("Erreur, il n'y a pas la quantité d'allumette que vous soouhaité retirer.")
            choixj1 = demande_allumettes(f"{joueur1}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        allumette -= choixj1

        if allumette <= 0:
            print("Vous avez retiré la dernière allumette.")
            perdant = 1
            cond_vic(perdant, joueur1, joueur2)
            break

        print(f"{joueur1} a pris {choixj1} allumettes.")
        if allumette > 1:
            print("Il reste", allumette, "allumettes.")
        else:
            print("Il reste", allumette, "allumette.")
        print("|" * allumette)

        # Tour du joueur 2
        print(f"{joueur2}, c'est votre tour.")
        choixj2 = demande_allumettes(f"{joueur2}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        
        while choixj2 > allumette:
            print("Erreur, il n'y a pas la quantité d'allumette que vous soouhaité retirer.")
            choixj2 = demande_allumettes(f"{joueur2}, choisissez combien d'allumettes vous voulez prendre (entre 1 et 3) : ")
        allumette -= choixj2

        if allumette <= 0:
            print("Vous avez retiré la dernière allumette.")
            perdant = 2
            cond_vic(perdant, joueur1, joueur2)
            break

        print(f"{joueur2} a pris {choixj2} allumettes.")
        if allumette > 1:
            print("Il reste", allumette, "allumettes.")
        else:
            print("Il reste", allumette, "allumette.")
        print("|" * allumette)


# Affichage des résultats
def cond_vic(perdant:int, joueur1: str, joueur2: str):
    if perdant == 1:
        ajoutscore[3] = 10
        ajout_val_score()
        print(f"{joueur2} a gagné et remporte {ajoutscore[3]} points !")
        print(f"{joueur1} a perdu.")

    elif perdant == 2:
        ajoutscore[2] = 10
        ajout_val_score()
        print(f"{joueur1} a gagné et remporte {ajoutscore[2]} points !")
        print(f"{joueur2} a perdu.")
    

# Fonction pour demander un nombre valide d'allumettes
def demande_allumettes(message: str):
    while True:
        try:
            choix = int(input(message))
            if 1 <= choix <= 3:
                return choix
            else:
                print("Erreur : Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")