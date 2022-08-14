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

def decorator_function(original_function):
	print(f'decorator function run start')
	def wrapper_function():
		print(f'weapper function start running')
		print(f'{original_function.__name__} is yash')
		return original_function()
	print(f'decorator fuction complit')
	return wrapper_function

def display():
	print('display function run start')
	print('display function rjun complet')

decorated_display = decorator_function(display)
decorated_display()
