import pandas as pd

# Beispiel: Trainingsdaten aus dem Judo-Training
daten = {
    "trainingsstunden_pro_woche": [3, 5, 4, 6, 2, 5, 7],
    "anzahl_würfe_pro_training": [15, 22, 18, 25, 10, 20, 28],
    "punkte_im_wettkampf": [4, 8, 6, 9, 2, 7, 10]
}

df = pd.DataFrame(daten)

# Korrelation zwischen allen numerischen Spalten berechnen
korrelationsmatrix = df.corr()

print(korrelationsmatrix)