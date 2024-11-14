import pandas as pd

def calculate_delays(df):
    # Create a new column for total delays
    # df['TOTAL_DELAY'] = df['DEP_DELAY'] + df['ARR_DELAY']
    df['ttl_delay'] = df['arr_delay'] + df['carrier_delay'] + df['weather_delay']
    + df['nas_delay'] + df['security_delay'] + df['late_aircraft_delay']

    return df

def average_delay_by_airline(df):
    return df.groupby('AIRLINE')['arr_delay', 'carrier_delay', 'weather_delay',
                                  'nas_delay', 'security_delay','late_aircraft_delay'].mean()