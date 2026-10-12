# Berechne die Marge mit pandas als eigene Spalte

import pandas as pd
#df = pd.read_csv...          dataframe einlesen

print("Heute berechnen wir die Marge mit Hilfe der pandas Funktion und erstellen eine neue Spalte")

df["Marge"] = df["Verkaufspreis"] - df["Einkaufspreis"]

