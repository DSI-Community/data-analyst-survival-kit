#Aufgabe: Nutze \groupby(), um das Durchschnittsgehalt pro Abteilung
# in einem fiktiven DataFrame zu berechnen.

import pandas as pd

#Besipiel Daten erzeugen
abteilung = {
    "Name" : ["Max", "Mustermann", "Musterfrau", "Tester", "Testerin", "Beispieline"],
    "Abteilung" : ["Sales", "Marketing", "Sales", "Sales", "Sales", "Marketing"],
    "Gehalt" : [50000, 55000, 40000, 60000, 70000, 40000]
}

#DataFrame erstellen
df = pd.DataFrame(abteilung)

abteilung_sortiert = df.groupby("Abteilung")["Gehalt"].mean().sort_values(ascending=False)
print(f"Das Durchschnittsgehalt pro Abteilung ist \n {abteilung_sortiert}")
