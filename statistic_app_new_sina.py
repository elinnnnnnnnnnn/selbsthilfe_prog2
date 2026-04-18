import time
import os
import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.zg.ch/rowstore/dataset/42eaeb94-520a-4b8e-b7f6-43de29979c22/json"

class DataDownloader():
    def __init__(self, url, cache_file = "data1.xlsx", timeout = 600):
        self.url = url
        self.cache_file = cache_file
        self.timeout = timeout

    def open_url(self):
        if os.path.exists(self.cache_file):
            age = time.time() - os.stat(self.cache_file).st_mtime

            if age > self.timeout:
                self.df = pd.read_json(self.url)
                self.df.to_json(self.cache_file)
            else:
                self.df = pd.read_json(self.cache_file)

        else:
            while True:
                try:
                    self.df = pd.read_json(self.url)
                    self.df.to_json(self.cache_file)
                    break
                except:
                    time.sleep(1)

        print(self.df.head())
        return self.df


class StatisticsApp():
    def __init__(self, downloader):
        self.downloader = downloader

    def load_data(self):
        self.df = self.downloader.open_url()
        return self.df

    def prepare_data(self):
        self.df["jahr"] = self.df["results"].apply(lambda x: x["jahr"])
        print(self.df["jahr"].head())

        self.df["anteil_prozent"] = self.df["results"].apply(lambda y: y["anteil_prozent"])
        print(self.df["anteil_prozent"].head())
        return self.df

    def calculate_statistics(self):
        # maximaler Anteil
        self.df["anteil_prozent"] = self.df["anteil_prozent"].astype(float)
        max_anteil = self.df["anteil_prozent"].max()

        # jahr mit dem maximalen Anteil
        idx = self.df["anteil_prozent"].idxmax()
        jahr = self.df.loc[idx, "jahr"]
        print(f"Im Jahr {jahr} gab es den höchsten Prozentanteil von {max_anteil}%")

        # durchschnittlicher Anteil
        avg = self.df["anteil_prozent"].mean()
        print(f"Der durchschnittliche Anteil der Bevölkerung über 80 im Altersheim beträgt {avg}%")

    def plot_data(self):
        # Typumwandlung
        self.df["anteil_prozent"] = self.df["anteil_prozent"].astype(float)
        self.df["jahr"] = self.df["jahr"].astype(int)

        # Jahre chronologisch sortieren
        self.df = self.df.sort_values("jahr")

        # Werte in Variablen speichern
        jahr = self.df["jahr"]
        anteil = self.df["anteil_prozent"]

        # Statistik
        avg = anteil.mean()
        max_val = anteil.max()
        idx = anteil.idxmax()
        jahr_max = self.df.loc[idx, "jahr"]

        # Plot
        plt.figure()                      # keine Überlagerung

        plt.plot(jahr,              # x Achse
                anteil,                   # y Achse
                 marker='o',              # Punkte auf Linie
                 label="Anteil %",
                 color='green'
        )

        plt.axhline(avg,
                    linestyle='--',
                    label=f"Durchschnitt({avg:.2f}%",
                    color='pink')

        plt.scatter(jahr_max,
                    max_val,
                    label=f"Maximum ({max_val:.2f}%)")

        plt.axhline(max_val,
                    linestyle=':',
                    label="Max Linie")

        plt.title("Anteil der Bevölkerung von über 80jährigen (Kanton Zug) im Altersheim")
        plt.xlabel("Jahr")
        plt.ylabel("Anteil (%)")

        plt.legend()

        plt.grid()

        plt.show()

if __name__ == "__main__":
    downloader = DataDownloader(url)

    app = StatisticsApp(downloader)
    app.load_data()
    app.prepare_data()
    app.calculate_statistics()
    app.plot_data()



