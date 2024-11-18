if __name__ == "__main__":
    joueur1 : int
    joueur2 : int
    victoirej1 : bool
    victoirej2 : bool
    val : int
    tableau1 :list[int]
    victoirej1 = False
    victoirej2 = False
    tableau1 =[0,0,0,0,0,0,0,0,0]
    val = 0
def affichagemorpion():
    
    for i in range(0,3):
        print("\n")
        for j in range(0,3):
            print(tableau1[i], end='')    
            
