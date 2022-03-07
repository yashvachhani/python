# week2 first step in programming

a = 3
b = 4

print(a+b) # 7

'''
exchange variables
a becomes b and b becomes a
simultaneously
'''

a,b = b,a

# if elif

x = 10

if x < 0:
   print("negative")

if x < 0:
   print("neg")
elif x > 0:
   print("pos")
else:
   print("Zero")

# while loop

while x <= 10:
   print(x)
   x += 1                    # increment i by 1

def sorter(x,y):
   return min(x,y),max(x,y)

n,m = sorter(8,7)

print(f'm is {m}')
print(f'n is {n}') 

# sort list

mylist = [5,2,1,6,2]
mylist.sort()                # sort in place
mylist = mylist.sort()

l = [i*i for i in range(5)]        # creates [0,1,4,8,16]
print(l)
l = [i for i in range(5) if(i%2==0)]     # creates[0,2,4]
print(l)


# week 1 pyhton the tail of the snake

# variables
'''
variables created at first definition

syntax: <variable name> = <value>

type of variable content can vary
''' 

num = 1

motto = 'Creating AI'
motto = 42

'''
no variable declaration
num is of type int
motto is of type str at first definition/assignment
motto becomes of type int at second assinment
comment start with # until end of line
'''

# possible operations

# int and str objects can be added using +

num = 3 + 3                      # stores 6 in num 
s = "bli" + "bla"                # stores 'blibla' in s

num += 4           
'''
add 4 to whatever
is already in num
i.e. num is 10 now
'''

# operating on strings

'''
strings are a sequence of characters
character index counted from 0 to n -1 where n is the length of the string
access the characters of a string S via square brackets S[]
start counting characters from 0(not 1)!
'''

s = 'abcdefg'
print(s[0])
print(s[1])
print(s[-2])
print(s[-4])
print(s[2:])
print('cdefg')
print(s[:-3])
print('abcd')
print(s[-2:])
print('fg')
print(s[:-3])
print('abcd')

print(len(s))

l = [1,2,3]+[4,5,6]

l[2] += 5
print(l)
