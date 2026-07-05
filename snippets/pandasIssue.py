import pandas as pd

data = {
    'Produktnummer': ['P001', 'P002', 'P003', 'P004'],
    'Verkaufspreis': [150.00, 45.50, 12.00, 89.99],
    'Einkaufspreis': [95.00, 30.00, 7.50, 60.00]
}

df = pd.DataFrame(data)

#  Neue Spalte 'Marge' berechnen
df['Marge'] = df['Verkaufspreis'] - df['Einkaufspreis']


print(df)

