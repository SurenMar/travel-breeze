# Travel Breeze

Web application built with **Django** that visually provides historical monthly weather data for any destination around the world.

 Users can explore locations, view interactive climate visualizations, and save favorite destinations.

## Tech Stack

### ⚙️ Backend
- Django
- SQLite
- Pandas
- MeteoStat API (weather data)
- Geopy / Nominatim API (location data)
- Plotly (data visualization)

### 🎨 Frontend
- HTML / Django Templates  
- Tailwind CSS
- JavaScript
- Leaflet.js (interactive maps)

## Features

### 👤 User Authentication
- Secure registration and login system using Django's built-in authentication.
- All core features are gated behind login to ensure a personalized experience.

### 🌍 Interactive Explore Page
- Browse a world map and search destinations by city and country.
- Add markers by clicking on the map or by entering a location manually.
- Select and save multiple destinations, which persist as markers on the map across sessions.
- View all saved locations when logged back in.

   <img width="450" alt="Screenshot 2025-06-02 at 9 00 22 PM" src="https://github.com/user-attachments/assets/6aa09b80-919b-462e-9b7a-cdedc28b3cbc" />

### 📚 Destination Library
- Displays all of the user’s saved destinations.
- Click on a location to view a detailed climate summary with an interactive bar graph.
- Toggle between weather metrics: **Temperature**, **Humidity**, **Precipitation**, and **Wind Speed**.
- View detailed data for any specific month.
- Easily remove destinations from your library.
  
   <img width="450" alt="Screenshot 2025-06-02 at 9 01 53 PM" src="https://github.com/user-attachments/assets/2df1e390-c6fc-4fbb-9b35-de00bb9281e1" /> <img width="450" alt="Screenshot 2025-06-02 at 9 02 21 PM" src="https://github.com/user-attachments/assets/b0bbec35-b6dc-4d8a-9212-602c3909bc16" />


### ❌ Error Handling
- Graceful feedback for invalid or duplicate inputs.
- Alerts for non-existent locations or unsupported geocoding/MeteoStat results.

## APIs and Data Processing

### 🌦️ Weather Data (MeteoStat & Pandas)
- Retrieves past year’s **hourly weather data** per location.
- Parses and calculates **monthly averages** for key metrics.
- Stores aggregated data in the database to optimize performance.

### 📍 Location Data (Geopy + Nominatim)
- Converts latitude/longitude to human-readable locations and vice versa.
- Supports both manual input and map-based selection via Leaflet.js.

### 📊 Visualization (Plotly)
- Weather data is rendered as interactive bar charts.
- Clean, responsive, and informative graphical representation of climate data.

## Database Schema (3 Tables)

- **User**: Inherits Django’s built-in user model.
- **Destination**: Stores location names, coordinates, and a foreign key to the user.
- **MonthlyWeather**: Contains 12 records per destination (one for each month) with weather averages, and a foreign key to destination.

## 🎨 Frontend Overview

- **HTML / Django Templates**: Utilizes template inheritance, dynamic content rendering, and Django forms.
- **Tailwind CSS**: Provides modern styling with responsive layouts.
- **JavaScript**: Handles map and button functionality with dynamic communication with Django views.
- **Leaflet.js**: Renders the world map and handles marker logic.

## 📌 Notes

- The frontend styling was initially generated using GenAI and then refined manually.
- This website as not been deployed.

## 🚀 Installation (via Bash)

### For Mac and Linux (Ubuntu) Users Only:
   1. Download the file `tb_install.sh` into a folder where you like the application to be.
   2. Make the script executable: `chmod +x tb_install.sh`.
   3. Run the file: `./tb_install.sh`.
   4. If you are missing any required programs, the script will notify you. Download these programs and re-run `tb_install.sh`.
   5. The script will download all libraries and framewords needed from the `requirements.txt` file
   6. Follow the steps provided once the script finishes.
   7. Type in the provided web address into your web browser and start exploring!

### For All Users:
   1. Download a ZIP file of **travel-breeze**.
   2. Unzip the file.
   3. The files will be in a folder called `travel-breeze-main`.
   4. Go into this file and ensure you have python and pip installed (installation steps vary depending on OS).
   5. Install the required libraries and frameworks from the `requirements.txt` file (installation steps vary depending on OS).
   6. Make `tb_run.sh` executable: `chmod +x tb_run.sh`.
   7. Run the executable and type in the provided web address into your web browser and start exploring!

## ✅ To-Do List

- Add ML model that classifies each of the destinations months as having suitable wether for biking or not.
  
   1. Add biking_suitability attribute to MonthlyWeather label.
   2. Read hourly biking dataset through ucimlrepo API and fetch hourly dataset.
   3. Remove rows for which the non-weather feature heavily dictates biking outcome (weekends, midnight hours, etc).
   4. Filter features and keep only weather information.
   5. Add labels 1, 0 to each row by averaging the total bicycle counts and analyzing the std dev of the counts of each row.
   6. Train SGDClassifier model with filtered data (SGDClassifier is used because it handles overfitting and provides online learning).
   7. Implement model into web app and predict suitability for eahc month each time a user selects a destination.
   8. After destination is selected, the user will be asked if they would ride a bicycle at their selected destination.
   9. Without storing in DB, use this information for online learning, and store the new prediction for the destination in DB.
   10. Add "Biking Suitability" to the Plotly graph and each months weather page.
