if __name__ == "__main__":
    choixj1: int =0
    choixj2 :int=0
    essai1 :int=0
    essai2 :int =0

    nombretoursj1 :int =1
    nombretoursj2 : int=0
    j1 : int
    j2 : int
    print(" tour du joueur 1")
    choixj1 =int(input("choisir un nombre"))
    while (essai2 != choixj1):
        nombretoursj2 = nombretoursj2 +1
        print("tour ", nombretoursj2)
        essai2 = int(input("j2 choisis une valeur"))
        print("la valeur choisi par le joueur 2 est :", essai2)
    print("valleur correcte, trouvé  en ", nombretoursj2,("tours"))
