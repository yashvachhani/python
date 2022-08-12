'''
what is closures?

A closure is a record storing a function together with an environment a mapping associating each free variable of the function with the value or storage location to which the name was bound when the closure was created. A closure , inlike a planin function, allows the function to access those captured variables through the closure's reference to them, even when the function is invoked outside their scope. 

'''

def outer_func():
	message = 'Hi'

	def inner_func():
		print(message)

	return inner_func

y = outer_func()

print(y)
print(y.__name__)
