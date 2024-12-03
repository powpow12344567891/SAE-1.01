def devinnettes(choix:int):
    essai:int
    nombretours:int=1
    if manche%2==1:
        essai=int(input("J2 choisis une valeur: "))
    else:
        essai=int(input("J1 choisis une valeur: "))
    while (essai!=choix):
        print("Tour",nombretours)
        nombretours+=1
        if essai<choix:
            print("La valeur", essai, "est plus petite que le valeur choisit.")
        elif essai>choix:
            print("La valeur", essai, "est plus grande que le valeur choisit.")
        else:
            print("La valeur est correcte, trouvé en", nombretours, "tours")
            return nombretours
        if manche%2==1:
            essai=int(input("J2 choisis une valeur: "))
        else:
            essai=int(input("J1 choisis une valeur: "))

if __name__=="__main__":
    manche_tt:int
    manche:int=0
    choix:int
    nombretoursj1:int=0
    nombretoursj2:int=0
    manche_tt=int(input("Entrez le nombre de manche que vous souhaiter réaliser: "))
    for i in range(manche_tt):
        #J1 choisit et J2 joue.
        manche=manche+1
        print("Round",i+1)
        print("manche",manche)
        if manche%2==1:
            print("Tour du joueur 1")
        else:
            print("Tour du joueur 2")
        choix=int(input("Entrez la valeur à trouver: "))
        devinnettes(choix)
        #J2 choisit et J1 joue.
        print("-----------------------------------------------------------------")
    print("Le joueur 1 a pris un total de "+str(nombretoursj1)+" tours, tandis que le joueur 2 a pris un total de "+str(nombretoursj2)+" tours.")