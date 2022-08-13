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

