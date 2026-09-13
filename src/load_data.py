"""
AIPI 510: Module 1 Project: Data Storytelling
- src/load_data.py
=================================================
Loads all raw FARS CSV files from data/raw/ into pandas DataFrames.    
    - accident.csv
    - drugs.csv
    - factor.csv
    - person.csv
    - safetyeq.csv
    - vehicle.csv
    - vision.csv
    - weather.csv
"""

import pandas as pd
import os

folder = "data/raw/"
files = ["accident.csv", "drugs.csv", "factor.csv", "person.csv",
         "safetyeq.csv", "vehicle.csv", "vision.csv", "weather.csv"]

def load_data():
    """
    Load all 8 raw FARS CSV files from data/raw/ into pandas DataFrames.

    Checks that each file exists before loading, and raises an error
    if any are missing. Prints the shape of each DataFrame once loaded.

    Returns:
        tuple of pd.DataFrame: (accident, drugs, factor, person,
        safetyeq, vehicle, vision, weather), in that order.
    """
    for f in files:
        path = folder + f
        if not os.path.exists(path):
            raise FileNotFoundError("File Not Found: " + path)

    accident = pd.read_csv(folder + files[0], low_memory=False)
    drugs = pd.read_csv(folder    + files[1], low_memory=False)
    factor = pd.read_csv(folder   + files[2], low_memory=False)
    person = pd.read_csv(folder   + files[3], low_memory=False)
    safetyeq = pd.read_csv(folder + files[4], low_memory=False)
    vehicle = pd.read_csv(folder  + files[5], low_memory=False)
    vision = pd.read_csv(folder   + files[6], low_memory=False)
    weather = pd.read_csv(folder  + files[7], low_memory=False)

    # print("accident:", accident.shape)
    # print("drugs:", drugs.shape)
    # print("factor:", factor.shape)
    # print("person:", person.shape)
    # print("safetyeq:", safetyeq.shape)
    # print("vehicle:", vehicle.shape)
    # print("vision:", vision.shape)
    # print("weather:", weather.shape)

    return accident, drugs, factor, person, safetyeq, vehicle, vision, weather

if __name__ == "__main__":
    load_data()