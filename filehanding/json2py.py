import json
emp_data ='''
        {
        "eid":101,
        "name":"rahul",
        "esal":"unfefined",
        "loc":true
        }  
        '''
emp_dict=json.loads(emp_data)
print(type(emp_dict))
print(emp_dict)