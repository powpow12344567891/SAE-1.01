<<<<<<< HEAD
if __name__ == "__ main__":
    lecteur1 : int = 110
    lecteur2 : int = 11
    scorej1 =str(lecteur1)
    scorej2 = str(lecteur2)
    file = open("score.txt", "r+", encoding="utf8")
    file.write(scorej1)
    file.write(scorej2)
    lecteur1 = file.read()
    print(lecteur1)
=======
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
>>>>>>> 0a011bdcf250456dfe74524ee4b552800f34f0f2
    file.close()
