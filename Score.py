if __name__ == "__main__":
    scorej1:  int
    scorej2 : int
    lecteurscorej1 : str
    lecteurscorej2 : str
    scorej1 = 100
    scorej2 = 200
    file = open("score.txt", "r+", encoding="utf8")
    file.write(str(scorej1))
    file.write("\n")
    file.write(str(scorej2))