
joueur1 : int
joueur2 : int
choix : int
tour : int
victoirej1 : bool
victoirej2 : bool
retourligne : int
val : int
tableau1 :list[str]
victoirej1 = False
victoirej2 = False
tour = 1
tableau1 =[" - "," - "," - " ," - "," - "," - " ," - "," - "," - "]
lignes_gagnantes = [
    [0, 1, 2],  # Ligne 1
    [3, 4, 5],  # Ligne 2
    [6, 7, 8],  # Ligne 3
    [0, 3, 6],  # Colonne 1
    [1, 4, 7],  # Colonne 2
    [2, 5, 8],  # Colonne 3
    [0, 4, 8],  # Diagonale principale
    [2, 4, 6]   # Diagonale secondaire
]
val = 0
retourligne = 1

def affichagemorpion():
    
    for i in range(0,9):
        if ((i == 3) or (i == 6) or (i == 9)):
            print("\n")
        print(tableau1[i], end='')    
    
def choixdujoueur1():
    affichagemorpion()
    print("\n")
    choix = int(input("choix de la case joueur 1 "))
    print("\n")
    while (choix > 9) or ( tableau1[choix-1] != " - "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 1 "))
    print("\n")
    tableau1[choix-1]  = str(" X ")
def choixdujoueur2():
    affichagemorpion()
    print("\n")
    choix = int(input("choix de la case joueur 2 "))
    print("\n")
    while (choix > 9) or ( tableau1[choix-1] != " - "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 2 "))
    print("\n")
    tableau1[choix-1]  = str(" 0 ")
def victoire():
        global victoirej1, victoirej2  # Utilisation des variables globales

        # Vérification de toutes les combinaisons gagnantes
        for ligne in lignes_gagnantes:
            if tableau1[ligne[0]] == tableau1[ligne[1]] == tableau1[ligne[2]] and tableau1[ligne[0]] != " - ":
                if tableau1[ligne[0]] == " X ":
                    victoirej1 = True
                elif tableau1[ligne[0]] == " 0 ":
                    victoirej2 = True
                    

def morpion():
    global tour
    while ((victoirej1==False) and (victoirej2==False) and (tour <= 9)):
        choixdujoueur1()
        victoire()
        tour = tour+1
        if ((victoirej1==False) and (victoirej2==False) and (tour <= 9)):
            choixdujoueur2()
            victoire()
            tour = tour+1

    if(victoirej1==True):
        print("Victoire du joueur 1")
        affichagemorpion()

    elif(victoirej2==True):
            print("Victoire du joueur 2")
            affichagemorpion()
    else:
        print("égalité")
        affichagemorpion()
    
if __name__ == "__main__":
    morpion()