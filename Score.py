if __name__ == "__ main__":
    lecteur1 : int = 110
    lecteur2 : int = 11
    scorej1 =str(lecteur1)
    scorej2 = str(lecteur2)
    file = open("score.txt", "r+", encoding="utf8")
    file.write(scorej1)
    file.write(scorej2)
    lecteur1 = file.read()
    print(int(lecteur1))
    file.close()