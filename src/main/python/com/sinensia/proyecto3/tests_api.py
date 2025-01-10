import requests

URL = "https://www.omdbapi.com/?t=avatar&apikey=b50f00d8&y=2010&type=movie"

payload = {}
headers = {}

response = requests.request("GET", URL, headers = headers, data = payload)

print(response.text)

import json
#Proporciona la ruta completa al archivo
with open('../data/archivo.json', 'r') as file:
    datos = json.load(file)
#Ahora puedes acceder a los datos como con cualquier diccionario en Python
print(datos['window'])