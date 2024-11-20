if __name__=="__main___":
    choixj1 :int
    choixj2 :int
    allumette:int=20
    perdant :int=0

    while allumette>0:
        choixj1=int(input("Joueur 1, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        if choixj1<1 or choixj1>3:
            while choixj1<1 or choixj1>3:
                print("Erreur")
                choixj1=int(input("Joueur 1, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        else:
            allumette=allumette-choixj1
        if allumette<=0:
            perdant=1
            break
        print("Il reste",allumette,"allumettes.")
        for allumette in range(allumette):
            print("|", end="")
        print("")
        choixj2=int(input("Joueur 2, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        if choixj2<1 or choixj2>3:
            while choixj2<1 or choixj2>3:
                print("Erreur")
                choixj2=int(input("Joueur 2, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        else:
            allumette=allumette-choixj2
        if allumette<=0:
            perdant=2
            break
        print("Il reste",allumette,"allumettes.")
        for allumette in range(allumette):
            print("|", end="")
        print("")
        
    if perdant==1:
        print("Le joueur 1 a perdu.")
    elif perdant==2:
        print("Le joueur 2 a perdu.")