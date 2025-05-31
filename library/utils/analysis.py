"""
This file contains functions which perform data analysis on parsed data
"""

def monthly_weather_avgs(data):
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
                'weather_code': weather_code / HOURS_IN_MONTH,
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