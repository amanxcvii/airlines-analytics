import pandas as pd

def calculate_delays(df):
    # Create a new column for total delays
    df['ttl_delay'] = df['atc_delay'] + df['operational_delay'] + df['weather_delay']
    + df['technical_delay'] + df['security_delay'] 
    return df

def average_delay(df):
    return df.groupby('Airline')['ttl_delay'].mean().round(2).reset_index()

def clean_flight_data(filePath):
    df = pd.read_csv(filePath)
    print(df)
    
    # Drop rows with missing values
    df = df.dropna()
    print(df)

    # Convert time columns to datetime
    df['Scheduled Departure Time'] = pd.to_datetime(df['Scheduled Departure Time'], errors='coerce')
    df['Actual Departure Time'] = pd.to_datetime(df['Actual Departure Time'], errors='coerce')

    return df