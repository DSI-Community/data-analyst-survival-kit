import pandas as pd


# Die CSV-Datei ist durch Semikolons statt durch Kommas getrennt.
daten = pd.read_csv("datei.csv", sep=";")

print(daten)