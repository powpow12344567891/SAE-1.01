if __name__ == "__main__":
    lecteur1 : str
    lecteur2 : str
    scorej1 =str("joueur1")
    scorej2 = str("joueur2")
    file = open("score.txt", "r+", encoding="utf8")
    file.write(scorej1)
    file.write("\n")
    file.write(scorej2,)
    lecteur1 = file.read()
    file.close()
