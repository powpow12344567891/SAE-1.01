if __name__ == "__main__":
    lecteur : str
    scorej1 =str("1")
    file = open("score.txt", "w", encoding="utf8")
    file.write(scorej1)
    lecteur = file.read()
    file.close()
    print(lecteur)