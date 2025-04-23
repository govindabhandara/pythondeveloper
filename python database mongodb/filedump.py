import requests, pymongo,json
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
fp=open('product.json','w')
json.dump(new_products,fp)
print(' New JSON File Created')