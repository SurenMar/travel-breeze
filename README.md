# Travel Breeze

Dockerized web app built with **Django** and **scikit-learn** that visually provides monthly weather data and biking suitability predictions for any location.

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

### 🛠️ DevOps
- Docker
- Bash (install script)

### 🧪 Testing
- Pytest

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

- Fine tuned and trained a RandomForestClassifier from scikit-learn with **91.8%** accuracy.
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

## 🚀 Installation

### Via Docker
1. Download **Docker** for your OS.
2. Start the **Docker Engine** in order to type docker commands.
3. Pull the image for this web app: `docker pull surenmardock/tb-image`.
4. Run a container for the image: `docker run -d -p 8000:8000 surenmardock/tb-image`.
5. If your port 8000 is occupied, choose a different host port. If not, move on.
6. Go to `http://localhost:8000` and start exploring!
7. To end the session, type `docker stop surenmardock/tb-image`.

### Via Auto Install Script (Mac + Ubuntu users only)
1. Download the file `tb_install.sh` into a folder where you like the application to be.
2. Make the script executable: `chmod +x tb_install.sh`.
3. Run the file: `./tb_install.sh`.
4. If you are missing any required programs, the script will notify you. Download these programs and re-run `tb_install.sh`.
5. The script will download all libraries and framewords needed from the `requirements.txt` file
6. Follow the steps provided once the script finishes.
7. Type in the provided web address into your web browser and start exploring!
8. To end the session, press `control` + `C`.

### Manually:
1. Download a ZIP file of **travel-breeze**.
2. Unzip the file.
3. The files will be in a folder called `travel-breeze-main`.
4. Go into this file and ensure you have python and pip installed (installation steps vary depending on OS).
5. Install the required libraries and frameworks from the `requirements.txt` file (installation steps vary depending on OS).
6. Make `tb_run.sh` executable: `chmod +x tb_run.sh`.
7. Run the executable and type in the provided web address into your web browser and start exploring!
8. To end the session, press `control` + `C`.

## ✅ To-Do List

*empty...*