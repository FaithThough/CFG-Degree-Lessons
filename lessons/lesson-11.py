# APIs
import requests
import json
def fetch_recipes(query, diet, meal_type, max_results):
    url = "https://api.edamam.com/api/recipes/v2"
    APP_ID = "bf22ab9c"
    APP_KEY = "0981ef39fe9aef76d8042378c2b0afd3"

    # Containing everything in a dictionary
    params = {
        'type': 'public',
        'q': query,
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'meal_type': meal_type,
        'diet': diet,
        'from': 0,
        'to': max_results # use max_results to limit the number of results
    }

    response = requests.get(url, params=params)
    # print(response.json())

    # # Seeing the keys:
    data = response.json()
    # recipes = data['hits']
    # for d in data:
    #     print(d)
    recipes = data.get('hits', [])
    if not recipes:
        print("No recipes found")
        return

    # slicing the list of recipes
    recipes = recipes[:max_results]

    for recipe in recipes:
        recipie_info = recipe['recipe']
        print(f'Recipie name: {recipie_info["label"]}')
        print(f'Calories: {recipie_info["calories"]}')
        print(f'URL: {recipie_info["url"]}')

def main():
    while True:
        query = input("What ingredient would you like to search for? ")
        diet = input("What dietary preference do you have from the following: balanced, high-fiber, high-protein, low-carb, low-fat, low-sodium ")
        meal_type = input("Enter your meal type from the following: Breakfast, Dinner, Lunch, Snack, Teatime ")
        max_results = int(input("Enter the maximum number of recipes to display: "))
        fetch_recipes(query,diet, meal_type, max_results)
        continue_search = input("Do you want to search for more recipes? yes/no ")
        if continue_search.lower() != 'yes':
            break

main()
