# Dictionary creation
my_dict = {'kumar': '001', 'sai': '002', 'ram': '003'}
print(my_dict)
type(my_dict)

new_dict = dict(kumar='001', sai='002')
print(new_dict)

# Nested dictionaries
emp_details = {'Employee': {'aaa': {'ID': '001', 'salary': '1000'}, 'bbb': {'ID': '002', 'salary': '2000'}}}
print(emp_details)

# Accessing items
print(my_dict['sai'])
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get('sai'))
for x in my_dict:
    print(x)  # Printing keys one after other
for x in my_dict.keys():
    print(x)
for x in my_dict.values():
    print(x)
for x, y in my_dict.items():  # Since we need to return 2 value .So use x,y
    print(x, y)

# Updating values
my_dict['kumar'] = '004'  # To update value
my_dict['Reddy'] = '003'
print(my_dict)

# Deleting Entries
my_dict.pop('Reddy')
print(my_dict)
(my_dict.popitem())  # Removes last item
print(my_dict)
del my_dict['ram']
print(my_dict)

# Converting dictionary into (data frame - data structure that consists of columns of various types
import pandas as pd
df = pd.DataFrame(emp_details['Employee'])
print(df)