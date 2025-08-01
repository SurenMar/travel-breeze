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

def monthly_weather_avgs_hh(data):
    """
    This function finds monthly weather averages given data
    """
    # List used to store averages for each month
    monthly_data = []
    month = 1
    
    # Running temprature total, mix, and min
    temp = 0
    min_temp = data[0]['temp']
    max_temp = data[0]['temp']
    # Running humidity total
    humidity = 0
    # Running percipitation total
    precipitation = 0
    # Running wind speed total
    wind_speed = 0
    # Running weather code total
    weather_code = 0
    
    # Constants
    MONTHS_IN_YEAR = 12
    HOURS_IN_MONTH = len(data) // MONTHS_IN_YEAR
    MS_IN_KMH = 3.6
    WIND_ADJ = 10
    
    for hour, row in enumerate(data, start=1):
        # Check if a months worth of data has been read
        if hour % HOURS_IN_MONTH == 0:
            averages = {
                'month': month,
                'avg_temp': temp / HOURS_IN_MONTH,
                'max_temp': max_temp,
                'min_temp': min_temp,
                'humidity': humidity / HOURS_IN_MONTH,
                'precipitation': precipitation,
                'wind_speed': wind_speed / HOURS_IN_MONTH,
                'weather_condition': _get_weather_condition(
                    int(round(weather_code / HOURS_IN_MONTH, 0))),
                'biking_suitability': 'Suitable' if predict(
                    temp / HOURS_IN_MONTH, humidity / HOURS_IN_MONTH,
                    wind_speed / HOURS_IN_MONTH / MS_IN_KMH / WIND_ADJ, 
                    precipitation / HOURS_IN_MONTH) else 'Not Suitable',
            }
            monthly_data.append(averages)
            month += 1
            
            # Reset data
            temp = 0
            max_temp = row['temp']
            min_temp = row['temp']
            humidity = 0
            precipitation = 0
            wind_speed = 0
            weather_code = 0
        # Increment running totals
        else:
            temp += row['temp']
            max_temp = max(max_temp, row['temp'])
            min_temp = min(min_temp, row['temp'])
            humidity += row['humidity']
            precipitation += row['precipitation']
            wind_speed += row['wind_speed']
            weather_code += row['weather_code']
    
    return monthly_data