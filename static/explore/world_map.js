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
    const errorBox = document.getElementById('error-box');
    if (newMarkers.length === 0) {
        // Show the error message
        errorBox.style.display = 'block';
        return;  // Stop here, don’t send the request
    } else {
        // Hide the error message if visible
        errorBox.style.display = 'none';
    }

    showSpinner()
    
    fetch('/explore/save-data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ destinations: newCoords })
    }).then(response => {
        if (response.ok) {
            newCoords = []
            hideSpinner()
        }
    })
}