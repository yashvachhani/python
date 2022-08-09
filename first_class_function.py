# First-class Functions:
'''
A Programming language is said to have function if it treats function as 
first-class citizens.
'''

# First-class citizen (Programming):
'''
A First-class citizen (sometimes called first-class objects) 
in a programming language is an entity which supports all the 
operations generally available to other entities. These 
operations typically include being passed as an argument, 
retutned from a function, and assigned to a variable.
'''

# this is what we use to do

def square(x):
   return x * x

# assining result of function after exicuting 
f = square(5)

print(square)
print(f)

# assining function to variable

f = square
print(f)

# use variable as a function
print(f(5))

# create map function for first class function understanding
# calling function from another function
def my_map(func,arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

squares = my_map(square,[1,2,3,4,5])

def cube(x):
	return x * x * x

cube = my_map(cube,[5,4,3,2,1])

print(squares)
print(cube)

# create another log function for simpler massage
# returnning function from another function
def logger(msg):
	def log_message():
		print('Log: ', msg)
	return log_message

log_hi = logger('Hi!')
log_hi()

# function that returns function

def html_tag(tag):
	def wrap_text(msg):
		print(f'{tag} {msg}')
	return wrap_text

print_hi = html_tag('hi')
print_hi('Test headline!')
print_hi('Another headline!')

print_hi = html_tag('p')
print_hi('Test Paragraph!')

p = html_tag('yash')
p('vachhani')

