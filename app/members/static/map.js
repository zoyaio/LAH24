

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


  // adds a marker
// TODOS: highlight the specific marker the user is hovering over + 
// have an onclick thing 
// have an onclick thing 

  console.log("{{eureka_elms|escapejs}}");
  var data = JSON.parse("{{eureka_elms|escapejs}}"); 
  console.log(data);
  const markers = []; 
  for (let i = 0; i < data.length; i++) {
    markers[i] = data[i];
  }
  console.log(markers);

  var marker = L.marker([51.5, -0.09]).addTo(map);
  
