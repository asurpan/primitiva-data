import requests
from bs4 import BeautifulSoup
import json

# URL de La Bruja de Oro (puedes ajustar si cambia)
url = "https://www.labrujadeoro.es/es/la-primitiva/resultados"

print("Descargando datos desde:", url)

# Descargar el HTML
response = requests.get(url, timeout=10)
response.raise_for_status()

# Parsear el HTML
soup = BeautifulSoup(response.text, "html.parser")

# Buscar los números de la Primitiva (ajusta si la web cambia)
numeros = []
for span in soup.select(".number-ball, .number, .bola, .num"):
    try:
        num = int(span.get_text().strip())
        numeros.append(num)
    except:
        pass

# Quitar duplicados y ordenar
numeros = sorted(list(set(numeros)))

# Guardar en JSON
data = {"frequent_numbers": numeros}
with open("frequent_numbers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Archivo frequent_numbers.json actualizado con:", numeros)
