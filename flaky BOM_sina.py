# nur mit request statt urllib.request 403 Zugriff nur Webbrowser umgehen
# dann ist request.get(url) statt urllib.request.urlopen(url)
# f.read() braucht man mit requests nicht

import requests                                         # für HTTP Anfrage
import time                                             # pausieren
import json                                             # JSON Text -> Python-Daten

url = "http://160.85.252.61:32101/"                     # URL abspeichern


def fetch_data():
    wait = 1
    while True:                                         # wird bis zum break wiederholt
        try:
            f = requests.get(url).text                  # Anfrage an Server, .text = Antwort als String
            data = json.loads(f)                        # Dictionary wird erstellt
            return data

        except:
            time.sleep(wait)                               # pausiert eine s & versucht erneut
            wait = wait * 2

def fix_umlauts(text):
    try:
        return text.encode("latin1").decode("utf-8")    # latin1 = Zeichencodierung
    except:
        return text


def parse_data(data):
    result = []

    for name, cost in data.items():
        if name is None or cost is None:                # fehlende Werte ignorieren
            continue

        try:
            cost = float(cost)
            if cost <0:
                continue
        except:
            continue

        name = fix_umlauts(name)                        # Ä,Ö,Ü werden umgewandelt
        result.append((name, cost))                     # Tupel werden der Liste results hinzugefügt

    result.sort()
    return result


def print_table(data):
    total = 0
    for name, cost in data:
        print(f"{name} | {cost:.2f}")                   # 2 Dezimalstellen runden
        total += cost                                   # Totalkosten werden berechnet
    print("-------+--------")
    print(f"SUM | {total:.2f}")


def main():
    raw = fetch_data()
    print(raw)
    print("------------------")
    parsed = parse_data(raw)
    print_table(parsed)

if __name__ == "__main__":
    main()



