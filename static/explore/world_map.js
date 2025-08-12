// Create map variable at starting coords
var map = L.map('map').setView([51.505, -0.09], 2);
map.setMaxBounds(map.getBounds());

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15,
    minZoom: 2,
    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Display each destinations_json coord from our database onto the map
let destinations = JSON.parse(document.getElementById('destinations_json').textContent);
destinations.forEach(destination => {
    L.marker([destination.latitude, destination.longitude]).addTo(map);
});

// Add coords and markers to a list on each user click
let newCoords = [];
let newMarkers = [];
map.on('click', (event) => {
    let lat = event.latlng.lat;
    let lon = event.latlng.lng;
    newMarkers.push(L.marker([lat, lon]).addTo(map));
    newCoords.push({ latitude: lat, longitude: lon });
});

// A function that resets all current markers (and coordinates of those markers)
function resetMarkers() {
    newCoords = [];
    newMarkers.forEach(marker => {
        marker.remove();
    });
    newMarkers = [];
}

// Several functions that handle saving/adding indicators
function showSaveSpinner() {
    document.getElementById('saving-indicator').style.display = 'block';
}

function hideSaveSpinner() {
    document.getElementById('saving-indicator').style.display = 'none';
}

function showAddSpinner() {
    document.getElementById('adding-indicator').style.display = 'block';
}

function hideAddSpinner() {
    document.getElementById('adding-indicator').style.display = 'none';
}

// Gets cookie (primarily used for csrf)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Intercept location-form submission
document.getElementById('enter-location-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission
    addLocation();
});

// Function that adds users typed solution to the map
function addLocation() {
    const errorDuplicate = document.getElementById('error-duplicate');
    const errorLocation = document.getElementById('error-location');
    const errorNoDest = document.getElementById('error-no-dest');
    const errorNoStations = document.getElementById('error-no-stations');
    const countryInput = document.querySelector('input[name="country"]').value;
    const cityInput = document.querySelector('input[name="city"]').value;

    errorDuplicate.style.display = 'none';
    errorLocation.style.display = 'none';
    errorNoDest.style.display = 'none';
    errorNoStations.style.display = 'none';

    showAddSpinner();

    // Use FormData to mimic a traditional form submission
    const formData = new FormData();
    formData.append('save_location', 'true');
    formData.append('country', countryInput);
    formData.append('city', cityInput);
    formData.append('enter_location', 'true'); // This is because we check for 'enter_location' in view

    // Gets handled in save_data's form processing
    fetch('/explore/save-data/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData // Send as FormData to match application/x-www-form-urlencoded
    })
    .then(response => {
        hideAddSpinner();
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    // Adds user's entered location to the map or displays error
    .then(data => {
        if (data.location_error) {
            errorLocation.style.display = 'block';
        } else if (data.duplicate_error) {
            errorDuplicate.style.display = 'block';
        } else if (data.lat && data.lon) {
            newMarkers.push(L.marker([data.lat, data.lon]).addTo(map));
            newCoords.push({ latitude: data.lat, longitude: data.lon });
        }
    })
    .catch(error => {
        console.error(error);
    })
}

// Function that sends selected locations to save_data view
function saveLocation() {
    const errorDuplicate = document.getElementById('error-duplicate');
    const errorLocation = document.getElementById('error-location');
    const errorNoDest = document.getElementById('error-no-dest');
    const errorNoStations = document.getElementById('error-no-stations');

    errorDuplicate.style.display = 'none';
    errorLocation.style.display = 'none';
    errorNoDest.style.display = 'none';
    errorNoStations.style.display = 'none';
    
    // Check if user has clicked on the map
    if (newMarkers.length === 0) {
        errorNoDest.style.display = 'block';
        return;
    } else {
        errorNoDest.style.display = 'none';
    }

    showSaveSpinner()
    
    fetch('/explore/save-data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ destinations: newCoords })
    // Process response and display any errors if needed
    })
    .then(response => {
        newCoords = []
        hideSaveSpinner()
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json()
    })
    .then(data => {
        // Remove markers of any invalid destination coordinates
        if (data.invalid_dests && data.invalid_dests.length > 0) {
            data.invalid_dests.forEach(invalid => {
                for (let i = newMarkers.length - 1; i >= 0; i--) {
                    const marker = newMarkers[i];
                    const markerLatLng = marker.getLatLng();
                    if (Math.abs(markerLatLng.lat - invalid.latitude) < 1e-6 &&
                        Math.abs(markerLatLng.lng - invalid.longitude) < 1e-6) {
                        marker.remove();
                        newMarkers.splice(i, 1);
                        newCoords.splice(i, 1);
                    }
                }
            });
            errorNoStations.style.display = 'block';
        } else {
            errorNoStations.style.display = 'none';
        }
        newMarkers = []
    })
    .catch(error => {
        console.error(error);
    })
}