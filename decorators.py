# Decorators

def outer_function(msg):
	def inner_function():
		print(f'hi {msg}')
	return inner_function

my_func=outer_function('my function')
hi = outer_function('hi')
bye = outer_function('bye')
yash = outer_function('yash')

my_func()
bye()
hi()
yash()

my_func()
my_func()

#################################
## outer functions and decorators
#################################

def decorator_function(message):
	def wrapper_function():
		print(message)
	return wrapper_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

#####################
## simplest decorator
#####################
# at the time of calling outer function pass the decorator function as an argument
# in side the inner function return the decorator functions with exicution
# in side the outer function return the inner function without exicuting
# so when we run creat variable to run function we call the outer function ad pass the decorator as an rgument
# than we run the variable that holds the outer functins refrance
# first it runs outer function than it will run inner function and at the last it will run the decorator function

# we use decorators to add functionalitys on our existing function without changing the existing function

# devloper can add this functionalitys in wraper function aka inner function

def decorator_function(original_function):
	def wrapper_function(*rags,**kwargs):
		print(f'wrapper function exicuted before {original_function.__name__}')
		return original_function(*rags,**kwargs)
	return wrapper_function

# decorator in class

class decorator_class(object):
	
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self,*args,**kwargs):
		print(f'call method {self.original_function.__name__}')
		return self.original_function(*args,**kwargs)

# defineing and useing decorator in ditailed mathod
def display():
	print('display function run complet')

decorated_display = decorator_function(display)
decorated_display()

# defineing and useing decorators in indusrtyal way
@decorator_function
def display():
	print('secound display')

display()

print(f'{decorated_display.__name__}')

# creating secound decorator
@decorator_function
def display_info(name,age):
	print(f'display info ran with arguments {name} {age}')

display_info('yash',22)

# displaying display function using decorator class
@decorator_class
def display():
	print('display function with class decorator')

# displaying display info using decorator class
@decorator_class
def display_info(name,age):
	print(f'display info with classruns {name} {age}')

display()
display_info('Vachhani yash', 22)

from functools import wraps

# logger decorator
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level = logging.INFO)
	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		logging.info(f'run with args {args} and kwargs {kwargs}')
		return orig_func(*args,**kwargs)
	return wrapper

# timer function
def my_timer(orig_func):
	import time
	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = orig_func(*args,**kwargs)
		t2 = time.time() - t1
		print(f'{orig_func.__name__} ran in: {t2} sec')
		return result
	return wrapper

import time

@my_logger
@my_timer
def display_info(name,age):
	time.sleep(8.888888888888888888)
	print(f'display_info ran with argument {name} {age}')

# stacked decorators syntex
display_info = my_logger(my_timer(display_info))
display_info('vachhani',22) 
