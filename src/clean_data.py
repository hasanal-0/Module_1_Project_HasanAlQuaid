"""
AIPI 510: Module 1 Project: Data Storytelling
- src/clean_data.py
Hasan Al-Quaid
=================================================
Cleaning up the data before any feature engineering and EDA

"""
import pandas as pd

def values_match(col1, col2):
    """
    Compare column values 

    Parameters:
        col1 (pd.Series): The first column to compare
        col2 (pd.Series): The second column to compare

    Returns:
        bool: return true if all corresponding values match, else, return false    
    """
    
    for a, b in zip(col1, col2):
        a_missing = pd.isna(a)
        b_missing = pd.isna(b)

        if a_missing and b_missing:
            continue
        elif a_missing != b_missing:
            return False
        elif a != b:
            return False

    return True


def remove_duplicate_columns(df):
    """
    Remove duplicated columns 
    
    Parameters:
        df (pd.DataFrame): The dataframe to check for duplicate columns

    Returns:
        pd.DataFrame: A copy containing only the kept columns
    
    """
    duplicate_mask = df.T.duplicated(keep="first")
    duplicate_pairs = []

    for i, is_duplicate in enumerate(duplicate_mask):
        if is_duplicate:
            for j in range(i):
                if values_match(df.iloc[:, i], df.iloc[:, j]):
                    duplicate_pairs.append((df.columns[i], df.columns[j]))
                    break

    print("Duplicate column pairs:")
    for duplicate, original in duplicate_pairs:
        print(f"{duplicate}  ----  {original}")

    print("Number of columns dropped:", duplicate_mask.sum())
    print("========================remove_duplicate_columns() Ended=======================================\n")
    return df.loc[:, ~duplicate_mask].copy()


def load_merged_data():
    """
    Load in the merged CSV

    Returns:
        pd.DataFrame: The merged accident, person, and motorcycle csv
    """
    return pd.read_csv("data/interim/merged_3_accident_person_vehicle.csv")


def report_missing_values(df):
    """
    Print the missing value counts and column names with missing data

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset

    Returns:
        None
    """
    missing_counts = df.isnull().sum()
    columns_with_missing = missing_counts[missing_counts > 0].sort_values(ascending=False)
    print("Number of columns with missing values:", len(columns_with_missing))
    print(columns_with_missing)
    print("========================report_missing_values() Ended=======================================\n")



def remove_missing_person_rows(df):
    """
    Investigate data that is missing the latter half of the files

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset.

    Returns:
        pd.DataFrame: The dataset after this cleaning step
    """
    # Looking at the data i noticed a good portion of some rows on the latter half were missing, so an investigation was done below:
    
    missing_person_rows = df[df["INJ_SEV"].isnull()]
    print(missing_person_rows.shape)
    print(missing_person_rows[["ST_CASE", "VEH_NO"]])

    person = pd.read_csv("data/raw/person.csv", low_memory=False)
    for st_case, veh_no in missing_person_rows[["ST_CASE", "VEH_NO"]].values:
        match = person[(person["ST_CASE"] == st_case) & (person["VEH_NO"] == veh_no)]
        print(f"ST_CASE {st_case}, VEH_NO {veh_no}: {len(match)} matches found in person.csv")

    # 7 state cases were not found in the person.csv, and this is what caused the data to be missing.
    # Investigation Finding: Since it is such a small subet of data that as affected, i decided to just drop those 7 rows of data,
    # Then and verify the resulting shape to make sure they got dropped
    print("df.shape:", df.shape)
    df = df.dropna(subset=["INJ_SEV"]).copy()
    print(df["INJ_SEV"].isnull().sum())
    print("df.shape after (expect 7 rows less than previous shape):", df.shape)
    print("========================remove_missing_person_rows() Ended=======================================\n")
    
    return df


def fill_missing_values(df):
    """
    Fill selected columns with the string "NAN", as all the data looks unuseful to my datastory telling and irrelevant

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset

    Returns:
        pd.DataFrame: The dataset after this cleaning step
    """
    # fill selected columns with the text "NAN"
    # a string placeholder, and not a pandas missing value
    columns_to_clean = [
        "WRK_ZONENAME",
        "PREV_SUS1NAME",
        "PREV_SUS2NAME",
        "PREV_DWINAME",
        "PREV_SUS3NAME",
        "PREV_OTHNAME",
        "PREV_SPDNAME",
        "PREV_ACCNAME",
        "TWAY_ID2",
        "MILEPTNAME",
        "VIN_12",
        "VIN_11",
        "VIN_10",
        "VIN_9",
        "VIN_8",
        "VIN_7",
        "VIN_6",
        "VIN_5"
    ]

    df[columns_to_clean] = df[columns_to_clean].fillna("NAN")
    return df


def remove_unneeded_columns(df):
    """
    This function's purpose is to drop ICFINALBODY_x and UNITTYPE. 
    
    # I made sure to print out the columns that were equal in the previous function for the case of the first two rows:
    # MCARR_ID ---- ICFINALBODY_x
    # DR_PRES ---- UNITTYPE
    # Even though they are different data that tell us different things, 
    # the first two columns were all 0s, and the last two rows were all 1s. 
    # These columns are not useful to me, and so they will just be removed entirely for simplcity.

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset

    Returns:
        pd.DataFrame: The dataset after this cleaning step
    """
    print("df.shape:", df.shape)
    df = df.drop(columns=["ICFINALBODY_x", "UNITTYPE"])
    print("Next two lines should return false if ICFINALBODY_x and UNITTYPE were removed properly:")
    print("ICFINALBODY_x" in df.columns)
    print("UNITTYPE" in df.columns)
    print("df.shape(should be reduction in 2 columns):", df.shape)
    print("========================remove_unneeded_columns() Ended=======================================\n")

    return df


def clean_numeric_columns(df):
    """
    Replace special codes and convert columns to numeric values.
    # Upon looking at the data, these columns would be useful, so i am preparing them to be used in a pairwise coorlatoin matrix in my EDA

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset

    Returns:
        pd.DataFrame: The dataset after this cleaning step
    """
    df["MOD_YEAR_x"] = df["MOD_YEAR_x"].replace([9998, 9999], pd.NA)
    df["MOD_YEAR_x"] = pd.to_numeric(df["MOD_YEAR_x"], errors="coerce")

    df["VSPD_LIM"] = df["VSPD_LIM"].replace([98, 99], pd.NA)
    df["VSPD_LIM"] = pd.to_numeric(df["VSPD_LIM"], errors="coerce")

    df["NUMOCCS"] = df["NUMOCCS"].replace(99, pd.NA)
    df["NUMOCCS"] = pd.to_numeric(df["NUMOCCS"], errors="coerce")

    df["AGE"] = df["AGE"].replace([998, 999], pd.NA)
    df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")

    df["TRAV_SP"] = df["TRAV_SP"].replace([998, 999], pd.NA)
    df["TRAV_SP"] = pd.to_numeric(df["TRAV_SP"], errors="coerce")
    df["TRAV_SP"] = df["TRAV_SP"].replace(997, 152) # 152 here is to show a speed of >=151, and not an exact measured speed.

    df["HOUR_x"] = df["HOUR_x"].replace(99, pd.NA)
    df["HOUR_x"] = pd.to_numeric(df["HOUR_x"], errors="coerce")
    return df


def save_clean_data(df):
    """
    Save the cleaned dataset to a new csv called merged_3_clean.csv

    Parameters:
        df (pd.DataFrame): The merged motorcycle dataset

    Returns:
        None
    """
    print("df.shape:", df.shape)
    df.to_csv("data/interim/merged_3_clean.csv", index=False)
    print("Saved cleaned data to: data/interim/merged_3_clean.csv")
    print("========================save_clean_data() Ended=======================================\n")



def clean_data():
    """Run each cleaning step in order and save the result.

    Returns:
        pd.DataFrame: The cleaned dataset.
    """
    with pd.option_context("display.max_rows", None):
        df = load_merged_data()
        # Display all the missing values, but only the ones that have greater than 0 missing values
        report_missing_values(df)

        df = remove_missing_person_rows(df)
        # Display all the missing values AGAIN, but only the ones that have greater than 0 missing values
        # Should see a change now that 7 rows were dropped above
        report_missing_values(df)

        #All the printd to the console form the function above
        # is not useful to my data telling story and irrelevant data, 
        # so they all simply will be filled with NaN.
        df = fill_missing_values(df)
        
        # verify it worked, it should now be 0
        print("Verify clean up worked, it should return 0 missing values")
        report_missing_values(df)

        df = remove_duplicate_columns(df)
        df = remove_unneeded_columns(df)
        df = clean_numeric_columns(df)

        save_clean_data(df)
    
    return df


if __name__ == "__main__":
    clean_data()
