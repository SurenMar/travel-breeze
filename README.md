# 🌬️ Travel Breeze

**Travel Breeze** is a web application built with Django that provides historical monthly weather data for destinations around the world. Users can explore locations, view interactive climate visualizations, and save favorite places—all through a clean and intuitive interface.

## Tech Stack

**Backend:**
- Django
- SQLite
- MeteoStat API (weather data)
- Geopy / Nominatim API (location data)
- Plotly (data visualization)

**Frontend:**
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

### 📚 Destination Library
- Displays all of the user’s saved destinations.
- Click on a location to view a detailed climate summary with an interactive bar graph.
- Toggle between weather metrics: **Temperature**, **Humidity**, **Precipitation**, and **Wind Speed**.
- View detailed data for any specific month.
- Easily remove destinations from your library.

### ❌ Smart Error Handling
- Graceful feedback for invalid or duplicate inputs.
- Alerts for non-existent locations or unsupported geocoding/MeteoStat results.

## APIs and Data Handling

### 🌦️ Weather Data (MeteoStat)
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

---

## 🎨 Frontend Overview

- **HTML / Django Templates**: Utilizes template inheritance, dynamic content rendering, and Django forms.
- **Tailwind CSS**: Provides modern utility-first styling with responsive layouts.
- **JavaScript**: Handles interactive map logic and dynamic communication with Django views (AJAX-style updates).
- **Leaflet.js**: Renders the world map and handles marker logic.
- **Plotly.js**: Displays dynamic charts for monthly weather trends.

---

## 📌 Notes

- The frontend design and styling were initially generated using GenAI and then refined manually.
- The project prioritizes clean UI/UX, performance, and modularity in both frontend and backend development.
