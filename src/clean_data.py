import pandas as pd 

def clean_flight_data(filePath):
    df = pd.read_csv(filePath)
    print(df)
    
    # Drop rows with missing values
    df = df.dropna()
    print(df)

    # Convert time columns to datetime
    # df['DEP_TIME'] = pd.to_datetime(df['DEP_TIME'], errors='coerce')
    # df['ARR_TIME'] = pd.to_datetime(df['ARR_TIME'], errors='coerce')

    return df
