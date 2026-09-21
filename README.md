# When Motorcycle Crashes Turn Fatal: Exploring the People and Conditions Involved

**AIPI 510 — Module 1: Data Storytelling**  
**Author: Hasan Al-Quaid**

## Project Overview

This project explores the circumstances of motorcycle-involved fatal crashes and the outcomes of the people involved. It combines accident, vehicle, and person records to examine patterns in age, speeding, helmet use, weather, lighting, location, and harmful events.

The main question is: **What conditions are associated with recorded deaths among motorcycle occupants involved in fatal crashes?**

## Dataset Description and Citation:

The data came from the **Fatality Analysis Reporting System (FARS)**, maintained by the National Highway Traffic Safety Administration (NHTSA). The FARS data is described as the "nationwide census providing NHTSA, Congress and the American public yearly data regarding fatal injuries suffered in motor vehicle traffic crashes."[FARS Data](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars).


The data I used for this project can be found here: [FARS 2024 Data](https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2024/National/).

- Navigate to the link listed, and download the `FARS2024NationalCSV.zip`
- Once that is downloaded, unzip and find the following:

| Files | 
| --- |
| `accident.csv` |
| `vehicle.csv` | 
| `person.csv` |

**Dataset citation:** 

National Highway Traffic Safety Administration, 2026. *Fatality Analysis Reporting System (FARS)* ,Sep 2026. U.S. Department of Transportation. [FARS data downloads](https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2024/National/).

**Documentaion:**

Navigate to [Crsh Stats](https://crashstats.nhtsa.dot.gov/#!/DocumentTypeList/23), and download the following file to use to interpert the data in the CSVs.

| Files | DOT HS # |
| --- | --- |
| `Fatality Analysis Reporting System Analytical User’s Manual, 1975-2024` | 813794 |
| `2024 FARS/CRSS Coding and Validation Manual` | 813798 |

## Project organization

```
Module_1_Project_HasanAlQuaid/
├── data/
│   ├── raw/
│   │   ├── accident.csv
│   │   ├── person.csv
│   │   └── vehicle.csv
│   ├── interim/
│   │   ├── motorcycles_accidents.csv
│   │   ├── merged_3_accident_person_vehicle.csv
│   │   └── merged_3_clean.csv
│   └── processed/
│       └── final_motorcycles.csv
├── src/
│   ├── load_data.py
│   ├── filter_motorcycle.py
│   ├── merge_3.py
│   └── feature_engineering.py
├── notebooks/
│   ├── clean_data.ipynb
│   ├── EDA.ipynb
│   └── final_visualizations.ipynb
└── README.md
```

### Data — `data/`

- **`raw/`** — Original source datasets:
  - `accident.csv`
  - `person.csv`
  - `vehicle.csv`

- **`interim/`** — Filtered, merged, and cleaned intermediate datasets:
  - `motorcycles_accidents.csv`
  - `merged_3_accident_person_vehicle.csv`
  - `merged_3_clean.csv`

- **`processed/`** — Final dataset used for analysis and visualization:
  - `final_motorcycles.csv`

### Python scripts — `src/`

- **`load_data.py`** — Loads the three source datasets
- **`filter_motorcycle.py`** — Selects only motorcycle related records
- **`merge_3.py`** — Merges the three csvs into one dataframe
- **`feature_engineering.py`** — Creates new features and final CSV 

### Notebooks — `notebooks/`

- **`clean_data.ipynb`** — Cleans the merged data and handles missing values and special codes.
- **`EDA.ipynb`** — Exploratory Data Analysis
- **`final_visualizations.ipynb`** — Creates clean visualizations and findings.

## Reproducing My Analysis

## Install
- Install the following if you do not have:
    - import pandas as pd
    - import os
    - import pandas as pd
    - import matplotlib.pyplot as plt
    - import seaborn as sns
    - import textwrap

## Usage

Run the data pipeline in the following processing order:
1. `load_data.py`
2. `filter_motorcycle.py`
    ``` 
    Outputs: /interim/motorcycles_accidents.csv
    ```
3. `merge_3.py`
    ``` 
    Outputs: interim/merged_3_accident_person_vehicle.csv
    ```
4. `clean_data.ipynb`
    ``` 
    Outputs: /interim/merged_3_clean.csv
    ```
5. `feature_engineering.py`
    ``` 
    Outputs: /processed/final_motorcycles.csv
    ```
6. `EDA.ipynb`
7. `final_visualizations.ipynb`

Plots appear below their corresponding code cells. Save the notebooks after running them to preserve the outputs.