if True:
    print('condition was true')

# defult true
if False:
    print('condition was False')

language = 'python'

# comparition oprators
# Equal                 ==
# Not Equal             !=
# Greater Than          >
# Less Than             <
# Greater or Equal      >=
# Less or Equal         <=
# Object Identity       is


if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
elif language == 'javascript':
    print('language is javascript')
else:
    print('no match')

# and
# or
# not

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('welcome to admin page')
else:
    print('plese enter valid creds')

# not
if not logged_in:
    print('plese log in')
else:
    print('welcome')


# Object Identity       is
# is

a = [ 1, 2, 3 ]
b = [ 1, 2, 3 ]
c = b
print( a is b )
print( a == b )
print( c is b )

# id of value in mamory
print(id(a))
print(id(b))
print(id(c))

# False values:
# False
# none
# Zero of any numeric type
# Any empty sequence. For example, '',(),[].
# Any empty mapping. For example, {}.
condition = [True,False,None,0,'',(),[],{},1]
for i in condition:
    print(i)
    if i:
        print('Evaluated to True')
    else:
        print('Evaluated to False')