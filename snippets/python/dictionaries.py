# Issue 3: Dictionaries nutzen
# Erstelle ein Dictionary mit 3 fiktiven Mitarbeitern und deren Gehältern. 
# Lass dir dann das Gehalt von einer bestimmten Person per print ausgeben.

# Dictionary erstellen
employees = {
    "name": ["Jan", "Michael", "Paula"],
    "salary": [41000, 45000, 44000]
}

emp1 = employees["name"][0]
salary1 = employees["salary"][0]

print(F"Das Jahresgehalt von {emp1} ist {salary1}")