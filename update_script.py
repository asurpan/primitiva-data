import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.labrujadeoro.es/primitiva-estadisticas.htm"
JSON_FILE = "frequent_numbers.json"

def scrape_frequent_numbers():
    print("Obteniendo datos desde La Bruja de Oro...")
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar la tabla de los números más frecuentes
    table = soup.find("table")
    if not table:
        raise ValueError("No se encontró la tabla de números frecuentes.")

    numbers = []
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) >= 1:
            try:
                num = int(cols[0].get_text(strip=True))
                numbers.append(num)
            except ValueError:
                continue

    print(f"Números encontrados: {numbers}")

    if not numbers:
        raise ValueError("No se encontraron números válidos.")

    data = {"frequent_numbers": numbers}

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Archivo {JSON_FILE} actualizado correctamente.")


if __name__ == "__main__":
    scrape_frequent_numbers()

