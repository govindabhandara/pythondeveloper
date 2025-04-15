import csv
import emp
fp = open('emp.csv','r')
csvreader=csv.reader(fp)

print(csvreader)
print(type(csvreader))

for user in csvreader:
    print(user)