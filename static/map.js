
// init + initial view
// TODO: setView should be user location
var map = L.map('map').setView([51.505, -0.09], 13);
// adds tile layer using open street map 
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// adds a marker
// TODOS: highlight the specific marker the user is hovering over + 
// have an onclick thing 
var marker = L.marker([51.5, -0.09]).addTo(map);
