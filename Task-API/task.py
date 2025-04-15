# Extract data from cloud base,DB,file
# HTTp method GET POST PUT DE  
import requests
import json

fp=open('new_users.json','w')
#extract data from source
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
'''print(type(resp_data))
print(type(resp_data.json()))'''
users=resp_data.json()

#transform
new_users=[]
for user in users:
    new_users.append({"user_id":user['id'],
                      "user_name":user['name'],
                      "city":user['address']['city'],
                      "mobile":user['phone']
                      })
print(new_users)

#load data into new json data/dump data into json data
json.dump(new_users,fp)
print('new file created')


