# travel-breeze
A website that gives monthly weather information from the past year at a given location, built using Django.

## Libraries/Frameworks Used
- Django (Database: SQLite, 3 tables)
- Leaflet.js
- Plotly
- MeteoStat (API)
- Geopy (API)
- Tailwind

## Website Usage

### 👤 User Accounts
- When the user loads the website, they are greeted with a home page prompting them to login or register.
- Until logged in, the user cannot access any of the services provided by the website.

### 🌍 Explore Page
- Once logged in, the user can navigate to the explore page where they can select or search for any destination on the map.
- Once the user selects (by clicking on the map) or searches (by entering country and city name) a destination, a marker appears on the map.
- The user can select several destinations at a time, or reset the currently selected ones.
- After all desired destinations have been selected, the user can save these destinations which adds them to the database.
- When the user logs back in, all saved destinations will appear as markers on the map.
- Different error texts will appear if the user enters invalid data.
- Errors include entering a duplicate location, entering a location that does not exist, etc.

### 📚 Library and Weather Data
- All of the user's saved destinations will appear under the Library section.
- When a destination is clicked on, the user will be presented with a bar graph presenting weather data from the past year for each month.
- Temprature data is presented initially, but the user can select humidty, precipitation, and wind speed along with temprature.
- Below the graph, there is a list of months. The user can select a month to show more detailed data for that particular month.
- A destination can be deleted by clicking the delete button in the destination overview page

