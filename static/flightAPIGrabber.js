function grabFlight() {
    var xhttp = new XMLHttpRequest();

    //xhttp.open("GET","http://asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146@flightxml.flightaware.com/json/FlightXML2/AirlineFlightSchedules?startDate=1545415916&endDate=1545761516&origin=JFK&destination=PIT&howMany=15", true);
    xhttp.open("GET","http://asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146@flightxml.flightaware.com/json/FlightXML2/AirlineFlightSchedules?startDate=1545415916&endDate=1545761516&origin=JFK&destination=PIT&howMany=15", true);
    
//    xhttp.setRequestHeader("Authorization", "Basic " + btoa("asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146"));
    
//    xhttp.setRequestHeader('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS');
  // xhttp.setRequestHeader("Content-Type", "text/xml");
   xhttp.withCredentials = true; 
//    xhttp.setRequestHeader("Authorization","asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146")
    document.getElementById("flightList").innerHTML = xhttp.send()

    console.log("got to this");

}

