"""
AIPI 510: Module 1 Project: Data Storytelling
- src/merge_3.py
Hasan Al-Quaid
=================================================
Merge 3 data frames into one big data frame 
    - motorcycles_accidents
    - accident
    - person
"""

from load_data import load_data
from filter_motorcycle import filter_motorcycle_data

def remove_duplicate_columns(df):
    """
    Remove duplicate columns in the three dataframes

    Parameter:
        df (pd.DataFrame): the mega dataframe, that has the  accident, person, and vehicle

    Returns:
        pd.DataFrame: the same dataset with duplicate columns dropped
    """
    duplicate_cols = df.T.duplicated()
    print("Dropping duplicate columns:", list(df.columns[duplicate_cols]))
    print("Number of columns dropped:", duplicate_cols.sum())
    
    return df.loc[:, ~duplicate_cols]

def merge_pipeline():
    accident, person, vehicle, = load_data()
    motorcycles_accidents = filter_motorcycle_data(vehicle)  
    print("motorcycles_accidents:", motorcycles_accidents.shape)

    merged = motorcycles_accidents.merge(accident, on="ST_CASE", how="left")
    print("After merging accident:", merged.shape)

    merged = merged.merge(person, on=["ST_CASE", "VEH_NO"], how="left")
    print("After merging person:", merged.shape)

    merged = remove_duplicate_columns(merged)
    print("Removed Duplicates DF:", merged.shape)

    return merged


if __name__ == "__main__":
    merged = merge_pipeline()
    merged.to_csv("data/interim/merged_3_accident_person_vehicle.csv", index=False)
