import requests
import json

response = requests.get('https://dummyjson.com/products') #make a get request to a url
data = response.json() #to parse json data from an HTTP response (usually From api)
products = data['products']  # Get the products list from the response

new_users = []
for product in products:
    new_users.append({
        "user_id": product['id'],
        "user_title": product['title'],
        "user_rating": product.get('rating', 0)  # Using .get() for safer access
    })

# Write to file once after collecting all data
with open('new_usr.json', 'w') as fp:
    json.dump(new_users, fp, indent=2)  # Added indent for better readability

print("Created new file with", len(new_users), "entries")