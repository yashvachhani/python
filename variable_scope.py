#LEGB

"""
Local, Enclosing, Global, Built-in
Abbreviation is in this order because python chacks value of variable in this order
"""

# Global & local

x = 'global x'

def test():
   y = 'local y'
   print(y) 
   print(x)

test()

def x_local():
   x = 'x local' 
   print(x)
   global y
   print(x)
   y  = 'this is global y'
   print(y)
x_local()

# Built-in
# we can over wright functions in built in functions of python
def min():
   pass

print(min())

# Enclosing 

def outer():
   x = 'outer x'
   def inner():
      nonlocal x
      x = 'inner x'
      print(x)
   inner()
   print(x)

outer()
      
