num = [1,2,3,4,5]

# simpale loop
for i in num:
    if i == 4:
        print('found!')
        break
    print(i)

# nested loop
for i in num:
    for k in 'yash':
        print(i,k)

# range
for i in range(8):
    print(i)

# while loop
x=0
while True:
    if x ==8:
        print (f'{x} is max',)
        break
    print(x)
    x+=1