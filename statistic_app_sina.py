import time
import os
import pandas as pd
import matplotlib.pyplot as plt

url = "https://dam-api.bfs.admin.ch/hub/api/dam/assets/22324832/master"

class DataDownloader():
    def __init__(self, url, cache_file = "data.xlsx", timeout =600):
        self.url = url
        self.cache_file = cache_file        # Nach Abfrage Lokal als Cache File Speichern
        self.timeout = timeout              # 10' abwarten

    def open_url(self):
        if os.path.exists(self.cache_file):
            age = time.time() - os.stat(self.cache_file).st_mtime      # Zeitdifferenz über 10'? Aktuelle Zeit minus letzte Änderungszeit
            if age > self.timeout:
                self.df = pd.read_excel(self.url, header = 3)
                self.df.to_excel(self.cache_file, index = False)
            else:
                self.df = pd.read_excel(self.cache_file)

        else:
            while True:
                try:
                    self.df = pd.read_excel(self.url, header = 3)
                    self.df.to_excel(self.cache_file, index=False)
                    break
                except:
                    time.sleep(1)

        return self.df


class StatisticsApp():
    def __init__(self, downloader):
        self.downloader = downloader

    def load_data(self):
        self.df = self.downloader.open_url()


    def prepare_data(self):
        self.df = self.df[
            (self.df["Leistungen"] == "Total") &
            (self.df["Altersklasse"] != "Altersklasse - Total")
        ]

        print(self.df[["Altersklasse", "Männer.1", "Frauen.1"]].head(10))


    def calculate_statistics(self):
        # Altersklasse mit höchsten monatlichen Gesundheitskosten pro Einwohner bei Frauen?
        max_cost_women = self.df["Frauen.1"].max()
        idx = self.df["Frauen.1"].idxmax()
        altersklasse = self.df.loc[idx, "Altersklasse"]

        print(f"Höchste Kosten Frauen: {altersklasse}")
        print(f"Wert: {max_cost_women}")


    def run(self):
        self.load_data()
        self.prepare_data()
        self.calculate_statistics()
        self.visualize_data()

        # Test prints zur Datenanalyse
        # print(self.df.head(8))
        # print(self.df.columns)
        # print(self.df.info())
        # print(self.df.describe())
        # print(self.df[["Altersklasse", "Männer.1", "Frauen.1"]].head(10))

    def visualize_data(self):
        self.df.plot(x="Altersklasse", y="Frauen.1", kind="bar")
        plt.show()



if __name__ == "__main__":
    downloader = DataDownloader(url)
    app = StatisticsApp(downloader)
    app.run()
