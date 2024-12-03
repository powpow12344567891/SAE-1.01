def allumette(joueur1:str, joueur2:str):
    choixj1 :int
    choixj2 :int
    allumette:int=20
    perdant :int=0

    print("Il reste",allumette,"allumettes.")
    for allumette in range(allumette):
        print("|", end="")
    print("")
    while allumette>=0:
        print(joueur1)
        choixj1=int(input("Veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        while choixj1<1 or choixj1>3:
            print("Erreur")
            print(joueur1)
            choixj1=int(input("Veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        allumette-=choixj1-1
        if allumette<=0:
            perdant=1
            break
        print(choixj1)
        print("Il reste",allumette,"allumettes.")
        for allumette in range(allumette):
            print("|", end="")
        print("")
        print(joueur2)
        choixj2=int(input("Veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
        while choixj2<1 or choixj2>3:
            print("Erreur")
            print(joueur2)
            choixj2=int(input("Veuillez choisir combien d'allumette vous voulez prendre, entre 1 et 3: "))
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