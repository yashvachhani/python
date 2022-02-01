l = [9,8,7,6,5,4,4,3,2,1]

# sorted function returns sorted list
sorted_l = sorted(l)
print(sorted_l)

# sorted method sorts list
l.sort()
print(l)

# sort list in desending order
l.sort(reverse=True)
print(l)

# sort method does not work in tuples that is only for list
tup = (1,2,3,4,5,6,7,8,9)
t = sorted(tup)
print(t)

di = {'name':'Corey','job':'programming','age':'None','os':'mac'}
d = sorted(di)
print(d)

# we can set function as key while sorting and it gives difrent perameter
l = [-3,-4,-1,2,4,3]
sorted_l = sorted(l,key=abs)
print(l)
