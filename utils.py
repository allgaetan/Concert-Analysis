import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze concerts data given a CSV file. The CSV file must use ',' as separator and must contain 4 columns: 'Date' (in DD/MM/YYYY format), 'Bands' (if multiple bands, they must be separated by ';'), 'City' and 'Venue'.")
    parser.add_argument("--csv", required=True, help="Path to the CSV file containing the concerts data.")
    parser.add_argument("--test", action="store_true", help="Run some test cases.")
    parser.add_argument("--plot", action="store_true", help="Generate plots of the number of concerts and bands seen by month and by year.")
    return parser.parse_args()

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

def plot(X, n_concerts, n_bands, show=False, save=False, file_path=None):
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

    if show:
        print("Displaying plot...")
        plt.show()
    if save:
        print("Saving plot...")
        if file_path is None:
            raise ValueError("file_path must be specified if save is True")
        plt.savefig(file_path)