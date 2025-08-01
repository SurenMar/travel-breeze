"""
Stores processor functions for all types of data
"""

from library.ml.ml_models.bike_clf import predict

def _get_weather_condition(weather_code):
    """
    A helper function to lookup the weather condition
    """
    weather_conditions = [
        "Clear",                     # 0
        "Fair",                      # 1
        "Partly cloudy",             # 2
        "Cloudy",                    # 3
        "Overcast",                  # 4
        "Fog",                       # 5
        "Freezing fog",              # 6
        "Light rain",                # 7
        "Rain",                      # 8
        "Heavy rain",                # 9
        "Freezing rain",             # 10
        "Heavy freezing rain",       # 11
        "Sleet",                     # 12
        "Heavy sleet",               # 13
        "Light snow",                # 14
        "Snow",                      # 15
        "Heavy snow",                # 16
        "Snow grains",               # 17
        "Rain showers",              # 18
        "Heavy rain showers",        # 19
        "Snow showers",              # 20
        "Heavy snow showers",        # 21
        "Thunderstorm",              # 22
        "Thunderstorm with hail"     # 23
    ]
    return weather_conditions[weather_code]

def clean_weather_data(weather_df):
    # Drop unnecessary columns and missing values
    weather_df = weather_df.drop(
        columns=['station', 'time', 'dwpt', 'snow',
        'wdir', 'wpgt', 'pres', 'tsun'], errors='ignore',
    ).dropna(axis=0)
    return weather_df

def process_weather_avgs(weather_df):
    """Returns the monthly info as a list of dicts"""

    # Create a list of dictionaries for all monthly weather info
    monthly_weather = []
    MS_IN_KMH = 3.6     # m/s in km/h
    WIND_ADJ = 10       # wind speed adjustment factor
    MONTHS_IN_YEAR = 12
    HOURS_IN_MONTH = len(weather_df) // MONTHS_IN_YEAR

    for m in range(12):
        # Splice weather_df for each month
        month_df = weather_df[m * HOURS_IN_MONTH : (m+1) * HOURS_IN_MONTH]

        monthly_weather.append({
            'month': m + 1,
            'avg_temp': float(month_df['temp'].mean()),
            'max_temp': float(month_df['temp'].max()),
            'min_temp': float(month_df['temp'].min()),
            'humidity': float(month_df['rhum'].mean()),
            'precipitation': float(month_df['prcp'].sum()),
            'wind_speed': float(month_df['wspd'].mean()),
            'weather_condition': _get_weather_condition(
                int(round(float(month_df['coco'].mean()), 0))),
            'biking_suitability': 'Suitable' if predict(
                float(month_df['temp'].mean()), 
                float(month_df['rhum'].mean()),
                float(month_df['wspd'].mean()) / MS_IN_KMH / WIND_ADJ, 
                float(month_df['prcp'].mean())) else 'Not Suitable',
        })
    return monthly_weather
