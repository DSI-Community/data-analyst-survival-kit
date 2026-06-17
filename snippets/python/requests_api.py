import requests

# URL der API festlegen
URL = "https://api.thecatapi.com/v1/images/search"

# Beispiel-Header (sofern erforderlich) | müsste bei Bedarf in .get() ergänzt werden
'''
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}",
    # oder je nach API:
    "X-Api-Key": api_key,
}
'''

# API-Call mit Error-Handling
try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Fehler: {e}")
except requests.exceptions.ConnectionError:
    print("Keine Verbindung")
except requests.exceptions.Timeout:
    print("Timeout")

# Ausgabe der abgerufenen Daten
print(data)