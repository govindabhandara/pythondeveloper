import requests,json,csv
#extract data from source-rest api/cloud api-cloud

response=requests.get('https://dummyjson.com/products')
product_data=response.json()
products=product_data['products']
# print(type(product_data))
# print(type(products))
#load into beauty.csv and beauty.json
fp1=open('beauty.csv','w',newline="")
csvwriter=csv.writer(fp1)
csvwriter.writerow(['pid','name','price','category'])
for product in products:
    csvwriter.writerow([product['id'],product['title'],product['price'],product['category']])
    print("new file")
    fp1.close()
