#LEGB

"""
Local, Enclosing, Global, Built-in
Abbreviation is in this order because python chacks value of variable in this order
"""

# Global 

x = 'global x'

def test():
    y = 'local y'
    print(x)

test()
 