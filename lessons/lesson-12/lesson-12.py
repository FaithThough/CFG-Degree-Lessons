# Write a Python script where a user inputs a time, which we convert to a Unix timestamp, and then use this timestamp
# to fetch data from an API.
#
# The Unix timestamp is an integer that represents times according to the number of seconds since midnight on the 1st
# of January 1970. For example: 20 seconds and 13 minutes past 1 am on the 10th of August 2023 can be written as
# 1691622800. let's use a hypothetical API that requires a Unix timestamp to fetch data.
#
# We'll assume this API endpoint looks something like https://example.com/api/data?timestamp={unix_timestamp}.

# --- Step-by-Step Implementation ---
# 1. Convert user input time to Unix timestamp.
# 2. Fetch data from the API using the Unix timestamp.
# 3. Display the fetched data
import requests
from datetime import datetime
from pprint import pprint


# Function to convert user input time to Unix timestamp
# Verify your logic using this online converter https://www.unixtimestamp.com/
def convert_to_unix_timestamp(date_time_str):
    # Convert the string to a datetime object
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    # Convert the datetime object to a Unix timestamp using the timestamp method and returns it.
    unix_timestamp = int(date_time_obj.timestamp())
    return unix_timestamp

# Function to fetch data from the API using the Unix timestamp
def fetch_data(unix_timestamp):
    url = f"https://example.com/api/data?timestamp={unix_timestamp}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

# Get time input from the user
user_input = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")

# Convert the input time to Unix timestamp
unix_timestamp = convert_to_unix_timestamp(user_input)
print(f"Unix Timestamp: {unix_timestamp}")

# Fetch data from the API using the Unix timestamp
api_data = fetch_data(unix_timestamp)

# Check if data was successfully fetched
if api_data:
    print("Data fetched successfully. Here are the details:")
    pprint(api_data)
else:
    print("No data available due to an API error.")

# This example demonstrates:
# 1. Converting a user-input time to a Unix timestamp.
# 2. Making an API request using the Unix timestamp.
# 3. Handling the API response and displaying the data.
