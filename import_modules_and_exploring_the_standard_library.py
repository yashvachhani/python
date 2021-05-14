import my_module

courses = ['History', 'Math', 'Physics', 'ComSci']

# calling index function from my_module.py file
index = my_module.find_index(courses,'ComSci')
print(index)

# import purticuler variable of function
from my_module import test as t

# printing variable from other file
print(t)

# import hoal file at ones
from my_module import *

# see system path 
from sys import path
print(path)

# apppend any path in to the system path
# sys.path.append('/Users/yash/Desktop/') 

# use random library
import random
random_course = random.choice(courses)
print(random_course)

# use math library
import math
print (math.sin(math.radians(90)))

# use datetime and calendar 
import datetime
import calendar
print(datetime.date.today())
print(calendar.isleap(2000))

# use os library
import os
print(os.getcwd())

# get any file location
print(os.__file__)