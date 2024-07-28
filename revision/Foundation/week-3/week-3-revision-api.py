import requests
import json
url = "https://hp-api.onrender.com/api/characters"
response = requests.get(url)
data = response.json()
# print(data)

# # Printing out all data in a better format
# for item in data:
#     print(item)

# # Printing out the names
# for item in data:
#     print(item['name'])

    # Printing out the houses with error handling
for item in data:
    name = item.get('name', 'unknown')
    house = item.get('house', 'unknown')
    if not house: # check if house is an empty string or none
        house = 'no'
    print(f"{name} is a member of {house} house")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")




