nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for i in nums:
   my_list.append(i)
print(my_list)

my_list = [n for n in nums]
print(my_list)

# I want 'n*n' for each 'n' in nums
my_list = []
for i in nums:
   my_list.append(i*i)
print(my_list)

my_list = [n*n for n in nums]
print(my_list)

# using maps and lambda
my_list = map(lambda n: n*n, nums)
print(list(my_list))

nums= [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums if n is even
my_list = []
for i in nums:
   if i%2 == 0:
      my_list.append(i)
print(my_list)

my_list = filter( lambda n: n%2 == 0,nums)
print(list(my_list))

my_list = [n for n in nums if n%2 == 0]
print(my_list)

# I want a (letter,num) pair for each latter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
   for num in range(4):
      my_list.append((letter,num))
print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# how to use zip
names = ['Bruce','Clark','peter','logan','wade']
heros = ['Batman','Superman','spiderman','Wolverine','Deadpool']
print(list(zip(names,heros)))
my_dict = {}

#dict comprihantion using zip
my_dict = {names:heros for names,heros in zip(names,heros) if names != 'Clark'}
print(my_dict)


num = [1,2,3,4,5,6,7,8,9,0,9,8,7,5,4,3,2,5,6,6,6,6,7,7,5,3,2,2,3,4,4,5,5,6,6]
# set comprihantion
my_set = {n for n in nums}
print(my_set)

# genrator function
my_gen = (n*n for n in nums)

for i in my_gen:
   print(i)
