import pandas as pd

#Nutze \groupby(), um das Durchschnittsgehalt pro Abteilung in einem fiktiven DataFrame zu berechnen.

data = { 
    "Vorname": ["Markus", "Maria", "Christine", "Lisa", "Jonas", "Sebastian", "Michael", "Tim", "Petra", "Alexandra"],
    "Abteilung": ["Sales", "Development", "Sales", "HR", "Sales", "Development", "Development", "HR", "Development", "HR"],
    "Gehalt": [55000, 52000, 51000, 43000, 58000, 50000, 49000, 45000, 48000, 43000 ]
    }

df = pd.DataFrame(data)

grouped_df = df.groupby("Abteilung")["Gehalt"].mean().sort_values(ascending=False)

print(grouped_df)