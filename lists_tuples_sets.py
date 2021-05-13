courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

# using values by index
print(courses[2])
print(courses[-3])
print(courses[::-1])
print(courses[1:2])

# append list ( append insert values at last)
courses.append('art')

# insert in to list( insert at purticular index )
courses.insert(0,"artificial inteligents")

print(courses)

# extend the list
courses_2 = ['education','art']

# store list inside a list
courses.insert(0,courses_2)
print(courses)

# append list to the list
courses.append(courses_2)
print(courses)

# extend list
courses.extend(courses_2)
print(courses)

# remove values
courses.remove('art')
print(courses)

# poped values ( default delete last value ) and returns value that poped
poped = courses.pop()
print(courses)
print( poped )

# reverse the list
courses.reverse()
print( courses)

# deleteing lists
print(courses.pop())
print(courses.pop(1))

# shorting list
courses.sort()
print(courses)

# sort numbers
numbers = [1,2,3,4,5,6,7,4,2,3,42,9,5,2,1,]
numbers.sort()
print(numbers )

# sort in reverse order
courses.sort(reverse=True)
numbers.sort(reverse=True)
print(courses)
print(numbers)

# store shorted list in ot the other list
sorted_courses = sorted(courses)
sorted_number = sorted(numbers)
print(sorted_courses)
print(sorted_number)

# find minimum values from list
print(min(courses))
print(min(numbers))

# find maximum values from list
print(max(courses))
print(max(numbers))

# sum of values from list
print(sum(numbers))

# find index of any values
print(courses.index('artificial inteligents'))

# chack value is in list or not (returns true or false)
print('Math' in courses)
print('Art' in courses)

# enumerate function print values and index (also takes starting index optionel)
for index, values in enumerate(courses):
    print(index, values)

# join the list as a string
courses_str = ' - '.join(courses)
print(courses_str)

# list are mutable change in one reflects on other
courses_2 = courses
print(courses)
print(courses_2)
courses_2[0] = 'Art'
print(courses)
print(courses_2)

# Immutable tuples
tuple_1 = ('History', 'Math', 'Physics', 'CompSci', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0] = 'art'
print(tuple_1)
print(tuple_2)

# sets
set_1 = {'History', 'Math', 'Physics', 'CompSci', 'Physics', 'CompSci'}
print(set_1)

# This chack in posible in lists tuples also but sets are optimised for this
print('Math' in set_1)

set_2 = {'History', 'Math', 'Art', 'Disign'}

# intersection to find comman values
print(set_1.intersection(set_2))

# union to join both sets
print(set_1.union(set_2))

# create empty list
empty_list = []
empty_list = list()

# create empty tuple
empty_tuple = ()
empty_tuple = tuple()

# create empty set
empty_set = {}      # this is dict, not a set
empty_set = set()   # this is the way to define empty set