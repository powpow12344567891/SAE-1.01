if __name__ =="__main__":
    scorej1:  int
    scorej2 : int
    ajoutscorej1 : int
    ajoutscorej2 : int
    lecteurscorej1 : str
    lecteurscorej2 : str
    
    def recup_val_score(scorej1, scorej2):
        file = open("score.txt", "r", encoding="utf8")  
        scorej1 = int(file.readline())
        scorej2 = int(file.readline())
        print("le score du joueur 1 est :" , scorej1)
        print("le score du joueur 2 est :" , scorej2)
        file.close()
        
    def ajout_de_val_score(scorej1, scorej2, ajoutscorej1, ajoutscorej2):
        file = open("score.txt", "w", encoding="utf8")
        file.write(str(scorej1 + ajoutscorej1))
        file.write("\n")
        file.write(str(scorej2 + ajoutscorej2))
        file.close()
        
