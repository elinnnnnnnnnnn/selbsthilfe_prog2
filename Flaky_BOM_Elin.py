import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import time
import json

class SafeRequest:
    URL = "http://160.85.252.61:32101"

#Versucht Daten vom Internet zu holen und wiederholt Abfrage, bei Fail
    def retry_http(self, retries=4,backoff_factor=2):
        attempt = 0
        while attempt < retries:
            attempt += 1
            try:
                response = requests.get(self.URL, timeout=5)
                response.raise_for_status()
                return response.content
            except (HTTPError, Timeout) as e:
                delay = backoff_factor ** attempt #Bei jedem weiteren Versuch, erhöht sich die Wartezeit exponentiel
                print(f"Error occured: {e} Retrying in {delay} seconds")
                time.sleep(delay)
            except RequestException as err:
                print(f"Request failed {err} Retrying...")
                time.sleep(1)
        print(f"Failed to retrieve {self.URL} after {retries} attempts")
        return None
#Diese Funktion wandelt die rohen Daten um
    def parse_data(self, data):
        json_data = json.loads(data)

        with open('data.json', 'w', encoding= 'utf-8') as file:
            json.dump(json_data,file,indent=4, ensure_ascii=False)
        print(json_data)
        return json_data
#Diese Funktion wandelt unlesbare Umlaute um
    def fix_umlauts(self, old_dict):
        fixed_dict = {}
        for key, value in old_dict.items():
            weird_word = key
            new_word = weird_word.encode('latin-1').decode('utf-8')
            fixed_dict[new_word] = value
        print(fixed_dict)
        return fixed_dict

#Diese Funktion validiert die Daten und druckt sie aus
    def print_table(self, material_dict: dict):
        total = 0
        for key, value in material_dict.items():
            if isinstance(value, int) and value > 0:
                value = int(value)
                total += value
                print(f"{key:<20} | {value}")
            else: #Bei deiser Methode werden alle ungültigen Zahlen eliminiert und NICHT aufbereitet
                continue
        print("--------------------")
        print(f"Total:           {total}")

def main():

    d = SafeRequest()
    data = d.retry_http()
    if not data:
        print("Heute leider nicht")
    else:
        fixed_data = d.parse_data(data)
        fixed_dict = d.fix_umlauts(fixed_data)
        d.print_table(fixed_dict)


if __name__ == "__main__":
    main()