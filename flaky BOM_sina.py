# nur mit request statt urllib.request 403 Zugriff nur Webbrowser umgehen
# dann ist request.get(url) statt urllib.request.urlopen(url)
# f.read() braucht man mit requests nicht

import requests                                         # für HTTP Anfrage
import time                                             # pausieren
import json                                             # JSON Text -> Python-Daten

url = "http://160.85.252.61:32101/"                     # URL abspeichern


def fetch_data():
    while True:                                         # wird bis zum break wiederholt
        try:
            f = requests.get(url).text                  # Anfrage an Server, .text = Antwort als String
            data = json.loads(f)                        # Dictionary wird erstellt
            return data

        except:
            time.sleep(1)                               # pausiert eine s & versucht erneut


def fix_umlauts(text):
    try:
        return text.encode("latin1").decode("utf-8")    # latin1 = Zeichencodierung
    except:
        return text


def parse_data(data):
    result = []

    for item in data:
        name = item.get("material")                     # Zugriff Dict mit .get() gibt None wenn Schlüssel fehlt
        cost = item.get("cost")                         # mit [] müsste man KeyError vorbeugen

        if name is None or cost is None:                # fehlende Werte ignorieren
            continue

        try:
            cost = float(cost)
        except:
            continue

        name = fix_umlauts(name)
        result.append((name, cost))

    result.sort()
    return result


def print_table(data):


def main():
    raw = fetch_data()
    parsed = parse_data(raw)
    print_table(parsed)

if __name__ == "__main__":
    main()



