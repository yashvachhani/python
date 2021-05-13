student={'name':'john','age':25,'courses':['math','CompSci']}
print(student)

# use value by key
print(student['name'])
print(student['courses'][1])

# if any key does not exist than it gives error so use the get way
print(student.get('courses','not found'))

# add new key value in dict
student['mobile_mumber'] = '555-555-5555'
print(student.get('mobile_mumber','not found'))

# update new key value in dict
student['name'] = 'jane'
print(student.get('name','not found'))

# update multipale values
student.update({'name':'june','age':21,'address' : '45 jems street'})
print (student)

# delete from dictionaries
del student['address']
print(student)

# pop values with return
pop_values = student.pop('age')
print(student)

# find lenth
print(len(student))

# get list of all keys
print(student.keys())

# get list of all values
print(student.values())

# get list of all keys and values as a per
print(student.items ())

# acess all keys and values
for key,value in student.items():
    print (key,value)