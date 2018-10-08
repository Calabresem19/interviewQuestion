import json
import requests
import pprint
import geopy.distance
import mysql.connector
import operator
from multiprocessing import Pool


def process_request(form_data): 
    leave_date =  form_data['LeaveDate']
    return_date = form_data['returnDate']
    to_airport= form_data['toAirport']
    from_airport = form_data['fromAirport']

    # Makes API Call to grab JSON from API and store in Python DICT    
    #api_date_json = requests.get('http://asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146@flightxml.flightaware.com/json/FlightXML2/AirlineFlightSchedules?startDate=1545415916&endDate=1545761516&origin=JFK&destination=PIT&howMany=15')


    mydb = mysql.connector.connect(
        host="test.travelwits.com",
        user="test",
        passwd="@test!@#",
        database="test"

    )



    mycursor = mydb.cursor()

    mycursor.execute("select Latitude , Longitude, IATA  from airports")

    myresult = mycursor.fetchall()

    airport_with_long_and_lat_dict = {}; 

    for x in myresult:
        airport_with_long_and_lat_dict[x[2]] = {"Latitude":x[0], "Longitude":x[1]}
#        print x[2]

    ten_closest_cities_from_city = {}
    ten_closest_cities_to_city = {}

    for key, value in airport_with_long_and_lat_dict.items():

        # coords 1 and 2 deal with from city 
        coords_1 = (airport_with_long_and_lat_dict[from_airport]["Latitude"], airport_with_long_and_lat_dict[from_airport]["Longitude"])
        coords_2 = (airport_with_long_and_lat_dict[key]["Latitude"], airport_with_long_and_lat_dict[key]["Longitude"])
        
        ten_closest_cities_from_city[key] = geopy.distance.vincenty(coords_1, coords_2).miles

        # coords 3 and 4 deal with to city 

        coords_3 = (airport_with_long_and_lat_dict[to_airport]["Latitude"], airport_with_long_and_lat_dict[to_airport]["Longitude"])
        coords_4 = (airport_with_long_and_lat_dict[key]["Latitude"], airport_with_long_and_lat_dict[key]["Longitude"])

        ten_closest_cities_to_city[key] = geopy.distance.vincenty(coords_3, coords_4).miles
   

#        print "test"





    sorted_ten_closest_cities_from_city =  sorted(ten_closest_cities_from_city.items(), key=operator.itemgetter(1))[:10]
    sorted_ten_closest_cities_to_city =  sorted(ten_closest_cities_to_city.items(), key=operator.itemgetter(1))[:10]
#    print sorted(ten_closest_cities_to_city.items())
#    print sorted_ten_closest_cities_from_city
#    print sorted_ten_closest_cities_to_city


    list_of_flights = [] 




#    print requests.get('http://asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146@flightxml.flightaware.com/json/FlightXML2/AirlineFlightSchedules?startDate='+leave_date+'&endDate='+return_date+'&origin=PIT&destination='+to_airport+'&howMany=15')

    print sorted_ten_closest_cities_to_city
    print sorted_ten_closest_cities_from_city 

    for x in sorted_ten_closest_cities_from_city:
        for y in sorted_ten_closest_cities_to_city:


            url = 'http://asafonov:2f34fc7f817274efd4ecd5a51b2ffd5817b08146@flightxml.flightaware.com/json/FlightXML2/AirlineFlightSchedules?startDate='+leave_date+'&endDate='+return_date+'&origin='+x[0]+'&destination='+y[0]+'&howMany=15'
            print url


#            p = Pool(10)

            api_date_json = requests.get(url)
        
            print x
            print y

            data = api_date_json.json()
#            print data
            for w in data['AirlineFlightSchedulesResult']['data']:
                list_of_flights.append(w)

#    for x in list_of_flights:
#        print x  



    

    
        
 

         


