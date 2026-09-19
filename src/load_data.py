"""
AIPI 510: Module 1 Project: Data Storytelling
- src/load_data.py
Hasan Al-Quaid
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
    Load all 3 raw FARS CSV files from data/raw/ into pandas DataFrames

    Checks that each file exists before loading, and raises an error
    if any are missing. Prints the shape of each DataFrame once loaded

    Returns:
        tuple of pd.DataFrame: (accident, person, vehicle), in that order
    """
    for f in files:
        path = folder + f
        if not os.path.exists(path):
            raise FileNotFoundError("File Not Found: " + path)

    accident = pd.read_csv(folder + files[0], low_memory=False)
    person = pd.read_csv(folder   + files[1], low_memory=False)
    vehicle = pd.read_csv(folder  + files[2], low_memory=False)

    print("accident:", accident.shape)
    # missing_counts = accident.isnull().sum()
    # columns_with_missing = missing_counts[missing_counts > 0].sort_values(ascending=False)
    # print("Number of columns with missing values accident:", len(columns_with_missing))
    # print(columns_with_missing)

    print("person:", person.shape)
    # missing_counts_person = person.isnull().sum()
    # columns_with_missing_person = missing_counts_person[missing_counts_person > 0].sort_values(ascending=False)
    # print("Number of columns with missing values Person:", len(columns_with_missing_person))
    # print(columns_with_missing_person)



    print("vehicle:", vehicle.shape)
    # missing_counts_vehicle = vehicle.isnull().sum()
    # columns_with_missing_vehicle = missing_counts_vehicle[missing_counts_vehicle > 0].sort_values(ascending=False)
    # print("Number of columns with missing values vehicle:", len(columns_with_missing_vehicle))
    # print(columns_with_missing_vehicle)

    return accident, person, vehicle

if __name__ == "__main__":
    load_data()