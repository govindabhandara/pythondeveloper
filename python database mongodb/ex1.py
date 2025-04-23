import requests,pymongo
from pymongo import MongoClient
products=requests.get('https://dummyjson.com/products')
mongoDB_url='mongodb://localhost:27017/'
try:
    client=pymongo.MongoClient(mongoDB_url)
    db=client['12am']
    prod_col=db['products']
    prod_col.insert_many(products)
    print("data insert sucessfully")

except Exception as err:
    print(err)
