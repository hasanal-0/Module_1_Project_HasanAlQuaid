"""
AIPI 510: Module 1 Project: Data Storytelling
- src/merge_3.py
=================================================
Merge 3 data frames into one big data frame 
    - motorcycles_accidents
    - accident
    - person
"""

from load_data import load_data
from filter_motorcycle import filter_motorcycle_data


def merge_pipeline():
    accident, person, vehicle, = load_data()
    motorcycles_accidents = filter_motorcycle_data(vehicle)  
    #print("motorcycles_accidents:", motorcycles_accidents.shape)

    merged = motorcycles_accidents.merge(accident, on="ST_CASE", how="left")
    #print("After merging accident:", merged.shape)

    merged = merged.merge(person, on=["ST_CASE", "VEH_NO"], how="left")
    #print("After merging person:", merged.shape)

    return merged


if __name__ == "__main__":
    merged = merge_pipeline()
    merged.to_csv("data/cleaned/merged_3_accident_person_vehicle.csv", index=False)
