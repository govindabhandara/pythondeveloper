import requests, csv
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
fp=open('product.csv','w',newline='')
csvwrite=csv.writer(fp)
csvwrite.writerow(['p_Id','p_Name','price'])

for product in new_products:
    csvwrite.writerow([product['pid'],product['pname'],product['price']])

print('New CSV File Created!')