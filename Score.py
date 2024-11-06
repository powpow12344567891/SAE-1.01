if __name__ =="__main__":
    scorej1:  int
    scorej2 : int
    lecteurscorej1 : str
    lecteurscorej2 : str
    scorej1 = 800
    scorej2 = 300
    file = open("score.txt", "w", encoding="utf8")
    file.write(str(scorej1))
    file.write("\n")
    file.write(str(scorej2))
    file.close()
    file = open("score.txt", "r", encoding="utf8")  
    lignes = int(file.readline())
    print(lignes)
    lignes2 = int(file.readline())
    print(lignes2)
    file.close()