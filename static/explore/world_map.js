// Create leafletjs map and set bounds
var map = L.map('map').setView([51.505, -0.09], 2);
map.setMaxBounds(map.getBounds());

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15,
    minZoom: 2,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Add marker for each destination
let destinations = JSON.parse(document.getElementById('destinations_json').textContent)
destinations.forEach(destination => {
    L.marker([destination.latitude, destination.longitude]).addTo(map)
})

// Save lat and lon values upon click to markers list
let newCoords = []
let newMarkers = []
map.on('click', (event) => {
    let lat = event.latlng.lat
    let lon = event.latlng.lng
    newMarkers.push(L.marker([lat, lon]).addTo(map))
    newCoords.push({ latitude: lat, longitude: lon })
})

function resetMarkers() {
    newCoords = []
    newMarkers.forEach(marker => {
        marker.remove()
    })
    newMarkers = []
}

function showSpinner() {
    document.getElementById('saving-indicator').style.display = 'block';
}

function hideSpinner() {
    document.getElementById('saving-indicator').style.display = 'none';
}

function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}        

function sendMarkers() {
    const errorNoDest = document.getElementById('error-no-dest');
    const errorNoStations = document.getElementById('error-no-stations')
    errorNoStations.style.display = 'none'
    // Check if user has clicked on the map
    if (newMarkers.length === 0) {
        errorNoDest.style.display = 'block';
        return;
    } else {
        errorNoDest.style.display = 'none';
    }

    showSpinner()
    
    fetch('/explore/save-data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ destinations: newCoords })
    // Process response and display any errors if needed
    }).then(response => {
        newCoords = []
        hideSpinner()
        return response.json()
    }).then(data => {
        // Remove markers of any invalid destination coordinates
        if (data.invalid_dests && data.invalid_dests.length > 0) {
            console.log('Invalid destinations:', data.invalid_dests);
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
}