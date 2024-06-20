import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def connect_to_database(database_name):
    connection = mysql.connector.connect(
        host=HOST,
        database=database_name,
        user=USER,
        password=PASSWORD
    )

    return connection


def get_all_records():
    database_name = "tests"
    try:
        # connection to the database
        db_connection = connect_to_database(database_name)
        cursor = db_connection.cursor()
        print(f"Connected to database: {database_name}")

        # Execute the query to fetch all records
        query = "SELECT * FROM abcreport"
        cursor.execute(query)
        records = cursor.fetchall()

        # print each record
        for record in records:
            print(record)
    except Exception:
        raise DbConnectionError("Failed to read data from db")

get_all_records()

def get_all_records_for_rep(rep_name):
    db_name = "tests"
    try:
        db_connection = connect_to_database(db_name)
        cursor = db_connection.cursor()
        print(f"Connected to database {db_name}")

        query = f"SELECT Item, Units, Total FROM abcreport WHERE Rep = '{rep_name}'"
        cursor.execute(query)
        records = cursor.fetchall()

        # print each record
        for record in records:
            print(record)

    except Exception:
        raise DbConnectionError("Failed to read data from db")


get_all_records_for_rep('Andrews')
