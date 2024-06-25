import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass
def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=db_name
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise DbConnectionError()


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'name': item[0],
            '12-13': 'Not Available' if item[1] else 'Available',
            '13-14': 'Not Available' if item[2] else 'Available',
            '14-15': 'Not Available' if item[3] else 'Available',
            '15-16': 'Not Available' if item[4] else 'Available',
            '16-17': 'Not Available' if item[5] else 'Available',
            '17-18': 'Not Available' if item[6] else 'Available',
        })
    return mapped


def get_all_booking_availability(_date):
    availability = []
    try:
        db_name = 'nano'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print('Connected')

        query = """
            SELECT teamMember, '12-13', '13-14', '14-15', '15-16', '16-17' , '17-18'
            FROM salon_bookings
            WHERE bookingDate = '{}'""".format(_date)

        cur.execute(query)

        result = cur.fetchall()
        availability = _map_values(result)
        cur.close()
    except Exception:
        raise DbConnectionError()

    finally:
        if db_connection:
            db_connection.close()  # Close the database connection
            print("DB connection is closed")

    return availability  # Return the availability

# Function to add a booking to the database
def add_booking(_date, teamMember, time, customer):
    try:
        db_name = 'nano'  # Database name
        db_connection = _connect_to_db(db_name)  # Connect to the database
        cur = db_connection.cursor()  # Create a cursor object to interact with the database
        print("Connected to DB: %s" % db_name)

        # Query to update booking information for a specific date and team member
        query = """
            UPDATE salon_bookings
            SET 
                `{time}` = 1, 
                `{time_id}` = '{customer}' 
            WHERE bookingDate = '{date}' AND teamMember = '{teamMember}'
            """.format(time=time, time_id=time + '-booking-id', customer=customer, date=_date, teamMember=teamMember)

        cur.execute(query)  # Execute the query
        db_connection.commit()  # Commit the transaction
        cur.close()  # Close the cursor

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()  # Close the database connection
            print("DB connection is closed")

# Example usage of the get_all_booking_availability function
if __name__ == '__main__':
    get_all_booking_availability('2020-12-15')
