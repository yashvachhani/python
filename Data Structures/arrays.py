'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
'''

monthly_expenses = [2200,2350,2600,2130,2190]

i = monthly_expenses[1]-monthly_expenses[0]
print(i)

ii =monthly_expenses[1]+monthly_expenses[0]+monthly_expenses[2]
print(ii)

iii = 2000 in monthly_expenses
print(iii) 

monthly_expenses.append(1980)
print(monthly_expenses)

monthly_expenses[3]=monthly_expenses[3]-200
print(monthly_expenses)


'''
You have a list of your favourite marvel super heros.
'''
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')

print(heros)

heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)

heros[2] = 'doctor strange'
print(heros)

heros.sort()
print(f'{heros}')

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

iv = int(input('enter number'))

l = [i for i in range(iv) if i % 2 == 1]

print(l)
