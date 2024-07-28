# Import necessary modules
import requests
import json

# Function to get availability by date from the server


def get_availability_by_date(date):
    # Send a GET request to the server to get availability for the specified date
    result = requests.get(
        'http://127.0.0.1:5001/availability/{}'.format(date),
        headers={'content-type': 'application/json'}
    )
    # Return the result as a JSON object
    return result.json()

# Function to add a new booking


def add_new_booking(date, stylist, time, customer):
    # Create a dictionary with the booking details
    booking = {
        "_date": date,
        "teamMember": stylist,
        "time": time,
        "customer": customer,
    }

    # Send a PUT request to the server to add the booking
    result = requests.put(
        'http://127.0.0.1:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )

    # Return the result as a JSON object
    return result.json()

# Function to display availability in a readable format


def display_availability(records):
    # Print the column headers
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        'NAME', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'))
    print('-' * 105)

    # Print each record in the availability data
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            item['name'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17'], item['17-18']
        ))

# Main function to run the application


def run():
    print('############################')
    print('Hello, welcome to our salon')
    print('############################')
    print()
    # Prompt the user to enter the date for the appointment
    date = input(
        'What date would you like to book your appointment for (YYYY-MM-DD): ')
    print()
    # Get availability for the specified date
    slots = get_availability_by_date(date)
    print('####### AVAILABILITY #######')
    print()
    # Display the availability
    display_availability(slots)
    print()
    # Ask the user if they want to book an appointment
    place_booking = input('Would you like to book an appointment (y/n)?  ')

    # Check if the user wants to book
    book = place_booking.lower() == 'y'

    if book:
        # Prompt the user for booking details
        cust = input('Enter your name: ')
        stylist = input('Choose stylist (Peter, Maddie, Dominic): ')
        time = input('Choose time based on availability (e.g 15-16): ')
        # Add the booking
        add_new_booking(date, stylist, time, cust)
        print("Booking is Successful")
        print()
        # Get and display the updated availability
        slots = get_availability_by_date(date)
        display_availability(slots)

    print()
    print('See you soon!')


# Run the application if this script is executed directly
if __name__ == '__main__':
    run()