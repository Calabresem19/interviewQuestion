from flask import Flask
from flask import render_template, url_for, request

from flightGrabber import process_request


app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True


with app.test_request_context():
    url_for('static', filename='flightAPIGrabber.js')
    url_for('static', filename='styles.css')



@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route('/getInformation', methods=['POST'])
def get_info():
    

#    print request.form

    list_of_flights = process_request(request.form)       
    
    #print list_of_flights
    print list_of_flights[0]
    print type(list_of_flights)

    return render_template('working.html', list_of_flights=list_of_flights)

