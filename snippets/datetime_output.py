from datetime import datetime

now = datetime.now()

datum = now.strftime("%d.%m.%Y")
uhrzeit = now.strftime("%H:%M:%S")

print("Aktuelles Datum:", datum)
print("Aktuelle Uhrzeit:", uhrzeit)