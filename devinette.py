if __name__ == "__main__":
    choixj1: int =0
    choixj2 :int=0
    essai1 :int=0
    essai2 :int =0

    nombretoursj1 :int =1
    nombretoursj2 : int=0
    j1 : int
    j2 : int
    print("Tour du joueur 1")
    choixj1 =int(input("Veuillez choisir un nombre: "))
    while (essai2 != choixj1):
        nombretoursj2 = nombretoursj2 +1
        print("Tour", nombretoursj2)
        essai2 = int(input("J2 choisis une valeur: "))
        if essai2<choixj1:
            print("La valeur", essai2, "est plus petite que le valeur choisit.")
        else:
            print("La valeur", essai2, "est plus grande que le valeur choisit.")
    print("La valeur est correcte, trouvé en", nombretoursj2, "tours")
