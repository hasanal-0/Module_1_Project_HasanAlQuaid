"""
AIPI 510: Module 1 Project: Data Storytelling
- src/load_data.py
=================================================
Loads all raw FARS CSV files from data/raw/ into pandas DataFrames.    
    - accident.csv
    - person.csv
    - vehicle.csv
"""

import pandas as pd
import os

folder = "data/raw/"
files = ["accident.csv","person.csv", "vehicle.csv"]

def load_data():
    """
    Load all 3 raw FARS CSV files from data/raw/ into pandas DataFrames.

    Checks that each file exists before loading, and raises an error
    if any are missing. Prints the shape of each DataFrame once loaded.

    Returns:
        tuple of pd.DataFrame: (accident, person, vehicle), in that order.
    """
    for f in files:
        path = folder + f
        if not os.path.exists(path):
            raise FileNotFoundError("File Not Found: " + path)

    accident = pd.read_csv(folder + files[0], low_memory=False)
    person = pd.read_csv(folder   + files[1], low_memory=False)
    vehicle = pd.read_csv(folder  + files[2], low_memory=False)

    # print("accident:", accident.shape)
    # print("person:", person.shape)
    # print("vehicle:", vehicle.shape)

    return accident, person, vehicle

if __name__ == "__main__":
    load_data()