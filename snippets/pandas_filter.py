import pandas as pd

# Beispiel-Daten
df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Clara", "David"],
    "Alter": [25, 32, 29, 41]
})

# Filter: nur Kunden über 30
df_ueber30 = df[df["Alter"] > 30]

print(df_ueber30)