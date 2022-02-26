my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9
#         -10-9 -8 -7 -6 -5 -4 -3 -2 -1

#list[start:end:step]

print(my_list[0:6])
print(my_list[-9:-7])
print(my_list[-3:9])
print(my_list[:])
print(my_list[4:])
print(my_list[:-3:-1])
print(my_list[::-1])
print(my_list[:-1:-2])
print(my_list[-1::-2])

# sliesing string
s = 'http://yashvachhani@kd.com'

# reverse the url
print(s[::-1])

# get the top level domain
print(s[-4:])

# get the url without the http://
print(s[7:])

# print the url without the http:// or the top level domain
print(s[7:4])
