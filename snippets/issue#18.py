import pandas as pd

#issue#18: Zeige, wie man eine Spalte, die Zahlen als Text (String) enthält, in echte Integer-Werte umwandelt.

#Beispiel
data = {
    'Name': ['Anna', 'Ben', 'Chris', 'Dana'],
    'Alter': ['25', '30', '40', '50'] 
}

df = pd.DataFrame(data)


# Umwandlung in Integer
df['Alter'] = df['Alter'].astype(int)
