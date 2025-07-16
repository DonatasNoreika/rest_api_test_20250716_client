import requests
import json

# r = requests.get("http://127.0.0.1:5000/")
# print(r.json()["about"])
#
# payload = {"vardas": "Donatas", 'pavarde': "Noreika", "amzius": 2000}
# r = requests.post("http://127.0.0.1:5000/", json=payload)
# print(r.json())

r = requests.get("http://127.0.0.1:5000/keliamieji/2401")
print(r.json())