file = "datei.txt"
with open(file , "r", encoding="utf-8") as datei:
    inhalt = datei.read()
    print(inhalt)
