from flask import Flask
from flask import render_template, url_for, request

from flightGrabber import process_request


app = Flask(__name__)


with app.test_request_context():
    url_for('static', filename='flightAPIGrabber.js')



@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route('/getInformation', methods=['POST'])
def get_info():
    

#    print request.form

    process_request(request.form)       


    return render_template('working.html')

