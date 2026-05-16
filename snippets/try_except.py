# Issue 2: absichtlich eine Division durch Null durchführen, Fehler mit try/except abfangen und eine Warnung ausgeben

try:
    # Hier wird absichtlich eine Division durch Null provoziert
    ergebnis = 10 / 0
except ZeroDivisionError:
    # Fehler wird abgefangen und eine Meldung ausgegeben
    print("Warnung: Eine Division durch Null ist nicht erlaubt!")