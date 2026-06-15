# Issue 3: Dictionaries nutzen
# Erstelle ein Dictionary mit 3 fiktiven Mitarbeitern und deren Gehältern. 
# Lass dir dann das Gehalt von einer bestimmten Person per print ausgeben.

# Dictionary erstellen
employees = {
    "Jan": 41000,
    "Michael": 45000,
    "Paula": 44000
}

emp1 = "Michael"
salary1 = employees[emp1]
print(f"Das Jahresgehalt von {emp1} ist {salary1}")