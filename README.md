# Travel Breeze

Web app built with **Django** and **Scikit-Learn** that visually provides monthly weather data and biking suitability predictions for any location.

Users can explore locations, view interactive climate visualizations, and save favorite destinations.

## Tech Stack

### ⚙️ Backend
- Django
- Scikit-Learn
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
- View detailed data for any specific month which also specifies whether that location is suitable for biking during that month.
- Easily remove destinations from your library.
  
   <img width="450" alt="Screenshot 2025-06-02 at 9 01 53 PM" src="https://github.com/user-attachments/assets/2df1e390-c6fc-4fbb-9b35-de00bb9281e1" /> <img width="450" alt="Screenshot 2025-07-31 at 10 35 15 PM" src="https://github.com/user-attachments/assets/97d739ca-7519-466b-81c9-ba8f9b60d90b" />

### ❌ Error Handling
- Graceful feedback for invalid or duplicate inputs.
- Alerts for non-existent locations or unsupported geocoding/MeteoStat results.

## ML Biking Suitability Classifier

- Fine tuned and trained a RandomForestClassifier from sklearn with **88.4%** accuracy.
- This classifier predicts whether riding a bike in a location at a certain month is ideal or not based on weather conditions.
- Initial training dataset is downloaded from UCIrving's ML Repo. Dataset name is Seoul Bike Sharing Demand.
- After processing, training dataset turned out to be about 1000 lines long with equal class distrubution

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

- Update install script to train ML model.
