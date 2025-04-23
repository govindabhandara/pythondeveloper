import requests,pymongo
from pymongo import MongoClient
data=requests.get('https://dummyjson.com/products')
product_data=data.json()
products=data.json()['products']
 
new_products=[]

for product in products:
    new_products.append ({
        'pid':product['id'],
        'pname':product['title'],
        'category':product['price'],
        'price':product['price'],
        'rating':product['rating']
    })
try:
    client=pymongo.MongoClient('mongodb://localhost:27017') 
    db=client['11am']
    product_col=db['products']
    product_col.insert_many(new_products)
    print('Product Data Written sucessfully')
except:
    pass
finally:
    pass