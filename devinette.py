def devinette(manche_tt:int):
    choixj1 :int=0
    choixj2 :int=0
    essai1 :int=0
    essai2 :int=0
    nombretoursj1 :int=0
    nombretoursj2 :int=0
    manche:int=0

    for i in range(manche_tt//2):
        #J1 choisit et J2 joue.
        manche=manche+1
        print("Round",i+1)
        print("-----------------------------------------------------------------")
        print("manche",manche)
        print("Tour du joueur 1")
        choixj1 =int(input("Veuillez choisir un nombre: "))
        while (essai2 != choixj1):
            nombretoursj2 += 1
            print("Tour", nombretoursj2)
            essai2 = int(input("J2 choisis une valeur: "))
            if essai2<choixj1:
                print("La valeur", essai2, "est plus petite que le valeur choisit.")
            else:
                print("La valeur", essai2, "est plus grande que le valeur choisit.")
        else:
            nombretoursj2 += 1
            print("Tour", nombretoursj2)
        print("La valeur est correcte, trouvé en", nombretoursj2-1, "tours")
        #J2 choisit et J1 joue.
        print("-----------------------------------------------------------------")
        manche=manche+1
        print("manche",manche)
        print("Tour du joueur 2")
        choixj2 =int(input("Veuillez choisir un nombre: "))
        while (essai1 != choixj2):
            nombretoursj1 += 1
            print("Tour", nombretoursj1)
            essai1 = int(input("J1 choisis une valeur: "))
            if essai1<choixj2:
                print("La valeur", essai1, "est plus petite que le valeur choisit.")
            else:
                print("La valeur", essai1, "est plus grande que le valeur choisit.")
        else:
            nombretoursj1 += 1
            print("Tour", nombretoursj1)
        print("La valeur est correcte, trouvé en", nombretoursj1-1, "tours")
        print("-----------------------------------------------------------------")
    return "Le joueur 1 a pris un total de "+str(nombretoursj1-1)+" tours, tandis que le joueur 2 a pris un total de "+str(nombretoursj2-1)+" tours."