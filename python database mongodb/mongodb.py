import requests

data=requests.get('https://dummyjson.com/products')
product_data=data.json()

print(type(product_data))