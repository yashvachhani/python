num = [1,2,3,4,5,6,7,8,9,10]


# n for each n in nums

my_list=[]

for n in num:
   my_list.append(n)
print(my_list)

# with list comprehensions

my_list = [n for n in num]

print(my_list)

# n*n for each n in nums

my_list=[]

for n in num:
   my_list.append(n*n)
print(my_list)

# using map lambda

my_list = map(lambda n:n*n, num)

print(list(my_list))

# I want 'n' for each 'n' in num if 'n' is even

my_list = []
for n in num:
   if n%2==0:
      my_list.append(n)
print(my_list)

#using a filter + lambda

my_list = filter(lambda n:n%2==0, num)

print(list(my_list)

#I want a (latter, nuum) pair for each letter in 'abcd' and each number in '0123'
for letter in 'abcd':
   for num in range(4):
      my_list.append((letter,num))
print(my_list)
