"""
AIPI 510: Module 1 Project: Data Storytelling
- src/feature_engineering.py
Hasan Al-Quaid
=================================================
Engineer featrues that would give me better insight into the data.
    - US_REGIONS: The US Census Bureau diveds the United states into 4 regions(NorthEast, South, MidWest, and West)
    - SEASON: maps the months of the year to seasons
    - WEEKEND: if the day of the accident was a weekday(False) or on the weekend(True)
    - TIME_PERIOD: splits the day up into 4 periods (Morning, Afternoon, Evening, and Night)
    - SPEED_INTERVAL: takes the speed and puts them in ranges of 20. ex: 0-20mph. 20-40mph.
    - SPEEDING: indicated if the driver was speeding(True) or not (False)
    - AGE_RANGE: make age ranges based off the drivers age, in intervals of 10s.
    - DIED: wheather the person died in the crash(True) or not(False)
    - MOST_HARMFUL_EVENT: group togeather harmful events into more managable/less groups
"""
import pandas as pd

STATE_TO_REGION = {
    # Northeast
    "Connecticut": "Northeast", "Maine": "Northeast", "Massachusetts": "Northeast",
    "New Hampshire": "Northeast", "Rhode Island": "Northeast", "Vermont": "Northeast",
    "New Jersey": "Northeast", "New York": "Northeast", "Pennsylvania": "Northeast",

    # South
    "Delaware": "South", "District of Columbia": "South", "Florida": "South",
    "Georgia": "South", "Maryland": "South", "North Carolina": "South",
    "South Carolina": "South", "Virginia": "South", "West Virginia": "South",
    "Alabama": "South", "Kentucky": "South", "Mississippi": "South", "Tennessee": "South",
    "Arkansas": "South", "Louisiana": "South", "Oklahoma": "South", "Texas": "South",

    # Midwest
    "Illinois": "Midwest", "Indiana": "Midwest", "Michigan": "Midwest",
    "Ohio": "Midwest", "Wisconsin": "Midwest",
    "Iowa": "Midwest", "Kansas": "Midwest", "Minnesota": "Midwest",
    "Missouri": "Midwest", "Nebraska": "Midwest", "North Dakota": "Midwest",
    "South Dakota": "Midwest",

    # West
    "Arizona": "West", "Colorado": "West", "Idaho": "West", "Montana": "West",
    "Nevada": "West", "New Mexico": "West", "Utah": "West", "Wyoming": "West",
    "Alaska": "West", "California": "West", "Hawaii": "West",
    "Oregon": "West", "Washington": "West",
}

MONTH_TO_SEASON = {
    # Spring
    "March": "Spring", "April": "Spring", "May": "Spring",

    # Summer
    "June": "Summer", "July": "Summer", "August": "Summer",

    # Fall
    "September": "Fall", "October": "Fall", "November": "Fall",


    # Winter
    "December": "Winter", "January": "Winter", "February": "Winter",

}

def us_regions(df):
    """
    Add a 'US_REGION' column based on the state name column,
    using the official 4 region US Census Bureau classification
    (Northeast, Midwest, South, West).

    Param:
        df (pd.DataFrame): dataframe to add a new feature to.

    Returns:
        pd.DataFrame: The df with a new column: US_REGION
    """

    print("--------------------------Start #1----------------------------------------")
    print("\nBeginning shape for US_REGION:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    df["US_REGION"] = df["STATENAME_x"].map(STATE_TO_REGION)

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for US_REGION:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in US_REGION: ", df["US_REGION"].isnull().sum())
    print("--------------------------End #1----------------------------------------")

    return df

def seasons(df):
    """
    Add a 'SEASON' column based that is based on the month

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: SEASON
    """

    print("--------------------------Start #2----------------------------------------")
    print("\nBeginning shape for SEASON:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    df["SEASON"] = df["MONTHNAME_x"].map(MONTH_TO_SEASON)

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for SEASON:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in SEASON: ", df["SEASON"].isnull().sum())
    print("--------------------------End #2----------------------------------------")

    return df

def weekend(df):
    """
    Add a 'WEEKEND' column, where it is true if the crash occurred on a Saturday
    or Sunday, else, it will be false.

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: WEEKEND(bool)
    """

    print("--------------------------Start #3----------------------------------------")
    print("\nBeginning shape for WEEKEND:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    df["WEEKEND"] = df["DAY_WEEKNAME"].isin(["Saturday", "Sunday"])

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for WEEKEND:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in WEEKEND: ", df["WEEKEND"].isnull().sum())
    print("--------------------------End #3----------------------------------------")

    return df


def time_period(df):
    """
    Add a 'TIME_PERIOD' column, where it will return the period of day the crash occured in.

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: TIME_PERIOD(str)
    """
    print("--------------------------Start #4----------------------------------------")
    print("\nBeginning shape for TIME_PERIOD:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    time_period_list = []

    for hour in df["HOUR_x"]:
        if pd.isna(hour) or hour == 99:
            time_period_list.append("Unknown")
        elif hour >= 5 and hour < 12:
            time_period_list.append("Morning")
        elif hour >= 12 and hour < 17:
            time_period_list.append("Afternoon")
        elif hour >= 17 and hour < 21:
            time_period_list.append("Evening")
        else:
            time_period_list.append("Night")
    df["TIME_PERIOD"] = time_period_list

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for TIME_PERIOD:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in TIME_PERIOD: ", df["TIME_PERIOD"].isnull().sum())
    print("--------------------------End #4----------------------------------------")

    return df

def speed_interval(df):
    """
    Add a 'SPEED_INTERVAL' column, where it will return the range of speed in intervals of 20

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: SPEED_INTERVAL(str)
    """

    print("--------------------------Start #5----------------------------------------")
    print("\nBeginning shape for SPEED_INTERVAL:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    speed_interval_list = []
    for speed in df["TRAV_SP"]:
        if pd.isna(speed) or speed in [998, 999]:
            speed_interval_list.append("Unknown")
        elif speed <= 20:
            speed_interval_list.append("0-20")
        elif speed <= 40:
            speed_interval_list.append("21-40")
        elif speed <= 60:
            speed_interval_list.append("41-60")
        elif speed <= 80:
            speed_interval_list.append("61-80")
        elif speed <= 100:
            speed_interval_list.append("81-100")
        elif speed <= 120:
            speed_interval_list.append("101-120")
        else:
            speed_interval_list.append("121+")
    df["SPEED_INTERVAL"] = speed_interval_list

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for SPEED_INTERVAL:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in SPEED_INTERVAL: ", df["SPEED_INTERVAL"].isnull().sum())
    print("--------------------------End #5----------------------------------------")

    return df


def speeding(df):
    """
    Add a 'SPEEDING' column, where it will return true or false if they classified rider as speeding or not.

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: SPEEDING(bool)
    """
    print("--------------------------Start #6----------------------------------------")
    print("\nBeginning shape for SPEEDING:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    speeding_list = []
    for speed_code in df["SPEEDREL"]:
        if speed_code == 9:
            speeding_list.append(pd.NA)
        elif speed_code in [2,3,4,5]:
            speeding_list.append(True)
        elif speed_code == 0:
            speeding_list.append(False)

    df["SPEEDING"] = speeding_list

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for SPEEDING:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in SPEEDING: ", df["SPEEDING"].isnull().sum())
    print("--------------------------End #6----------------------------------------")

    return df

def age_ranges(df):
    """
    Add a 'AGE_RANGE' column, where it will return the range of age in intervals of 10

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: AGE_RANGE(str)
    """

    print("--------------------------Start #7----------------------------------------")
    print("\nBeginning shape for AGE_RANGE:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    age_ranges = []
    for age in df["AGE"]:
        if pd.isna(age) or age in [998, 999]:
            age_ranges.append("Unknown")
        elif age == 0:
            age_ranges.append("0")
        elif age <= 10:
            age_ranges.append("0 to 10")
        elif age <= 20:
            age_ranges.append("11 to 20")
        elif age <= 30:
            age_ranges.append("21 to 30")
        elif age <= 40:
            age_ranges.append("31 to 40")
        elif age <= 50:
            age_ranges.append("41 to 50")
        elif age <= 60:
            age_ranges.append("51 to 60")
        elif age <= 70:
            age_ranges.append("61 to 70")
        elif age <= 80:
            age_ranges.append("71 to 80")
        elif age <= 90:
            age_ranges.append("81 to 90")
        else:
            age_ranges.append("91+")

    df["AGE_RANGE"] = age_ranges

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for AGE_RANGE:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in AGE_RANGE: ", df["AGE_RANGE"].isnull().sum())
    print("--------------------------End #7----------------------------------------")

    return df

def died(df):
    """
    Add a 'DIED' column, where it will return true or false if the person died in the crash.

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: DIED(bool)
    """
    print("--------------------------Start #8----------------------------------------")
    print("\nBeginning shape for died:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    died_list = []
    for injury in df["INJ_SEV"]:
        if injury == 4:
            died_list.append(True)
        else:
            died_list.append(False)

    df["DIED"] = died_list

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for DIED:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in DIED: ", df["DIED"].isnull().sum())
    print("--------------------------End #8----------------------------------------")
    return df

def most_harmful_event(df):
    """
    Add a 'MOST_HARMFUL_EVENT' column, that will have groups related codes of the most events in the crash

    Param:
        df (pd.DataFrame): dataframe to add new a feature to.

    Returns:
        pd.DataFrame: The df with a new column: MOST_HARMFUL_EVENT(str)
    """
    print("--------------------------Start #9----------------------------------------")
    print("\nBeginning shape for most_harmful_event:", df.shape) 
    col_old = df.shape[1]
    row_old = df.shape[0]

    mhe_list = []
    for harmful_code in df["M_HARM"]:
        if harmful_code in [98,99]:
            mhe_list.append("Unknown")
        elif harmful_code in [1,2,3,4,51,6,44,7,16,72,5]:
            mhe_list.append("Non-collision")
        elif harmful_code in [12,54,55]:
            mhe_list.append("Collision with Motor Vehicle")
        elif harmful_code in [8,9,10,74,11,49,18,15,14,45,73,91]:
            mhe_list.append("Collision with moving object/animal")
        elif harmful_code in [17,19,58,20,50,21,23,24,52,25,57,26,59,46,30,31,32,33,34,35,38,39,40,41,42,48,53,43,93]:
            mhe_list.append("Collision with fixed object")
        else:
            mhe_list.append(False)

    df["MOST_HARMFUL_EVENT"] = mhe_list

    col_new = df.shape[1]
    row_new = df.shape[0]
    print("Ending shape for most_harmful_event:", df.shape)
    print("\nVerification:")
    print(f"Rows are the same as old {row_old}, new {row_new}: {row_old == row_new}")
    print(f"Col are NOT the same as old {col_old}, new {col_new}: {col_old == col_new}")
    print(f"Is col now greater by 1 from old column number: {(col_old + 1) == col_new}")
    print("Check for any null values in most_harmful_event: ", df["MOST_HARMFUL_EVENT"].isnull().sum())
    print("--------------------------End #9----------------------------------------")

    return df

def feature_engineering(df):
    """
    Call all functions that will add new featrues one by one.

    Param:
        df (pd.DataFrame): dataframe to add new features to.

    Returns:
        pd.DataFrame: The df with new columns
    """
    us_regions(df)
    seasons(df)
    weekend(df)
    time_period(df)
    speed_interval(df)
    speeding(df)
    age_ranges(df)
    died(df)
    most_harmful_event(df)

    return df

if __name__ == "__main__":

    merge_3_df = pd.read_csv("data/interim/merged_3_clean.csv")

    print("\nOriginal Shape of merged_3_clean: ", merge_3_df.shape)
    original_columns = set(merge_3_df.columns)
    merge_3_df = feature_engineering(merge_3_df)
    new_columns = set(merge_3_df.columns) - original_columns

    print("\nShape after feature engineering: ", merge_3_df.shape)  
    print("\nNew columns added:", new_columns)

    merge_3_df.to_csv("data/processed/final_motorcycles.csv", index=False)