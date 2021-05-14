# simple function 
def func():
    pass

# print location and type of function
print(func)

# retuns none because notiong is there
print(func())

# hello function print hello
def hello_func():
    print('hello world')

hello_func()

# function takes nothing returns string
def returns_hello():
    return('hello world returned')

string = returns_hello()
print(string)

# we can trit exicuted function as a datatype that return by function
print(len(returns_hello()))
print(returns_hello().upper())

# function takes argument and retuns 
# also set optnal values
def coustom_hello(name='monkey'):
    return(f'Hello {name} ')

name = 'Yash'

# print coustom values
print(coustom_hello(name))

# acess without velues
print(coustom_hello())

name = 'Vachhani Yash'
print(coustom_hello(name))

# args and kwargs function
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

args = ['computer science','artificial inteligents']
kwargs = {'name': 'yash', 'age': 21}

# args takes every values and kwargs takes every key value pares
student_info('computer science','artificial inteligents', name='yash',age=21)

# set kwargs as a predefine
student_info(args,kwargs)

# set kwargs as a predefine
student_info(*args,**kwargs)

# set kwargs as a kwargs
student_info(args,kwargs=kwargs)

'''
small program of chaking year is leap year or not
'''


# number of days per month. first value placeholder
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """ returns true for leap year, false for non-leap year. """
    return year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 )

def days_in_month(year,month):
    """ returns number of days in that month in that year. """
    if not 1 <= month <= 12:
        return "return invelid month"

    if month == 2 and is_leap(year) :
        return 29
    
    return month_days[month]

print(days_in_month(200,2))