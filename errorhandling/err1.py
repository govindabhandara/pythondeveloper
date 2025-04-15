'''
try:
    risky_code()
except:
    some Exception as e:
handle_exception(e)
'''

'''
try:
    number=int(input("enter number"))
    result=10/number
except ZeroDivisionError as err:
    print("cannot divide by zero")
except ValueError as err:
    print("invalid , enter again valid num")
else:
    print(f'result:',result)
'''


'''
try:
   file=open("a.txt",'r')
   content=file.read()
   print(content)
except FileNotFoundError as err:
   print("Error : File isnot found")
else:
   print("file read operation sucess")
finally:
   if 'file' in locals():
      file.close()
      print("file operation is sucess")
'''
