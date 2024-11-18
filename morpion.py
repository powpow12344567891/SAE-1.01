if __name__ == "__main__":
    joueur1 : int
    joueur2 : int
    choix : int
    tour : int
    victoirej1 : bool
    victoirej2 : bool
    val : int
    tableau1 :list[str]
    victoirej1 = False
    victoirej2 = False
    tour = 1
    tableau1 =[" - "," - "," - " ," - "," - "," - " ," - "," - "," - "]
    val = 0
def affichagemorpion():
    
    for i in range(0,3):
        print("\n")
        
        for j in range(0,3):
            
            print(tableau1[i], end='')    
    
affichagemorpion()
choix = int(input)
if()