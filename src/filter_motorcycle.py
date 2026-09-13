"""
AIPI 510: Module 1 Project: Data Storytelling
- src/filter_motorcycle.py
=================================================
Filters the loaded FARS data to include only motorcycle-related records.
"""

from load_data import load_data

def filter_motorcycle_data():
    """
    Load all raw FARS data and filter the vehicle data down to
    motorcycle-type vehicles only.

    Uses BODY_TYP codes 80-89, which cover motorcycles, mopeds,
    scooters, off-road motorcycles, three-wheel motorcycles, etc.
    per the FARS data dictionary.

    Returns:
        pd.DataFrame: only the vehicle rows where BODY_TYP is a
        motorcycle code.
    """
    accident, drugs, factor, person, safetyeq, vehicle, vision, weather = load_data()
    
    motorcycle_codes = list(range(80, 90))
    motorcycles_accidents = vehicle[vehicle["BODY_TYP"].isin(motorcycle_codes)]
    
    return motorcycles_accidents

if __name__ == "__main__":
    motorcycles_accidents = filter_motorcycle_data()
    
    # Save the filtered motorcycle accidents to a csv
    #motorcycles_accidents.to_csv("data/cleaned/motorcycles_accidents.csv", index=False)