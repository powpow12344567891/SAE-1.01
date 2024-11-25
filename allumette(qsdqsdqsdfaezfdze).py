def allumette(Joueur1:str)
    choixj1 :int
    choixj2 :int
    allumette:int=20
    perdant :int=0

    print("Il reste",allumette,"allumettes.")
    for allumette in range(allumette):
        print("|", end="")
    print("")
    while allumette>=0:
        choixj1=int(input("Joueur 1, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        while choixj1<1 or choixj1>3:
            print("Erreur")
            choixj1=int(input("Joueur 1, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        allumette-=choixj1-1
        if allumette<=0:
            perdant=1
            break
        print(choixj1)
        print("Il reste",allumette,"allumettes.")
        for allumette in range(allumette):
            print("|", end="")
        print("")
        choixj2=int(input("Joueur 2, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        while choixj2<1 or choixj2>3:
            print("Erreur")
            choixj2=int(input("Joueur 2, veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        allumette-=choixj2-1
        if allumette<=0:
            perdant=2
            break
        print(choixj2)
        print("Il reste",allumette,"allumettes.")
        for allumette in range(allumette):
            print("|", end="")
        print("")

    if perdant==1:
        print("Le joueur 1 a perdu.")
    elif perdant==2:
        print("Le joueur 2 a perdu.")