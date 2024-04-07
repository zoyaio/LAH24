

// gets current position
var position = navigator.geolocation.getCurrentPosition(showPosition); 

// inits map with current position of user
function showPosition(pos) {
    var map = L.map('map').setView([pos.coords.latitude, pos.coords.longitude], 13);
    // adds tile layer using open street map 
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
  }


    // have an onclick thing 
  var marker = L.marker([51.5, -0.09]).addTo(map);
