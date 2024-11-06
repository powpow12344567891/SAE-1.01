if __name__ == "__main__":
    lecteur1 : int 
    lecteur2 : int 
    scorej1 : str
    scorej2 : str
    lecteur1 = 100
    lecteur2 = 200
    scorej1 =str(lecteur1)
    
    scorej2 = str(lecteur2)
    file = open("score.txt", "r+", encoding="utf8")
    file.write(scorej1)
    file.write("\n")
    file.write(scorej2)
    lecteur1 = file.read()
    file.close()