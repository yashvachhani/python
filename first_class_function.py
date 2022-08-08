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
