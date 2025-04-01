import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def str_to_date(str):
    return datetime.strptime(str, "%d/%m/%Y").date()

def date_to_str(date):
    return date.strftime("%d/%m/%Y")

def parse_bands(concerts, id):
    bands = str(concerts["Bands"][id])
    if bands == "nan":
        return []
    bands = bands.split(";")
    return bands

def get_band_count(concerts, band):
    count = 0
    for index, row in concerts.iterrows():
        bands = parse_bands(concerts, index)
        if band in bands:
            count += 1
    return count

def plot(X, n_concerts, n_bands):
    x = np.arange(len(X))
    bar_width = 0.4
    plt.figure()
    plt.title("Distribution of the number of concerts and bands seen")
    plt.bar(x - bar_width /2, n_concerts, width=bar_width, label="Number of concerts")
    plt.bar(x + bar_width /2, n_bands, width=bar_width, label="Number of bands")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.xticks(x, X, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()