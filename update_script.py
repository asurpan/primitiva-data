import requests
from bs4 import BeautifulSoup
import json

url = "https://www.labrujadeoro.es/primitiva"
print("Descargando datos desde:", url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
except Exception as e:
    print("Error al descargar la página:", e)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

numeros = []
for span in soup.select(".number-ball, .number, .bola, .num"):
    try:
        num = int(span.get_text().strip())
        numeros.append(num)
    except ValueError:
        continue

numeros = sorted(set(numeros))
data = {"frequent_numbers": numeros}

with open("frequent_numbers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Archivo frequent_numbers.json actualizado con:", numeros)
