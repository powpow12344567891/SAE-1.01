if __name__ == "__main__":
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
    val = 0
    retourligne = 1
9
def affichagemorpion():
    
    for i in range(0,9):
        if ((i == 3) or (i == 6) or (i == 9)):
            print("\n")
        print(tableau1[i], end='')    
    
affichagemorpion()
def choixdujoueur1():
    print("\n")
    choix = int(input("choix de la case joueur 1 "))
    print("\n")
    while (choix > 9) or ( tableau1[choix-1] != " - "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 1 "))
    print("\n")
    tableau1[choix-1]  = str(" X ")
    affichagemorpion()
def choixdujoueur2():
    print("\n")
    choix = int(input("choix de la case joueur 1 "))
    print("\n")
    while (choix > 9) or ( tableau1[choix-1] != " - "):
        print("\n", "choix non valide")
        choix = int(input("choix de la case joueur 1 "))
    print("\n")
    tableau1[choix-1]  = str(" 0 ")
    affichagemorpion()    

while ((victoirej1==False) or (victoirej2==False)):
    choixdujoueur1()
    choixdujoueur2()
