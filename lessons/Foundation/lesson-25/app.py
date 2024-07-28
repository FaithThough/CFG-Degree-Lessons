from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability



app = Flask(__name__)
@app.route('/availability/<date>')
def get_bookings(date):
    res = get_all_booking_availability(date)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# Example URL to access this route:
# http://127.0.0.1:5001/availability/2020-12-16

# Route to add a new booking
@app.route('/booking', methods=['PUT'])
def book_appt():
    # Get the booking data from the request body in JSON format
    booking = request.get_json()
    # Call the function to add the booking with the provided data
    add_booking(
        _date=booking['_date'],
        teamMember=booking['teamMember'],
        time=booking['time'],
        customer=booking['customer'],
    )
    # Return the booking data as a confirmation response
    return booking

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    # Enable debug mode and set the port to 5001
    app.run(debug=True, port=5001)