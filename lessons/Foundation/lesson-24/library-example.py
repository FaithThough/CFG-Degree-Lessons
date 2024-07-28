import mysql.connector
from config import USER, PASSWORD, HOST


# Custom exception for handling database connection errors
class DbConnectionError(Exception):
    pass


# Function to connect to the database (library entrance)
def _connect_to_db(database_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=database_name
    )
    return connection


# Function to fetch and print all records (read all books)
def get_all_records():
    db_name = 'tests'
    try:
        db_connection = _connect_to_db(db_name)  # Entering the library
        cursor = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = "SELECT * FROM abcreport"
        cursor.execute(query)
        records = cursor.fetchall()  # List of all books

        for record in records:
            print(record)  # Reading each book

    except Exception:
        raise DbConnectionError("Failed to read data from DB")  # Library closed sign

    finally:
        if db_connection:
            db_connection.close()  # Exiting the library
            print("DB connection is closed")


# Function to calculate commission (reward for reading pages)
def calc_commission(sold_items, commission_rate):
    total_sales = sum(item[2] for item in sold_items)  # Summing pages read
    commission = total_sales * (commission_rate / 100)  # Calculating reward
    return commission


# Function to fetch records for a specific rep (reading books by a specific author)
def get_all_records_for_rep(rep_name):
    db_name = 'tests'
    try:
        db_connection = _connect_to_db(db_name)  # Entering the library
        cursor = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = f"SELECT Item, Units, Total FROM abcreport WHERE Rep = '{rep_name}'"
        cursor.execute(query)
        records = cursor.fetchall()  # Books by a specific author

        for record in records:
            print(record)  # Reading each book

        commission = round(calc_commission(records, commission_rate=10), 2)
        print(f"Commission for {rep_name} is £{commission}")  # Reward for reading

    except Exception:
        raise DbConnectionError("Failed to read data from DB")  # Library closed sign

    finally:
        if db_connection:
            db_connection.close()  # Exiting the library
            print("DB connection is closed")

    return rep_name, commission


# Function to insert a new record (donating a new book)
def insert_new_record(record):
    db_name = 'tests'
    try:
        db_connection = _connect_to_db(db_name)  # Entering the library
        cursor = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(record.keys()),
            record['OrderDate'],
            record['Region'],
            record['Rep'],
            record['Item'],
            record['Units'],
            record['UnitCost'],
            record['Total'],
        )
        cursor.execute(query)
        db_connection.commit()  # Placing the book on the shelf
        print("Record added to DB")

    except Exception:
        raise DbConnectionError("Failed to read data from DB")  # Library closed sign

    finally:
        if db_connection:
            db_connection.close()  # Exiting the library
            print("DB connection is closed")


# Main function to plan the library visit
def main():
    # Uncomment to fetch all records
    # get_all_records()

    # Uncomment to fetch records for a specific rep and calculate commission
    # get_all_records_for_rep('Morgan')

    # Insert a new record
    new_record = {
        'OrderDate': '2020-12-15',
        'Region': 'Central',
        'Rep': 'Johnson',
        'Item': 'post-it-notes',
        'Units': 220,
        'UnitCost': 2.5,
        'Total': 220 * 2.5,
    }
    insert_new_record(new_record)


# Execute the main function if this script is run
if __name__ == '__main__':
    main()